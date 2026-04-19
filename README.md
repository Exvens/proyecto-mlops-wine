# proyecto-mlops-wine ## Fase 5: Monitoreo y Observabilidad (Diseño Propuesto)

Para asegurar que el modelo mantenga su rendimiento en producción, se propone la siguiente arquitectura de monitoreo:

1. **Monitoreo de Infraestructura (FastAPI):**
   * Herramienta: Prometheus + Grafana.
   * Métricas: Latencia de la API (tiempo de respuesta), tasa de errores HTTP (ej. 500s, 400s) y uso de CPU/RAM del contenedor.

2. **Monitoreo del Modelo (Data & Concept Drift):**
   * Herramienta: Evidently AI o Datadog.
   * Métricas: 
     * **Data Drift:** Monitorear si cambian las distribuciones químicas del vino (ej. si de repente todos los vinos entrantes tienen niveles de alcohol muy altos comparados con el set de entrenamiento).
     * **Concept Drift:** Comparar las predicciones de calidad contra los resultados reales de catas humanas (cuando estén disponibles) para medir si el MSE de 0.30 se degrada con el tiempo.