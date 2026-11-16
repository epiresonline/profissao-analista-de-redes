# Módulo 10 — Automação, IA Ops & O Livro Autoatualizável
## 10.2 Construção de Skills e Agentes Especialistas

No diretório `.agents/skills/`, mantemos um ecossistema de habilidades especializadas que expandem a inteligência artificial para interagir com o mundo físico da infraestrutura:

```mermaid
graph TD
    A["Agentes & Skills Pulse TI"] --> B["mikrotik-helper: Geração de scripts RouterOS v6/v7"]
    A --> C["beszel-manager: Provisionamento e métricas de servidores"]
    A --> D["hesk-ticket-logger: Gestão completa de chamados e API"]
    A --> E["daily-calendar-logger: Registro e cores no Google Calendar"]
    A --> F["backup-inspector: Auditoria de rotinas de dumps"]
    A --> G["pulse-client-auditor: Validação das 6 categorias estruturais"]
```

Cada skill possui sua instrução YAML de frontmatter, scripts em Python ou PowerShell e testes automatizados.
