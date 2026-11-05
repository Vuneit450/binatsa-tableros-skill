# Plantilla BINATSA · ATC (versión 0.1.3; probada en Tableau)

Hecha a partir de la plantilla de Cobranza (mismo diseño, acciones y nombres internos de cálculos) con `herramientas/crear_plantilla_atc.py`. Datos inventados de llamadas entrantes.

## Qué trae
- Vistas: Dirección, Operación, Asesores y Guía y glosario, en 2300 x 1300.
- Datos inventados (`Data/datos/`): resumen diario por asesor (15 asesores ficticios, 3 canales, 120 días) y detalle de llamadas entrantes (30 días, con tipificación).

## Tarjetas
- **Dirección:** Recibidas, Atendidas, Nivel de servicio, % Abandono > 5 s, ASA y TMO.
- **Operación:** Recibidas, Abandonadas, Nivel de atención, Atendidas por asesor, Personas conectadas y Demoradas > 20 s.
- **Asesores:** % Tipificación, Horas disponibles, Horas en auxiliares, Atendidas por hora y Horas conectado.
- Metas estándar de ATC (`referencias/giros/atc.md`): NS 90 %, abandono 5 %, ASA 20 s, TMO 10 min. Abandono, ASA, TMO, demoradas y auxiliares invierten el color (bajar es mejorar).

## Selectores
- Mapa de calor de Dirección (canal × día): Recibidas, Atendidas, Abandonadas, Nivel de servicio, Nivel de atención, % Abandono > 5 s, ASA, TMO y Demoradas; por defecto, Nivel de servicio.
- Mapa de Operación (hora × día): Recibidas, Atendidas, Abandonadas, % atención y % abandono.
- Mapa de Asesores: Atendidas, Nivel de servicio, TMO, % Tipificación, Atendidas por hora y horas.

## Marcadores
Los mismos de la plantilla de Cobranza (`{Campaña}`, `{Cliente}`, canales, logo, colores, `https://URL-DEL-VIDEO`, `{Fuente 1}`…), más `{reporte de llamadas entrantes}` en el pie de Dirección.

## Pendiente
1. Abrirla en Tableau y corregir lo que falle.
2. Vistas propias del giro: Nivel de servicio (detalle) y Encuestas.
3. La fuente de resumen conserva columnas de cobranza en cero (para no romper cálculos que no se usan); limpiarlas cuando la plantilla esté validada.
