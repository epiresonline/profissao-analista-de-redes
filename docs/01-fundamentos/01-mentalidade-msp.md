# Módulo 01 — Fundamentos & Mentalidade MSP
## 01.1 Mentalidade MSP vs TI Tradicional

Trabalhar como **Engenheiro de Redes e Infraestrutura em um MSP (Managed Service Provider / MSSP)** é completamente diferente de atuar na TI interna de uma única empresa. 

### A Diferença Fundamental

| Característica | TI Interna Tradicional | Operação em MSP / MSSP (Pulse TI) |
| :--- | :--- | :--- |
| **Escopo** | 1 empresa, 1 cultura, 1 conjunto de ferramentas. | 25+ empresas simultâneas, realidades distintas. |
| **Heterogeneidade** | Padrão único de hardware e software. | MikroTik, SonicWall, Proxmox, VMware, Oracle, Postgres, Windows Server, Linux. |
| **Postura** | Muitas vezes reativa (esperar o chamado abrir). | Pró-ativa, orientada a observabilidade e auditoria constante. |
| **Documentação** | Frequentemente negligenciada ou informal. | Vital: Se não está documentado no padrão, não existe. |
| **Segurança** | Foco perimetral interno. | Zero-Trust estrito: isolamento total entre clientes. |
| **Precificação e Tempo** | Salário fixo sem apuração de rentabilidade de horas. | Horas técnicas faturáveis e governança em blocos de 30 min. |

### Princípios do Engenheiro MSP de Alto Nível
1. **Multi-Tenancy Mental:** Você deve ser capaz de mudar de contexto em segundos entre um hospital com Oracle TASY (`092 - HOS` ou `124 - SBO`) e uma indústria com Protheus (`133 - ALM`) sem misturar informações, senhas ou configurações.
2. **Padronização como Escudo:** Sem padrões rígidos de nomenclatura, pastas e procedimentos, gerenciar mais de 20 clientes torna-se caótico. O padrão não é burocracia: é a salvaguarda da sanidade técnica da equipe.
3. **Automação Preventiva:** Tarefas manuais repetidas mais de duas vezes devem ser automatizadas por scripts PowerShell, Bash, Python ou Skills de IA.
