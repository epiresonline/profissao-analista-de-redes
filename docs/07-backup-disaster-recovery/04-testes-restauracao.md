# Módulo 07 — Backup Estratégico, Nuvem & DRP
## 07.4 O Teste Mandatório de Restauração & DRP (Disaster Recovery Plan)

> **"A única certeza de que você possui um backup é o teste bem-sucedido de restauração."**

### O Plano de Recuperação de Desastres (DRP)
O DRP define o passo a passo exato a ser executado quando um servidor queima, um storage é corrompido ou uma unidade sofre um ataque cibernético.

### Indicadores Obrigatórios de DRP
- **RPO (Recovery Point Objective):** Quanto tempo de perda de dados a empresa tolera. Na Pulse TI, o RPO padrão para bancos hospitalares e ERPs é de no máximo **1 hora** (via archive logs) e para sistemas administrativos de **24 horas**.
- **RTO (Recovery Time Objective):** Quanto tempo o time de engenharia leva para colocar o ambiente em operação novamente após o desastre. Nosso RTO alvo para serviços críticos é de **2 a 4 horas**.

### Homologação Periódica de Restauração
A cada trimestre, o Analista de Redes N3 realiza a restauração do dump de um cliente em um ambiente de testes isolado (Sandbox no Proxmox ou VirtualBox em `000 - EDU`), validando:
1. Se o banco sobe sem erros de integridade relacional.
2. Se a aplicação consegue autenticar e ler os últimos registros cadastrados.
3. Se os índices e triggers estão íntegros.
