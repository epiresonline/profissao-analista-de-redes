# Módulo 08 — Observabilidade & Monitoramento
## 08.3 Grafana: Dashboards & Métricas Operacionais

O **Grafana** atua como a interface visual e analítica da nossa infraestrutura, consolidando métricas provenientes do Zabbix, bancos de dados e fontes de séries temporais.

### Tipos de Dashboards Utilizados
1. **NOC Central Pulse TI (Visão Global):** Telão de monitoramento que exibe em tempo real o status dos 25 clientes, indicando perdas de conectividade, links caídos e latência de rotas principais.
2. **Dashboard de Capacidade (Capacity Planning):** Indicadores de tendência de crescimento de disco e consumo de RAM, permitindo alertar o cliente com antecedência antes que o storage fique sem espaço.
3. **Dashboard Executivo para Clientes:** Relatórios visuais limpos apresentados em reuniões de prestação de contas, demonstrando a estabilidade da infraestrutura e cumprimento de SLAs.
