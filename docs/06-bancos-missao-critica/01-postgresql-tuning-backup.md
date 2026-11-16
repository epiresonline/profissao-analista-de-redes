# Módulo 06 — Bancos de Dados Corporativos & Missão Crítica
## 06.1 PostgreSQL: Tuning, Manutenção & Backup `pg_dump`

O PostgreSQL é o motor de dados de clientes chave da Pulse TI, como a Nexus Software (`062 - SFT`), CIEM (`109 - POL`) e Bella Sabor Alimentos (`133 - ALM`).

### Parâmetros Críticos de Tuning (`postgresql.conf`)
Para servidores com 16 GB de RAM dedicados a banco:
- `shared_buffers = 4GB` (25% da memória física disponível).
- `effective_cache_size = 12GB` (75% da memória física disponível).
- `maintenance_work_mem = 1GB` (Acelera reindexação e rotinas de vacuum).
- `work_mem = 32MB` (Memória por operação de ordenação/sort).
- `checkpoint_completion_target = 0.9` (Suaviza I/O de escrita em disco).
- `wal_buffers = 16MB`.

### Rotina de Backup Homologada com `pg_dump` Custom Format (`-Fc`)
Nunca utilize dump em texto puro (`.sql`) para bancos em produção. O formato customizado (`-Fc` / Custom) é comprimido por padrão, permite restauração paralela multi-thread com `pg_restore -j 4` e possibilita selecionar tabelas isoladas na recuperação:

```bash
#!/bin/bash
# Script de Backup Oficial PostgreSQL Pulse TI
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
DB_NAME="db_producao"
BACKUP_DIR="/var/backups/postgres"
FILE_NAME="${BACKUP_DIR}/${DB_NAME}_${TIMESTAMP}.dump"

mkdir -p "$BACKUP_DIR"

# Executar pg_dump com formato customizado comprimido
pg_dump -U postgres -h 127.0.0.1 -p 5432 -Fc -b -v "$DB_NAME" > "$FILE_NAME"

# Reter apenas os últimos 7 dias localmente
find "$BACKUP_DIR" -type f -name "*.dump" -mtime +7 -delete
```
