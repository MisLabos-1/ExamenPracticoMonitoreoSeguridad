# CI/CD con Jenkins

## Objetivo

Automatizar el proceso de integración y despliegue.

## Pipeline

El pipeline ejecuta:

1. Checkout
2. Tests
3. Docker Build
4. Deploy
5. Verification

## Jenkins

Jenkins se ejecuta como contenedor Docker.

## Docker

Jenkins tiene acceso al Docker Engine mediante:

/var/run/docker.sock

## Persistencia

Los datos de Jenkins se almacenan en:

jenkins-data