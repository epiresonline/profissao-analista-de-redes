# Módulo 05 — Infraestrutura, Hipervisores & Sistemas
## 05.2 Linux Server Hardening de Produção (Debian / Ubuntu / Rocky)

Servidores Linux expostos em nuvem ou em DMZs internas devem operar sob rigoroso processo de endurecimento (**hardening**).

### Checklist de Hardening Obrigatório

1. **Desativação de Login Root por Senha:**
```bash
# Em /etc/ssh/sshd_config:
PermitRootLogin prohibit-password
PasswordAuthentication no
PubkeyAuthentication yes
```
2. **Alteração da Porta SSH Padrão:**
Utilizar portas altas (ex.: `22022`) para eliminar 99% do ruído de bots de varredura.
3. **Instalação e Ajuste do Fail2ban:**
Protege contra ataques de força bruta no SSH e serviços web:
```ini
# /etc/fail2ban/jail.local
[sshd]
enabled = true
port = 22022
maxretry = 3
bantime = 86400
findtime = 600
```
4. **Firewall UFW ou Iptables Restritivo:**
Bloquear tudo por padrão e liberar apenas as portas necessárias:
```bash
ufw default deny incoming
ufw default allow outgoing
ufw allow 22022/tcp comment 'SSH Administrativo'
ufw enable
```
5. **Configuração de NTP e Fuso Horário:**
Garantir sincronismo absoluto com `pool.ntp.br` e timezone `America/Sao_Paulo`.
