# Módulo 06 — Bancos de Dados Corporativos & Missão Crítica
## 06.2 Oracle Database 19c & Philips TASY Hospitalar

Nos hospitais atendidos pela Pulse TI (como a Fundação Hospital Santa Otília `124 - HSO` e Hospital Santa Teresinha `092 - HST`), o ERP de gestão hospitalar é o **Philips TASY**, rodando sobre banco de dados **Oracle 19c Enterprise/Standard**.

### Particularidades Críticas do Oracle TASY
1. **Ambiente 24x7 Ininterrupto:** Um hospital não para. Não existe "janela de manutenção" de 4 horas durante o dia. Qualquer intervenção no banco deve ser previamente alinhada com o NOC e executada em horários de menor afluência.
2. **Modo ARCHIVELOG Obrigatório:** O banco de dados Oracle deve operar permanentemente em modo `ARCHIVELOG`. Isso permite a recuperação pontual no tempo (**Point-in-Time Recovery - PITR**) até o minuto anterior a qualquer falha.
3. **Backup via Oracle RMAN (Recovery Manager):**  
   Os backups de bancos de dados Oracle não utilizam ferramentas convencionais de arquivo, mas sim o **RMAN**, integrado aos Archive Logs diários.

### Estrutura Típica de Script RMAN
```sql
RUN {
    ALLOCATE CHANNEL ch1 DEVICE TYPE DISK;
    ALLOCATE CHANNEL ch2 DEVICE TYPE DISK;
    BACKUP AS COMPRESSED BACKUPSET DATABASE 
        FORMAT '/backup/oracle/tasy_%d_%T_%s_%p.bkp'
        PLUS ARCHIVELOG 
        FORMAT '/backup/oracle/arch_%d_%T_%s_%p.bkp'
        DELETE ALL INPUT;
    RELEASE CHANNEL ch1;
    RELEASE CHANNEL ch2;
}
```
