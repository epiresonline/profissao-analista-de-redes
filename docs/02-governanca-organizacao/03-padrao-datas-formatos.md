# Módulo 02 — Governança & Arquitetura de Workspace
## 02.3 Padrão Brasileiro de Datas e Metadados

Para garantir conformidade legal, auditoria e clareza para equipes técnicas brasileiras e clientes atendidos, a Pulse TI adota uma política estrita sobre representação de datas.

### A Diretriz Mandatória: `DD/MM/YYYY`

Em todo o corpo de textos legíveis por humanos, tabelas de controle, Procedimentos Operacionais Padrão, chamados de helpdesk e reuniões, **a data deve ser grafada compulsoriamente no formato brasileiro: `DD/MM/YYYY`** (ex.: `16/11/2026`).

### A Única Exceção Técnica: Arquivos de Máquina
Apenas em nomes de arquivos gerados por scripts onde a ordenação cronológica alfanumérica é indispensável para rotação automática, utiliza-se a norma ISO (`YYYY-MM-DD` ou `YYYYMMDD`):

```bash
# Nome do arquivo de dump (para ordenação de backup):
db_backup_prodatus_2026-11-16.dump

# Metadado no corpo do relatório técnico:
# "Backup executado com sucesso em 16/11/2026 às 03:00."
```

### Tabela Padronizada de Metadados de Documentos

Todo documento de engenharia deve iniciar com a tabela canônica:

```markdown
---
# METADADOS DE ENGENHARIA
| Campo | Especificação |
| :--- | :--- |
| **Cliente** | 062 - PRO - Prodatus Informática |
| **Responsável Técnico** | Eduardo Pires — Analista de Redes N3 |
| **Data de Homologação** | 16/11/2026 |
| **Classificação** | Confidencial / Uso Interno Pulse TI |
| **Versão** | 2.1 |
---
```
