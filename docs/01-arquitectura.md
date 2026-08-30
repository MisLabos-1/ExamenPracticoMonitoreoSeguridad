# Arquitectura

## Arquitectura general

Cliente
    |
    v
Nginx
    |
    +---- app1
    |
    +---- app2

Los componentes se ejecutan mediante Docker sobre Ubuntu 24.04
utilizando WSL2.

## Componentes

### Nginx

Actúa como:

- Reverse proxy.
- Punto de entrada.
- Balanceador de carga.

### app1

Primera instancia de la aplicación Flask.

### app2

Segunda instancia de la aplicación Flask.

## Red

Todos los servicios pertenecen a la red Docker:

devsecops-net

## Disponibilidad

La aplicación dispone de múltiples instancias.

Si una instancia falla, la otra puede continuar procesando solicitudes.

## Recuperación

Los contenedores utilizan:

restart: unless-stopped

La salud de las aplicaciones se verifica mediante el endpoint:

/health