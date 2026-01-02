import os

# --- PATHS ---
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")
RESULTS_DIR = os.path.join(PROJECT_ROOT, "results")

# Data files
ESCENARIOS_JSON = os.path.join(SRC_DIR, "escenarios_cdmx.json")
HISTORICO_JSON = os.path.join(SRC_DIR, "datos_historicos_2026.json")
API_TOKEN_FILE = os.path.join(SRC_DIR, "api_token.txt")

# Result files
VALIDACION_PNG = os.path.join(RESULTS_DIR, "Validacion_2026.png")
SIMULACION_ANUAL_PNG = os.path.join(RESULTS_DIR, "Simulacion_Anual.png")
POSTER_JPG = os.path.join(RESULTS_DIR, "Project_Tlazolteotl_Elon_Pager.jpg")
BLUEPRINT_JPG = os.path.join(DOCS_DIR, "Blueprint_V1.jpg")

# --- PHYSICS CONSTANTS (v2.0 - Master Technical Datasheet) ---

# Tower Geometry
ALTURA_TORRE = 100  # meters
ANCHO_BASE = 40  # meters
ANCHO_CUELLO = 10  # meters
PROFUNDIDAD_CIMENTACION = 8  # meters (cisterna subterránea)
DIAMETRO_LOSA = 45  # meters

# Aerodynamics & Mass Balance
DENSIDAD_AIRE = 0.95  # kg/m³
VELOCIDAD_INTAKE = 1.5  # m/s (passive thermal suction)
VELOCIDAD_THROAT = 12.0  # m/s (Venturi acceleration)
FLUJO_AIRE_DIARIO = 9.3e6  # m³/día (validated)
DELTA_T_TERMICA = 7  # °C (urban heat island effect)

# CO2 Capture (Biological)
CO2_EN_AIRE = 0.00075  # kg/m³ (415 ppm atmospheric concentration)
TASA_ABSORCION_AGUA = 0.40  # 40% CO2 dissolves in water curtain
RATIO_ALGAS_CO2 = 1.8  # 1kg Spirulina consumes 1.8kg CO2
BIOMASA_DIARIA = 8.8  # kg/día (peso seco Spirulina)

# Water Balance
CAPTACION_WARKA = 0.5  # L/m² (fog collection)
AGUA_NEBULIZACION = 2160  # L/día (1.5 L/min recirculación)
AGUA_EVAPORACION = 350  # L/día (pérdida según HR)
AGUA_PURGA = 430  # L/día (20% a biorreactor)
AGUA_NETA_COSECHADA = 6289  # L/día (disponible)

# Electrostatic Precipitation (ESP)
VOLTAJE_OPERACION = 45  # kV (operating voltage)
CORRIENTE_MAXIMA = 0.005  # A (5 mA safety limit)
POTENCIA_IONIZACION = 90  # Watts (incluye pérdidas corona)
RESISTENCIA_TIERRA_MAX = 2  # Ohms
DIAMETRO_ELECTRODO_TUNGSTENO = 0.25  # mm
ALTURA_ESP_ANILLO = 3.5  # metros del suelo

# Nebulization (Wet Scrubber)
DROPLET_SIZE_MIN = 10  # microns
DROPLET_SIZE_MAX = 20  # microns
DROPLET_SIZE_OPTIMAL = 15  # microns (sweet spot - máxima captura inercial)
PRESION_NEBULIZACION = 70  # bar (1000 psi)
RATIO_LIQUIDO_GAS = 1.2  # L/m³ (L/G ratio)

# Bioreactor
VOLUMEN_BIORREACTOR = 5000  # Litros (tanque subterráneo)
TIEMPO_RETENCION_HIDRAULICA = 48  # horas
PH_SPIRULINA_OPTIMO = 10.0  # pH alcalino
TEMP_BIORREACTOR_OPTIMA = 32.5  # °C
TASA_CRECIMIENTO_SPIRULINA = 0.4  # g/L/día

# Energy Generation
POTENCIA_TURBINA_MIN = 80  # Watts (VAWT output range)
POTENCIA_TURBINA_MAX = 150  # Watts
VIENTO_INICIO_TURBINA = 0.5  # m/s (MagLev bearing threshold)

# Structural Materials
DIAMETRO_BAMBU_PRINCIPAL = 16.5  # cm (promedio 15-18)
DIAMETRO_BAMBU_SECUNDARIO = 11  # cm (promedio 10-12)
ESPESOR_ETFE = 0.2  # mm (por capa)
AREA_PIEL_ETFE = 3800  # m²

# Maintenance & OPEX
COSTO_OPEX_ANUAL = 20300  # USD/año
COSTO_CAPEX_TORRE = 350000  # USD (inversión inicial)
VIDA_UTIL_BAMBU = 50  # años (con tratamiento)
VIDA_UTIL_ETFE = 30  # años
