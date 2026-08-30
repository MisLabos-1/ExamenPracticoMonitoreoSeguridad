# Security Scanning

## Objetivo

Incorporar controles de seguridad dentro del pipeline CI/CD.

## Herramientas

### Gitleaks

Detecta posibles secretos en el código fuente.

Ejemplos:

- Passwords
- API Keys
- Tokens
- Credentials

### Trivy

Analiza vulnerabilidades en imágenes Docker.

## Flujo

Checkout
    |
    v
Gitleaks
    |
    v
Tests
    |
    v
Docker Build
    |
    v
Trivy
    |
    v
Deploy

## Política

El pipeline debe detenerse cuando se detecten:

- Secretos.
- Vulnerabilidades críticas.

## Reportes

Los reportes pueden almacenarse temporalmente en:

reports/