# Módulo 10 — Automação, IA Ops & O Livro Autoatualizável
## 10.4 A Engenharia por Trás Deste Livro Vivo

Este livro não é um arquivo PDF estático que envelhece na prateleira digital. Ele é um **Livro Vivo e Autoatualizável** conectado diretamente à evolução contínua da engenharia da Pulse TI.

### A Mecânica da Autoatualização
1. **Auditoria Automatizada Local (`scripts/update_book.py`):**
   - Inspeciona o estado da infraestrutura e dos clientes.
   - Atualiza a contagem de ativos, capítulos e conformidades.
   - Alimenta automaticamente o [Histórico & Changelog](../changelog.md) com a data brasileira atual (`DD/MM/YYYY`).
2. **Esteira de Integração Contínua (GitHub Actions):**
   - Ao receber o commit e push na branch `main`, a action `.github/workflows/gh-pages.yml` compila o site MkDocs Material.
   - O livro é publicado automaticamente na web no endereço:  
     `https://epiresonline.github.io/profissao-analista-de-redes/`
3. **Execução em Um Clique:**
   O Analista de Redes N3 pode acionar o script `update_book.bat` a qualquer momento para consolidar e publicar novas descobertas e POPs criados no dia a dia.
