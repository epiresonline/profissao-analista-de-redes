# Módulo 06 — Bancos de Dados Corporativos & Missão Crítica
## 06.3 MySQL & MariaDB de Alta Confiabilidade

Em portais web, servidores corporativos e no próprio webserver legado da Pulse TI (`123 - PLS`), bases MySQL e MariaDB exigem parâmetros adequados para evitar travamentos de tabelas (**table locks**) durante backups.

### A Flag Mandatória: `--single-transaction`

Ao executar `mysqldump` em tabelas do motor **InnoDB**, a flag `--single-transaction` é indispensável:

```bash
mysqldump -u root -p \
    --single-transaction \
    --quick \
    --routines \
    --triggers \
    --events \
    --databases bz_db hesk_db > /backup/mysql/pulse_dbs_$(date +%F).sql
```

### Por Que Usar Essas Flags?
- `--single-transaction`: Cria um snapshot consistente em nível de transação sem travar as tabelas para leitura ou escrita. O usuário final continua utilizando o sistema sem notar lentidão.
- `--quick`: Força o dump a ler linha por linha do servidor, evitando descarregar tabelas gigantescas na memória RAM antes de escrever no disco.
- `--routines --triggers --events`: Garante que stored procedures, triggers e agendamentos internos do MySQL sejam salvaguardados.
