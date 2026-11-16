# Módulo 08 — Observabilidade & Monitoramento
## 08.4 Matriz de Severidade & Prevenção de Fadiga de Alertas

A "fadiga de alertas" (**Alert Fatigue**) é uma das doenças operacionais mais perigosas da TI. Se os técnicos recebem 500 mensagens de alerta por dia no WhatsApp ou Telegram, eles passam a ignorar todas as notificações. Quando um servidor de missão crítica realmente cai, ninguém reage.

### A Matriz de Severidade Pulse TI

| Nível de Severidade | Impacto Técnico | Canal de Notificação | Ação Requerida |
| :--- | :--- | :--- | :--- |
| **Info / Aviso** | Evento sem impacto operacional imediato (ex.: novo usuário logado). | Apenas log e dashboard. | Nenhuma ação imediata. |
| **Média** | Degradação não-crítica (ex.: uso de disco em 80%, link secundário caiu). | Canal de monitoramento silencioso. | Tratamento em horário comercial. |
| **Alta** | Risco iminente de parada (ex.: CPU em 95% há 30 min, banco com conexões esgotando). | Alerta no grupo de engenharia. | Resolução prioritária pelo N2/N3. |
| **Desastre / Crítica** | Queda total de serviço essencial (ex.: hospital sem sistema TASY, roteador de borda inalcançável). | Notificação push sonora + acionamento do plantão N3. | Ação imediata em regime de emergência. |
