# Monitoring

## Objetivo

Implementar monitoreo de la plataforma mediante Prometheus y Grafana.

## Componentes

- Prometheus
- Grafana
- Flask Prometheus Exporter

## Métricas

Las aplicaciones exponen métricas mediante:

/metrics

Prometheus consulta las aplicaciones cada 15 segundos.

## Targets

- app1:5000
- app2:5000

## Visualización

Grafana utiliza Prometheus como fuente de datos.

## Dashboard

El dashboard permite visualizar:

- Estado de las aplicaciones.
- Solicitudes HTTP.
- Solicitudes por segundo.
- Disponibilidad de instancias.

## Persistencia

Se utilizan volúmenes Docker:

- prometheus-data
- grafana-data