# Módulo 03 — Segurança Zero-Trust & Gestão de Acessos
## 03.1 Política Estrita de Credenciais (Regra 11: Zero Senhas em Texto Puro)

A **Regra 11** da governança Pulse TI é a cláusula de proteção máxima do nosso ecossistema:

> **"É expressamente proibido registrar, exibir, versionar ou trafegar senhas, tokens de API, certificados privados ou chaves criptográficas em texto puro em qualquer documento markdown, script compartilhado, chamado ou chat."**

### Por Que Essa Regra Existe?
Em ambientes MSP, a documentação é consultada por múltiplos colaboradores, sincronizada com sistemas de controle de versão (Git) e wikis internas. Se uma credencial for commitada em texto puro:
1. O vazamento compromete permanentemente aquele cliente.
2. O histórico do Git retém a credencial mesmo que você a delete em commits subsequentes.
3. Viola-se a conformidade da LGPD (Lei Geral de Proteção de Dados) e normas ISO 27001.

### O Padrão Correto de Documentação
Em vez de colocar a senha no documento, o Analista de Redes documenta os **metadados de acesso** e a referência exata para o cofre seguro:

```markdown
<!-- FORMA INCORRETA (PROIBIDA) -->
Servidor: 192.168.1.100
Usuario: admin
Senha: SuperSenhaSecreta123!

<!-- FORMA CORRETA (HOMOLOGADA) -->
| Parâmetro | Detalhe da Conexão |
| :--- | :--- |
| **Host / IP** | `192.168.1.100` (ou DNS `pls-app01.netbird.selfhosted`) |
| **Protocolo / Porta** | SSH (Porta 22) |
| **Usuário** | `admin_pulse` |
| **Localização do Cofre** | KeePass: `Clientes/062 - SFT/Servidores/SFT-SRV-APP` |
| **Cofre Pulse Control** | Entry ID: `#348` |
```
