# Módulo 04 — Engenharia Avançada MikroTik RouterOS
## 04.5 QoS, Queues e Priorização de Tráfego de Produção

Em empresas médicas, callcenters (`142 - TEL`) ou indústrias, links de Internet podem sofrer saturação repentina por downloads, backups em nuvem ou vídeos em alta definição. Sem uma engenharia de Qualidade de Serviço (**QoS**), o tráfego crítico sofre atrasos inaceitáveis.

### A Hierarquia de Prioridades Pulse TI

| Prioridade | Tipo de Tráfego | Protocolos / Aplicações | Tratamento no RouterOS |
| :---: | :--- | :--- | :--- |
| **P1 (Crítica)** | Telefonia IP & VoIP | SIP (5060 UDP), RTP (10000-20000 UDP) | Banda reservada, sem buffering |
| **P2 (Alta)** | Sistemas de Gestão & DNS | TASY, Protheus, Optix PACS, DNS (53) | Prioridade de fila 1, DSCP EF |
| **P3 (Média)** | Conexões Administrativas | SSH, Winbox, RDP, NetBird VPN | Prioridade de fila 3 |
| **P4 (Padrão)** | Navegação Web & E-mail | HTTP (80), HTTPS (443) | Prioridade de fila 6 |
| **P5 (Baixa)** | Backups Cloud & Downloads | Rclone, Google Drive, Torrents | Limitado em caso de contenção |

### Marcação de Pacotes no Mangle
```routeros
/ip firewall mangle
# Marcar conexões VoIP (SIP/RTP)
add chain=prerouting action=mark-connection new-connection-mark=VOIP-CONN \
    passthrough=yes protocol=udp port=5060,10000-20000 comment="Conn VoIP"
add chain=prerouting action=mark-packet new-packet-mark=VOIP-PKT \
    passthrough=no connection-mark=VOIP-CONN comment="Pkt VoIP"

# Marcar conexões administrativas Winbox/SSH
add chain=prerouting action=mark-connection new-connection-mark=ADMIN-CONN \
    passthrough=yes protocol=tcp port=22022,8205 comment="Conn Admin"
add chain=prerouting action=mark-packet new-packet-mark=ADMIN-PKT \
    passthrough=no connection-mark=ADMIN-CONN comment="Pkt Admin"
```
