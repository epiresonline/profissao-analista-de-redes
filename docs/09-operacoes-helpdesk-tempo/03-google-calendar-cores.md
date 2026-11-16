# Módulo 09 — Gestão de Operações, Helpdesk & Tempo
## 09.3 Classificação Visual por Cores no Google Calendar

O Google Calendar da engenharia de redes da Pulse TI não é apenas uma agenda pessoal: é um painel visual imediato do tipo de esforço técnico aplicado em cada cliente.

### A Tabela Oficial de Cores Homologada

| ID da Cor | Cor Visual | Categoria Técnica de Atuação | Exemplos de Atividades |
| :---: | :---: | :--- | :--- |
| **`colorId: 9`** | 🔵 **Azul** | **Redes e Conectividade** | MikroTik, VPNs, Switches, Firewalls, DNS, VLANs |
| **`colorId: 6`** | 🟠 **Laranja** | **Servidores & Datacenter / VMs** | Proxmox VE, VMware, Linux Server, Storage NAS |
| **`colorId: 10`** | 🟢 **Verde** | **Sistemas & Aplicações** | Docker, Hesk, Protheus, Optix PACS, Tomcat |
| **`colorId: 2`** | 🍏 **Verde Claro** | **Bancos de Dados** | PostgreSQL, Oracle 19c TASY, MySQL, pgAdmin |
| **`colorId: 3`** | 🟣 **Roxo** | **Backup, Segurança & KeePass** | Rclone, Políticas DRP, Cofre de Senhas, Auditorias |
| **`colorId: 7`** | 🩵 **Turquesa** | **Documentação Técnica & POPs** | Elaboração de Runbooks, Auditoria de Workspace |
| **`colorId: 4`** | 🌸 **Rosa** | **Reuniões & Alinhamentos** | Alinhamentos semanais, reuniões executivas de NOC |
| **`colorId: 11`** | 🔴 **Vermelho** | **Incidentes Críticos & Emergências** | Paradas de produção, quedas totais, resposta a crises |

### Disparo Obrigatório para `redes@pulseti.com`
Todo evento criado via CLI ou API deve conter compulsoriamente o parâmetro:
```bash
--attendee "redes@pulseti.com" --send-updates all
```
Garantindo que a equipe de engenharia e os plantonistas recebam o aviso do agendamento em tempo real.
