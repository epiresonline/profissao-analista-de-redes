# Módulo 08 — Observabilidade & Monitoramento
## 08.1 Zabbix Enterprise: SNMP, Agentes & Triggers com Histerese

O **Zabbix Server** (`123 - PLS`) é a plataforma de monitoramento corporativo tradicional da Pulse TI, responsável por coletar dados de switches, roteadores MikroTik, interfaces WAN e servidores.

### Boas Práticas Homologadas em Zabbix
1. **SNMP v2c e v3 com Community Não-Padrão:** Nunca utilizar a community `public`. Em todos os equipamentos dos clientes, a community é alterada para um padrão alfanumérico seguro configurado exclusivamente no Zabbix Server.
2. **Uso de Zabbix Agent 2:** Nos servidores Linux e Windows, adotamos preferencialmente o **Zabbix Agent 2**, desenvolvido em Go, com suporte a plugins nativos e menor consumo de recursos.
3. **Triggers Inteligentes com Histerese:** Evitar triggers que disparam e resolvem a cada segundo gerando rajadas de notificações. Utilizar funções de média e histerese:
```ini
# Disparar alarme quando o uso de CPU ultrapassar 90% na média dos últimos 5 minutos:
min(/HOST-LINUX/system.cpu.util,5m) > 90

# Resolver o alarme apenas quando a CPU cair abaixo de 75%:
max(/HOST-LINUX/system.cpu.util,5m) < 75
```
