# Módulo 04 — Engenharia Avançada MikroTik RouterOS
## 04.3 Cloud DNS Dinâmico (`*.sn.mynetname.net`)

Muitas filiais e clínicas médicas não possuem planos de Internet com IP público estático. A contratação de IP fixo frequentemente encarece a mensalidade do cliente sem necessidade real, desde que a engenharia de redes utilize recursos inteligentes de DDNS.

### O Serviço MikroTik Cloud DNS
A MikroTik fornece gratuitamente o serviço **IP Cloud**, que gera um nome DNS permanente atrelado ao número de série exclusivo da RouterBOARD:

```routeros
# Habilitar DDNS e sincronização de horário
/ip cloud
set ddns-enabled=yes ddns-update-interval=1m update-time=yes
```

### Obtendo o Endereço Gerado
Ao executar o comando:
```routeros
/ip cloud print
```
O RouterOS retornará o FQDN oficial do dispositivo, no padrão:
```
dns-name: 48920a1b2c3d.sn.mynetname.net
```

### Aplicação Prática na Operação Pulse TI
1. **Configuração de Túneis VPN:** Em vez de apontar uma filial para um endereço IP volátil (`200.x.x.x`), o túnel WireGuard ou SSTP aponta para o endereço `sn.mynetname.net`.
2. **Acesso Administrativo via Winbox:** O Analista N3 acessa o roteador remotamente através de `48920a1b2c3d.sn.mynetname.net:8205`.
3. **Catálogo no Pulse Control Web:** O nome DNS é registrado no inventário do cliente, garantindo conexão contínua mesmo após reinicializações do modem da operadora.
