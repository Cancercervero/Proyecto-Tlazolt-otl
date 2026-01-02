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
ALTURA_TORRE = 100
ANCHO_BASE = 40
ANCHO_CUELLO = 10
DENSIDAD_AIRE = 0.95
CO2_EN_AIRE = 0.00075  # kg/m3
TASA_ABSORCION_AGUA = 0.40
RATIO_ALGAS_CO2 = 1.8  # 1kg algas consume 1.8kg CO2
CAPTACION_WARKA = 0.5  # L/m2
