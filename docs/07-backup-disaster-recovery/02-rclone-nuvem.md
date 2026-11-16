# Módulo 07 — Backup Estratégico, Nuvem & DRP
## 07.2 Automação Multi-Nuvem com Rclone (Google Drive, AWS S3, Wasabi)

O **Rclone** é a ferramenta oficial homologada pela Pulse TI para sincronização, espelhamento e expurgo de arquivos de backup entre servidores locais e provedores de nuvem.

### Comando Homologado de Sincronização Segura
```bash
rclone sync /var/backups/postgres gdrive-pulse:Clientes/062-PRO/Backups \
    --log-file=/var/log/rclone_backup.log \
    --log-level=INFO \
    --transfers=4 \
    --checkers=8 \
    --contimeout=60s \
    --timeout=300s \
    --retries=3 \
    --stats=1m
```

### Regras Críticas no Uso do Rclone
1. **Diferença entre `copy` e `sync`:**
   - `rclone copy`: Apenas copia novos arquivos e atualizações. Nunca deleta nada no destino.
   - `rclone sync`: Torna o destino **idêntico** à origem. Se um arquivo for deletado localmente, ele será apagado na nuvem. **Use `sync` apenas em pastas de rotação diária que já possuem expurgo local configurado.**
2. **Criptografia Rclone (Crypt Remote):** Para clientes de medicina diagnóstica ou dados bancários, utiliza-se a camada `rclone crypt` para criptografar os dados em trânsito e em repouso na nuvem com chaves mantidas exclusivamente no cofre KeePass da Pulse TI.
