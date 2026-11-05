# Giro ATC (atención a clientes, llamadas entrantes)

Métricas, reglas de cálculo y vistas propias de las campañas de ATC. El diseño, las tarjetas, los tooltips y la interactividad son los generales (`referencias/diseno.md`, `referencias/tooltips.md`). Definiciones estándar: confirmarlas con el cliente al inicio y registrar en `brief.md` las que difieran.

## Categorías del giro
- **Control de arriba:** Campaña (lista con "Todas" por defecto), solo si el libro tiene más de una campaña o subcampaña.
- **Resaltar al pasar el mouse:** una sola acción por vista con todos los campos en común; para que se iluminen juntos, usar el mismo nombre de campo en todas las hojas (por ejemplo Asesor, Canal).
- **Franja:** bloque de 30 minutos, en la zona horaria acordada con el cliente.

## Tarjetas
- **Fila principal:** Recibidas, Atendidas, Nivel de servicio, % Abandono > 5 s, ASA y TMO.
- **Fila de apoyo (opcional):** Promedio diario de recibidas, Nivel de atención, Demoradas > 20 s, Espera máxima, Personas conectadas y Atendidas por persona.
- **Bajar es mejorar** en abandono, ASA, TMO, demoradas y espera: el color del delta se invierte.
- **Deltas en puntos porcentuales (pp)** para Nivel de servicio, Nivel de atención y abandono; en % para los demás.

## Mapa de calor de Dirección
- **Filas:** franja. **Columnas:** días del rango.
- **Opciones del selector KPI:** Recibidas, Atendidas, Abandonadas, Nivel de servicio, Nivel de atención, % Abandono > 5 s, ASA, TMO, Demoradas y Personas conectadas.
- **Por defecto:** Nivel de servicio.

## Operación en ATC
Son las cinco hojas obligatorias de `referencias/diseno.md`, adaptadas a llamadas entrantes:
1. **🕒 ¿A qué hora entra más y cuándo nos falta gente?** Mapa de calor franja contra día, con selector (recibidas, NS, abandono, ASA, TMO, personas conectadas).
2. **🏆 ¿Quién produce y quién necesita apoyo?** Tabla por asesor: atendidas, TMO, % tipificación, tiempo disponible, auxiliares y asistencia, con total general.
3. **📞 ¿Por qué llaman?** Barras por tipificación, de mayor a menor, apiladas por campaña si hay más de una.
4. **👥 ¿Quién atiende más?** Barras por asesor con sus llamadas atendidas.
5. **📈 ¿Cuánto entra cada día?** Mapa de calor campaña (o tipificación) contra día, con selector (recibidas, atendidas, abandonadas, NS).

## Vistas propias del giro (según los datos)
- **🔎 Nivel de servicio (detalle):** NS por mes, por franja promedio, por intervalo y por tipificación.
- **⭐ Encuestas:** solo si la campaña tiene encuestas. Tarjetas de enviadas, completas, % respuesta, NPS, % promotores, % detractores y las preguntas propias del cliente (por ejemplo resolución, espera, conocimiento del asesor), más la distribución de NPS, NPS por tipificación y la tendencia diaria.

## Glosario (definiciones estándar)

**📞 Llamadas**
- **Recibidas:** llamadas únicas (identificador de llamada + hora de inicio) que entraron = atendidas + abandonadas. No cuentan ocupado, transferencia de salida, falla de red ni desconexión del sistema.
- **Atendidas:** contestadas por un asesor (terminada por el asesor o el cliente, conferencia o transferida).
- **Abandonadas:** el cliente colgó antes de ser atendido (en cola, timbrando o sin respuesta).
- **Demoradas:** atendidas con espera mayor a 20 s. Espera = tiempo en cola + pendiente.
- **Intentos y efectivas (salientes, si las hay):** intentos = llamadas salientes únicas; efectivas = salientes de 35 s o más; % efectivas = efectivas ÷ intentos.

**✅ Indicadores de servicio**
- **Nivel de servicio (NS):** 1 − demoradas ÷ atendidas. Meta estándar BINATSA: 90 % (verde ≥ 90 %, rojo < 90 %).
- **Nivel de atención:** atendidas ÷ recibidas.
- **% Abandono > 5 s:** abandonadas con espera mayor a 5 s ÷ recibidas. Meta estándar BINATSA: 5 % (verde ≤ 5 %, rojo > 5 %).
- **Abandono rápido ("ghost"):** abandonadas con espera menor a 6 s; se reporta aparte porque no refleja falta de atención.
- **ASA:** espera promedio antes de ser atendido = (cola + pendiente) ÷ atendidas. Meta estándar BINATSA: 20 s (verde ≤ 20 s, rojo > 20 s).
- **TMO (AHT):** tiempo promedio por llamada atendida = (pendiente + conversación + espera + post-llamada) ÷ atendidas. Meta estándar BINATSA: 10 min (verde ≤ 10 min, rojo > 10 min).
- **Tipificación:** motivo con que el asesor cerró la llamada atendida. % tipificación = tipificadas ÷ atendidas.

**⭐ Encuestas** (si aplica)
- **NPS:** % promotores − % detractores, sobre encuestas completas.
- **Escala:** la define cada cliente. Por ejemplo, en 0–10: promotor 8–10, pasivo 6–7, detractor 0–5. Registrarla en `brief.md`.
- **CSAT y CES:** respuestas favorables (por ejemplo 4–5 en escala de 1–5) ÷ respuestas.
- **FCR:** clientes que dicen que se resolvió en la primera llamada ÷ respuestas.
- **% Respuesta:** encuestas completas ÷ encuestas enviadas.

**🔁 Retención:** si la campaña atiende cancelaciones, sus métricas están en `referencias/giros/retenciones.md`.

**👥 Plantilla**
- **HC:** plantilla de la campaña; la asistencia solo incluye a esos asesores.
- **Asistencia:** A = el asesor tuvo actividad ese día; F = sin actividad.
- **Auxiliares:** tiempo en estados no disponibles (baño, comida, etc.).
- **Disponible:** tiempo listo para recibir llamadas.
- **Personas conectadas:** asesores distintos con actividad o llamada atendida en el periodo o franja.

## Reglas por acordar (por escrito, antes de construir)
1. Umbral del nivel de servicio (estándar: 20 s). Las metas estándar (NS 90 %, abandono 5 %, ASA 20 s, TMO 10 min; semáforo de dos colores: verde cumple, rojo no cumple) solo cambian si el cliente pide otras; registrarlas en `brief.md`.
2. Umbral de abandono (estándar: 5 s) y si el abandono rápido se excluye.
3. Qué cuenta como recibida: llave única de la llamada y qué estados se excluyen.
4. Qué componentes suman al TMO.
5. Zona horaria de las franjas.
6. Escala de la encuesta y qué respuestas cuentan como promotor, pasivo y detractor.
7. Si hay varias campañas: cuáles suman al total.
8. Catálogo de tipificaciones y sus grupos.

## Datos mínimos
- **Llamadas entrantes,** una por llamada: identificador, campaña, fecha y hora de inicio, tiempos (cola, pendiente, timbrado, conversación, espera, post-llamada), resultado, asesor y tipificación.
- **Actividad de asesores:** estado, inicio y fin (disponible y auxiliares).
- **Plantilla (HC)** por campaña.
- **Encuestas,** si hay: llamada o asesor, fecha y respuestas.
- **Catálogos:** asesores (login → nombre completo), tipificaciones y sus grupos, y campañas.
