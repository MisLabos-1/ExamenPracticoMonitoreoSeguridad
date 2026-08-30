# Examen Practico Final

## Descripción

Plataforma DevSecOps implementada localmente utilizando
WSL2 y Docker.

## Arquitectura

Developer
    |
    v
Jenkins
    |
    +-- Gitleaks
    |
    +-- Tests
    |
    +-- Docker Build
    |
    +-- Trivy
    |
    v
Deployment
    |
    v
Nginx
    |
    +-- App 01
    |
    +-- App 02
    |
    +-- Prometheus
    |      |
    |      v
    |    Grafana
    |
    +-- Filebeat
           |
           v
      Elasticsearch
           |
           v
         Kibana

## Tecnologías

- WSL2
- Ubuntu
- Docker
- Docker Compose
- Python
- Flask
- Gunicorn
- Nginx
- Prometheus
- Grafana
- Elasticsearch
- Kibana
- Filebeat
- Jenkins
- Gitleaks
- Trivy
- Git

## Componentes

### Aplicación

Dos instancias Flask:

- APP1
- APP2

### Balanceador

Nginx distribuye las solicitudes.

### Monitoring

Prometheus recolecta métricas.

Grafana visualiza métricas.

### Logging

Filebeat recolecta logs.

Elasticsearch almacena eventos.

Kibana permite búsquedas.

### CI/CD

Jenkins automatiza:

- Tests
- Build
- Security Scan
- Deployment

### Seguridad

Gitleaks detecta secretos.

Trivy analiza vulnerabilidades.

## Ejecución

docker compose up -d

## Accesos

| Servicio | URL |
|---|---|
| Aplicación | http://localhost |
| Jenkins | http://localhost:8080 |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |
| Kibana | http://localhost:5601 |
| Elasticsearch | http://localhost:9200 |

# Despliegue rápido del proyecto

## Objetivo

Esta sección permite realizar una prueba rápida del despliegue completo del proyecto en una computadora local.

El objetivo es únicamente descargar el proyecto y levantar todos los servicios mediante Docker Compose.

---

# Requisitos previos

Antes de iniciar, se debe contar con:

- Git instalado.
- Docker Engine instalado.
- Docker Compose instalado.
- WSL2 + Ubuntu en caso de utilizar Windows.

Verificar las herramientas:

```bash
git --version
docker --version
docker compose version

---
# Despliegue del Proyecto

git clone https://github.com/MisLabos-1/ExamenPracticoMonitoreoSeguridad.git

cd REPOSITORIO

sudo sysctl -w vm.max_map_count=262144

docker compose up -d --build

docker compose ps