# Flujograma: Admision Hospitalizado

## Metadata

- **Nombre del Proceso**: Admision de Paciente Hospitalizado
- **Sistema**: InterSystems TrakCare (ALMA)
- **Perfil ALMA**: CLXX Admision Hospitalizado
- **Version**: 1.0
- **Fecha Creacion**: 2025-11-13
- **Basado en**: Manual 23MEUI [HOS] Admision Hospitalizado v2.1

## Objetivo

Documentar el proceso completo de admision administrativa de un paciente que ingresa a hospitalizacion, desde la llegada del paciente hasta el alta administrativa.

## Actores Principales

1. **Personal de Admision**: Responsable del registro y gestion administrativa
2. **Paciente/Familiar**: Proporciona informacion y documentacion
3. **Sistema ALMA**: Valida datos, genera alertas, almacena informacion
4. **Personal Medico**: Autoriza alta medica (prerequisito para alta administrativa)

## Alcance del Proceso

### Inicio
Paciente llega al establecimiento con indicacion de hospitalizacion

### Fin
- Paciente registrado y ubicado en cama/unidad, O
- Paciente dado de alta administrativamente

## Puntos de Decision Clave

1. ¿El paciente existe en el sistema?
2. ¿Tiene preadmision registrada?
3. ¿Se asigna cama inmediatamente?
4. ¿Tiene seguros adicionales?
5. ¿Medico autoriza alta?

## Procesos Relacionados

- **Preadmision**: Proceso previo (opcional)
- **Gestion de Camas**: Asignacion de ubicacion fisica
- **Alta Medica**: Prerequisito para alta administrativa
- **Facturacion**: Proceso posterior

## Archivos del Proceso

- `flujograma.md` - Diagrama visual del proceso
- `documentacion.md` - Descripcion detallada de cada paso
- `versiones/` - Historial de cambios

---

**Estado**: Activo
**Responsable Documentacion**: Claude AI + Usuario
