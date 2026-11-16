# Módulo 02 — Governança & Arquitetura de Workspace
## 02.1 A Taxonomia Padrão Ouro dos Clientes

Quando se administra um ambiente multi-tenant com dezenas de empresas, nomes vagos como "Cliente 1" ou "Empresa X" geram desastres operacionais. Na Pulse TI, implementamos a **Taxonomia Padrão Ouro de Três Blocos**:

```
<CODIGO> - <SIGLA> - <Nome Oficial da Empresa>
```

### Anatomia do Padrão

1. **`<CODIGO>` (3 dígitos numéricos):** Identificador exclusivo atribuído na entrada do cliente. Permite ordenação alfanumérica consistente em sistemas de arquivos, bancos de dados e ferramentas de automação (ex.: `002`, `062`, `112`, `124`).
2. **`<SIGLA>` (3 letras maiúsculas):** Mnemônico universal usado em prefixos de chamados, branches, tags de monitoramento, hostnames de ativos e eventos de agenda (ex.: `PTI`, `PRO`, `PRN`, `HSO`, `DOQ`).
3. **`<Nome Oficial>`:** Razão social ou nome fantasia consolidado da organização.

### Exemplos Reais Homologados

- `000 - EDU - Eduardo Pires` (Laboratório de testes e P&D)
- `002 - PTI - Pulse TI` (Matriz NOC Central Pulse TI)
- `062 - PRO - Prodatus Informática`
- `092 - HST - Hospital Santa Teresinha`
- `112 - PRN - PRN Diagnósticos`
- `120 - URG - Urgetrauma Ortopedia e Traumatologia`
- `123 - PLS - PLS Tecnologia` (Datacenter Cloud e VPSs)
- `124 - HSO - Fundação Hospital Santa Otilia`
- `133 - DOQ - Tortas Doquinha`

> [!IMPORTANT]
> A sigla de 3 letras é sagrada. Ela é a "chave estrangeira" humana e computacional que conecta o chamado no Hesk (`[PRN] Falha no link`), o evento no Google Calendar (`[PRN] Manutenção em Switch`), o hostname do servidor (`pls-prn-srv-app01`) e a pasta do cliente no Google Drive.
