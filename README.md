# Análisis de Desempeño Logístico y Ventas (Python + Power BI)

![Dashboard Preview](dashboard_final.png)

## 📋 Resumen del Proyecto
Desarrollo de un pipeline de datos para procesar 10,000 registros de ventas, calculando el **Lead Time** (tiempo de entrega) y detectando cuellos de botella mediante análisis de dispersión.

---

## 🚀 Proceso Técnico

### 1. ETL con Python
Se utilizó la librería **Pandas** para:
* Convertir tipos de datos (Strings a Datetime).
* Calcular la diferencia de días entre compra y entrega.
* Exportar el dataset limpio con delimitadores regionales (`;`) para compatibilidad.

### 2. Dashboard en Power BI
* **KPI Card:** Visualización del promedio de días de entrega.
* **Análisis de Dispersión:** Correlación entre cantidad pedida y retraso operativo.
* **Semaforización:** Reglas de color para identificar sucursales con entrega mayor a 45 días.

---

## 📈 Resultados
* **Identificación de Nodos Críticos:** Se detectaron sucursales con alta demanda pero baja eficiencia logística.
* **Optimización de Reportes:** Reducción del tiempo de procesamiento manual de datos mediante automatización con script.
