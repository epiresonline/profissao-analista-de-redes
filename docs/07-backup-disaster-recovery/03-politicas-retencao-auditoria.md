# Módulo 07 — Backup Estratégico, Nuvem & DRP
## 07.3 Políticas de Retenção & Auditoria Automatizada

De nada adianta ter scripts de backup configurados se ninguém verifica se eles estão realmente rodando. O "backup invisível" que falha silenciosamente durante semanas é o pesadelo de qualquer operação de TI.

### A Skill `backup-inspector`
Para garantir a integridade de todos os 25 clientes, a Pulse TI utiliza a skill e script automatizado `backup-inspector`:
- **Varredura Contínua:** Analisa diariamente a pasta `05 - BACKUP E SEGURANCA` de cada cliente no workspace.
- **Detecção de Defasagem:** Alerta se o dump mais recente tiver data anterior a 24 horas em bancos de missão crítica.
- **Verificação de Tamanho Mínimo:** Alerta se um arquivo de backup tiver tamanho suspeito (ex.: um banco de dados que sempre gera arquivos de 5 GB subitamente gera um arquivo de 10 KB devido a um erro de autenticação).
