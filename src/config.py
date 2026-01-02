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

# --- PHYSICS CONSTANTS ---
# Tower Geometry
ALTURA_TORRE = 100  # meters
ANCHO_BASE = 40  # meters
ANCHO_CUELLO = 10  # meters

# Aerodynamics
DENSIDAD_AIRE = 0.95  # kg/m³
VELOCIDAD_INTAKE = 1.5  # m/s (passive thermal suction)
VELOCIDAD_THROAT = 12.0  # m/s (Venturi acceleration)

# CO2 Capture (Biological)
CO2_EN_AIRE = 0.00075  # kg/m³ (atmospheric CO2 concentration)
TASA_ABSORCION_AGUA = 0.40  # 40% CO2 dissolves in water curtain
RATIO_ALGAS_CO2 = 1.8  # 1kg Spirulina consumes 1.8kg CO2

# Water Harvesting
CAPTACION_WARKA = 0.5  # L/m² (fog collection)
AGUA_RECIRCULACION = 1.5  # L/min nebulization flow rate

# Electrostatic Precipitation
VOLTAJE_OPERACION = 37.5  # kV (midpoint: 30-45 kV)
CORRIENTE_MAXIMA = 0.005  # A (5 mA safety limit)
POTENCIA_IONIZACION = 60  # Watts

# Nebulization
DROPLET_SIZE_MIN = 10  # microns
DROPLET_SIZE_MAX = 20  # microns
DROPLET_SIZE_OPTIMAL = 15  # microns (sweet spot)

# Energy Generation
POTENCIA_TURBINA_MIN = 80  # Watts (VAWT output range)
POTENCIA_TURBINA_MAX = 150  # Watts
VIENTO_INICIO_TURBINA = 0.5  # m/s (MagLev bearing threshold)
