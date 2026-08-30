# Plan de Pruebas

| ID | Prueba | Resultado esperado |
|---|---|---|
| T01 | Health Check | HTTP 200 |
| T02 | Balanceo | Respuestas APP1 y APP2 |
| T03 | Caída APP1 | APP2 continúa disponible |
| T04 | Prometheus | Detecta instancia caída |
| T05 | Grafana | Muestra estado |
| T06 | Logs | Eventos visibles en Kibana |
| T07 | Jenkins | Pipeline exitoso |
| T08 | Gitleaks | Detecta secretos |
| T09 | Trivy | Detecta vulnerabilidades |
| T10 | Recuperación | Contenedor reiniciado |