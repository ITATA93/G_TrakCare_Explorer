# Instrucciones para Crear Flujogramas
## Hospital Provincial de Ovalle - Dr. Antonio Tirado Lanas

## Proceso de Creación de Flujogramas

### 1. Preparación
Antes de crear un flujograma, define:
- **Nombre del proceso**: Título descriptivo del flujo
- **Objetivo**: Qué proceso se está documentando
- **Actores**: Quiénes participan (médicos, enfermeras, pacientes, etc.)
- **Puntos de inicio y fin**: Dónde comienza y termina el proceso

### 2. Estructura del Proyecto

```
ALMA/
├── Flujograma/                # Carpeta principal de flujogramas
│   ├── INSTRUCCIONES.md       # Este archivo - guía de uso
│   ├── _plantilla/            # Plantilla base para nuevos flujogramas
│   │   ├── README.md
│   │   ├── flujograma.md
│   │   └── documentacion.md
│   └── [nombre-proceso]/      # Carpeta por cada proceso
│       ├── README.md          # Metadata del proceso
│       ├── flujograma.md      # Diagrama Mermaid (VERTICAL por defecto)
│       ├── flujograma-horizontal.md  # Diagrama horizontal (opcional)
│       ├── flujograma.png     # Exportación PNG
│       ├── flujograma.svg     # Exportación SVG
│       └── documentacion.md   # Documentación detallada
├── Manuales PDF/              # Manuales fuente del sistema ALMA
│   └── [Varios PDFs de procesos clínicos]
└── Normas_graficas_hospital_Ovalle/  # Manual de identidad visual
    └── manual_normas_hdo.pdf
```

### 3. Orientaciones de Flujogramas

#### Diagrama Vertical (Por Defecto)
- Archivo: `flujograma.md`
- Sintaxis: `flowchart TD` (Top-Down)
- Uso: Procesos lineales, secuencias claras
- Mejor para: Imprimir en formato vertical, visualizar en móviles

#### Diagrama Horizontal (Opcional)
- Archivo: `flujograma-horizontal.md`
- Sintaxis: `flowchart LR` (Left-Right)
- Uso: Procesos con muchas ramificaciones paralelas
- Mejor para: Presentaciones, pantallas anchas

### 4. Formato Mermaid

Ejemplo básico:

\`\`\`mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#E8BB00','primaryTextColor':'#000','primaryBorderColor':'#707372','lineColor':'#707372','secondaryColor':'#508FCF','tertiaryColor':'#42A095','fontSize':'14px','fontFamily':'Arial'}}}%%
flowchart TD
    A[Inicio] --> B{Decisión}
    B -->|Sí| C[Acción 1]
    B -->|No| D[Acción 2]
    C --> E[Fin]
    D --> E
\`\`\`

### 5. Elementos Estándar

#### Formas:
- `([ ])` - Inicio/Fin (óvalo)
- `[ ]` - Proceso/Acción (rectángulo)
- `{ }` - Decisión (rombo)
- `[( )]` - Entrada de datos
- `[/ /]` - Documento

#### Conexiones:
- `-->` - Flujo normal
- `-.->` - Flujo opcional
- `==>` - Flujo importante

### 6. Colores Institucionales (OBLIGATORIO)

**Hospital Provincial de Ovalle - Normas Gráficas**

Todos los flujogramas DEBEN usar los colores institucionales del hospital.

#### Paleta de Colores Oficial:

**Colores principales:**
- 🟡 **Amarillo (#E8BB00)** - PANTONE 130 C - Color principal
- ⚫ **Gris (#707372)** - PANTONE 424 C - Complementario

**Colores complementarios:**
- 🔵 **Azul Saphire (#003E8C)** - PANTONE BLUE 072 C
- 🔵 **Azul Intenso (#0064AA)** - PANTONE 2935 C
- 🔵 **Azul Ocean (#508FCF)** - PANTONE 2925 C
- 🟢 **Verde Mint (#42A095)** - PANTONE 3268 C
- 🟢 **Verde Aqua (#A5CBCA)** - PANTONE 3248 C
- 🟣 **Lavanda (#7A6CA6)** - PANTONE 2587 C
- 🟣 **Violeta (#AD90BE)** - PANTONE 2573 C
- 🔴 **Magenta (#D3006A)** - PANTONE 214 C
- 🟠 **Naranja (#D37F22)** - PANTONE 158 C

#### Configuración de Tema Mermaid:

**SIEMPRE** incluir esta línea al inicio de cada diagrama:

\`\`\`mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#E8BB00','primaryTextColor':'#000','primaryBorderColor':'#707372','lineColor':'#707372','secondaryColor':'#508FCF','tertiaryColor':'#42A095','fontSize':'14px','fontFamily':'Arial'}}}%%
\`\`\`

#### Clases de Estilo Estándar:

\`\`\`mermaid
classDef startEnd fill:#E8BB00,stroke:#707372,stroke-width:3px,color:#000
classDef busqueda fill:#508FCF,stroke:#003E8C,stroke-width:2px,color:#fff
classDef registro fill:#E8BB00,stroke:#D37F22,stroke-width:2px,color:#000
classDef prevision fill:#AD90BE,stroke:#7A6CA6,stroke-width:2px,color:#000
classDef decision fill:#D3006A,stroke:#AD90BE,stroke-width:2px,color:#fff
classDef sistema fill:#42A095,stroke:#A5CBCA,stroke-width:2px,color:#000
classDef alta fill:#D37F22,stroke:#707372,stroke-width:2px,color:#fff
\`\`\`

#### Tipografía:
- **Oficial Hospital**: DIN Pro
- **Complementaria**: Gob.cl
- **En Mermaid**: Arial (por compatibilidad)

### 7. Proceso de Trabajo con el Asistente

Cuando necesites crear un flujograma, proporciona:

1. **Nombre del proceso**
2. **Descripción general**
3. **Pasos principales** (puedes listarlos o describir el flujo)
4. **Puntos de decisión** (si/no, opciones múltiples)
5. **Actores involucrados**
6. **Casos especiales o excepciones**
7. **Orientación preferida** (vertical u horizontal)

El asistente te ayudará a:
- Estructurar el flujograma
- Generar el código Mermaid con colores institucionales
- Aplicar normas gráficas del hospital
- Documentar el proceso
- Crear archivos organizados
- Generar imágenes PNG y SVG
- Versionar cambios en GitHub

### 8. Revisión y Validación

Antes de confirmar:
- ✅ Verificar colores institucionales aplicados
- ✅ Todos los caminos llegan a un fin
- ✅ Las decisiones tienen todas sus salidas
- ✅ Nombres claros y descriptivos
- ✅ Ortografía y terminología médica correcta
- ✅ El flujo es lógico
- ✅ Incluye encabezado "Hospital Provincial de Ovalle"

### 9. Exportación de Imágenes

Usar Mermaid CLI para generar imágenes:

\`\`\`bash
# PNG
mmdc -i flujograma.md -o flujograma.png -t neutral -b transparent

# SVG
mmdc -i flujograma.md -o flujograma.svg -t neutral -b transparent
\`\`\`

### 10. Commit y Sincronización

Una vez creado y revisado:
- El asistente hará commit con descripción clara
- Se sincronizará automáticamente con GitHub
- Quedará documentado en el historial

---

## Ejemplo Rápido

**Usuario dice:**
"Necesito un flujograma para el proceso de admisión de pacientes en urgencias"

**Asistente ayudará a:**
1. Crear carpeta `admision-urgencias/`
2. Generar estructura de archivos
3. Construir diagrama Mermaid con colores institucionales
4. Aplicar normas gráficas del Hospital Provincial de Ovalle
5. Documentar el proceso
6. Generar imágenes PNG y SVG
7. Hacer commit y push

---

## Comandos Útiles

- **Ver flujograma en GitHub**: Los archivos `.md` con Mermaid se renderizan automáticamente
- **Editar flujograma**: Modificar el archivo `flujograma.md`
- **Nueva versión**: Guardar copia en `versiones/` antes de cambios mayores
- **Generar imagen**: `mmdc -i flujograma.md -o flujograma.png`
- **Ver manual de normas**: Revisar `Normas_graficas_hospital_Ovalle/manual_normas_hdo.pdf`

---

## Referencias

- **Manual de Normas Gráficas**: `Normas_graficas_hospital_Ovalle/manual_normas_hdo.pdf`
- **Manuales ALMA**: `Manuales PDF/`
- **Sintaxis Mermaid**: https://mermaid.js.org/
- **Mermaid CLI**: https://github.com/mermaid-js/mermaid-cli

---

**¿Listo para crear tu primer flujograma?**

Solo describe el proceso y el asistente te guiará paso a paso, aplicando automáticamente las normas gráficas del Hospital Provincial de Ovalle.
