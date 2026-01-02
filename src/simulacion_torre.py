import numpy as np
import matplotlib.pyplot as plt
import json
import os

# --- CONFIGURACIÓN DEL MODO DE DATOS ---
# Opciones: "simulado" | "cdmx_real"
MODO_DATOS = "simulado"  # ⬅️ CAMBIA ESTO A "cdmx_real" PARA USAR DATOS REALES

# --- FUNCIÓN PARA CARGAR DATOS REALES ---
def cargar_datos_reales():
    """Carga parámetros desde escenarios_cdmx.json generado por datos_cdmx.py"""
    archivo = "escenarios_cdmx.json"
    
    if not os.path.exists(archivo):
        raise FileNotFoundError(
            f"⚠️  No se encontró '{archivo}'.\n"
            f"   Primero ejecuta: python datos_cdmx.py"
        )
    
    with open(archivo, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    params = data['escenario_actual']
    metadata = {
        'estacion': data['estacion'],
        'timestamp': data['timestamp_medicion'],
        'pm25_real': params['pm25_real'],
        'viento_real': params['viento_real'],
        'categoria': params['categoria_calidad']
    }
    
    return params, metadata

# --- CONFIGURACIÓN DE LA HIPÓTESIS (PARAMETROS) ---
if MODO_DATOS == "cdmx_real":
    try:
        params, metadata = cargar_datos_reales()
        NUM_PARTICULAS = params['num_particulas']
        VELOCIDAD_VIENTO = params['velocidad_viento']
        EFICIENCIA_RED = params['eficiencia_red']
        ANCHO_CUELLO = params['ancho_cuello']
        print("\n✅ MODO: DATOS REALES DE CDMX")
        print(f"   Estación: {metadata['estacion']}")
        print(f"   Fecha: {metadata['timestamp']}")
        print(f"   PM2.5: {metadata['pm25_real']} µg/m³ ({metadata['categoria']})")
        print(f"   Viento: {metadata['viento_real']} m/s" if metadata['viento_real'] else "   Viento: Estimado")
        print()
    except FileNotFoundError as e:
        print(f"\n{e}\n")
        exit(1)
else:
    # VALORES SIMULADOS (ORIGINALES)
    NUM_PARTICULAS = 2000
    VELOCIDAD_VIENTO = 1.5
    EFICIENCIA_RED = 0.7
    ANCHO_CUELLO = 10
    metadata = None

ALTURA_TORRE = 100       # Altura relativa de la torre
ANCHO_BASE = 40          # Ancho en la entrada (suelo)

# --- INICIO DE SIMULACIÓN ---
# Coordenadas iniciales (todas en el suelo y distribuidas en el ancho de la base)
x = np.random.uniform(-ANCHO_BASE/2, ANCHO_BASE/2, NUM_PARTICULAS)
y = np.zeros(NUM_PARTICULAS) 

# Estados: 1 = Volando (Aire sucio), 0 = Atrapada (Lodo/Agua limpia)
estado = np.ones(NUM_PARTICULAS) 

print(f"--- INICIANDO SIMULACIÓN PROYECTO TLAZOLTÉOTL ---")
print(f"Lanzando {NUM_PARTICULAS} partículas al sistema...")

# Ciclo de tiempo (Simulación del ascenso del aire)
for t in range(ALTURA_TORRE):
    # 1. FÍSICA: Efecto Venturi (Aceleración)
    # Mientras más sube y más se estrecha el tubo, más rápido viaja el aire
    factor_estrechamiento = 1 + (t / ALTURA_TORRE) * 2.5 
    y += VELOCIDAD_VIENTO * factor_estrechamiento
    
    # 2. CAOS: Movimiento lateral (Turbulencia natural)
    x += np.random.uniform(-1, 1, NUM_PARTICULAS)
    
    # 3. GEOMETRÍA: Paredes de la torre (Hiperboloide)
    # Calcula el ancho permitido en esta altura específica
    ancho_actual = ANCHO_BASE - ( (ANCHO_BASE - ANCHO_CUELLO) * (y / ALTURA_TORRE) )
    ancho_actual = np.maximum(ancho_actual, ANCHO_CUELLO) # Límite físico del cuello
    
    # 4. FILTRADO: La Red Húmeda + Ionización
    # Generamos probabilidad aleatoria para cada partícula en este instante
    probabilidad = np.random.rand(NUM_PARTICULAS)
    
    # Si la partícula sigue volando Y la probabilidad cae dentro de la eficiencia:
    atrapadas_ahora = (estado == 1) & (probabilidad < (EFICIENCIA_RED * 0.05)) 
    estado[atrapadas_ahora] = 0 # Se marca como atrapada (se vuelve azul)

    # 5. LIMITES: Rebote en las paredes
    rebote = (x > ancho_actual/2) | (x < -ancho_actual/2)
    x[rebote] *= -0.9 # Rebota hacia adentro perdiendo un poco de inercia

# --- CÁLCULO DE RESULTADOS ---
particulas_atrapadas = np.sum(estado == 0)
particulas_escapadas = np.sum(estado == 1)
eficiencia_final = (particulas_atrapadas / NUM_PARTICULAS) * 100

print(f"\n--- REPORTE DE INGENIERÍA ---")
print(f"Modo de Datos: {MODO_DATOS.upper()}")
if metadata:
    print(f"PM2.5 medido: {metadata['pm25_real']} µg/m³")
    if metadata['viento_real']:
        print(f"Viento medido: {metadata['viento_real']} m/s")
print(f"Partículas capturadas (Lodo): {particulas_atrapadas}")
print(f"Partículas emitidas (Aire sucio): {particulas_escapadas}")
print(f"EFICIENCIA TOTAL DEL SISTEMA: {eficiencia_final:.2f}%")

# ==============================================================================
# --- MÓDULO DE CÁLCULO DE RECURSOS + BIORREACTOR DE ALGAS (XPRIZE MODE) ---
# ==============================================================================

print(f"\n--- REPORTE DE TERRAFORMACIÓN (XPRIZE METRICS) ---")

# 1. FLUJO DE AIRE (El Pulmón)
radio_promedio = (ANCHO_BASE + ANCHO_CUELLO) / 4
area_seccion = np.pi * (radio_promedio ** 2)
# Flujo volumétrico diario (m3/día)
flujo_aire_m3_dia = area_seccion * (VELOCIDAD_VIENTO * 1.5) * 86400

# 2. CAPTURA DE CARBONO (CO2) CON ALGAS
# Datos científicos base:
co2_en_aire = 0.00075  # kg de CO2 por m3 de aire (aprox 415 ppm)
tasa_absorcion_agua = 0.40 # 40% del CO2 se disuelve en la cortina de agua/niebla
ratio_algas = 1.8 # 1 kg de algas consume 1.8 kg de CO2

# Cálculo
co2_potencial_dia = flujo_aire_m3_dia * co2_en_aire
co2_capturado_dia = co2_potencial_dia * tasa_absorcion_agua
biomasa_generada_dia = co2_capturado_dia / ratio_algas
co2_anual_toneladas = (co2_capturado_dia * 365) / 1000

print(f"🌿 BIO-REACTOR DE ALGAS:")
print(f"   - CO2 Secuestrado: {co2_capturado_dia:.2f} kg/día")
print(f"   - IMPACTO ANUAL: {co2_anual_toneladas:.2f} TONELADAS de CO2 eliminadas")
print(f"   - Biomasa producida: {biomasa_generada_dia:.2f} kg/día (Fertilizante/Biofuel)")

# 3. AIRE LIMPIO
aire_limpio_dia = flujo_aire_m3_dia * (eficiencia_final / 100)
personas_equivalente = int(aire_limpio_dia / 11)

print(f"\n🌬️  AIRE PURIFICADO: {aire_limpio_dia:,.0f} m³/día")
print(f"   (Equivalente a lo que respiran unas {personas_equivalente:,} personas al día)")

# 4. AGUA (Cosecha Warka)
# Superficie del hiperboloide (aprox)
area_lateral = np.pi * ((ANCHO_BASE+ANCHO_CUELLO)/2) * ALTURA_TORRE 
captacion_warka = 0.5 # L/m2 (niebla)
agua_total = area_lateral * captacion_warka

print(f"\n💧 AGUA COSECHADA: {agua_total:,.0f} Litros/día")
print(f"   (Alimenta biorreactor de algas + humidificadores)")

# 5. ENERGÍA (Turbina MagLev)
densidad_aire = 0.95 
area_turbina = np.pi * ((ANCHO_CUELLO/2)**2)
vel_salida = VELOCIDAD_VIENTO * 2.5
potencia = 0.5 * densidad_aire * area_turbina * (vel_salida**3) * 0.35
energia = (potencia * 24) / 1000

print(f"\n⚡ ENERGÍA GENERADA: {energia:.2f} kWh/día")
print(f"   (Alimenta ionizadores, bombas y sistema de algas)")

print(f"\n--- ESTADO DEL SISTEMA: LISTO PARA PITCH XPRIZE ---")



# --- VISUALIZACIÓN GRÁFICA ---
titulo = f"Simulación de Flujo: Proyecto Tlazoltéotl [{MODO_DATOS.upper()}]\nEficiencia Calculada: {eficiencia_final:.2f}%"
if metadata and metadata['pm25_real']:
    titulo += f" | PM2.5: {metadata['pm25_real']} µg/m³"

plt.figure(figsize=(7, 9))
plt.title(titulo)
plt.xlabel("Ancho de la Torre")
plt.ylabel("Altura (Ascenso del Aire)")

# Graficar partículas atrapadas (Azul = Agua sucia/Lodo)
plt.scatter(x[estado==0], y[estado==0], color='#0077be', s=10, alpha=0.4, label='Partículas Atrapadas')

# Graficar partículas escapadas (Rojo = Contaminación remanente)
plt.scatter(x[estado==1], y[estado==1], color='#ff4d4d', s=15, label='Partículas Escapadas')

# Dibujar las paredes de la torre (Referencia visual)
plt.plot([-ANCHO_BASE/2, -ANCHO_CUELLO/2], [0, ALTURA_TORRE], 'k--', linewidth=3, alpha=0.7) 
plt.plot([ANCHO_BASE/2, ANCHO_CUELLO/2], [0, ALTURA_TORRE], 'k--', linewidth=3, alpha=0.7)

plt.ylim(0, ALTURA_TORRE + 10)
plt.legend(loc='lower right')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()
