# Módulo 04 — Engenharia Avançada MikroTik RouterOS
## 04.1 Hardening Homologado MikroTik RouterOS (v6 & v7)

O MikroTik RouterOS é a espinha dorsal de conectividade dos clientes da Pulse TI. No entanto, sua configuração padrão de fábrica expõe serviços vulneráveis que devem ser imediatamente desativados em produção.

### Script de Hardening Homologado Pulse TI

Ao provisionar qualquer roteador RouterOS, o Analista N3 executa o seguinte script:

```routeros
# ========================================================
# PULSE TI - HARDENING HOMOLOGADO DE ROUTEROS (v6 / v7)
# Autor: Eduardo Pires (Analista de Redes N3)
# ========================================================

/ip service
set telnet disabled=yes
set ftp disabled=yes
set www disabled=yes
set api disabled=yes
set api-ssl disabled=yes

# Alterar porta e restringir SSH
set ssh port=22022 disabled=no

# Proteger Winbox com porta customizada e address-list
set winbox port=8205 address=100.64.0.0/10,192.168.0.0/16 disabled=no

# Desativar descoberta de vizinhança na interface WAN
/ip neighbor discovery-settings
set discover-interface-list=LAN

# Desativar serviços de largura de banda e teste públicos
/tool bandwidth-server set enabled=no

# Desativar proxy e socks
/ip proxy set enabled=no
/ip socks set enabled=no

# Desativar UPnP
/ip upnp set enabled=no
```

> [!CAUTION]
> Nunca deixe a porta padrão `8291` do Winbox aberta para o mundo (`0.0.0.0/0`). Ela é alvo de ataques de força bruta automatizados 24 horas por dia.
