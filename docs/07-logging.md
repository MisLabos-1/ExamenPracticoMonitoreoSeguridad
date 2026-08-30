# Logging

## Objetivo

Implementar centralización de logs mediante Filebeat,
Elasticsearch y Kibana.

## Arquitectura

Containers
    |
    v
Filebeat
    |
    v
Elasticsearch
    |
    v
Kibana

## Componentes

### Filebeat

Recolecta logs generados por los contenedores Docker.

### Elasticsearch

Almacena e indexa los eventos.

### Kibana

Permite realizar búsquedas y visualización de logs.

## Logs recolectados

- devsecops-app-01
- devsecops-app-02
- devsecops-nginx

## Docker Metadata

Filebeat agrega información del contenedor, permitiendo
filtrar eventos por nombre.

## Persistencia

Los datos se almacenan en:

elasticsearch-data