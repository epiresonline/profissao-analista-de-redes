# Módulo 05 — Infraestrutura, Hipervisores & Sistemas
## 05.4 Docker & Docker-Compose em Produção

O uso de contêineres Docker é padrão em nossas operações para hospedar serviços como Beszel Hub, Wiki.js, portais de laudos, pgAdmin e servidores web.

### Padrão Homologado de `docker-compose.yml`

Um arquivo `docker-compose.yml` de produção da Pulse TI deve seguir os seguintes critérios:
- Definição explícita de política de reinício (`restart: unless-stopped`).
- Mapeamento explícito de volumes persistentes (nunca deixar dados em camada efêmera).
- Associação a redes dedicadas (`networks:` bridge isoladas).
- Não expor portas de banco de dados diretamente no host quando o banco for consumido apenas por outro container da mesma stack.

```yaml
version: '3.8'

services:
  app-web:
    image: nginx:alpine
    container_name: pls-web-portal
    restart: unless-stopped
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html:ro
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    networks:
      - pulse-net

networks:
  pulse-net:
    driver: bridge
```
