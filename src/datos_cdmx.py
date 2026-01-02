import requests
import json
from datetime import datetime
import os

# --- CONFIGURACIÓN ---
API_URL = "https://api.waqi.info/feed/mexico-city/?token="
TOKEN_FILE = "api_token.txt"
OUTPUT_FILE = "escenarios_cdmx.json"

def cargar_token():
    """Carga el API token desde archivo"""
    if not os.path.exists(TOKEN_FILE):
        raise FileNotFoundError(f"⚠️  No se encontró '{TOKEN_FILE}'. Crea el archivo con tu token de AQICN.")
    
    with open(TOKEN_FILE, 'r') as f:
        token = f.read().strip()
    return token

def obtener_datos_cdmx(token):
    """Obtiene datos en tiempo real de CDMX desde AQICN API"""
    url = API_URL + token
    
    print("🌐 Consultando API de AQICN...")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data['status'] != 'ok':
            raise Exception(f"Error en API: {data.get('data', 'Sin mensaje')}")
        
        return data['data']
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error de conexión: {e}")

def extraer_metricas(data):
    """Extrae las métricas relevantes del JSON de respuesta"""
    metricas = {
        'aqi': data.get('aqi', 'N/A'),
        'pm25': data['iaqi'].get('pm25', {}).get('v', None),
        'pm10': data['iaqi'].get('pm10', {}).get('v', None),
        'temperatura': data['iaqi'].get('t', {}).get('v', None),
        'humedad': data['iaqi'].get('h', {}).get('v', None),
        'viento': None,  # AQICN puede no tener datos de viento
        'timestamp': data['time']['s'],
        'estacion': data['city']['name']
    }
    
    # Intenta obtener datos de viento si están disponibles
    if 'w' in data['iaqi']:
        metricas['viento'] = data['iaqi']['w'].get('v', None)
    
    return metricas

def calcular_parametros_modelo(metricas):
    """
    Convierte datos reales a parámetros del modelo de simulación
    
    Mapeo:
    - PM2.5 (µg/m³) → NUM_PARTICULAS
    - Viento (m/s) → VELOCIDAD_VIENTO del modelo
    """
    pm25 = metricas['pm25']
    viento = metricas.get('viento')
    
    # MAPEO PM2.5 → NUM_PARTICULAS
    if pm25 is None:
        num_particulas = 2000  # Valor por defecto
        categoria = "Sin datos"
    elif pm25 <= 50:
        num_particulas = int(500 + (pm25 / 50) * 1500)  # 500-2000
        categoria = "Buena"
    elif pm25 <= 100:
        num_particulas = int(2000 + ((pm25 - 50) / 50) * 3000)  # 2000-5000
        categoria = "Moderada"
    elif pm25 <= 150:
        num_particulas = int(5000 + ((pm25 - 100) / 50) * 3000)  # 5000-8000
        categoria = "Mala"
    else:
        num_particulas = int(8000 + min((pm25 - 150) / 50, 5) * 1400)  # 8000-15000
        categoria = "Contingencia"
    
    # MAPEO VIENTO → VELOCIDAD_VIENTO (Estimación si no hay datos)
    if viento is None:
        # Si no hay datos de viento, estimamos basado en la calidad del aire
        # (Mayor contaminación suele correlacionar con menos viento)
        if pm25 is None or pm25 < 75:
            velocidad_viento = 1.5  # Condiciones normales
        else:
            velocidad_viento = 0.8  # Menor viento en alta contaminación
        viento_estimado = True
    else:
        # Conversión directa: velocidad real (m/s) → parámetro del modelo
        if viento <= 2:
            velocidad_viento = 0.3 + (viento / 2) * 0.5  # 0.3-0.8
        elif viento <= 4:
            velocidad_viento = 0.8 + ((viento - 2) / 2) * 0.7  # 0.8-1.5
        else:
            velocidad_viento = 1.5 + min((viento - 4) / 2, 2) * 1.0  # 1.5-2.5
        viento_estimado = False
    
    return {
        'num_particulas': num_particulas,
        'velocidad_viento': round(velocidad_viento, 2),
        'pm25_real': pm25,
        'viento_real': viento,
        'viento_estimado': viento_estimado,
        'categoria_calidad': categoria,
        'eficiencia_red': 0.7,  # Mantener valor base
        'ancho_cuello': 10      # Mantener geometría base
    }

def guardar_escenarios(metricas, parametros):
    """Guarda los datos en archivo JSON reutilizable"""
    escenarios = {
        'ultima_actualizacion': datetime.now().isoformat(),
        'estacion': metricas['estacion'],
        'timestamp_medicion': metricas['timestamp'],
        'escenario_actual': parametros,
        'datos_atmosfericos_crudos': {
            'aqi': metricas['aqi'],
            'pm25': metricas['pm25'],
            'pm10': metricas['pm10'],
            'temperatura': metricas['temperatura'],
            'humedad': metricas['humedad'],
            'viento': metricas['viento']
        }
    }
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(escenarios, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Datos guardados en '{OUTPUT_FILE}'")

def imprimir_reporte(metricas, parametros):
    """Muestra un reporte formateado en consola"""
    print("\n" + "="*60)
    print("📊 REPORTE DE DATOS REALES - CIUDAD DE MÉXICO")
    print("="*60)
    print(f"🏙️  Estación: {metricas['estacion']}")
    print(f"🕐 Timestamp: {metricas['timestamp']}")
    print(f"📈 AQI (Índice): {metricas['aqi']}")
    print()
    print("--- DATOS ATMOSFÉRICOS CRUDOS ---")
    print(f"   PM2.5: {metricas['pm25']} µg/m³")
    print(f"   PM10:  {metricas['pm10']} µg/m³")
    print(f"   Temperatura: {metricas['temperatura']}°C")
    print(f"   Humedad: {metricas['humedad']}%")
    
    if metricas['viento'] is not None:
        print(f"   Viento: {metricas['viento']} m/s")
    else:
        print(f"   Viento: N/A (estimado para el modelo)")
    
    print()
    print("--- PARÁMETROS CALIBRADOS PARA EL MODELO ---")
    print(f"   NUM_PARTICULAS: {parametros['num_particulas']}")
    print(f"   VELOCIDAD_VIENTO: {parametros['velocidad_viento']}")
    print(f"   Categoría de Calidad: {parametros['categoria_calidad']}")
    
    if parametros['viento_estimado']:
        print(f"   ⚠️  Viento estimado (no hay datos directos)")
    
    print("="*60 + "\n")

def main():
    """Función principal"""
    try:
        # 1. Cargar token
        token = cargar_token()
        
        # 2. Obtener datos
        data = obtener_datos_cdmx(token)
        
        # 3. Extraer métricas
        metricas = extraer_metricas(data)
        
        # 4. Calcular parámetros
        parametros = calcular_parametros_modelo(metricas)
        
        # 5. Guardar y reportar
        guardar_escenarios(metricas, parametros)
        imprimir_reporte(metricas, parametros)
        
        print("✅ Proceso completado exitosamente.")
        print(f"💡 Ahora puedes ejecutar 'python simulacion_torre.py' con MODO_DATOS='cdmx_real'")
        
    except FileNotFoundError as e:
        print(f"❌ {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
