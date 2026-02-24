# G_TrakCare_Explorer

> Satellite project in the Antigravity ecosystem — Gemini CLI variant.

**Domain:** `01_HOSPITAL_PRIVADO`
**Status:** Active
**Orchestrator:** GEN_OS
**Prefix:** G_
**AG Counterpart:** `AG_TrakCare_Explorer`

## Proposito

Explorador de TrakCare/ALMA -- documentacion tecnica, flujogramas de procesos
clinicos, manuales de usuario y normas graficas del Hospital de Ovalle.
Incluye wiki local con MkDocs para capacitacion del personal.

- Flujogramas de procesos clinicos y administrativos del HIS
- Manuales PDF de capacitacion para usuarios de TrakCare
- Normas graficas institucionales del Hospital de Ovalle
- Wiki local navegable con MkDocs (recarga automatica)

## Arquitectura

```
G_TrakCare_Explorer/
├── .gemini/                          # Configuracion Gemini CLI
├── .claude/                          # Configuracion Claude Code
├── .subagents/                       # Dispatch multi-vendor
├── Flujograma/                       # Diagramas de flujo de procesos
├── Manuales PDF/                     # Manuales de capacitacion
├── Normas_graficas_hospital_Ovalle/  # Normas graficas institucionales
├── IMagene/                          # Recursos de imagen
├── Soporte/                          # Documentos de soporte tecnico
├── wiki/                             # Sitio MkDocs generado
├── scripts/                          # Scripts de automatizacion
├── config/                           # Configuracion del proyecto
├── docs/                             # Documentacion y estandares
├── exports/                          # Exportaciones de sesion
└── mkdocs.yml                        # Configuracion MkDocs
```

## Uso con Gemini CLI

```bash
# Explorar flujogramas disponibles
gemini "Lista todos los flujogramas de procesos disponibles"

# Buscar en manuales
gemini "Busca instrucciones para registrar admision de paciente en TrakCare"

# Consultar normas graficas
gemini "Muestra las normas graficas del Hospital de Ovalle"

# Generar documentacion
gemini "Genera resumen del proceso de alta medica segun los flujogramas"
```

## Scripts

| Herramienta | Funcion |
|-------------|---------|
| `mkdocs serve` | Inicia wiki local en http://localhost:8000 |
| `mkdocs build` | Genera sitio estatico en `wiki/site/` |

### Wiki Local (MkDocs)

```bash
# Activar entorno e iniciar wiki
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .\.venv\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt
mkdocs serve
```

## Configuracion

- `GEMINI.md` -- Perfil del proyecto para Gemini CLI
- `CLAUDE.md` -- Instrucciones para Claude Code
- `mkdocs.yml` -- Configuracion de la wiki MkDocs
- `requirements.txt` -- Dependencias Python (mkdocs)

## Contenido Disponible

| Directorio | Contenido |
|------------|-----------|
| `Flujograma/` | Diagramas de procesos clinicos y administrativos |
| `Manuales PDF/` | Guias de usuario para personal hospitalario |
| `Normas_graficas_hospital_Ovalle/` | Identidad visual institucional |
| `Soporte/` | Documentos de soporte tecnico TrakCare |
| `IMagene/` | Recursos graficos e imagenes |

## Proyectos Relacionados

| Proyecto | Sinergia |
|----------|----------|
| `G_Consultas` | Queries SQL para TrakCare/ALMA |
| `G_Informatica_Medica` | Estandares y transformacion digital |
| `G_Hospital` | Documentacion administrativa |
| `G_Analizador_RCE` | Validacion de datos clinicos |
