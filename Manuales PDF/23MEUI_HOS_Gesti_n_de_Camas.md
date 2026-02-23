# 23MEUI [HOS] Gestión de Camas 

ENTRENAMIENTO 

Gestión de Camas 

CLXX Gestión Camas 

Chile Edition 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Control de cambios 

Versión 

Fecha 

Descripción del cambio 

Modificado por 

3.0 

3.1 

07-ene-2023 

Actualización del documento 

Learning Services 

07-Jul-2024 

Edición Gráfica 

Equipo Learning 

Copyright  ©  2024  InterSystems  Corporation.  Todos  los  derechos  reservados.  Este  documento  es  confidencial  y 
privado, requiere autorización escrita para imprimir y distribuir. All rights reserved. This document is confidential and 
proprietary. Printing renders document uncontrolled. 

Contenidos 

1.  Acceso a TrakCare ............................................................................................ 5 

2.  Pantalla de Inicio ............................................................................................... 6 

3.  Gestión de Camas ............................................................................................. 7 
Servicios Clínicos ............................................................................................................... 7 

3.1. 

2.1.1 

Pre Admisiones .................................................................................................... 8 

3.1.1.  Egresos Programados ......................................................................................... 9 

3.2. 

Admisiones Programadas .................................................................................................. 9 

2.1.2 

Descripción Columnas Resumen Servicios Clínicos ......................................... 10 

3.2.1.  Mapa – Lista ....................................................................................................... 11 

3.3. 

Resumen por Especialidad, Unidad Funcional, por Hospital y por Servicio de Salud ..... 12 

3.4.  Gestión Camas ................................................................................................................. 13 

3.5. 

Pacientes Actuales ........................................................................................................... 14 

3.6.  Movimiento Traslado Interno ............................................................................................ 14 

3.7. 

3.8. 

Búsqueda de camas ......................................................................................................... 17 

Solicitud de Traslado ........................................................................................................ 18 

4.  Solicitud Hospitalización desde Urgencia ..................................................... 19 
Descripción proceso desde Urgencia ............................................................................... 19 

4.1. 

4.2.  Gestión Solicitud de Hospitalización desde Servicio de Urgencia ................................... 21 

4.2.1.  Desde el Mapa de Piso ...................................................................................... 21 

4.2.2.  Desde Lista de Solicitudes: ................................................................................ 24 

4.3. 

Cambio de Estado de la Solicitud Hospitalización, desde Servicio de Urgencia: ............ 27 

4.3.1.  Rechazo Solicitud de Cama/Hospitalización ..................................................... 29 

4.3.2.  Solicitud de Hospitalización Rechazada: Cancelar Episodio (Pre-Admisión)

30 

4.3.3.  Aceptar Solicitud de Hospitalización .................................................................. 33 

Otras Funcionalidades en Listado de Solicitudes: ........................................................................ 34 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 2 de 119 

 
 
 
4.3.4.  Visualización fecha y hora solicitud de hospitalización ..................................... 35 

4.3.5.  Fecha Admisión.................................................................................................. 35 

Solicitud de Hospitalización desde Servicio Urgencia “No Editable” ............................... 36 

Visualización de Solicitudes de Cama por Hospital ......................................................... 37 

Perfil: Jefe Gestión Camas ............................................................................................... 38 

Solicitudes de Hospitalización desde Servicio Urgencia Gineco-Obstétrica ................... 39 

4.4. 

4.5. 

4.6. 

4.7. 

5.  Gestión de Hospitalización Electiva .............................................................. 41 
Solicitud de Hospitalización del paciente. ........................................................................ 41 

5.1. 

5.2.  Gestión Hospitalización Electiva ...................................................................................... 42 

5.3. 

5.4. 

5.5. 

5.6. 

5.7. 

Consulta Solicitud de Hospitalización Electiva ................................................................. 42 

Incluir una nueva Solicitud de Hospitalización Electiva ................................................... 47 

Asignar Unidad ................................................................................................................. 49 

Registro Gestión Hospitalización Electiva ........................................................................ 51 

Remover (eliminar) Solicitud de Hospitalización Electiva ................................................ 53 

6.  Gestión Extra - Sistema .................................................................................. 54 
Ingreso Extra-Sistema ...................................................................................................... 55 

6.1. 

6.2. 

6.3. 

6.4. 

6.5. 

Incluir Solicitud Hospitalización Extra Sistema ................................................................. 57 

Lista Derivaciones ............................................................................................................ 60 

Registro Gestión ............................................................................................................... 61 

Remover Registro ............................................................................................................. 62 

7.  Lista de Preadmisiones ................................................................................... 64 

8.  Búsquedas ....................................................................................................... 67 
Búsqueda por Paciente .................................................................................................... 67 

8.1. 

8.2. 

Búsqueda Por Atención .................................................................................................... 69 

9.  Consultar Pabellón .......................................................................................... 71 

10.  Archivo ............................................................................................................. 72 
10.1.  Enviar/Recibir ................................................................................................................... 73 

10.1.1.  Enviar ................................................................................................................. 73 

10.1.2.  Recibir ................................................................................................................ 74 

10.2.  Consulta FC de Paciente .................................................................................................. 75 

10.3.  Solicitud FC ...................................................................................................................... 77 

11.  Resumen Solicitudes de Cama ....................................................................... 79 

12.  Solicitud de Traslado Interno ......................................................................... 83 
12.1.  Gestión Solicitud de Traslado Interno .............................................................................. 85 

12.1.1.  Estado Gestión Camas ...................................................................................... 87 

12.1.2.  Solicitud de Traslado Interno Aceptada ............................................................. 88 

12.1.3.  Solicitud de Traslado Interno Rechazada .......................................................... 92 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 3 de 119 

 
13.  Reconversión Camas: ..................................................................................... 96 
13.1.  A “Demanda”: ................................................................................................................... 96 

13.2.  Reconversión de Cama Programada (Estacional) ......................................................... 105 

13.2.1.  Antes de reconvertir la cama: .......................................................................... 107 

13.2.2.  Después de reconvertir la cama: ..................................................................... 107 

14.  Otras Funcionalidades del mapa de Piso .................................................... 108 
14.1.  Reserva de Cama: .......................................................................................................... 108 

14.2.  Revertir Reserva de Cama ............................................................................................. 110 

14.3.  Ubicación/Unidad Temporal ........................................................................................... 113 

14.4.  Reversar Ubicación Temporal ........................................................................................ 114 

14.5.  Bloquear Cama ............................................................................................................... 116 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 4 de 119 

 
 
 
1. 

Acceso a TrakCare  

Seleccione  el  ícono  TrakCare  en  su  escritorio.  Los  flujos  presentados  en  este  manual 
representan el funcionamiento general de TrakCare en Chile, es posible que algunas imágenes 
presenten diferencias menores respecto de la configuración usada en su establecimiento. Estas 
variaciones son esperables y no implican cambios significativos a las instrucciones descritas en 
este manual.  

Ingrese los datos de USUARIO y CONTRASEÑA que se le han entregado. Haga clic en Iniciar 

Sesión. 

Si usted sólo tiene asignado un Grupo de Seguridad, ingresará directamente a la pantalla inicial. 
Si tiene asignado más de un Grupo de Seguridad, Perfil de Acceso o Local deberá seleccionar 
el que usará durante esta sesión. 

Grupo de Seguridad: CLXX Gestión Camas 

Al  ingresar  por  primera  vez,  el  sistema  le  pedirá  que  cambie  su  contraseña  inicial  para  que 
registre una clave personalizada que pueda recordar fácilmente. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 5 de 119 

 
 
 
 
 
 
 
 
 
 
 
2. 

Pantalla de Inicio 

Al  ingresar  al  sistema,  verá  que  la  pantalla  se  divide  en  las  siguientes  secciones:  Enlaces, 
Notificaciones, Menús y pantalla del menú actual. 

Los enlaces permiten realizar las siguientes acciones durante su sesión. 

Menú  

Inicio 

  Muestra una serie de menús disponible para el usuario. 

  Volver a pantalla inicial. 

Herramientas 

  Accede a herramientas generales. 

Mensajes 

Usuario 

Permite recibir y enviar mensajes entre los usuarios del sistema. 

Muestra el usuario registrado en la sesión actual. Se recomienda verificar este 
dato antes de iniciar el registro de información. Permite cambiar su contraseña. 

Bloquear 

Bloquea la sesión actual del usuario. Para desbloquear ingrese su contraseña. 

Las  Notificaciones 
revisión: 

  le  permiten  revisar  mensajes  de  alertas  que  el  sistema  genera  para  su 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 6 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Al seleccionar los Menús 
actual. 

 se mostrarán diferentes contenidos en la sección pantalla del menú 

3. 

Gestión de Camas 

3.1. 

Servicios Clínicos 

La gestora de cama visualizará todas las unidades que sean configuradas en preferencias en el 
Menú Servicios Clínicos. Desde esta pantalla podrá tener un monitoreo de las camas dentro de 
cada unidad de su Establecimiento. 

En  la  parte  superior  de  Servicios  Clínicos,  contiene  un  contador  de  Altas  y  Admisiones 
programadas.  Con  esta  información  la  gestora  conocerá  la  disponibilidad  de  cama  con  los 
egresos programados.  

El  conteo  se  realiza  con  las  pre-admisiones  que  estén  generadas  o  programadas  para  el  día 
actual, para mañana y para las próximas 48 horas días. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 7 de 119 

 
 
 
 
 
 
 
 
 
 
2.1.1 

 Pre Admisiones  

En el listado de pre-admisiones (menú de la Gestora de Camas) 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 8 de 119 

 
 
 
 
 
 
 
 
 
3.1.1. 

  Egresos Programados 

En  la  ventana  de  inicio,  se  ven  reflejadas  las  altas  programadas  para  el  día  de  “hoy”,  para 
“mañana”, para la “semana”, los egresos “confirmados hoy”, los egresos que aún están “por 
confirmar” y el “total de egresos programados”.   

3.2. 

Admisiones Programadas 

En el costado derecho, se puede apreciar el detalle para las admisiones programadas. En las 
que se muestran las admisiones para “Hoy”, las de “Mañana” y las admisiones programadas 
para los “Próximos días”. 

Definición de Conceptos: 

  Hoy (color Rosado): Son aquellos pacientes que presentan Alta en día de hoy; con o sin confirmación. 

  Mañana (color Calipso): Son aquellos pacientes que presentan Alta para el día de Mañana; con o sin confirmación. 

  Esta Semana (color Café): Son aquellos pacientes que presentan Alta durante esta semana. 

Confirmados Hoy (color Amarillo): Son aquellos pacientes que presentan Alta para Hoy con el check de Confirmación 
Fecha Estimada de Egreso. 

Sin Confirmar (color Verde): Son aquellos pacientes que presentan Alta para el día de hoy SIN el check de Confirmación 
Fecha Estimada de Egreso. 

  Total Egresos Programados (color Blanco): Sumatoria de todos los egresos programados. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 9 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
 
 
Se puede registrar la fecha Estimada de Egreso con o sin “Confirmación”. Esta información será 
reflejada en el menú Servicios Clínicos en Egresos Programados y en el Paciente (Mapa de 
piso): 

Al actualizar esta información, aparecerá en la cama del paciente (Mapa de Piso) una franja de 
color y un tooltip (mensaje emergente cuando se acerca el mouse) que indicará la fecha estimada 
de alta para ese paciente. El color asignado será en función de la fecha Estimada de Alta, con 
respecto a la fecha cronológica del registro. Ejemplos: considerando fecha de registro 29 agosto 
2016: está información además se verá reflejada en el conteo de Egresos Programados, como 
muestra la imagen. 

2.1.2 

  Descripción Columnas Resumen Servicios Clínicos 

Descripción Columnas: 

•  Mapa: Permite cambiar la vista a mapa de piso 
•  Lista Piso: Permite cambiar la vista de lista  
•  Establecimiento: El nombre del establecimiento  
•  Unidades  Funcionales:  agrupaciones  de  camas  en  función  de  una  clasificación  de 

servicios clínicos. Ejemplo: Área Médica Adulto Cuidados Básicos 

•  Total de Camas: es el número de camas totales del servicio (censables): disponibles y 

fuera de servicio. 

•  Camas  Disponibles:  es  el  número  de  camas  realmente  instaladas  en  el  hospital,  en 

condiciones de uso inmediato para la atención de pacientes hospitalizados. 

•  Camas Ocupadas: es la permanencia de un paciente hospitalizado ocupando una cama 
de hospital, durante el período comprendido entre las 0 horas y las 24 horas del mismo 
día. El ingreso y egreso de un paciente en el mismo día debe ser considerado como día 
cama ocupado.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 10 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
•  Camas Bloqueadas: Corresponde a cama hospitalaria que están fuera de servicio por 
diversos  motivos,  ya  sea,  aislamiento,  falta  de  personal,  falta  de  equipamiento, 
mantención u otro motivo. 

•  Solicitudes  de  Camas:  lista  de  solicitudes  de  hospitalización  desde  Servicio  de 
Urgencia, Ambulatorio o solicitud de traslado interno desde el mismo Establecimiento 
•  Pre-Admisiones: lista de pacientes con solicitud de hospitalización que han sido “Pre-

admitidos”. 

•  Pacientes Extra-Servicio: pacientes que están acostados en servicios clínicos que no 

corresponden a su especialidad (pacientes ectópicos) 

3.2.1. 

  Mapa – Lista 

Ambos tipos de visualizaciones permiten al usuario, revisar información de los pacientes en los 
diferentes servicios clínicos, del establecimiento. Son complementarias, existe información en el 
mapa de piso que no se visualiza en la lista de piso y viceversa. 

Al seleccionar el ícono de “Mapa” 
 permitirá a la gestora de camas revisar los distintos servicios 
clínicos  de  su  Establecimiento,  con  sus  estaciones  de  enfermería,  donde  podrá  gestionar  las 
solicitudes de hospitalización desde Servicio de Urgencia y solicitudes de traslado interno. 

Al seleccionar “Lista Piso” permitirá a la gestora ver la información de los pacientes hospitalizados 
y en espera de cama en forma más estructurada: por ejemplo, podrá visualizar la “Ocupación 
Días Cama” de cada paciente por servicio clínico. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 11 de 119 

 
 
 
 
 
 
 
 
 
 
3.3. 

 Resumen por Especialidad, Unidad Funcional, por Hospital y por Servicio 
de Salud 

Resumen Especialidad  Refiere los servicios clínicos según especialidad del hospital 

Resumen Unidades Funcionales Refiere los servicios agrupados por unidad funcional 

Resumen por Hospital   Hace referencia a todas las camas del centro hospitalario seleccionado 
en la sesión de usuario (local de logueo). 

Resumen por Servicio de Salud  entrega a la gestora información del estado de camas de todo 
el Servicio de Salud (información en red, que se alimenta de los datos de cada hospital con el 
sistema). 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 12 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
3.4. 

Gestión Camas 

Este  submenú  entrega  una  representación  de  la  ocupación  de  camas  según  los  parámetros 
ingresados en la búsqueda. A la derecha se muestra el código utilizado para describir los Estados 
de las Camas y en la parte inferior se muestra el resumen de las camas de cada unidad en el 
plazo establecido. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 13 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
3.5. 

Pacientes Actuales 

 Este  menú  permite  la  búsqueda  de  pacientes  que  tienen  un  episodio  actual  para  atenciones 
ambulatorias,  hospitalizados  y  urgencia.  Permite  filtrar  por  Fecha  de  Admisión  y  Tipo  de 
Admisión.  Además,  cuenta  con  el  casillero  Alta  Médica  para  filtrar  a  aquellos  pacientes  que 
cuentan con este tipo de alta. Se pueden incluir datos del paciente para filtrar esta búsqueda. 

Se  despliega  una  pantalla  con  los  pacientes  que  actualmente  tienen  un  episodio  abierto  y 
distintos datos que se identifican en las columnas. 

3.6. 

Movimiento Traslado Interno 

Este  menú  permite  realizar  un  movimiento  de  traslado  dentro  del  recinto  en  forma  rápida. 
Seleccione al paciente luego haga clic sobre el menú de acción representado por los tres puntos 
horizontales,  la  acción  anterior  provoca  que  a  la  derecha  de  la  pantalla  se  abra  una  ventana 
emergente  con  una  serie  de  menús,  luego  damos  clic  en  el  menú  Gestión  Cama  seleccione 
Mov. Traslado Interno. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 14 de 119 

 
 
 
 
 
 
 
 
 
 
 
En esta pantalla podrá gestionar las siguientes acciones: 

Médico Tratante: Permite asignar a un nuevo médico tratante para el paciente. Al hacer clic en  
 Nuevo, podrá iniciar el registro, use las lupas para seleccionar los datos del nuevo médico y 
el  motivo  del  cambio.  Puede  marcar  el  casillero  para  asignarlo  como  Médico  de  Cabecera. 
Cuando termine de completar los datos haga clic en Guardar para completar la asignación. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 15 de 119 

 
 
 
 
 
 
 
 
 
Lista de Movimientos Servicios Clínicos: Registra los movimientos de traslado interno que se 
realizan con el paciente dentro del mismo establecimiento. Seleccione 
 Nuevo para ver los 
Detalles del Movimiento donde debe indicar los datos del traslado junto con el motivo. Puede 
marcar el casillero Reserva de Cama en caso de que no logre asignar una cama, en este caso 
debe registrar una razón para esta reserva (ej. camas ocupadas). 

Lista de Salidas: Permite registrar las salidas diarias del paciente hacia otros establecimientos 
  Nuevo,  podrá  iniciar  el  registro  de  la  Salida 
externos  u  otros  destinos.  Al  hacer  clic  en 
Temporal completando los datos de salida del paciente. Haga clic en Actualizar para generar el 
registro de esta salida. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 16 de 119 

 
 
 
 
 
 
 
 
El nuevo registro se agregó a la Lista de Salidas. Cuando el paciente retorne se podrán completar 
los datos haciendo clic en la Fecha de Permiso. 

3.7. 

Búsqueda de camas 

 Permite ejecutar la búsqueda de camas de todo el recinto, por especialidad y disponibilidad de 
camas.  Seleccione  los  filtros  correspondientes  a  la  búsqueda  requerida  y  luego  seleccione  el 
botón Buscar.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 17 de 119 

 
 
 
 
 
 
 
 
 
 
 
Se desplegará una Lista de Camas con datos relevantes sobre su ocupación. 

3.8. 

Solicitud de Traslado 

Permite  realizar  una  solicitud  formal  de  traslado  de  un  paciente  a  otro  servicio.  Este  tipo  de 
solicitudes deben ser revisadas y autorizadas por la enfermera o matrona del servicio de destino. 
Seleccione al paciente luego haga clic sobre el menú de acción representado por los tres puntos 
horizontales,  la  acción  anterior  provoca  que  a  la  derecha  de  la  pantalla  se  abra  una  ventana 
emergente  con  una  serie  de  menús,  luego  damos  clic  en  el  menú  Gestión  Cama  luego 
seleccione Solicitud de Traslado. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 18 de 119 

 
 
 
 
 
 
 
 
 
Complete los datos de la Unidad/Servicio, Especialidad, Motivo de Solicitud y Observaciones. 
Luego haga clic en Actualizar para registrar esta solicitud. 

4. 

Solicitud Hospitalización desde Urgencia 

4.1. 

Descripción proceso desde Urgencia 

Paciente  en  Servicio  de  Urgencia  que  requiere  una  cama  para  hospitalizado.  Médico  de 
Urgencia, genera Solicitud de Hospitalización.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 19 de 119 

 
 
 
 
 
 
 
 
 
 Seleccione  al  paciente  desde  el  mapa  de  piso  luego  haga  clic  sobre  el  menú  de  acción 
representado por los tres puntos horizontales, la acción anterior provoca que a la derecha de la 
pantalla se abra una ventana emergente con una serie de menús, luego damos clic en el menú 
Solicitud de hospitalización. 

Para generar una solicitud de hospitalización, se deben completar los siguientes campos: 

•  Unidad/Servicio: se refiere a la unidad de hospitalización requerida (campo obligatorio). 
•  Especialidad: de la unidad de hospitalizado requerida (campo obligatorio). 
•  Profesional: Médico responsable del paciente en la unidad hospitalizado. La lista que 
se despliega corresponde al médico asociado a especialidad. Debe ser asociado a 
Unidad/Servicio  de  Destino  (Configuración  particular  de  proyecto,  campo  “No” 
obligatorio).  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 20 de 119 

 
 
 
 
 
 
 
 
Al Actualizar, se mostrará en el mapa de piso del Servicio de Urgencia un ícono asociado al 
 , a quien se le realizó la solicitud de Hospitalización. Además, mostrará a que 
paciente 
unidad fue la requerida (tool tip). 

4.2. 

 Gestión Solicitud de Hospitalización desde Servicio de Urgencia 

Para gestionar la solicitud de hospitalización desde Servicio de Urgencia, la gestora de cama 
puede realizarlo de 2 formas. 

4.2.1. 

 Desde el Mapa de Piso 

Debe ingresar al mapa de piso de la unidad requerida y visualizar al paciente en la estación de 
enfermería de ésta.  

Para realizar esta acción, se debe seleccionar el ícono  

  de la columna “Mapa”.  

Importante: La acción Gestionar la solicitud de hospitalización, se puede realizar entrando al mapa de 
piso (punto anterior), no así desde “Lista Piso”, ya que este no muestra los íconos correspondientes al 
proceso.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 21 de 119 

 
 
 
 
 
 
 
Al seleccionar el ícono descrito, se desplegará el mapa de piso de la unidad seleccionada. 

Dentro de la Estación de Enfermería de la unidad, aparecerá el paciente con ícono 
la solicitud de hospitalización.  

 indicando 

Al seleccionar el ícono 
generada por el Médico de Urgencia, además de dos nuevos campos. 

 “Activar Gestión de Cama” se visualizará la solicitud de Hospitalización, 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 22 de 119 

 
 
 
 
 
 
 
 
 
•  Campo “Crear Pre-admisión” Este campo generará un nuevo episodio en el sistema, de tipo 
hospitalizado en estado “Pre-Admisión”. Es importante revisar que el check de pre-admisión se 
encuentre marcado (siempre vendrá por defecto así), ya que de lo contrario no se podrá aceptar 
o rechazar la solicitud de cama para el paciente.  

•  Campo “Gestión de cama en curso” este campo indica tanto al Médico de urgencia como a la 
gestora de camas, que la solicitud está siendo gestionada. Este campo viene con la respuesta “Si” 
por  defecto,  lo  cual  generará  un  ícono  que  será  mostrado  en  el  mapa  de  piso  del  servicio  de 
urgencia y en la Estación de Enfermería de la unidad / servicio clínico requerido, que evidenciará 
que la “Solicitud de Cama está en Gestión”.  

•  En esta instancia, la gestora de camas también podría “editar” datos relacionados con la solicitud 
de  hospitalización  como  la  Unidad/Servicio,  Especialidad  o  Profesional,  según  sea  necesario  y 
corresponda. 

Al  actualizar  la  pantalla  anterior,  este  ícono 
  será  visualizado  tanto  en  la  unidad  de 
hospitalizado, estación de enfermería (unidad solicitada), como en el mapa de piso de urgencia 
(de donde nace la solicitud). 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 23 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
4.2.2. 

Desde Lista de Solicitudes:  

*Nuevo Flujo para Gestión de Solicitud de Hospitalización desde Urgencia 

Existe una nueva forma para gestora de camas, gestionar estas solicitudes. La diferencia con la 
mostrada anteriormente es que la gestión pueda ser realizada desde una sola pantalla (Gestión, 
y Cambio de estado). Esto se puede lograr desde el enlace contador de la columna “Solicitudes 
de Cama”.  

Desde  el  menú  Servicios  Clínicos,  se  debe  acceder  a  enlace  contador  de  la  columna  “Solicitudes  de 
Cama” de la unidad donde se encuentra la solicitud a gestionar.  

Se  desplegará  un 
“Requerida/Solicitada” para la unidad seleccionada. 

listado  con 

todas 

las  solicitudes  de  hospitalización  en  estado 

Luego de que el Médico de Urgencia genere la Solicitud de Hospitalización, caerá en el listado 
de solicitudes para la unidad con estado “Requerido/Solicitado”.  

Para poder aceptar o rechazar esta solicitud, primero se deberá generar la pre-admisión, la cual 
 de seleccionar quede activo para el cambio de estado de la solicitud.  
permitirá que el check 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 24 de 119 

 
 
 
 
 
 
 
 
 
 
 
Para definir una solicitud como “Gestión de cama en Curso”. Se puede realizar desde esta misma 
pantalla, desde el ícono 

. 

Se  desplegará  una  ventana  emergente  desde  el  costado  derecho  de  la  pantalla,  en  la  que 
podremos entrar a la solicitud de hospitalización para el paciente seleccionado.  

Dentro de esta pantalla se encontrará el casillero 
episodio de tipo Hospitalizado con estado Pre-Admisión.  

 (check) “Crear Pre-admisión” el cual generará un 

Y  el  campo  “Gestión  de  cama  en  curso”  que  genera  un  ícono,  donde  el  médico  de  urgencia 
tomará  conocimiento  que  el  paciente  tiene  una  solicitud  de  hospitalización  en  gestión,  por  la 
gestora de cama.  

Al actualizar la pantalla “Solicitud de Hospitalización” aparecerá el ícono 
y el check de seleccionar aparecerá activo para cambiar el estado de la solicitud.  

 “Gestión en Curso”, 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 25 de 119 

 
  
 
 
 
 
 
 
 
 
 
Para aceptar o rechazar la solicitud del paciente, se debe hacer clic en el 

 check del paciente 

luego haga clic sobre el menú de acción representado por los tres puntos horizontales 
, la 
acción  anterior  provoca  que  a  la  derecha  de  la  pantalla  se  abra  una  ventana  emergente  con 
menús, luego damos clic en el menú “Cambio de Estado”. 

Se desplegará la siguiente pantalla.  

Luego de seleccionar el nuevo estado de la solicitud y actualizar, volverá a visualizar el listado 
de solicitudes. La solicitud gestionada con anterioridad desaparecerá del listado. Ya que sólo se 
visualizarán las solicitudes en estado “Requeridas/Solicitadas”. En los mapas de piso de urgencia 
y hospitalizado, se visualizarán los íconos mencionados en cada proceso.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 26 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
4.3. 

Cambio  de  Estado  de  la  Solicitud  Hospitalización,  desde  Servicio  de 
Urgencia: 

Una  vez  creada  la  pre-admisión  la  gestora  puede  aceptar  o  rechazar  la  solicitud  de 
hospitalización. Para esto deberá volver al menú Servicios Clínicos. Y seleccionar la columna 
“Solicitudes de Cama”. 

  Al  seleccionar  la  fila  correspondiente  a  la  unidad  requerida,  se  desplegará  un  listado  con 
distintas solicitudes para la unidad seleccionada. 

Dentro de este listado, se visualizarán las solicitudes de cama que provengan desde el Servicio 
de Urgencia, Hospitalizado (traslado interno) y Ambulatorio (siempre del mismo Establecimiento).  

También se encontrará información referente a la Solicitud de Hospitalización y al paciente. La 
columna  “Unidad  de  Origen”  mostrará  la  unidad  actual  del  paciente  que  tenga  un  episodio 
hospitalizado o de urgencia abierto, ambos del mismo establecimiento.  

Los Estados de las solicitudes de Hospitalización son tres:  

1)  Requerido/Solicitado: Se genera este estado en forma automática, cuando existe alguna Solicitud 
de Hospitalización desde Urgencia, Ambulatorio u Hospitalización para un Servicio Clínico, dentro 
del mismo Establecimiento. El Área de Gestión camas, evalúa y analiza disponibilidad.  

2)  Aceptado/Asignado: Gestión Camas da el visto bueno a la solicitud de Hospitalización al Servicio 

Clínico solicitante (u otro, según disponibilidad) o del traslado interno requerido.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 27 de 119 

 
 
 
 
         
 
 
 
3)  Rechazado/Cancelado: Este estado debe ser seleccionado, cuando no existe disponibilidad actual 
a  la  solicitud  requerida.  Gestión  Camas  gestiona  alternativas  de  disponibilidad  fuera  del 
establecimiento  de  salud.  Cada  vez  que  el  usuario  registra  un  estado  de  solicitud  de  cama 
Rechazado/Cancelado,  el  sistema  le  solicitará  que  registre  en  forma  obligatoria  las  razones  de 
esta acción. 

Dentro  de  este  listado  se  mostrarán  sólo  el  estado  de  solicitudes  “Requerido/Solicitado”.  Los 
estados “Aceptado/Asignado” y “Rechazado/Cancelado” desaparecen del listado al momento del 
cambio  de  estado.  Por  ello  es  muy  importante,  registrar  el  cambio  de  estado  cuando  el 
usuario esté 100% seguro de esta acción. 

Una vez seleccionada la solicitud del paciente, para registrar el estado: aceptar o rechazar la 
solicitud la gestora de cama haga clic sobre el menú de acción representado por los tres puntos 

verticales 
emergente con menús, luego damos clic en el menú “Cambio de Estado”. 

 , la acción anterior provoca que a la derecha de la pantalla se abra una ventana 

Se desplegará la siguiente pantalla. Al desplegar el campo “Estado de Cambio” aparecerán los 
tres estados mencionados anteriormente.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 28 de 119 

 
 
 
 
 
 
 
 
 
 
4.3.1. 

  Rechazo Solicitud de Cama/Hospitalización 

Para rechazar la solicitud se debe seleccionar el estado Rechazado/Cancelado.  

Al  seleccionar  Rechazado/Cancelado,  se  desbloqueará  el  campo 
“Razón  para 
Rechazar/Cancelar  Cama”,  donde  al  seleccionar  la  lupa  (look  up)  aparecerán  los  siguientes 
motivos.  

Al  actualizar  (guardar)  aparecerá  un  mensaje  para  aquellas  solicitudes  desde  Servicio  de 
Urgencia, el cual indica a modo de recordatorio al usuario, la cancelación/suspensión del episodio 
Hospitalizado en estado pre-admisión, generado para gestionar dicha solicitud. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 29 de 119 

 
 
 
 
 
 
 
 
 
El paciente desaparecerá, ya que sólo se visualizan los de estado Requerido/Solicitado. 

Al realizar esta acción en el mapa de urgencia aparecerá un ícono 
 indicando que la solicitud 
de hospitalización fue rechazada/cancelada y el motivo de ésta. Mientras que en la estación de 
enfermería de la unidad requerida el paciente desaparece, ya que no se realizaría el ingreso a 
esta unidad.  

Importante: Al rechazar una solicitud de hospitalización, la gestora de cama debe Cancelar/Suspender el 
episodio de hospitalización creado como Pre-admisión. En el caso que el paciente vuelva a hospitalizarse 
tiempo  después,  tendrá  dos  pre-admisiones  de  hospitalización  creadas.  Esta  acción  se  realiza  como  se 
indica a continuación.  

4.3.2. 

 Solicitud de Hospitalización Rechazada: Cancelar Episodio (Pre-Admisión) 

Dentro  del  menú  Lista  de  Preadmisiones  se  encuentra  un  listado  con  aquellos  pacientes  que 
contengan un episodio de hospitalizado en estado pre-admisión.  Aparecerá el ícono de Rechazo  
, el cual identificará que el paciente contiene una solicitud de hospitalización rechazada que 

debe ser Cancelada.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 30 de 119 

 
 
 
 
 
 
 
 
 
 
Al seleccionar el ícono se desplegará el menú lateral “Rechazo Solicitud de Cama” y el motivo 
del rechazo.  

Al ingresar, veremos el registro de hospitalización. 

Para editar el estado, seleccionamos el botón con los 3 puntos verticales 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 31 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
Lo que desplegará desde el costado derecho de la pantalla, el menú de opciones, seleccionamos 
el acordeón “Editar” y hacemos clic en “Cambio de estado”. 

La acción anterior abrirá la pantalla Detalles de Cambio de Estado, en la que seleccionaremos el 
estado “Cancelado” y seleccionamos el motivo de la suspensión, luego presionamos Actualizar. 

Al actualizar el estado cancelado, se visualizará el episodio Hospitalizado del paciente, que antes 
estaba en estado “Pre-Admisión” y ahora “Cancelado”.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 32 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
4.3.3. 

Aceptar Solicitud de Hospitalización 

Para  aceptar  es  condicionante  haber  creado  la  pre-admisión  desde  el  ícono  “Activar  Gestión 
Cama”, visible en el listado de solicitudes de camas. 

Se debe ingresar a la columna Solicitudes Cama, desde el menú Servicios Clínicos.  

Al ingresar aparecerá el listado de las distintas solicitudes de cama para la unidad seleccionada. 
Una vez seleccionado el paciente haga clic sobre el menú de acción representado por los tres 

puntos horizontales 
ventana emergente con menús, luego damos clic en el menú “Cambio de Estado”.  

, la acción anterior provoca que a la derecha de la pantalla se abra una 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 33 de 119 

 
 
 
 
 
  
 
 
Se desplegará la siguiente pantalla. En donde se debe seleccionar el estado Aceptado/Asignado 
en el campo “Estado del Cambio”. 

  indicando  que  la  solicitud  fue 
Al  actualizar,  el  estado  Aceptado/Asignado  gatilla  un  ícono 
aceptada por la gestora de cama, el cual se mostrará en el mapa de urgencia como en la estación 
de enfermería de la unidad requerida. 

Otras Funcionalidades en Listado de Solicitudes:   

Para acceder a esta información se debe seleccionar el link contador de la columna Solicitudes 
de Cama.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 34 de 119 

 
 
 
 
 
 
 
 
 
      
 
 
 
Donde se desplegará el listado de solicitudes de cama para la unidad seleccionada. 

4.3.4. 

 Visualización fecha y hora solicitud de hospitalización  

4.3.5. 

Fecha Admisión 

Es  posible  visualizar  y  ordenar  cronológicamente  la  fecha  y  Hora  Admisión  del  paciente,  del 
episodio donde se le realizó la Solicitud de Hospitalización. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 35 de 119 

 
 
 
 
 
 
 
 
 
 
 
4.4. 

  Solicitud de Hospitalización desde Servicio Urgencia “No Editable” 

El Médico / Matrona cuando realiza la solicitud de hospitalización desde el servicio de urgencia, 
a un paciente en específico, puede equivocarse en: 

•  Datos de la Unidad/Servicio de destino 

•  Especialidad asociada  

•  Profesional 

•  de paciente (no corroboración de doble identificación) 

Si el Clínico, vuelve a repetir la solicitud en el mismo paciente o bien re-edita la solicitud inicial, 
todo lo registrado por la gestora de camas, en relación a esa solicitud queda nulo (y se pierde 
toda trazabilidad de tiempos y gestiones de la gestora de camas en relación a esa solicitud). Por 
lo tanto, para llevar un registro de estos “errores de digitación”, se bloquea opción de re-editar la 
solicitud de hospitalización desde el menú “Solicitud de Hospitalización” que tiene el perfil Médico 
de Urgencia, y es solamente la Gestora de camas quien puede editar los campos de esta solicitud 
en el caso de errores de digitación en: Unidad de destino, especialidad o profesional. En el caso 
de error de selección de paciente, la gestora de camas debe “Rechazar/Cancelar” la solicitud con 
la razón: “Error de digitación” y el Médico debe realizar una nueva solicitud de hospitalización al 
paciente correcto. 

Los campos estarán bloqueados desde 2 accesos que tiene el Médico de Urgencia: 

1.- Desde el ícono de “Solicitud de Hospitalización”: 
bloqueados 

 y los campos del componente estarán 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 36 de 119 

 
 
 
 
 
 
2.- Seleccionando al paciente, Menú “Solicitud de Hospitalización”, estará bloqueado: 

4.5. 

Visualización de Solicitudes de Cama por Hospital 

Dentro del Menú Servicios Clínicos, la gestora de camas tiene diferentes resúmenes por nivel. 
Dentro del Resumen por Hospital, se encuentra la columna “Solicitudes de Camas”.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 37 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
Al seleccionar el link contador de la columna “Solicitudes de Cama” se desplegará el listado con 
todas las solicitudes del Establecimiento, provenientes desde Urgencia, Hospitalizado (traslado 
interno) y Ambulatorio. 

4.6. 

Perfil: Jefe Gestión Camas 

El Listado de solicitudes de la gestora de camas, por servicio clínico de destino, sólo permite 
visualizar las solicitudes en estado “Requerido/Solicitado”, con el objetivo de poder visualizar, 
priorizar  y  gestionar  las  solicitudes  que  se  van  registrando  desde  los  distintos  puntos  del 
establecimiento y evitar confusiones con las solicitudes que ya fueron gestionadas: Aceptadas o 
Rechazadas. Por lo tanto, en el listado de solicitudes de la gestora de cama, no visualizará las 
solicitudes aceptadas o rechazadas. 

Sin embargo, para los casos de uso en que la solicitud ya fue gestionada por el usuario, es decir, 
cambió de estado, y la situación del paciente cambió u otro suceso inesperado se presentó, no 
es posible revertir este acto desde el perfil de la gestora de camas.  

Producto de esta “posible” situación, se creó el grupo de seguridad “Jefe Gestión Camas”, con 
el fin de poder revertir este acto, pero siempre de manera controlada, y “solo” es posible revertir 
el estado Aceptado/Asignado a Rechazado/Cancelado. 

En el listado de solicitudes del menú servicios clínicos, la Jefe de Gestión Camas podrá visualizar 
solo  dos  estados  de  solicitudes  de  hospitalización,  con  la  posibilidad  de  revertir  el  estado 
aceptado, si es estrictamente necesario. 

Si, el estado que cambia la Jefe Gestión Camas es de Aceptado a Rechazado, una vez que 
actualice este cambio, en el sistema, esta solicitud desaparecerá del listado de solicitudes (no se 
visualizarán las solicitudes en estado “Rechazado”). 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 38 de 119 

 
 
 
 
 
 
 
4.7. 

Solicitudes  de  Hospitalización  desde  Servicio  Urgencia  Gineco-
Obstétrica 

El  proceso  de  atención  de  pacientes  Obstétricas  en  el  servicio  de  urgencia  gineco-obstétrica, 
tiene  un  flujo  de  gestión  camas  más  bien  “autogestionado”,  donde  las  pacientes  pasan 
directamente a la unidad de pre-parto cuando se encuentran en el proceso de trabajo de parto. 
Por esta razón, la solicitud de hospitalización de la Matrona de Urgencia tiene la particularidad 
de  poder  crear  una  pre-admisión  al  mismo  tiempo  que  registra  la  solicitud  de  hospitalización. 
Esta  acción  sólo  debe  aplicar  para  pacientes  de  tipo  “Obstétricas”  en  trabajo  de  parto.  Para 
pacientes  ginecológicas  u  obstétricas  que  requieran  hospitalización,  donde  la  cama  debe  ser 
gestionada  por  la  gestora  de  camas,  el  usuario  no  debe  marcar  el  check  de  crear  pre-
admisión. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 39 de 119 

 
 
 
 
 
 
 
 
 
 
 
Si  el  usuario,  registra  el  check  de  “Crear  Pre-admisión”,  la  gestora  de  camas  visualizará  la 
solicitud en el listado de solicitudes, específicamente en el servicio solicitado, sin embargo, no 
podrá  marcar  el  inicio  de  su  gestión,  ya  que  el  paciente,  tendrá  creado  el  episodio  de 
hospitalización,  en  estado  pre-admitido.  Sólo  podrá  cambiar  de  estado  la  solicitud  (Aceptar  o 
Rechazar). 

Si el usuario de Urgencia G-O, no marcó el check de Crear Pre-admisión, la solicitud seguirá el 
curso normal de los eventos en relación con las acciones de la gestora de Camas. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 40 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
5. 

Gestión de Hospitalización Electiva 

5.1. 

Solicitud de Hospitalización del paciente. 

Desde Especialidades Ambulatorio, el Médico Tratante del Paciente realizará la solicitud. 

Seleccione al paciente desde la agenda luego haga clic sobre el menú de acción representado 
por los tres puntos horizontales 
, la acción anterior provoca que a la derecha de la pantalla se 
abra una ventana emergente con una serie de menús, luego damos clic en el menú Solicitudes 
Clínicas seleccione Sol. Hosp.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 41 de 119 

 
 
 
 
 
 
 
5.2. 

Gestión Hospitalización Electiva 

La persona encargada de Gestión Camas, tendrá dentro de sus Menús: “Gestión Hospitalización 
Electiva” y dos sub-menú asociados a esta gestión: 

5.3. 

 Consulta Solicitud de Hospitalización Electiva    

Este sub-menú permitirá a la gestora de camas poder visualizar el listado de todas las solicitudes 
de hospitalización electiva realizadas por sistemas TrakCare (dentro de la red), según los criterios 
de búsqueda que haya seleccionado el usuario. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 42 de 119 

 
 
 
 
 
 
 
 
 
 
Con distintos criterios de búsqueda, si buscamos simplemente por rango de fechas, aparecerán 
todas las solicitudes realizadas por algún médico del área de especialidades. 

El listado de pacientes permitirá a través de íconos e información rápida, poder visualizar datos 
como:  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 43 de 119 

 
 
 
 
 
  
 
 
 
a)  Diagnóstico  del  Paciente: 

  este  ícono  a  través  de  un  tool  tip,  evidenciará  la  hipótesis 
diagnóstica del paciente, relacionada a la solicitud de Hospitalización Electiva, registrada por el 
médico de especialidad que realizó la solicitud. 

b)  Registro Clínico Electrónico del paciente: al realizar clic sobre este ícono 

 se abrirá un menú 
emergente desde la derecha, en el que la gestora de camas, podrá visualizar la historia clínica del 
paciente, según episodios registrados en el sistema. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 44 de 119 

 
 
 
 
 
 
 
 
 
c)  Datos socio-demográficos del paciente que requiere la hospitalización electiva: Nombre paciente, RUN, 

fecha de nacimiento, edad, sexo. 

d)  Tiempo de Espera desde “registrada” la solicitud 

Especialidad  que  solicita  Hospitalización  Electiva:  se  visualiza  como  un  “link”  que  permite  al 
usuario visualizar los detalles de la solicitud de hospitalización electiva que realizó el médico de 
Especialidades Ambulatorio. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 45 de 119 

 
 
 
 
 
 
 
 
e)  Establecimiento de Origen y Destino: se visualizarán los establecimientos de la red de origen de 

la solicitud y de destino, siempre que registren en TrakCare. 

f)  Prioridad de la Solicitud: es la definida por el Médico quien realiza la solicitud de Hospitalización 
electiva, la gestora de camas puede modificarla. La trazabilidad de estos cambios queda visible 
para el usuario (fecha, hora, quien lo realizó). Para registrar el cambio, debe hacer clic en el link 
de  la  prioridad,  se  seguida,  se  abrirá  la  ventana  que  le  permitirá  seleccionar  una  de  las  3 
prioridades,  para  confirmar  presione  en  Actualizar.    Con  esto,  se  agregará  la  información 
actualizada. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 46 de 119 

 
 
 
 
 
 
 
 
Motivo de la Hospitalización: se visualizará el motivo que registró el Médico al realizar la Solicitud de 
Hospitalización Electiva 

5.4. 

  Incluir una nueva Solicitud de Hospitalización Electiva  

Este  sub-menú  debe  ser  utilizado  por  la  gestora  de  camas,  cuando  recibe  solicitudes  de 
hospitalización electiva por distintas vías de comunicación, menos por TrakCare. Es decir, toda 
solicitud realizada por correo electrónico, llamada telefónica, etc. que requiere ser gestionada 
por el sistema y es necesaria transcribirla. 

Existen dos opciones: 

•  Que el paciente ya exista en el índice maestro de pacientes de la red  
•  Paciente nuevo 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 47 de 119 

 
 
 
 
 
  
 
 
 
Dependiendo de la opción anterior, es si buscamos al paciente por distintos criterios de búsqueda 
(ya  está  en  base  de  datos)  o  lo  creamos  en  la  base  y  además  le  realizamos  la  solicitud  de 
hospitalización electiva. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 48 de 119 

 
 
 
 
 
 
 
 
 
5.5. 

Asignar Unidad  

La Enfermera de Gestión Camas, puede asignar la Unidad/Servicio Clínico con fecha y hora de 
Ingreso paciente. Este registro crea inmediatamente un Episodio de Hospitalización en estado 
de “Pre-admisión” del paciente. Además, alimenta el contador de Ingresos Programados. 

Desde las solicitudes de hospitalización electiva seleccione al paciente luego haga clic sobre 
el menú de acción representado por los tres puntos horizontales, la acción anterior provoca que 
a  la  derecha  de  la  pantalla  se  abra  una  ventana  emergente  con  una  serie  de  menús 
seleccionamos Gestión Hosp. Electiva, luego damos clic en el menú Asignar Unidad. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 49 de 119 

 
 
 
 
 
 
 
 
 
A  continuación,  damos  clic  en  el  botón  Nuevo  que  está  en  la  parte  inferior  de  la  ventana. 
Verificamos la información de los detalles de hospitalización damos actualizar. 

Si se realiza una consulta por las solicitudes de hospitalización Electiva en estado “Pre-admisión”, 
se  visualizarán  todas  las  solicitudes  que  ya  se  les  designó  (gestora  de  camas)  una 
Unidad/Servicio Clínico. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 50 de 119 

 
 
 
 
 
 
 
 
 
 
 
Es  posible  obtener  de  mi  listado  de  pacientes  con  solicitudes  de  hospitalización  electiva  en 
estado “Pre-admisión” el historial de su “Lista de Espera” (seleccionando el link “Pre-admisión”) 

5.6. 

  Registro Gestión Hospitalización Electiva 

Este menú permite definir el estado de gestión de la solicitud de hospitalización electiva. Desde 
las solicitudes de hospitalización Electiva seleccione al paciente luego haga clic sobre el menú 
de  acción  representado  por  los  tres  puntos  horizontales,  la  acción  anterior  provoca  que  a  la 
derecha de la pantalla se abra una ventana emergente con una serie de menús seleccionamos 
Gestión Hosp. Electiva, luego damos clic en el menú Registro Gestión. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 51 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
Es posible registrar un estado de revisión y agregar observaciones en relación a la revisión. 

Luego podrá revisar el Estado de Solicitud y el Estado de Revisión haciendo clic en los enlaces 
de cada registro. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 52 de 119 

 
 
 
 
 
 
 
 
 
 
Se desplegarán los datos de cada solicitud para mantener la trazabilidad del proceso. 

5.7. 

Remover (eliminar) Solicitud de Hospitalización Electiva 

Sólo es posible remover o eliminar una solicitud de hospitalización electiva en estado “Inicial”, 
Desde las solicitudes de hospitalización Electiva seleccione al paciente luego haga clic sobre el 
menú de acción representado por los tres puntos horizontales, la acción anterior provoca que a 
la derecha de la pantalla se abra una ventana emergente con una serie de menús seleccionamos 
Gestión  Hosp.  Electiva,  luego  damos  clic  en  el  menú  Remover  Sol.Hosp.  Se  visualizará  una 
ventana emergente, donde está la fecha y motivo de la remoción. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 53 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
En el caso de que al paciente ya se le haya asignado una Unidad/Servicio, es decir, ya tenga en 
el sistema TrakCare un episodio de hospitalización en estado “Pre-admitido”, lo correcto en ese 
caso, si se desea “Eliminar” la solicitud de hospitalización electiva, sería cancelar el episodio. 

6. 

Gestión Extra - Sistema 

Este menú permite realizar el seguimiento y gestión de la demanda de solicitudes de cama y 
derivaciones de pacientes desde y hacia el extrasistema (macro-red pública y privada).  

Existen  diferentes  casos  en  los  que  un  establecimiento  realiza  derivaciones  hacia  el  Extra 
sistema. Por ejemplo, un establecimiento que no cuenta con la capacidad de atención requerida 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 54 de 119 

 
 
 
 
 
 
 
 
 
 
por el paciente (ej. Cuidados intensivos) debe derivar al paciente a la macro-red para que reciba 
el cuidado necesario. Otro ejemplo lo constituyen las solicitudes de hospitalización que puede 
recibir un establecimiento desde otro hospital de la macro-red.  

A  continuación,  se  describen  las  funciones  específicas  de  los  sub-menús  por  medio  de  la 
secuencia esperada de los eventos. 

6.1. 

Ingreso Extra-Sistema 

A través de este menú, el usuario puede ingresar los pacientes que han sido derivados al extra 
sistema.  

El primer paso es buscar al paciente, a través de algún dato demográfico. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 55 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Una vez dentro, seleccione el número de registro que corresponde al paciente. 

Se mostrarán las solicitudes de hospitalización que se han generado anteriormente para este 
paciente, en caso de que exista. Presione el botón 

 Nuevo. 

Completar información requerida para realizar la gestión de seguimiento. Recuerde revisar cada 
sección para asegurarse que ha completado todos los datos. Es muy importante verificar que los 
Detalles de Origen y Destino reflejen correctamente la derivación. En el campo Establecimiento 
de  Destino  debe 
ingresar  Macro-Red  Privada  o  Macro-Red  Pública  para  diferenciar 
apropiadamente entre ambas redes. Cuando haya finalizado haga clic en Actualizar. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 56 de 119 

 
 
 
 
 
 
 
 
 
 
Esta derivación se agregará al Listado de derivaciones, para seguimiento de pacientes. 

6.2. 

Incluir Solicitud Hospitalización Extra Sistema 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 57 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
Permite  registrar  una  solicitud  de  hospitalización  de  un  paciente  al  establecimiento.  Esta 
funcionalidad es útil en el Rescate de pacientes derivados al extra sistema. 

Pasos a seguir: 

En la pantalla de búsqueda ingrese algún dato del paciente y haga clic en el botón Buscar. 

Seleccione el número de registro que corresponde al paciente. 

Se mostrarán las solicitudes de hospitalización que se han generado anteriormente para este 
paciente. Haga clic en el botón 

 Nuevo. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 58 de 119 

 
 
 
 
 
 
 
 
 
 
Utilice  las  lupas,  casilleros  y  cuadros  de  texto  para  completar  los  datos  de  la  solicitud  de 
Hospitalización. Recuerde revisar cada sección para asegurarse que ha completado todos los 
datos. Cuando haya finalizado haga clic en Guardar. 

Esta solicitud se agregará a la Lista de Ingresos de Solicitudes de Hospitalización. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 59 de 119 

 
 
 
 
 
 
 
 
 
6.3. 

Lista Derivaciones 

En este sub-menú, el usuario podrá realizar seguimiento de las derivaciones al extra sistema. 
Utilice las lupas y casilleros para establecer los criterios de búsqueda que le permitirán filtrar las 
solicitudes. Luego haga clic en Buscar. 

Aparecerán todas las solicitudes que cumplan con los criterios establecidos de búsqueda. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 60 de 119 

 
 
 
 
 
 
 
 
 
 
 
6.4. 

Registro Gestión 

Desde el sub-menú Lista de Derivaciones (listado de pacientes en seguimiento de derivación al 

extra sistema), seleccione al paciente desde los tres puntos horizontales 
menú Registro Gestión que se ubica dentro del acordeón de Gestión Extra-Sistema. 

 y Seleccione el sub-

El usuario podrá registrar el estado de su gestión (con relación al paciente seleccionado el Lista 
Derivaciones)  y  observaciones  en  texto  libre,  una  vez  ingresada  la  información,  presionamos 
Actualizar.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 61 de 119 

 
 
 
 
 
 
 
 
 
 
Al  actualizar,  podemos  ver  que  la  información  se  carga  en  la  Lista  de  Revisión.  Ahora  ya 
podemos guardar los datos.  

Al  hacer  clic  en  el  estado  podrá  visualizar  el  histórico  de  los  estados  de  revisión/gestión 
realizados con el paciente (fecha, hora, comentario, usuario). 

6.5. 

Remover Registro 

Desde el sub-menú Lista de Derivaciones (listado de pacientes en seguimiento de derivación al 

extra sistema), seleccione al paciente desde los tres puntos horizontales 
menú Remover Registro que se ubica dentro del acordeón de Gestión Extra-Sistema. 

 y Seleccione el sub-

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 62 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
En la ventana Remover Registro puede ingresar los datos del cambio de estado. Use las lupas 
para seleccionar un Motivo e ingrese comentarios para explicar con mayor detalle. Cuando haya 
finalizado haga clic en Actualizar. El paciente saldrá de la lista de seguimiento. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 63 de 119 

 
 
 
 
 
 
 
 
 
 
7. 

Lista de Preadmisiones 

En la Lista de Preadmisiones puede realizar una búsqueda completando los campos con algún 
dato y luego hacer clic en Buscar. 

Aparecerá el listado de los pacientes que se encuentran en espera del ingreso hospitalario. Para 
autorizar la admisión de un paciente de esta lista haga clic en la Fecha de Ingreso del paciente. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 64 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
En la siguiente pantalla debe confirmar los datos demográficos del paciente y luego haga clic en 
Actualizar. 

Aparecerá la Preadmisión del paciente, seleccione el Número de Episodio.         

Verá el Registro de Hospitalización donde debe completar los campos obligatorios (marcados 
en negrita). En caso de una paciente embarazada que no tenga registrada la fecha probable de 
parto,  usted  deberá  ingresarla  solamente  si  se  encuentra  en  la  búsqueda  automática  (lupa). 
Recuerde hacer clic en Guardar. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 65 de 119 

 
 
 
 
                  
 
 
 
En la siguiente pantalla podrá ingresar detalles de seguro u otra previsión que tenga el paciente. 
Seleccione Actualizar para avanzar. Con esto se completa el proceso de registro del paciente, 
por lo que desaparecerá de la lista de Preadmisiones. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 66 de 119 

 
 
 
 
 
 
 
 
 
 
 
8. 

Búsquedas 

Este menú permite realizar búsquedas por paciente o por episodios de atención. 

8.1. 

Búsqueda por Paciente 

1.  Puede encontrar un paciente en el sistema para visualizar sus datos demográficos. 

2.  Seleccione el menú Búsquedas.  

3.  Seleccione el Sub-menú Pacientes. 

4.  Ingrese RUN del paciente o algún dato que estime conveniente. 

5.  Haga clic en Buscar. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 67 de 119 

 
 
 
 
 
 
 
 
Se  mostrará  el  Listado  de  Pacientes  encontrados,  para  el  ejemplo  anterior,  buscamos  por 
apellido “Salas”. A continuación, se mostrarán todos los pacientes de apellido “Salas”. Para ver 
los detalles de un paciente seleccione el N° de Registro. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 68 de 119 

 
 
 
 
 
 
8.2. 

 Búsqueda Por Atención 

En  esta  búsqueda  puede  encontrar  un  paciente,  ver  la  lista  de  atenciones  (episodios)  pasadas,  y  la 
atención actual. 

1.  Seleccione el menú Búsqueda.  
2.  Seleccione el Sub-menú Atención. 
3. 
4.  Haga clic en Buscar. 

Ingrese RUN del paciente o algún criterio que estime conveniente. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 69 de 119 

 
 
 
 
 
 
 
 
El sistema mostrará el Listado de Episodios o Atenciones del Paciente. Es posible identificar los 
episodios por la letra de inicio del N° de episodio. Los de tipo ambulatorio comienzan con la letra 
A, los de hospitalización con la letra H y los de urgencia con la letra U. Para revisar un registro 
haga clic en el N° del Episodio. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 70 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
9. 

Consultar Pabellón 

Este menú permite realizar una consulta rápida a la lista de agendamientos quirúrgicos. Puede 
realizar la búsqueda a través de los campos fecha (desde, hasta), estado de la solicitud, área 
quirúrgica, N° de registro y N° de Quirófano. Ingrese los campos y haga clic en Buscar. 

Se mostrarán todos los registros que cumplan con los criterios establecidos. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 71 de 119 

 
 
 
 
 
10. 

Archivo 

Permite realizar una serie de tareas con la ficha clínica (FC) del paciente, como enviar y recibir, 
consultar ficha del paciente y la solicitud de la ficha. Es importante mencionar que la búsqueda 
de la FC del paciente se puede realizar con diferentes filtros de búsqueda (RUN, N° de ficha, 
Nombre y Apellido, etc.). 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 72 de 119 

 
 
 
 
 
 
 
10.1. 

 Enviar/Recibir 

Podrá enviar y recibir la ficha del paciente, para enviar solo debemos ingresar unidad de destino 
y enviar la solicitud, luego para recibir debe ir a opciones, recibe, así la ficha del paciente quedará 
en la unidad actual. 

10.1.1. 

Enviar 

Para hacer el envío de una ficha clínica primero debe realizar la búsqueda ingresando algún dato 
y  luego  clic  en  Buscar.  El  sistema  mostrará  en  los  detalles  de  la  solicitud  la  información 
correspondiente a la ficha clínica, con datos del nombre paciente, número de ficha, volumen, etc. 

Antes de realizar el envío puede ver la trazabilidad de la ficha clínica haciendo clic en el dato que 
está en la columna Unidad Actual. Esto abrirá el Historial de movimientos, donde se detallan 
todos los cambios de ubicación del paciente seleccionado. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 73 de 119 

 
 
 
 
 
 
 
 
 
 
Finalmente, para hacer el envío debe seleccionar la unidad de destino y hacer clic en Enviar 
Solicitud. 

10.1.2. 

Recibir 

Para recibir una ficha clínica primero debe realizar la búsqueda ingresando algún dato y luego 
clic en Buscar. El sistema mostrará en los detalles de la solicitud la información correspondiente 
a la ficha clínica, con datos del nombre paciente, número de ficha, volumen, etc. 

En el menú flotante Opciones deberá seleccionar Recibe. 

El sistema mostrará una pantalla con los detalles de la recepción. Al hacer clic en Actualizar, la 
ficha clínica será recibida. 

Usted puede confirmar esta recepción de dos formas, la primera es la casilla que se marca con 
un check en la columna de Recibido. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 74 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
La  otra  manera  de  confirmar  la  recepción,  es  haciendo  clic  en  el  dato  de  la  columna  Unidad 
Actual,  donde  puede  acceder  al  Historial  de  Movimiento  y  revisar  la  columna  Transacción 
donde se reflejan los envíos y recepciones realizados. 

10.2. 

 Consulta FC de Paciente 

Este sub-menú permite realizar la búsqueda de la ficha clínica del paciente, en caso de que se 
desconozca  el  lugar  en  donde  se  encuentra.  Puede  ingresar  directamente  seleccionando  al 
paciente  desde  el  mapa  de  piso  o  bien  ingresar  información  del  paciente  en  los  filtros  de 
búsqueda.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 75 de 119 

 
 
 
 
 
 
 
 
 
 
Se mostrarán las Fichas Clínicas de los pacientes que cumplen con los criterios de búsquedas 
ingresados. 

Seleccione el N° de registro y podrá saber el lugar actual de la ficha.  

Verá la unidad actual de la ficha clínica, el número de volúmenes (podrá crearlo si es necesario). 
Además, se muestra el historial de movimientos de la ficha clínica. 

Puede seleccionar Enviar Ficha a y seleccionar la unidad de destino. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 76 de 119 

 
 
 
 
 
 
 
 
 
 
10.3. 

Solicitud FC 

Permite realizar una solicitud de la FC del paciente a la unidad en donde se encuentra, en caso 
que no haya recibido la ficha y el paciente se encuentre en la unidad. 

Podemos realizar la Solicitud FC de dos formas distintas. La primera, a través del menú principal 
y luego ingresando algún filtro de búsqueda para encontrar al paciente.   

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 77 de 119 

 
 
 
 
 
 
 
O  seleccionando  al  paciente  desde  el  mapa  de  piso  e  ingresado  al  menú  emergente, 
seleccionando Solicitud FC. 

Ahora podrá ver los detalles de la solicitud a realizar. Seleccione la unidad a la cual desea hacer 
la solicitud de la FC.  

Puede ver los Volúmenes Pasivos  de la ficha (reactivar alguno si lo necesita) o bien ver los 
Requerimientos Anteriores. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 78 de 119 

 
 
 
 
 
 
 
   
11. 

 Resumen Solicitudes de Cama 

Este menú muestra un resumen de las solicitudes de cama prioritarias, las que se han recibido y 
las que se han enviado a los distintos servicios o unidades. Se puede administrar el cambio 
de estado para uno o más pacientes de manera simultánea. Para ello, seleccione al o a los 
 correspondientes y posteriormente haga 
pacientes que necesite marcando las casillas 

clic en el menú de los tres puntos verticales 

. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 79 de 119 

 
 
 
 
 
 
 
 
A  continuación  seleccione  el  acordeón  Administrar  e  ingrese  al  sub  menú  Cambio  de 
estado. 

El enlace Preferencias le permitirá configurar las Unidades que se mostrarán en esta pantalla. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 80 de 119 

 
 
 
 
 
 
 
 
 
En la lista, estarán todas las solicitudes de cama para la sala seleccionada desde la preferencias.  

Desde los tres puntos verticales 
, podemos entrar al menú emergente Guardar y damos cloc 
en  Guardar  por  Usuario,  esto  le  permite  guardar  estos  cambios  por  usuario  (es  decir  se 
guardarán estas preferencias sólo para el usuario de la sesión).  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 81 de 119 

 
 
 
 
 
 
 
 
 
El  botón  Actualizar  refrescará  la  pantalla  y  se  mostrarán  las  solicitudes  que  se  configuraron 
como Preferencias.  

El botón Eliminar borrará los elementos que se han registrado como Preferencias.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 82 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
12. 

Solicitud de Traslado Interno 

La solicitud de traslado interno, se refiere a aquellas solicitudes de cama entre servicios clínicos 
dentro  del  mismo  Establecimiento.  Son  registradas  por  la  enfermera  tratante  del  piso  y 
gestionadas por la gestora de cama.  

Enfermera Hospitalizado genera solicitud de traslado a otra unidad/servicio clínico del mismo 
establecimiento,  selecciona  al  paciente,  y  realiza  clic  en  el  menú  Gestión  Cama  y  sub-menú 
“Solicitud de Traslado”. 

Se  desplegará  la  siguiente  pantalla,  se  deben  completar  los  datos  referentes  a  la  unidad 
requerida para el traslado. 

Al  actualizar  aparecerá  la  solicitud  en  estado  Requerido.  Podemos  revisarlo  ingresando 
nuevamente en el menú de Solicitud de Tralsado desde el menú emergente.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 83 de 119 

 
 
 
 
 
 
Veremos que en la parte inferior, aparece la solicitud con la información de la solicitud realizada. 

Al volver al perfil de Gestión de Camas, podemos ver en el mapa de piso, que el paciente ahora 

nos aparece con un ícono 
clic sobre el ícono, se abrirá el menú emergente y veremos la fecha y hora de la solicitud. 

 que indica que tiene una solicitud de traslado requerida, al hacer 

También podemos verlo al cambiar la vista de la unidad a lista de pacientes. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 84 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
En la unidad solicitada aparecerá el paciente en la estación de enfermería con el mismo ícono 

12.1. 

Gestión Solicitud de Traslado Interno 

Para  aceptar  o  rechazar  la  solicitud  la  Gestora  de  Cama  debe  ingresar  al  menú  Servicios 
Clínicos. Y en la columna “Solicitudes de Cama” seleccionar el número perteneciente a la unidad 
donde se derivó la solicitud.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 85 de 119 

 
 
 
 
 
 
 
 
 
Se desplegará el listado de solicitudes de cama para la unidad seleccionada. Para aceptar la 
solicitud se debe seleccionar al paciente y dar clic en los tres puntos verticales para abrir el 
menú emergente. Desde ahí, bajo el acordeón Administrar, seleccionamos el menú Cambio de 
Estado.  

Dentro  del  componente,  seleccionamos  la  instancia  indicada,  ésta  puede  ser  “Aceptado  / 
Asignado”, “Rechazado / Cancelado”, “Requerido / Solicitado”.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 86 de 119 

 
 
 
 
 
 
 
 
 
Sólo en caso de Rechazar una solicitud será necesario indicar la Razón del rechazo. Luego de 
este paso, damos clic en Actualizar.  

12.1.1. 

Estado Gestión Camas 

Las solicitudes tienen los siguientes estados:  

1)  Requerido/Solicitado: Se refiere a la creación de la solicitud de cama para otra unidad, la cual debe ser 

gestionada. 

2)  Aceptado/Asignado: Se refiere a la gestión de dicha solicitud, la cual fue aceptada para la nueva unidad.  
3)  Rechazado/Cancelado: Se refiere al rechazo de la solicitud, esto incurrirá en que el paciente se mantenga 

en la unidad solicitante o sea derivado a otra unidad. 

Importante:   

Sí la solicitud del paciente es Aceptada cambiará el ícono 

 de color indicando que la solicitud 

fue aceptada 
de la unidad donde está acostado como la solicitada.  

, el cual se mostrará en el mapa de piso asociado al paciente, tanto en el mapa 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 87 de 119 

 
 
 
 
 
 
 
 
 asociado al paciente desaparecerá en el mapa 
En el caso que ésta sea Rechazada el ícono 
de piso de la unidad donde está acostado y en la unidad solicitada el paciente no se mostrará en 
la estación de enfermería.  

Al cambiar el estado, la solicitud de traslado interno desaparecerá del listado de “solicitudes”, ya 
que ésta contiene sólo las solicitudes con estado “Requerido/Solicitado”.  

12.1.2. 

Solicitud de Traslado Interno Aceptada 

Vista desde la unidad de origen: 

Vista desde la unidad solicitada: 

Para  mover  al  paciente  a  la  cama  de  nuevo  destino,  la  enfermera  tratante  de  la  unidad 
solicitada,  deberá  realizar  un  “Movimiento  de  Traslado  Interno”  desde  el  menú  “Gestión 
Cama”, sub-menú “Movimiento Traslado Interno”.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 88 de 119 

 
 
 
 
 
 
 
 
 
En la Lista de movimientos de sala y cama, generar 

 Nuevo movimiento de traslado.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 89 de 119 

 
 
 
 
 
 
Seleccionar Unidad / Servicio Clínico y Cama. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 90 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Movimiento creado.  

Importante:  el  ícono  de  traslado  aceptado 
,  desaparece  al  momento  en  que  la 
enfermera/matrona de la unidad solicitada, traslada al paciente a la cama designada vía sistema 
(Movimiento de traslado creado).  

Paciente acostada en cama seleccionada en unidad de traslado.  

Y en la unidad de origen, el paciente abandona la cama. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 91 de 119 

 
 
 
 
 
 
 
 
12.1.3. 

Solicitud de Traslado Interno Rechazada 

Con la solicitud generada, el gestor de cama, tomará la solicitud desde el listado de solicitudes 
para la unidad requerida. 

Unidad Solicitante: Unidad Médico Quirúrgico 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 92 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
Unidad Solicitada: Unidad de Medicina 

El encargado de Gestión de Camas, deberá ingresar al menú principal, y seleccionar El menú 
Gestión de Camas, lo que desplegará el acordeón de “Servicios Clínicos”. 

En la ventana de Servicios clínicos, bajo la columna “Solicitudes de Cama”, damos clic en el 
número que corresponda a la unidad de destino de la solicitud realizada.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 93 de 119 

 
 
 
 
 
 
Se desplegará el listado de pacientes con solicitudes para la unidad seleccionada. Para rechazar 
una solicitud se debe seleccionar al paciente desde la casilla 
 y luego abrir el menú contextual 
desde  los  tres  puntos  verticales,  acá  debe  seleccionar  la  opción  “Cambio  de  estado”  que  se 
encuentra dentro del menú desplegable “Administrar”.  

Se  desplegará  la  siguiente  pantalla,  en  donde  se  debe  seleccionar  el  estado  de  cambio 
Rechazado / Cancelado y establecer la  razón del  rechazo. Note que el motivo de rechazo se 
encuentra en negrita, lo que indica que es de carácter obligatorio para poder avanzar. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 94 de 119 

 
 
 
 
 
 
 
 
 
Una vez seleccionado el rechazo y el motivo de rechazo, damos clic en Actualizar. 

Al actualizar desaparecerá el paciente en el listado de solicitudes. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 95 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
No aparecerá tampoco en la estación de enfermería de la unidad solicitada.  

Y en la unidad solicitante el paciente no tendrá el ícono 

 con la solicitud de traslado.  

13. 

Reconversión Camas:  

Se describen dos tipos de Reconversión Camas: 

13.1. 

 A “Demanda”: 

Paciente  que  ingresa  desde  Servicio  de  Urgencia,  necesita  hospitalizarse  en  Pediatría  y  no  hay  camas 
disponibles.  En  la  unidad  de  Traumatología  hay  una  cama  disponible  y  finalmente  el  paciente  queda 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 96 de 119 

 
 
 
 
 
 
 
 
hospitalizado. La unidad de Trumatología queda como responsable (Médico Tratante) del paciente a pesar 
de que esté acostado en otra Unidad (paciente ectópico). 

El médico solicita la hospitalización desde la Urgencia, para hacerlo entra al menú del paciente desde los 
tres puntos verticales. 

Solicitud de Hospitalización desde Urgencia para unidad de Traumatología. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 97 de 119 

 
 
 
 
 
 
 
Resumen Servicio Clínico columna Solicitudes de Camas donde se visualizará la solicitud desde 
Urgencia.  

La gestora de cama seleccionará el paciente dese la casilla correspondiente, para luego aceptar 
la Solicitud.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 98 de 119 

 
 
 
 
 
 
 
 
El Médico de Urgencia dará el Cierre a la atención de Urgencia con destino Hospitalización (Alta 
Médica) 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 99 de 119 

 
 
 
 
 
 
 
 
 
 
Admisión de Urgencia realiza el Cierre de Urgencia Administrativo. 

Admisión  de  Hospitalizado  registra  la  hospitalización  del  paciente.  Desde  el  mapa  de  piso  se 
ingresa al menú del paciente, donde entraremos a “Registro de Hospitalización”. 

En el registro, complete los datos obligatorios, en el caso que falte algún dato como estado civil 
y religión. Luego actualice.  

Al actualizar, se abrirá la preadmisión para este paciente, donde debemos seleccionar su Nº de 
episodio. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 100 de 119 

 
 
 
 
 
 
 
 
 
Los  campos  Unidad/Servicio  y  Especialidad  vendrán  por  defecto  de  la  solicitud  de 
hospitalización realizada en urgencia. Al Actualizar el paciente quedará Hospitalizado. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 101 de 119 

 
 
 
 
 
 
 
 
Enfermera tratante o gestora de camas mueve al paciente de la Estación de Enfermería de la 
unidad  Pediatría  a  la  Unidad  de  Traumatología  (cama  prestada)  mediante  el  menú  “Mov. 
Traslado Interno”; Nuevo Movimiento. 

Para  completar  la  acción  se  debe  agregar  la  Unidad/Servicio  Clínico  a  trasladar.  Según 
corresponda, podría agregar también la unidad responsable del paciente. 

Nota: el campo Unidad Responsable del paciente indicará que será la unidad tratante de la atención del 
paciente que se encuentra fuera de la unidad de origen.   

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 102 de 119 

 
 
 
 
 
 
 
 
Al actualizar aparece el siguiente mensaje de alerta 

Al seleccionar cancelar, será devuelto para cambiar el servicio/unidad.  

Al aceptar, el paciente será movido automáticamente a la Estación de Enfermería de la unidad 

de destino. En la unidad de destino, en la estación, aparecerá con el ícono 
el paciente está al cuidado de otra unidad responsable.  

, que indica que 

Devolución del paciente a Unidad de origen. 

Para realizar la devolución del paciente a su unidad de origen, se debe generar un movimiento 
de traslado interno.  Desde el menú del paciente, seleccionamos “Gestinón de Camas” y bajo 
elegimos “Mov. de Transado Interno”. Luego de ingresar, creamos una nueva instancia desde el 
botón 

 Nuevo. Se asigna la Unidad/Servicio clínico Unidad de Medicina  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 103 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
Al actualizar el paciente desaparecerá del mapa de piso de la unidad Traumatología, moviéndose 
automáticamente a la estación de enfermería de la unidad de origen (Unidad de Medicina).  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 104 de 119 

 
 
 
 
 
 
 
 
 
 
 
13.2. 

Reconversión de Cama Programada (Estacional) 

La Unidad de Traumatología reconvierte una cama por la campaña de invierno a la Unidad de Medicina 

Para esto se requiere reconvertir la cama ubicada en Traumatología a la especialidad de Medicina.  Para 
realizar la conversión de camas, se debe hacer clic sobre el nombre de la cama luego convertir Cama - 
Local 

Se  desplegará  la  especialidad  activa  para  la  cama  seleccionada.  Antes  de  agregar  la  nueva 
Especialidad es necesario registrar una Fecha “Hasta” para convertir la Especialidad.  

Al  actualizar  se  debe  agregar  la  nueva  especialidad  a  la  que  pertenecerá  la  cama  de 
Traumatología  Ed,  en  este  caso  Pediatría  Ed.  Además,  debemos  agregar  una  fecha  desde  y 
hasta, que será considerada dentro de la programación de este tipo de reconversión cama.   

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 105 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Al Actualizar en la cama seleccionada aparecerá un ícono que, al posicionarse sobre él, mostrará 
una leyenda con la especialidad de la nueva cama reconvertida. La cama reconvertida queda 

con el ícono 

Entonces la visualización de los servicios Clínicos sería la siguiente en cada caso:  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 106 de 119 

 
 
 
 
13.2.1. 

Antes de reconvertir la cama:  

13.2.2. 

Después de reconvertir la cama:  

Se puede observar que existe un cambio en el Total de las camas en la sección de Especialidad 
y Unidad Funcional. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 107 de 119 

 
 
 
 
 
14. 

Otras Funcionalidades del mapa de Piso  

14.1. 

 Reserva de Cama: 

La reserva de cama puede ser realizada por la enfermera de piso, En los casos que Paciente 
necesite realizarse un procedimiento en otro establecimiento de salud por ejemplo RMN, para 
eso deberá seleccionar al paciente desde el mapa de piso e ir a menú Gestión Cama, Sub menú 
“Movimiento de Traslado Interno”. 

Se  habilitará  una  pantalla  en  la  cual  deberá  registrar  el  nuevo  movimiento,  Una  vez  que  se 
registra el movimiento deberá completar los datos de ubicación Temporal (Lugar donde se va a 
ser  dirigido  el  paciente),  Marcar  Check  de  Reserva  de  Cama  y  colocar  la  razón  de  cama  no 
disponible. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 108 de 119 

 
 
 
 
 
 
En ubicación Temporal, al seleccionar la lupa 
en el sistema. 

 se desplegará el listado de unidades cargadas 

Mediante la lupa 
a seleccionar. 

 de “razón para cama no disponible” se desplegará un listado con 4 causales 

Una  vez  registrada  esta  información,  presionamos  el  botón  “Guardar”,  con  esto,  el  paciente 
aparecerá en el mapa de piso de origen con la cama Reservada. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 109 de 119 

 
 
 
 
 
 
 
14.2. 

Revertir Reserva de Cama 

Para reversar la cama que fue Reservada por la enfermera de piso, Matrona o Gestora de Cama, 
se debe seleccionar al paciente ya sea desde el mapa de piso, o de la lista de pacientes, ambas 
visualizaciones de la unidad permiten acceder al menú de “Movimiento Traslado Interno”.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 110 de 119 

 
 
 
 
 
 
 
 
Se  desplegará  una  pantalla  en  la  cual  deberá  seleccionar  Nuevo  Movimiento,  Se  habilitará 
pantalla en la cual se deberá colocar la Unidad/Servicio Clínico y cama en la cual se encuentra 
el paciente, posteriormente seleccionar el botón Guardar. 

En el apartado “Cama” una vez que presionamos la lupa 
, se desplegará el listado de todas 
las camas con relación a la unidad / Servicio seleccionado, donde podremos encontrar la cama 
que ha sido reservada anteriormente. A continuación, presionamos Guardar. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 111 de 119 

 
 
 
 
 
 
 
 
 
El movimiento realizado se visualizará en el listado de movimientos del paciente 

En el mapa de piso el paciente será visualizado sin la reserva de cama 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 112 de 119 

 
 
 
 
 
 
 
 
14.3. 

Ubicación/Unidad Temporal 

Se utiliza la funcionalidad de bloqueo temporal en el caso de que un paciente se encuentre en 
alguna  Unidad  Transitoria  dentro  del  mismo  Establecimiento  por  ejemplo  en  Pabellón, 
Hemodinamia,  Diálisis,  algún  procedimiento  Endoscópico,  Examen  de  TAC,  AngioTAC.  Para 
registrar esta ubicación Temporal se deberá seleccionar al paciente, menú Mov. Traslado Interno. 

Se desplegará una pantalla en la cual se debe registrar nuevo movimiento, Ubicación Temporal 
posteriormente guardar. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 113 de 119 

 
 
 
 
 
 
 
 
 
 
En Mapa de piso el paciente seleccionado quedará con una franja de color turquesa con Tool Tip 
que informa la ubicación Temporal del paciente. 

14.4. 

Reversar Ubicación Temporal 

Si necesita reversar la unidad Temporal deberá seleccionar nuevamente el paciente, menú Mov. 
Traslado Interno. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 114 de 119 

 
 
 
 
 
 
Se desplegará una pantalla en la cual se debe registrar nuevo movimiento, en Unidad/Servicio 
Clínico y Cama donde se encuentra el paciente, posteriormente Guardar. 

Una vez ingresado los datos correspondientes, el paciente se visualizará en el mapa de piso sin 
la franja de color Turquesa 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 115 de 119 

 
 
 
 
 
 
 
 
14.5. 

Bloquear Cama 

Para realizar el Bloqueo de Cama la Enfermera, Matrona o Gestora, deberá seleccionar desde 
la barra superior, donde se encuentra el nombre de la cama. 

Al seleccionar la barra, se desplegará una pantalla en la cual se deberá registrar fecha de inicio, 
hora de inicio y el motivo por el cual la cama no se encuentra disponible, completado este registro 
seleccionar el botón actualizar. 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 116 de 119 

 
 
 
 
 
 
 
 
La cama bloqueada se visualizará en el mapa de piso indicando el motivo de cama no disponible 
y la fecha en que estará disponible nuevamente.  

Para  volver  habilitar  esa  cama  se  deberá  seleccionar  nuevamente  la  barra  del  nombre  de  la 
cama. 

Se desplegará nuevamente la pantalla en la que indicamos la hora y fecha anteriormente. En la 
parte  inferior,  se  encuentra  el  historial  de  bloqueos  realizados  en  la  cama  seleccionada,  a 
continuación, deberá seleccionar el ultimo bloqueo de cama registrado dando clic en la fecha del 

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 117 de 119 

 
 
 
 
 
 
 
 
 
último bloqueo. Al hacer esta acción se completarán los datos de bloqueo de cama que fueron 
registrados  anteriormente,  en  esta  pantalla  deberá  agregar  fecha  y  hora  de  término  de 
desbloqueo de cama, posteriormente Actualizar. Esto dejará nuevamente la cama habilitada y el 
registro en la lista de cambios. 

Otra forma de habilitar la cama es a través del botón “Eliminar”, esto habilita la cama de manera 
inmediata. 

Sin embargo, lo que hace es eliminar la indicación desde el registro.  

Confidencial y privado, requiere autorización para imprimir.            VOLVER AL ÍNDICE 

 Página 118 de 119 

 
 
 
 
 
 
 
 
 
 
 
 
 
InterSystems Chile 

Avenida del Valle No 890, 6o piso  
Ciudad Empresarial, Huechuraba 

Santiago, Chile 

Tel: +56.2.28926000 

InterSystems Corporation  

World Headquarters 

One Memorial Drive  

Cambridge, MA 02142-1356  

Tel: +1.617.621.0600 

InterSystems.com/cl 

InterSystems.com 

InterSystems  TrakCare,  InterSystems  HealthShare,  InterSystems  Caché,  InterSystems  Ensemble,  and  InterSystems 
DeepSee are registered trademarks of InterSystems Corporation. Other product names are trademarks of their respective 
vendors. Copyright © 2024 InterSystems Corporation. All rights reserved. 4-15
