import json
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# ==============================================================================
# --- VISUALIZACIÓN MULTI-ESCALA: DÍA / SEMANA / MES / AÑO ---
# ==============================================================================

print("📊 Cargando datos históricos...")

# Cargar datos
with open('src/datos_historicos_2026.json', 'r') as f:
    data = json.load(f)

# Extraer datos diarios
fechas_str = data['datos_diarios']['fechas']
fechas = [datetime.strptime(f, '%Y-%m-%d') for f in fechas_str]
pm25_diario = np.array(data['datos_diarios']['pm25'])
co2_diario = np.array(data['datos_diarios']['co2_capturado'])
agua_diaria = np.array(data['datos_diarios']['agua_captada'])

# Extraer agregaciones
pm25_semanal = data['agregaciones']['semanal']['pm25']
co2_semanal = data['agregaciones']['semanal']['co2']
agua_semanal = data['agregaciones']['semanal']['agua']

pm25_mensual = data['agregaciones']['mensual']['pm25']
co2_mensual = data['agregaciones']['mensual']['co2']
agua_mensual = data['agregaciones']['mensual']['agua']

pm25_anual = data['agregaciones']['anual']['pm25']
co2_anual = data['agregaciones']['anual']['co2']
agua_anual = data['agregaciones']['anual']['agua']
energia_anual = data['agregaciones']['anual']['energia']

print(f"✅ Datos cargados: {len(fechas)} días procesados")

# ==============================================================================
# --- GRÁFICAS COMPARATIVAS ---
# ==============================================================================

fig = plt.figure(figsize=(18, 12))
fig.suptitle('PROYECTO TLAZOLTÉOTL - ANÁLISIS HISTÓRICO 2026 CDMX', 
             fontsize=18, fontweight='bold', y=0.995)

# ============ FILA 1: CONTAMINACIÓN (PM2.5) ============

# Subplot 1: PM2.5 Diario
ax1 = plt.subplot(3, 4, 1)
ax1.plot(fechas, pm25_diario, color='red', alpha=0.6, linewidth=0.8)
ax1.axhline(y=75, color='orange', linestyle='--', label='Moderado', linewidth=1.5)
ax1.axhline(y=150, color='red', linestyle='--', label='Mala', linewidth=1.5)
ax1.set_title('PM2.5 Diario', fontweight='bold')
ax1.set_ylabel('PM2.5 (µg/m³)')
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.3)
ax1.tick_params(axis='x', rotation=45)

# Subplot 2: PM2.5 Semanal
ax2 = plt.subplot(3, 4, 2)
ax2.bar(range(1, 53), pm25_semanal, color='crimson', alpha=0.7, edgecolor='darkred')
ax2.axhline(y=75, color='orange', linestyle='--', linewidth=1.5)
ax2.set_title('PM2.5 Promedio Semanal', fontweight='bold')
ax2.set_xlabel('Semana del Año')
ax2.set_ylabel('PM2.5 (µg/m³)')
ax2.grid(True, alpha=0.3, axis='y')

# Subplot 3: PM2.5 Mensual
ax3 = plt.subplot(3, 4, 3)
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
colores_meses = ['#d73027', '#fc8d59', '#fee08b', '#d9ef8b', '#91cf60', '#1a9850',
                 '#1a9850', '#91cf60', '#d9ef8b', '#fee08b', '#fc8d59', '#d73027']
ax3.bar(meses, pm25_mensual, color=colores_meses, edgecolor='black', linewidth=1.2)
ax3.axhline(y=75, color='orange', linestyle='--', linewidth=1.5)
ax3.set_title('PM2.5 Promedio Mensual', fontweight='bold')
ax3.set_ylabel('PM2.5 (µg/m³)')
ax3.tick_params(axis='x', rotation=45)
ax3.grid(True, alpha=0.3, axis='y')

# Subplot 4: PM2.5 Anual + Comparativa
ax4 = plt.subplot(3, 4, 4)
ax4.bar(['CDMX 2026\n(Real)', 'Objetivo\nOMS'], [pm25_anual, 10], 
        color=['orangered', 'green'], edgecolor='black', linewidth=2)
ax4.set_title('PM2.5 Anual vs. OMS', fontweight='bold')
ax4.set_ylabel('PM2.5 (µg/m³)')
ax4.text(0, pm25_anual + 5, f'{pm25_anual:.1f}', ha='center', fontweight='bold', fontsize=12)
ax4.text(1, 15, '10', ha='center', fontweight='bold', fontsize=12)
ax4.grid(True, alpha=0.3, axis='y')

# ============ FILA 2: CO2 CAPTURADO ============

# Subplot 5: CO2 Diario
ax5 = plt.subplot(3, 4, 5)
ax5.fill_between(fechas, co2_diario, color='green', alpha=0.4)
ax5.plot(fechas, co2_diario, color='darkgreen', linewidth=1)
ax5.set_title('CO2 Capturado Diario', fontweight='bold')
ax5.set_ylabel('CO2 (kg/día)')
ax5.grid(True, alpha=0.3)
ax5.tick_params(axis='x', rotation=45)

# Subplot 6: CO2 Semanal
ax6 = plt.subplot(3, 4, 6)
co2_semanal_kg = [c for c in co2_semanal]  # Ya en kg
ax6.bar(range(1, 53), co2_semanal_kg, color='forestgreen', alpha=0.7, edgecolor='darkgreen')
ax6.set_title('CO2 Capturado Semanal', fontweight='bold')
ax6.set_xlabel('Semana del Año')
ax6.set_ylabel('CO2 (kg/semana)')
ax6.grid(True, alpha=0.3, axis='y')

# Subplot 7: CO2 Mensual
ax7 = plt.subplot(3, 4, 7)
ax7.bar(meses, co2_mensual, color='seagreen', edgecolor='darkgreen', linewidth=1.2)
ax7.set_title('CO2 Capturado Mensual', fontweight='bold')
ax7.set_ylabel('CO2 (kg/mes)')
ax7.tick_params(axis='x', rotation=45)
ax7.grid(True, alpha=0.3, axis='y')

# Subplot 8: CO2 Anual + Equivalencia
ax8 = plt.subplot(3, 4, 8)
arboles_equivalentes = co2_anual / 0.02  # 1 árbol = ~20kg CO2/año
ax8.bar(['CO2 Total\n2026'], [co2_anual], color='darkgreen', edgecolor='black', linewidth=2, width=0.4)
ax8.set_title('CO2 Anual Capturado', fontweight='bold')
ax8.set_ylabel('CO2 (Toneladas/año)')
ax8.text(0, co2_anual + 0.05, f'{co2_anual:.2f} ton\n≈{int(arboles_equivalentes)} árboles', 
         ha='center', fontweight='bold', fontsize=10)
ax8.grid(True, alpha=0.3, axis='y')

# ============ FILA 3: AGUA COSECHADA ============

# Subplot 9: Agua Diaria
ax9 = plt.subplot(3, 4, 9)
ax9.fill_between(fechas, agua_diaria, color='dodgerblue', alpha=0.4)
ax9.plot(fechas, agua_diaria, color='darkblue', linewidth=1)
ax9.set_title('Agua Cosechada Diaria', fontweight='bold')
ax9.set_ylabel('Agua (L/día)')
ax9.grid(True, alpha=0.3)
ax9.tick_params(axis='x', rotation=45)

# Subplot 10: Agua Semanal
ax10 = plt.subplot(3, 4, 10)
ax10.bar(range(1, 53), agua_semanal, color='deepskyblue', alpha=0.7, edgecolor='darkblue')
ax10.set_title('Agua Cosechada Semanal', fontweight='bold')
ax10.set_xlabel('Semana del Año')
ax10.set_ylabel('Agua (L/semana)')
ax10.grid(True, alpha=0.3, axis='y')

# Subplot 11: Agua Mensual
ax11 = plt.subplot(3, 4, 11)
ax11.bar(meses, agua_mensual, color='steelblue', edgecolor='darkblue', linewidth=1.2)
ax11.set_title('Agua Cosechada Mensual', fontweight='bold')
ax11.set_ylabel('Agua (L/mes)')
ax11.tick_params(axis='x', rotation=45)
ax11.grid(True, alpha=0.3, axis='y')

# Subplot 12: Resumen Anual
ax12 = plt.subplot(3, 4, 12)
ax12.axis('off')
resumen_texto = f"""
RESUMEN ANUAL 2026
{'='*30}

🌬️  PM2.5 Promedio CDMX
   {pm25_anual:.1f} µg/m³

🌿 CO2 Capturado
   {co2_anual:.2f} toneladas
   ({int(arboles_equivalentes)} árboles equiv.)

💧 Agua Cosechada
   {agua_anual:,.0f} litros
   ({agua_anual/365:.0f} L/día promedio)

⚡ Energía Generada
   {energia_anual:,.0f} kWh
   (Autosustentable)

{'='*30}
PROYECTO TLAZOLTÉOTL
Alameda Central, CDMX
"""
ax12.text(0.1, 0.95, resumen_texto, transform=ax12.transAxes, 
          fontsize=11, verticalalignment='top', fontfamily='monospace',
          bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout(rect=[0, 0, 1, 0.99])
plt.savefig('results/Validacion_2026.png', dpi=150, bbox_inches='tight')
print(f"\n✅ Gráfica guardada: 'results/Validacion_2026.png'")
plt.show()

print("\n" + "="*60)
print("📊 ANÁLISIS COMPLETADO")
print("="*60)
print(f"Archivos generados:")
print(f"  - src/datos_historicos_2026.json (datos base)")
print(f"  - results/Validacion_2026.png (visualización)")
print("="*60)
