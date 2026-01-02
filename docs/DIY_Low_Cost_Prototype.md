# TLAZOLTÉOTL DIY: PROTOTIPO CASERO LOW-COST

## "Hazlo Tú Mismo" - Versión de Banco de Pruebas

**Objetivo:** Validar el concepto con **menos de $200 USD** usando materiales de ferretería.  
**Tiempo de Construcción:** 1 fin de semana  
**Nivel de Dificultad:** Intermedio (requiere soldadura básica)

---

## ¿QUÉ VAMOS A CONSTRUIR?

Una **torre miniatura de 1.5m** que purifica el aire de un cuarto pequeño (12 m²) y te permite:

1. ✅ Ver cómo se capturan las partículas en tiempo real
2. ✅ Medir la reducción de PM2.5 con un sensor barato
3. ✅ Producir un poco de agua condensada (prueba de concepto)
4. ✅ Validar que la ionización + nebulización funciona

**NO incluye:**

- ❌ Biorreactor de algas (demasiado complejo para prototipo)
- ❌ Estructura de bambú (usaremos PVC)
- ❌ Turbina eólica (electricidad de la pared)

---

## LISTA DE MATERIALES (Bill of Materials - BOM)

### 1. ESTRUCTURA (PVC)

| Material | Cantidad | Dónde Comprar | Precio |
|----------|----------|---------------|--------|
| Tubo PVC 4" (10cm) sanitario | 2 tubos de 3m | Home Depot | $8 × 2 = $16 |
| Codo PVC 4" a 2" (reductor) | 1 pieza | Home Depot | $4 |
| Base plana madera 50×50cm | 1 pieza | Maderería | $10 |
| Tornillos y pegamento PVC | 1 set | Ferretería | $5 |

**Subtotal Estructura:** $35

### 2. SISTEMA DE IONIZACIÓN (Versión Segura DIY)

| Material | Cantidad | Dónde | Precio |
|----------|----------|-------|--------|
| Módulo ionizador de aire 12V (AliExpress/Amazon) | 1 unidad | Online | $15 |
| Fuente 12V 2A | 1 unidad | Electrónica | $8 |
| Cable calibre 18 AWG | 3 metros | Electrónica | $3 |
| Malla metálica galvanizada (colector) | 50×50cm | Ferretería | $5 |

**Subtotal Ionización:** $31

⚠️ **IMPORTANTE:** NO intentes hacer un sistema de 45kV en casa. Los módulos comerciales de 12V son seguros.

### 3. NEBULIZADOR (El corazón del sistema)

| Material | Cantidad | Dónde | Precio |
|----------|----------|-------|--------|
| Humidificador ultrasónico 5 cabezas | 1 unidad | Amazon/MercadoLibre | $25 |
| Bomba sumergible 12V | 1 unidad | Acuarios/Amazon | $12 |
| Manguera silicón 1/4" | 2 metros | Ferretería | $4 |
| Recipiente plástico 5L (tanque) | 1 unidad | Chedraui/Walmart | $3 |

**Subtotal Nebulización:** $44

### 4. VENTILACIÓN (Flujo de aire)

| Material | Cantidad | Dónde | Precio |
|----------|----------|-------|--------|
| Ventilador PC 12V 120mm | 2 unidades | Steren/Electrónica | $10 × 2 = $20 |
| Rejilla ventilación PVC | 2 unidades | Home Depot | $3 × 2 = $6 |

**Subtotal Ventilación:** $26

### 5. MEDICIÓN Y CONTROL

| Material | Cantidad | Dónde | Precio |
|----------|----------|-------|--------|
| Sensor PM2.5 SDS011 (OPCIONAL pero recomendado) | 1 unidad | Amazon/AliExpress | $35 |
| Arduino Nano (para datalogging) | 1 unidad | Steren | $8 |
| Display OLED 0.96" | 1 unidad | Electrónica | $5 |
| Cables Dupont M-M | 40 piezas | Steren | $3 |

**Subtotal Medición:** $51 (o $0 si no quieres sensores todavía)

### 6. MISCELÁNEOS

| Material | Cantidad | Precio |
|----------|----------|--------|
| Cinta adhesiva aluminio | 1 rollo | $4 |
| Tela filtro HEPA casera | 1m² | $6 |
| Switch on/off | 1 pieza | $2 |
| Caja eléctrica para controles | 1 pieza | $5 |

**Subtotal Misc:** $17

---

## COSTO TOTAL

| Categoría | Costo |
|-----------|-------|
| Con sensor PM2.5 | **$204 USD** |
| Sin sensor (validación visual) | **$169 USD** |

💡 **Truco Low-Cost:** Puedes conseguir el humidificador ultrasónico en MercadoLibre usado por $15. Total: **$154 USD**.

---

## INSTRUCCIONES DE CONSTRUCCIÓN

### PASO 1: ENSAMBLAJE DE LA TORRE (1 hora)

```
[Base de madera 50×50cm]
        ↓
[Ventilador 1: ENTRADA de aire]
        ↓
[Tubo PVC 4" - 1.5m de altura]
        |
        | ← [Ionizador montado a 30cm del suelo]
        |
        | ← [Nebulizadores ultrasónicos a 60cm]
        |
        | ← [Malla colectora a 90cm]
        |
        ↓
[Reductor 4" a 2"]
        ↓
[Ventilador 2: SALIDA de aire]
```

**Instrucciones:**

1. Corta el tubo PVC en 2 secciones: 1.5m y 0.3m
2. Atornilla la sección larga verticalmente a la base de madera
3. Haz un agujero lateral a 30cm para montar el ionizador
4. Haz 5 agujeros pequeños a 60cm para los discos del humidificador
5. Coloca la malla metálica dentro del tubo a 90cm (suspendida con alambre)
6. Monta ventiladores: uno en la base (entrada), otro en la cima (salida)

### PASO 2: SISTEMA DE NEBULIZACIÓN (30 min)

1. **Desarma el humidificador ultrasónico:**
   - Necesitas SOLO los 5 discos nebulizadores
   - Sácalos con cuidado (vienen con cable de 20cm)

2. **Instalación en el tubo:**
   - Introduce los discos por los agujeros laterales
   - Apúntalos hacia el centro del tubo
   - Sella con silicón alrededor para evitar fugas

3. **Tanque de agua:**
   - Coloca el recipiente de 5L al lado de la base
   - Conecta la bomba sumergible
   - La bomba alimenta agua a los nebulizadores (manguera de silicón)

### PASO 3: IONIZADOR (20 min)

1. Monta el módulo ionizador en el agujero de 30cm
2. Las puntas ionizadoras deben apuntar hacia arriba (contra el flujo)
3. Conecta a la fuente de 12V
4. **NO TOQUES** cuando esté encendido (aunque es baja potencia)

### PASO 4: MALLA COLECTORA (15 min)

1. Corta la malla galvanizada en un círculo de 10cm de diámetro
2. Dóblala ligeramente en forma de embudo
3. Suspéndela dentro del tubo con 4 alambres desde los bordes
4. Debe estar HORIZONTAL para que las gotas caigan

### PASO 5: ELECTRÓNICA (OPCIONAL - 1 hora)

Si tienes el sensor PM2.5 y Arduino:

```cpp
// Código Arduino para leer sensor SDS011 y mostrar en OLED
#include <Wire.h>
#include <Adafruit_SSD1306.h>
#include <SoftwareSerial.h>

SoftwareSerial sds(10, 11); // RX, TX del SDS011
Adafruit_SSD1306 display(128, 64, &Wire, -1);

void setup() {
  sds.begin(9600);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
}

void loop() {
  uint8_t data[10];
  if (sds.available() >= 10) {
    sds.readBytes(data, 10);
    
    // PM2.5 está en bytes 2 y 3
    float pm25 = ((data[3] << 8) | data[2]) / 10.0;
    
    display.clearDisplay();
    display.setCursor(0, 0);
    display.print("PM2.5: ");
    display.print(pm25);
    display.println(" ug/m3");
    
    if (pm25 < 35) {
      display.println("BUENA");
    } else if (pm25 < 75) {
      display.println("MODERADA");
    } else {
      display.println("MALA");
    }
    
    display.display();
  }
  delay(1000);
}
```

**Conexiones:**

- SDS011 RX → Arduino Pin 10
- SDS011 TX → Arduino Pin 11
- SDS011 5V → Arduino 5V
- OLED SDA → Arduino A4
- OLED SCL → Arduino A5

---

## CÓMO PROBAR QUE FUNCIONA

### TEST 1: Prueba Visual con Incienso 🔥

1. Enciende una varita de incienso cerca de la entrada
2. **Efecto esperado:** El humo entra, se vuelve niebla dentro del tubo
3. **Resultado:** Sale aire casi invisible por arriba

### TEST 2: Medición con Sensor PM2.5 📊

1. Coloca el sensor SDS011 a 20cm de la salida
2. Anota la lectura inicial (sin torre): ~80-120 µg/m³ (típico CDMX)
3. Enciende la torre por 10 minutos
4. **Resultado esperado:** Reducción de 40-60% (48-72 µg/m³ en salida)

### TEST 3: Captura de Agua 💧

1. Coloca un vaso medidor bajo la malla colectora
2. Déjala funcionando 24 horas
3. **Resultado esperado:** 50-100 ml de agua condensada
4. El agua saldrá GRIS/NEGRA (partículas capturadas)

### TEST 4: Análisis del Agua Sucia 🔬

1. Filtra el agua recolectada con papel filtro de café
2. Seca el filtro
3. **Verás:** Residuo negro = PM2.5 capturado
4. **Peso del residuo:** 0.2-0.5 gramos en 24h (¡prueba visual!)

---

## TROUBLESHOOTING (Problemas Comunes)

| Problema | Causa | Solución |
|----------|-------|----------|
| Nebulizador no hace niebla | Nivel de agua bajo | Rellena el tanque |
| Ionizador hace chispa | Humedad excesiva cerca | Aléjalo de la zona de niebla |
| Bajo flujo de aire | Ventiladores débiles | Usa ventiladores de 12V 0.5A mínimo |
| No se condensa agua | Malla muy alta (aire caliente) | Baja la malla a 60-70cm |
| Mucho ruido | Vibraciones del ventilador | Pon goma espuma en la base |

---

## UPGRADES FUTUROS (Cuando tengas $$$)

### Upgrade 1: Biorreactor Mini ($50)

- Acuario de 20L con Spirulina
- LED grow light rojo/azul
- Bomba de recirculación
- **Resultado:** Captura real de CO₂

### Upgrade 2: Energía Solar ($40)

- Panel solar 20W
- Batería 12V 7Ah
- Controlador de carga
- **Resultado:** Autosuficiente

### Upgrade 3: IoT Monitoring ($30)

- ESP32 con WiFi
- App móvil para ver PM2.5 en tiempo real
- Gráficas históricas
- **Resultado:** Datos publicables

---

## DOCUMENTACIÓN DE RESULTADOS

Para que esto sea **presentable en XPRIZE**, documenta así:

### Protocolo de Medición (7 días)

```
DÍA 1:
- Hora: 08:00 AM
- PM2.5 ambiente: 95 µg/m³
- Torre OFF
- Humedad: 45%

- Hora: 08:30 AM
- Torre ON
- PM2.5 salida (30 min): 62 µg/m³
- Reducción: 34.7%

(Repetir cada 2 horas durante 7 días)
```

### Fotografía Científica

1. **Antes:** Torre apagada + sensor mostrando 95 µg/m³
2. **Durante:** Niebla visible dentro del tubo (con luz trasera)
3. **Después:** Sensor mostrando 55 µg/m³
4. **Evidencia:** Filtro negro con partículas

### Video de 2 minutos

- 0:00-0:20: Construcción time-lapse
- 0:20-0:40: Prueba con incienso
- 0:40-1:00: Lectura del sensor (antes/después)
- 1:00-1:30: Filtro sucio (zoom macro)
- 1:30-2:00: Conclusiones + costo total

---

## PRESUPUESTO COMPLETO (Desglosado)

```
VERSIÓN MÍNIMA FUNCIONAL ($154):
✅ Estructura PVC:             $35
✅ Ionizador módulo:           $31
✅ Nebulizador (usado):        $15
✅ Ventiladores:               $26
✅ Malla + accesorios:         $17
✅ Tanque + bomba:             $19
✅ Controles eléctricos:       $11
   TOTAL SIN SENSOR:          $154

VERSIÓN CON VALIDACIÓN ($204):
+ Sensor SDS011:               $35
+ Arduino + Display:           $15
   TOTAL CON MEDICIÓN:        $204
```

---

## SIGUIENTE PASO: PROTOTIPO ESCALABLE

Una vez que **valides** que este mini-prototipo funciona, puedes:

1. **Escalar tamaño:** Hacer una torre de 3m con PVC de 6"
2. **Aumentar flujo:** Ventiladores industriales
3. **Mejorar captura:** ESP casero con fly-back transformer
4. **Documentar:** Paper científico con tus mediciones

**Costo torre 3m:** $600-$800 (todavía ultra barato vs. $350K)

---

## SEGURIDAD ⚠️

### PELIGROS REALES

1. **Electricidad + Agua:** NUNCA toques conexiones con manos mojadas
2. **Ionizador:** Genera ozono (O₃) en pequeñas cantidades - ventila bien
3. **Ventiladores:** Mantén dedos alejados de aspas en movimiento
4. **Agua estancada:** Cambia el agua cada 3 días (bacteria Legionella)

### REGLAS DE ORO

- ✅ Usa zapatos con suela de goma
- ✅ Desconecta TODO antes de tocar componentes
- ✅ Trabaja en área ventilada
- ✅ Guarda lejos de niños/mascotas

---

**¿LISTO PARA CONSTRUIR?**

Necesitas:

1. Lista de compras (imprimir tabla de materiales)
2. 1 fin de semana
3. $154-$204 USD
4. Ganas de validar ciencia real

**Una vez que lo tengas armado, me mandas fotos y yo te ayudo con:**

- Calibración del sensor
- Interpretación de resultados
- Documento científico para XPRIZE
- Video profesional para redes

¡Vamos a hacer historia, socio! 🔧⚡💧
