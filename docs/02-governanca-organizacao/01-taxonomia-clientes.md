# Módulo 02 — Governança & Arquitetura de Workspace
## 02.1 A Taxonomia Padrão Ouro dos Clientes

Quando se administra um ambiente multi-tenant com dezenas de empresas, nomes vagos como "Cliente 1" ou "Empresa X" geram desastres operacionais. Na Pulse TI, implementamos a **Taxonomia Padrão Ouro de Três Blocos**:

```
<CODIGO> - <SIGLA> - <Nome Oficial da Empresa>
```

### Anatomia do Padrão

1. **`<CODIGO>` (3 dígitos numéricos):** Identificador exclusivo atribuído na entrada do cliente. Permite ordenação alfanumérica consistente em sistemas de arquivos, bancos de dados e ferramentas de automação (ex.: `002`, `062`, `112`, `124`).
2. **`<SIGLA>` (3 letras maiúsculas):** Mnemônico universal usado em prefixos de chamados, branches, tags de monitoramento, hostnames de ativos e eventos de agenda (ex.: `PTI`, `SFT`, `DIA`, `SBO`, `ALM`).
3. **`<Nome Oficial>`:** Razão social ou nome fantasia consolidado da organização.

### Exemplos Reais Homologados

- `000 - EDU - Eduardo Pires` (Laboratório de testes e P&D)
- `002 - PTI - Pulse TI` (Matriz NOC Central Pulse TI)
- `062 - SFT - Nexus Software & Soluções`
- `092 - HOS - Hospital Geral Esperança`
- `112 - DIA - DiagCenter Medicina Diagnóstica`
- `120 - TRA - Centro de Traumatologia Integrada`
- `123 - CLD - Cloud Datacenter & VPS` (Datacenter Cloud e VPSs)
- `124 - SBO - Hospital Regional São Bento`
- `133 - ALM - Alimentos Bella Sabor`

> [!IMPORTANT]
> A sigla de 3 letras é sagrada. Ela é a "chave estrangeira" humana e computacional que conecta o chamado no Hesk (`[DIA] Falha no link`), o evento no Google Calendar (`[DIA] Manutenção em Switch`), o hostname do servidor (`cld-dia-srv-app01`) e a pasta do cliente no Google Drive.
