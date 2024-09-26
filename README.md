# Arquitectura hexagonal mas CQRS con fastapi

> Este proyecto es un ejemplo de como se puede implementar una arquitectura hexagonal con CQRS en python utilizando FastAPI. Usamos MongoDB como base de dato para los **query** y Postgres para los **comandos**. Para sincronizar ambos sistemas de base de datos usamos las tareas asincronas de FastAPI.
En un entorno de producción sería recomendable usar un sistema de mensajería como RabbitMQ o AWS SQS para la sincronización.

## Requisitos

- Docker
- Docker-compose

## Ejecutar el proyecto

Cambiar la variable de entorno **ENV** en el archivo **.env** a:

- **ENV=development** para ejecutar en modo desarrollo
- **ENV=production** para ejecutar en modo producción

```bash
docker compose up --build
```
## ejecutar los test

Para este paso el proyecto debe estar corriendo y en modo **desarrollo**.

```bash
docker exec -it  code-challenge-app-1 pytest
```