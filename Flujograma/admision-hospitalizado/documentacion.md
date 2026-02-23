# Documentación Detallada: Proceso de Admisión Hospitalizado

## Descripción General

El proceso de admisión hospitalizado es el conjunto de actividades administrativas que realiza el personal de admisión para registrar formalmente el ingreso de un paciente al establecimiento hospitalario, asignarle una ubicación física y gestionar los aspectos financieros de su atención.

---

## Pasos Detallados del Proceso

### FASE 1: ACCESO Y BÚSQUEDA

#### 1.1 Acceso al Sistema
**Actor:** Personal de Admisión
**Sistema:** ALMA (TrakCare)
**Formulario:** Pantalla de inicio

**Acciones:**
1. Seleccionar perfil "CLXX Admisión Hospitalizado"
2. Ingresar a la pantalla principal
3. Ubicarse en "Registro de Hospitalización"

**Tiempo estimado:** 30 segundos

---

#### 1.2 Búsqueda del Paciente
**Actor:** Personal de Admisión
**Sistema:** ALMA
**Formulario:** Búsqueda de paciente

**Acciones:**
1. Ingresar criterios de búsqueda:
   - RUN (preferido)
   - Número de Registro
   - Apellidos y nombres
   - Fecha de nacimiento
2. Hacer clic en "Buscar"
3. Revisar resultados

**Decisión:** ¿El paciente existe en el sistema?

**Tiempo estimado:** 1-2 minutos

---

### FASE 2: CREACIÓN O ACTUALIZACIÓN DE DATOS

#### 2.1 Crear Nuevo Paciente (si NO existe)
**Actor:** Personal de Admisión
**Sistema:** ALMA
**Formulario:** Registro de Pacientes

**Datos obligatorios a ingresar:**

**Antecedentes Personales:**
- RUN o identificación
- Nombres
- Apellido Paterno
- Apellido Materno
- Sexo
- Fecha de Nacimiento
- Nacionalidad

**Domicilio de Residencia:**
- Dirección
- Comuna
- Región
- Teléfono de contacto

**Antecedentes Previsionales:**
- Previsión de Salud (FONASA, ISAPRE, etc.)
- Plan (si aplica)

**Acción final:** Hacer clic en "Actualizar"

**Tiempo estimado:** 5-8 minutos

---

#### 2.2 Verificar Preadmisión (si paciente existe)
**Actor:** Personal de Admisión
**Sistema:** ALMA
**Formulario:** Lista de Preadmisiones

**Acciones:**
1. Consultar si existe solicitud de hospitalización pendiente
2. Si existe preadmisión:
   - Seleccionar la fecha de ingreso
   - Verificar datos del paciente
   - Hacer clic en número de episodio
3. Si NO existe preadmisión:
   - Continuar con registro manual

**Tiempo estimado:** 1-2 minutos

---

### FASE 3: REGISTRO DEL EPISODIO

#### 3.1 Completar Formulario de Episodio
**Actor:** Personal de Admisión
**Sistema:** ALMA
**Formulario:** Registro del Episodio

**Datos obligatorios:**

**Detalles de Admisión:**
- Establecimiento (por defecto)
- Fecha de Registro Hospitalización (automática)
- Hora de Registro Hospitalización (automática)
- Tipo de Episodio: Hospitalizado

**Procedencia del Paciente:**
- Establecimiento de origen
- Unidad/Servicio de origen (si aplica)

**Clasificación Clínica:**
- Unidad Clínica/Servicio (destino hospitalización)
- Especialidad
- Profesional de Salud (si se conoce)

**Motivo:**
- Motivo de Hospitalización (descripción)
- Procedencia del Paciente (ej: Urgencia, Policlínico, etc.)

**Tiempo estimado:** 3-5 minutos

---

### FASE 4: ASIGNACIÓN DE UBICACIÓN

#### 4.1 Decidir Asignación de Cama
**Actor:** Personal de Admisión
**Criterios de decisión:**
- ¿Hay cama disponible en la unidad?
- ¿El paciente requiere cama inmediata?
- ¿Existe orden específica del médico?

**Decisión:** Asignar cama o dejar en estación de enfermería

---

#### 4.2 Seleccionar Cama (si se asigna)
**Actor:** Personal de Admisión
**Sistema:** ALMA
**Formulario:** Detalles de la Cama (dentro de Registro Episodio)

**Acciones:**
1. Usar lupa para búsqueda de cama disponible
2. Seleccionar:
   - Sala/Piso
   - Habitación
   - Cama específica
3. Confirmar selección

**Resultado:** Paciente aparecerá en esa cama en el Mapa de Piso

**Tiempo estimado:** 1-2 minutos

---

#### 4.3 Asignar a Estación de Enfermería (si NO se asigna cama)
**Actor:** Personal de Admisión
**Sistema:** ALMA

**Acciones:**
1. Dejar campo de cama vacío
2. El sistema asignará automáticamente a:
   - Estación de Enfermería, o
   - Sala de Espera
   de la unidad seleccionada

**Resultado:** Paciente aparecerá en esa ubicación temporal en el Mapa de Piso

**Tiempo estimado:** 0 minutos (automático)

---

### FASE 5: GESTIÓN DE PREVISIÓN

#### 5.1 Verificar Previsión Base
**Actor:** Personal de Admisión
**Sistema:** ALMA
**Formulario:** Detalles de Previsión

**Acciones:**
1. Revisar previsión registrada en datos del paciente
2. Verificar que esté vigente y sea correcta
3. Actualizar si es necesario

---

#### 5.2 Registrar Seguros Adicionales (si aplica)
**Actor:** Personal de Admisión
**Sistema:** ALMA
**Formulario:** Detalles de Previsión por Programa Social

**Datos a registrar:**
- Seguro/Programa (usar lupa para buscar)
- Detalle de Seguro/Programa (especificar tipo)
- Prioridad de la Previsión (orden de uso)
- Tipo/Póliza de Seguro (número)
- Número de Titular de la Tarjeta
- Fecha Desde (inicio vigencia)
- Fecha Hasta (fin vigencia)
- Observaciones

**Acción:** Hacer clic en "Guardar" para agregar a la lista

**Tiempo estimado:** 2-3 minutos por seguro

---

#### 5.3 Guardar Lista de Previsiones
**Actor:** Personal de Admisión
**Sistema:** ALMA

**Acciones:**
1. Verificar que todos los seguros/programas estén en la lista
2. Hacer clic en "Guardar" (botón principal)

---

### FASE 6: VALIDACIÓN Y FINALIZACIÓN

#### 6.1 Guardar Episodio
**Actor:** Personal de Admisión
**Sistema:** ALMA

**Acción:** Hacer clic en botón "Actualizar" del formulario principal

**El sistema procesará y validará la información**

---

#### 6.2 Gestionar Alertas del Sistema
**Actor:** Personal de Admisión
**Sistema:** ALMA

**Alertas posibles:**

**Alerta 1: "Paciente Extra-Servicio"**
- **Causa:** La unidad/servicio no coincide con la especialidad
- **Acción:** Confirmar si es correcto o corregir la asignación

**Alerta 2: "Actualizar previsión del paciente"**
- **Causa:** Recordatorio para verificar datos previsionales
- **Acción:** Revisar y confirmar

**Alerta 3: Otras validaciones**
- Seguir instrucciones del sistema

**Tiempo estimado:** 1 minuto por alerta

---

#### 6.3 Confirmación de Registro
**Sistema:** ALMA
**Resultado:** Paciente registrado exitosamente

**Verificaciones:**
1. El paciente aparece en el Mapa de Piso
2. Se muestra en la ubicación correcta (cama o estación)
3. Los datos son visibles en "Pacientes Actuales"

**Tiempo estimado:** 30 segundos

---

### FASE 7: ESTADÍA HOSPITALARIA

#### 7.1 Consultas Durante la Estadía
**Actor:** Personal de Admisión (consulta)
**Sistema:** ALMA

**Opciones disponibles:**

**Pacientes Actuales:**
- Ver lista de todos los pacientes hospitalizados
- Filtrar por fecha, unidad, especialidad

**Servicios Clínicos:**
- Visualizar Mapa de Piso
- Ver ocupación de camas
- Consultar estadísticas

**Búsquedas:**
- Por Paciente: datos demográficos, historial
- Por Atención: episodios previos

**Archivo:**
- Consultar ubicación de Ficha Clínica
- Enviar/Recibir FC entre unidades
- Solicitar FC para atención

---

### FASE 8: ALTA ADMINISTRATIVA

#### 8.1 Verificar Alta Médica
**Actor:** Médico tratante (prerequisito)
**Sistema:** ALMA

**Prerequisito obligatorio:**
- El médico debe haber realizado el alta médica previamente
- Sin alta médica NO se puede realizar alta administrativa

---

#### 8.2 Realizar Alta Administrativa
**Actor:** Personal de Admisión
**Sistema:** ALMA
**Formulario:** Alta del Episodio

**Acceso:**
1. Seleccionar paciente desde Mapa de Piso
2. Hacer clic en menú contextual "Alta Adm. Hosp."

**Datos a completar:**
- Fecha de Alta (automática, modificable)
- Hora de Alta (automática, modificable)
- Establecimiento de Referencia (si paciente es derivado)
- Destino del Egreso (domicilio, otro establecimiento, etc.)

**Acción:** Hacer clic en "Actualizar"

**Tiempo estimado:** 2-3 minutos

---

#### 8.3 Confirmación de Alta
**Sistema:** ALMA
**Resultado:** Paciente dado de alta

**Efectos:**
1. El paciente desaparece del Mapa de Piso
2. La cama queda disponible
3. El episodio cambia a estado "Cerrado"
4. Se genera información para facturación

---

## PROCESOS ADICIONALES

### A. Fusión de Registros

**Cuándo usar:** Cuando se detectan registros duplicados o se identifica un paciente NN

**Proceso:**
1. Acceder a "Fusión de Registro"
2. Buscar Paciente Origen (registro temporal/duplicado)
3. Buscar Paciente Destino (registro definitivo)
4. Verificar datos a mantener (marcar casillas)
5. Ingresar contraseña del usuario
6. Confirmar fusión
7. Sistema unifica registros

**Revertir Fusión (si hay error):**
1. Buscar paciente fusionado
2. En Antecedentes Especiales seleccionar "Desasociar Paciente"
3. Ingresar contraseña
4. Actualizar

**Tiempo estimado:** 5-7 minutos

---

### B. Gestión de Archivo Clínico

#### B.1 Enviar Ficha Clínica
**Cuándo:** Cuando se requiere enviar la FC a otra unidad

**Proceso:**
1. Menú Archivo → Enviar/Recibir
2. Buscar paciente
3. Verificar ubicación actual de la FC
4. Seleccionar unidad de destino
5. Hacer clic en "Enviar Ficha Clínica"

#### B.2 Recibir Ficha Clínica
**Cuándo:** Cuando llega una FC enviada a la unidad

**Proceso:**
1. Menú Archivo → Enviar/Recibir
2. Buscar paciente
3. En opciones seleccionar "Recibe"
4. Confirmar recepción
5. La FC queda en la unidad actual

#### B.3 Solicitar Ficha Clínica
**Cuándo:** Cuando se necesita la FC y no ha llegado

**Proceso:**
1. Menú Archivo → Solicitud FC
2. Buscar paciente
3. Verificar ubicación actual de la FC
4. Completar detalles de solicitud
5. Enviar solicitud

**Tiempo estimado:** 2-3 minutos por operación

---

## CASOS ESPECIALES

### 1. Pacientes Gineco-Obstétricos
**Diferencia:** Se debe registrar la Fecha Probable de Parto

**Ubicación del campo:** En el formulario Registro del Episodio, sección "Detalles del Parto"

**Importancia:** Permite planificar la atención y disponibilidad de recursos

---

### 2. Pacientes NN (No identificados)
**Cuándo ocurre:** Paciente ingresa sin identificación (ej: inconsciente, amnesia)

**Proceso:**
1. Crear registro temporal con datos genéricos:
   - RUN temporal o sin RUN
   - Nombre: NN + fecha (ej: NN-13/11/2023)
2. Completar resto del proceso normalmente
3. Cuando se identifica al paciente:
   - Buscar si tiene registro previo
   - Realizar Fusión de Registros
   - El nombre temporal queda como "Nombre Social"

---

### 3. Pacientes Extra-Servicio
**Qué significa:** Paciente hospitalizado en una unidad que no corresponde a su especialidad

**Causa común:** Falta de camas en la unidad apropiada

**Alerta del sistema:** "El Paciente será identificado como Paciente Extra-Servicio"

**Acción:** Confirmar que es correcto (el sistema lo marca para seguimiento)

---

## INDICADORES Y MÉTRICAS

### Tiempos Estándar del Proceso
- **Admisión completa (paciente nuevo):** 10-15 minutos
- **Admisión con preadmisión:** 5-8 minutos
- **Solo actualización de datos:** 3-5 minutos
- **Alta administrativa:** 2-3 minutos

### Campos Obligatorios Mínimos
Total: 10 campos críticos que deben estar completos

### Alertas Comunes
- Paciente Extra-Servicio: 15-20% de casos
- Actualizar previsión: 30-40% de casos
- Otras validaciones: 5-10% de casos

---

## ROLES Y RESPONSABILIDADES

### Personal de Admisión
**Responsabilidades:**
- Registro completo y preciso de datos del paciente
- Verificación de documentación
- Asignación de ubicación
- Gestión de previsión y seguros
- Alta administrativa
- Consultas y reportes

**NO es responsable de:**
- Alta médica (responsabilidad del médico)
- Traslados entre camas (Gestión de Camas)
- Atención clínica del paciente

### Sistema ALMA
**Funciones automáticas:**
- Validación de datos obligatorios
- Generación de alertas
- Asignación de números de episodio
- Actualización de ocupación de camas
- Registro de trazabilidad

---

## ANEXOS

### Formularios ALMA en Orden de Uso

1. **Búsqueda de paciente** - Registro de Hospitalización
2. **Registro de Pacientes** - Datos Demográficos
3. **Lista de Preadmisiones** - Gestión Hosp Electiva (opcional)
4. **Registro del Episodio** - Registro de Hospitalización
5. **Detalles de la Cama** - Dentro de Registro Episodio
6. **Detalles de Previsión** - Seguros y Programas
7. **Alta del Episodio** - Alta Administrativa

---

**Versión:** 1.0
**Fecha última actualización:** 2025-11-13
**Basado en:** Manual 23MEUI [HOS] Admisión Hospitalizado v2.1
**Sistema:** InterSystems TrakCare (ALMA)
