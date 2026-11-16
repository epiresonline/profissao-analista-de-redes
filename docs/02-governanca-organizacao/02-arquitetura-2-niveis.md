# Módulo 02 — Governança & Arquitetura de Workspace
## 02.2 A Arquitetura Estrita em 2 Níveis (Zero Labirinto de Pastas)

Um dos erros mais comuns em operações de TI é a criação desordenada de sub-sub-subpastas (`Documentos/Antigos/Redes/2023/Testes/Novo/Nova Pasta (2)/config.txt`). Isso destrói a produtividade, quebra scripts de backup e cega agentes de inteligência artificial.

### A Regra Estrita de 2 Níveis

Na Pulse TI, vigora a regra inegociável de **estritamente 2 níveis**:

- **Nível 1:** A Pasta do Cliente (`<CODIGO> - <SIGLA> - <Nome>`)
- **Nível 2:** As 6 Categorias Padronizadas com arquivos diretos (sem subpastas internas):

```
g:\\Meu Drive\\2K26\\Clientes-Pulse-TI\\
└── 112 - PRN - PRN Diagnósticos/
    ├── 01 - DOCUMENTACAO/
    │   ├── 112 - PRN - DOCUMENTACAO_TECNICA.md
    │   ├── 112 - PRN - Topologia_Rede.drawio
    │   └── 112 - PRN - Inventario_Ativos.xlsx
    ├── 02 - PROCEDIMENTOS/
    │   ├── POP-PRN-001 — Reinicialização do Serviço PACS.md
    │   └── POP-PRN-002 — Troca de Switch de Borda.md
    ├── 03 - REDES E CONECTIVIDADE/
    │   ├── PRN-ROUTER-BORDA-2026-11-16.rsc
    │   ├── PRN-ROUTER-BORDA-2026-11-16.backup
    │   └── vpn_matriz_prn.ovpn
    ├── 04 - SISTEMAS E BANCOS/
    │   ├── docker-compose-pacs.yml
    │   └── backup_db_laudocontrol_schema.sql
    ├── 05 - BACKUP E SEGURANCA/
    │   ├── 112 - PRN - Politica de Backup e Seguranca.md
    │   └── rotina_backup_rclone_s3.ps1
    └── 06 - HISTORICO E RELATORIOS/
        ├── 112 - PRN - Historico e Relatorios.md
        └── Relatorio_Auditoria_Conformidade_2026.pdf
```

### Como Lidar com Arquivos Múltiplos ou Código-Fonte?
Se uma aplicação possuir centenas de arquivos (como um projeto Node.js, repositório de frontend ou biblioteca), **é proibido descompactá-los criando um Nível 3**. Eles devem ser armazenados compactados em arquivo `.zip` diretamente dentro da categoria correspondente (ex.: `04 - SISTEMAS E BANCOS/portal_laudos_v2.1.zip`).

Dessa forma, a árvore permanece limpa, auditável em 1 segundo e compatível com ferramentas automatizadas.
