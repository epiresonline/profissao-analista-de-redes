# Módulo 04 — Engenharia Avançada MikroTik RouterOS
## 04.2 Firewall Filter, NAT e Proteções de Produção

Um firewall de borda profissional deve aplicar filtragem em estado de conexão (**stateful inspection**), proteção contra scanners e prevenção de ataques DoS/Brute Force.

### Estrutura do Firewall Filter

```routeros
# ========================================================
# TABELA DE FILTER RULES (ORDEM DE PROCESSAMENTO CRÍTICA)
# ========================================================

/ip firewall filter

# 1. Aceitar conexões já estabelecidas e relacionadas
add chain=input action=accept connection-state=established,related,untracked comment="Aceitar Estabelecidas/Relacionadas"
add chain=forward action=accept connection-state=established,related,untracked comment="Aceitar Estabelecidas/Relacionadas"

# 2. Descartar pacotes inválidos
add chain=input action=drop connection-state=invalid comment="Dropar Invalidos"
add chain=forward action=drop connection-state=invalid comment="Dropar Invalidos"

# 3. Proteção contra Port Scan (adiciona IP atacante a blacklist temporária)
add chain=input action=add-src-to-address-list address-list="PORT-SCAN-BLOCK" address-list-timeout=1d \\
    protocol=tcp psd=21,3s,3,1 comment="Detectar Port Scanner"
add chain=input action=drop src-address-list="PORT-SCAN-BLOCK" comment="Bloquear Port Scanners"

# 4. Permitir ICMP (Ping) controlado da LAN e VPNs
add chain=input action=accept protocol=icmp in-interface-list=LAN comment="Aceitar ICMP da LAN"

# 5. Dropar todo o restante direcionado ao próprio roteador vindo da WAN
add chain=input action=drop in-interface-list=WAN comment="DROP Input WAN Restante"

# 6. Regra de FastTrack consciente (Forward)
add chain=forward action=fasttrack-connection connection-state=established,related comment="FastTrack Estabelecidas"
```

> [!WARNING]
> **Atenção ao FastTrack com Queues/IPsec:** Se você utiliza Queue Trees complexas ou túneis IPsec pesados, o FastTrack pode ignorar o processamento das filas de QoS. Nesses casos específicos, o Analista N3 deve desativar o FastTrack para garantir priorização absoluta de pacotes.
