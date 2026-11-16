# Módulo 08 — Observabilidade & Monitoramento
## 08.2 Beszel Hub: O Monitoramento Ultraleve para MSPs

Enquanto o Zabbix é robusto e complexo, o **Beszel Hub** (`https://bz.pulseti.cloud-ip.cc`) é a solução moderna, ágil e ultraleve adotada pela Pulse TI para monitorar servidores, VMs e containers Docker em tempo real.

### Por Que Adotamos o Beszel?
- **Agente Binário Mínimo:** Consumo de CPU inferior a 0.5% e menos de 20 MB de RAM.
- **Docker First:** Detecta automaticamente todos os contêineres Docker em execução na máquina, monitorando consumo de CPU e memória individual sem qualquer configuração manual.
- **Métricas Essenciais Instantâneas:** CPU, RAM, uso de discos, I/O de armazenamento, largura de banda de rede e temperatura.
- **API REST Integrada:** Permite o provisionamento e cadastro automatizado de novos servidores através de scripts e skills (`beszel-manager`).
