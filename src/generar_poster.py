from PIL import Image, ImageDraw, ImageFont
import os

# --- CONFIGURACIÓN ---
# Usamos el plano real subido por el usuario y los resultados de validación
FILE_1 = "docs/Blueprint_V1.jpg"
FILE_2 = "results/Validacion_2026.png"

OUTPUT_NAME = "results/Project_Tlazolteotl_Elon_Pager.jpg"

def crear_poster():
    print("🎨 Generando Lámina Maestra de Proyecto Tlazoltéotl...")
    
    # 1. Cargar imágenes
    if not os.path.exists(FILE_1) or not os.path.exists(FILE_2):
        print(f"❌ ERROR: No encuentro los archivos {FILE_1} o {FILE_2}.")
        return

    img1 = Image.open(FILE_1)
    img2 = Image.open(FILE_2)

    # 2. Redimensionar para que tengan la misma altura
    # Vamos a usar una altura fija de 1200px para buena calidad
    target_height = 1200
    
    # Calcular nuevos anchos manteniendo proporción
    aspect1 = img1.width / img1.height
    aspect2 = img2.width / img2.height
    
    new_w1 = int(target_height * aspect1)
    new_w2 = int(target_height * aspect2)
    
    img1 = img1.resize((new_w1, target_height), Image.Resampling.LANCZOS)
    img2 = img2.resize((new_w2, target_height), Image.Resampling.LANCZOS)

    # 3. Crear lienzo vacío (Ancho total + margen)
    total_width = new_w1 + new_w2 + 40
    canvas = Image.new('RGB', (total_width, target_height + 200), (10, 15, 25)) # Fondo azul marino muy oscuro
    draw = ImageDraw.Draw(canvas)

    # 4. Pegar imágenes
    canvas.paste(img1, (20, 160))
    canvas.paste(img2, (new_w1 + 20, 160))

    # 5. Agregar Encabezado de Ingeniería
    try:
        # Intentar cargar fuentes del sistema (Windows)
        font_title = ImageFont.truetype("arialbd.ttf", 70) # Bold
        font_sub = ImageFont.truetype("arial.ttf", 35)
    except:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    # Título y Subtítulo
    title_text = "PROJECT TLAZOLTÉOTL: URBAN TERRAFORMING SYSTEM"
    subtitle_text = "VALIDATION 2026 (BASED ON 2025 CDMX DATA): 10,204 TONS CO2 REMOVED | 1.8M L WATER | ZERO ENERGY"
    
    # Dibujar texto centrado
    title_bbox = draw.textbbox((0, 0), title_text, font=font_title)
    title_w = title_bbox[2] - title_bbox[0]
    draw.text(((total_width - title_w) // 2, 30), title_text, fill=(0, 255, 255), font=font_title) # Cyan Neon
    
    sub_bbox = draw.textbbox((0, 0), subtitle_text, font=font_sub)
    sub_w = sub_bbox[2] - sub_bbox[0]
    draw.text(((total_width - sub_w) // 2, 110), subtitle_text, fill=(255, 255, 255), font=font_sub) # Blanco

    # Créditos en el pie
    footer_text = "SIMULATED DATA BASED ON CDMX ATMOSPHERIC PATTERNS | ALAMEDA CENTRAL DEPLOYMENT CASE STUDY"
    footer_bbox = draw.textbbox((0, 0), footer_text, font=font_sub)
    footer_w = footer_bbox[2] - footer_bbox[0]
    draw.text(((total_width - footer_w) // 2, target_height + 170), footer_text, fill=(150, 150, 150), font=font_sub)

    # 6. Guardar
    canvas.save(OUTPUT_NAME, quality=95)
    print(f"✅ ¡LISTO! Imagen guardada como: {OUTPUT_NAME}")
    print("   Ahora tienes la evidencia definitiva combinando simulación y análisis.")

if __name__ == "__main__":
    crear_poster()
