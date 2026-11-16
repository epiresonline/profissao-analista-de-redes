# Módulo 09 — Gestão de Operações, Helpdesk & Tempo
## 09.4 Elaboração de POPs e Runbooks N1/N2 à Prova de Falhas

Um **Procedimento Operacional Padrão (POP / Runbook)** é o documento que permite que um operador nível 1 ou estagiário execute uma tarefa complexa com o mesmo rigor e precisão de um Analista de Redes N3.

### O Padrão Ouro de Estrutura de POP Pulse TI

```markdown
# POP-[SIGLA]-[NUMERO] — [Nome Claro do Procedimento]

## 1. Metadados do Procedimento
| Campo | Detalhe |
| :--- | :--- |
| **Cliente / Projeto** | [CODIGO] - [SIGLA] - [Nome do Cliente] |
| **Elaborado por** | Eduardo Pires (Analista de Redes N3) |
| **Nível Operacional** | N1 / N2 / N3 |
| **Data de Homologação**| DD/MM/YYYY |
| **Objetivo** | Descrever em uma frase o que o POP resolve |

## 2. Pré-requisitos & Riscos
- Acessos necessários no KeePass.
- Nível de impacto (ex.: Causa indisponibilidade momentânea de rede?).

## 3. Passo a Passo Técnico de Execução
Comandos exatos em blocos de código com prints ou saídas esperadas.

## 4. Validação e Teste de Conformidade
Como o operador comprova que o procedimento funcionou com sucesso.

## 5. Procedimento de Rollback (Plano de Retorno)
Se algo der errado, como desfazer a alteração imediatamente.
```
