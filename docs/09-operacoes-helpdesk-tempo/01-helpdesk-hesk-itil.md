# Módulo 09 — Gestão de Operações, Helpdesk & Tempo
## 09.1 Gestão de Chamados no Hesk Helpdesk e APIs de Automação

A central oficial de chamados e suporte da Pulse TI opera no **Hesk Helpdesk** (`https://help.pulseti.com`), sob governança da Matriz Pulse TI (`002 - PTI - Pulse TI`).

### A Diretriz da Primeira Resposta Técnica Imediata
Devido à integração de qualidade e SLAs contratados com nossos clientes:
> **Todo chamado aberto no Hesk DEVE conter obrigatoriamente uma primeira resposta técnica imediata informando o escopo inicial da intervenção.**

### Automação via Skill `hesk-ticket-logger`
Sempre que o engenheiro inicia uma intervenção técnica relatada no chat ou console, o assistente executa o script oficial:

```powershell
python ".agents/skills/hesk-ticket-logger/scripts/create_ticket.py" `
    --client "DIA" `
    --title "Manutenção Preventiva em Switch de Borda" `
    --body "Iniciando verificação de firmware e redundância de portas." `
    --calendar
```

O script:
1. Registra o chamado via API REST no Hesk.
2. Adiciona automaticamente a primeira nota técnica de acolhimento.
3. Gera o evento correspondente na agenda do Google Calendar vinculado ao link público de rastreio (`https://help.pulseti.com/ticket.php?track={TRACKID}`).
