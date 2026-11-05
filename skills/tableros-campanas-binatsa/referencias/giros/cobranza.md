# Giro Cobranza (llamadas salientes y gestión de cartera)

Métricas, reglas de cálculo y vistas propias de las campañas de cobranza. El diseño, las tarjetas, los tooltips y la interactividad son los generales (`referencias/diseno.md`, `referencias/tooltips.md`). Este glosario es la fuente de las definiciones de la Guía y glosario y de los tooltips: si cambia una definición, se cambia aquí primero. Confirmar las definiciones con el cliente al inicio y registrar en `brief.md` las que difieran.

## Categorías del giro
- **Segmento (o bucket):** tramo de días de mora. Nombres y rangos los da cada cliente (no asumir A/B/C). Su color es una rampa del primario del cliente, de claro (menos mora) a oscuro (más mora), igual en todas las hojas.
- **Canal:** subcampaña o producto (por ejemplo dos productos y dos tramos de mora), si el cliente separa así su cartera.
- **Control de arriba:** Segmento o Canal, el que use el cliente (pueden ir los dos).
- **Resaltar al pasar el mouse:** una sola acción por vista, por su campo de categoría principal: Canal (o Segmento) en Dirección y Asesor en Operación y Asesores. Usar el mismo nombre de campo en todas las hojas.

## Tarjetas
- **Fila principal:** Monto recuperado, Pagos recibidos, Promesas de pago, Monto prometido, % cartera gestionada y % contacto con titular.
- **Fila de apoyo (opcional, según los datos):** Tasa de recuperación, Intentos por cuenta, % conexión, Pago por llamada, Cuentas sin gestión y Contactos clave.
- **Bajar es mejorar** en Cuentas sin gestión e Intentos por cuenta: el color del delta se invierte.
- Preferir métricas que ayuden a decidir. Descartar las descriptivas sin acción: día de mayor volumen, franja más cargada, pico de personas, peso del fin de semana, días con operación.

## Mapa de calor de Dirección
- **Filas:** segmento (o canal, si el cliente trabaja por canal). **Columnas:** días del rango.
- **Opciones del selector KPI**, en este orden (quitar solo las que el cliente no tenga en sus datos): Promesas, Monto recuperado, Pagos recibidos, Monto prometido, Tasa de recuperación, Intentos de llamada, Intentos por cuenta, Cuentas asignadas, Cuentas gestionadas, Cuentas sin gestión, Cuentas contactadas, Contacto con titular, Contactos clave, % cartera gestionada, % sin gestión, % conexión, % contacto con titular, % promesa, Pagos por promesa (%) y Pago por llamada.
- **Por defecto:** Promesas.

## Operación en Cobranza
Son las cinco hojas obligatorias de `referencias/diseno.md`:
1. **🕒 ¿En qué horas contestan los titulares?** Hora contra día; selector con Gestiones, Contactos con titular, Promesas, Cuentas distintas, % contacto y % promesa.
2. **🏆 ¿Quién produce y quién necesita apoyo?** Tabla por asesor: gestiones, cuentas, intentos por cuenta, % contacto, % promesa, monto prometido, monto recuperado, y hora de primera y última gestión; con total general.
3. **📞 ¿Qué está pasando en las llamadas?** Tipificaciones de mayor a menor, apiladas por segmento o canal.
4. **👥 ¿Quién marca más?** Llamadas por asesor.
5. **📈 ¿Cuánto se marca cada día?** Segmento o canal contra día; selector con Llamadas, Contestadas, Conversaciones, % conexión y % contacto.

## Vistas propias del giro (según los datos)
- **👥 Asesores:** si el cliente tiene metas por asesor (por ejemplo llamadas por día, casos trabajados o vueltas por caso), tarjetas de cumplimiento, mapa de cumplimiento por asesor y día, y faltantes.
- **🗂️ Avance de cartera:** cuentas por segmento y por fecha de asignación, cuántas siguen en gestión y cuántas se retiraron.
- **⏰ Adherencia:** si hay datos de conexión de asesores: adherencia por día y turno, y entradas tarde.
- **📅 Cierre diario:** tabla de un indicador por fila contra días, para el reporte diario de operación.
- **🏠 Visitas:** si la campaña tiene gestión en campo: visitas por resultado y por segmento.

## Glosario (definiciones estándar)
Contacto, promesa y los demás resultados se identifican **por la tipificación**, según el catálogo acordado con el cliente (regla 4). Cada cliente nombra distinto sus tipificaciones: al iniciar se mapea cuáles cuentan como contacto con titular y cuáles como promesa, y se confirma con el usuario.

**🗂️ Cartera y cobertura**
- **Cuentas asignadas:** cuentas en la cartera del periodo y segmento; es la base contra la que se mide todo.
- **Cuentas gestionadas:** cuentas distintas con al menos una gestión (llamada, visita o mensaje con respuesta) en el rango.
- **% cartera gestionada (cobertura):** cuentas gestionadas ÷ cuentas asignadas.
- **Cuentas sin gestión:** asignadas − gestionadas. **% sin gestión** = 1 − % cartera gestionada.
- **% sigue en gestión:** cuentas asignadas que no se han retirado de su campaña.

**📞 Gestión y contacto**
- **Intentos de llamada:** llamadas salientes realizadas en el rango.
- **Intentos por cuenta:** intentos ÷ cuentas gestionadas.
- **Vueltas de base:** intentos ÷ cuentas asignadas (por ejemplo 200 intentos ÷ 100 cuentas = 2 vueltas).
- **% conexión:** llamadas contestadas ÷ llamadas salientes. Cuenta **llamadas**.
- **Cuentas contactadas:** cuentas donde se habló con alguna persona (titular o tercero).
- **Contacto con titular (RPC):** gestiones cuya tipificación indica que se habló con el titular.
- **% contacto con titular:** cuentas con contacto con titular ÷ cuentas gestionadas. Cuenta **cuentas**, no llamadas (por eso es distinto de % conexión).
- **Contactos clave (KP):** contactos con la persona clave que define el cliente; **Monto KP** = monto asociado a esos contactos.

**🤝 Promesas y pagos**
- **Promesas de pago:** gestiones con tipificación de promesa (fuente oficial: regla 10).
- **% promesa:** promesas ÷ contactos con titular.
- **Monto prometido:** suma del monto de las promesas.
- **Pagos recibidos:** número de pagos aplicados (un pago parcial también cuenta).
- **Monto recuperado:** suma de los pagos aplicados en el rango, por la fecha que diga la regla 9.
- **Tasa de recuperación:** monto recuperado ÷ monto en cobranza de los mismos días.
- **Pagos por promesa:** pagos ÷ promesas del mismo periodo.
- **Pago por llamada:** monto recuperado ÷ llamadas salientes; solo cuenta el pago de los asesores en los días que hicieron llamadas.

**👥 Equipo y metas** (si el cliente las tiene; las metas nunca se asumen)
- **Cumplimiento de meta:** valor real ÷ meta (por asesor y día), con tope de 100 %. Por ejemplo, llamadas del día ÷ meta diaria de llamadas.
- **Faltantes:** por cada asesor y día, meta − real (cero si ya cumplió), sumados en el rango.
- **Día-asesor (jornada):** un asesor en un día con actividad.
- **Adherencia:** tiempo conectado dentro del turno ÷ duración del turno. **Entrada tarde:** jornada que empezó después de la tolerancia acordada (por ejemplo 15 min).
- **Gestiones por día activo:** gestiones ÷ días en que el asesor trabajó. **Hora de primera y última gestión:** promedio diario.

## Reglas por acordar (por escrito, antes de construir)
1. **Segmentos:** nombres, límites oficiales y si hay adicionales. Si distintas fuentes los escriben distinto, elegir uno.
2. **Filtros de cartera:** qué cuentas se excluyen (por estatus, producto o segmento).
3. **Cuenta gestionada:** qué canales cuentan como gestión (llamada, visita, WhatsApp, SMS, email) y si las llamadas automáticas cuentan.
4. **Contacto y promesa:** qué tipificaciones cuentan como contacto, contacto con titular, contacto clave y promesa. Vive en el catálogo.
5. **Contacto con titular total:** si suma llamadas salientes y entrantes.
6. **Promesa cumplida:** ventana de días para buscar el pago desde la promesa y si cuenta el pago parcial.
7. **Atribución de entrantes** a un envío previo (SMS, email…): regla y días de ventana.
8. **Días laborables** y festivos.
9. **Monto recuperado:** por fecha de pago o por fecha de aplicación.
10. **Fuente oficial de promesas:** tipificación de las gestiones o tabla de promesas, y qué canales cuentan.
11. **Metas:** si el cliente tiene metas (por asesor, por día o por segmento) y cuáles. No son estándar.

## Datos mínimos
| # | Tabla | Nivel de detalle | Campos mínimos |
|---|---|---|---|
| 1 | Cartera / asignación | Una foto por cuenta por día | Fecha de corte, contrato, estatus, días de mora, fecha de asignación, saldos (vencido y actual), campaña o canal, producto, segmento |
| 2 | Gestiones | Un registro por intento o acción | Contrato, fecha y hora, asesor, tipo de marcación o canal (preview, predictivo, entrante, WhatsApp…), resultado (tipificación), con quién hubo contacto, monto y fecha de promesa, segmento |
| 3 | Promesas | Una por promesa | Cuenta, fecha de captura, fecha compromiso, monto, asesor, campaña o canal |
| 4 | Pagos | Uno por pago | Folio, contrato, estatus, días de mora, canal, monto, fecha de pago, fecha de aplicación, tipo de pago, segmento |
| 5 | Entrantes | Una por llamada entrante | Contrato o teléfono, fecha y hora, atendida o abandonada, espera, asesor, resultado |
| 6 | Envíos masivos | Uno por envío | Contrato, fecha y hora, canal (SMS, email, mensaje de voz, WhatsApp, carta), estatus de entrega y respuestas |
| 7 | Visitas | Una por visita | Contrato, fecha, resultado y, si aplica, promesa |
| 8 | Plantilla y conexión | Por día y por asesor | Asesores disponibles, turno, conexión y monitoreos de calidad |
| 9 | Catálogos | Referencia | Asesores (login → nombre completo), segmentos y rangos, tipificaciones y su grupo (contacto, titular, promesa), canales, días hábiles y festivos y, si hay, metas |

No todas aplican a todos los proyectos: confirmar con el usuario cuáles tiene el cliente y pedir las que existan desde la primera carga.
