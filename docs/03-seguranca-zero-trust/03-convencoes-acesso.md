# Módulo 03 — Segurança Zero-Trust & Gestão de Acessos
## 03.3 Convenções Decodificadas de Acesso: NetBird, PuTTY SSH e Winbox

Para simplificar a operação de suporte sem comprometer a segurança, homologamos convenções universais para os principais métodos de acesso remoto:

### 1. RDP por IP da Malha NetBird (`rdp://100.x.x.x`)
- **Protocolo:** Microsoft Remote Desktop Protocol (Porta 3389).
- **Camada de Transporte:** Túnel encriptado WireGuard via malha NetBird.
- **Forma de Uso:** Conexão direta utilizando o IP fixo virtual da interface NetBird (ex.: `mstsc /v:100.81.222.29`).
- **Vantagem:** Não requer encaminhamento de portas (NAT/Port Forward) nos roteadores dos clientes e elimina a exposição de RDP na Internet pública.

### 2. RDP por Split-DNS NetBird (`rdp://*.netbird.selfhosted`)
- **Resolução de Nomes:** DNS corporativo interno mantido pelos servidores NetBird.
- **Forma de Uso:** `mstsc /v:pls-doq-vm-app-protheus.netbird.selfhosted`.
- **Vantagem:** Independência de endereçamento IP. Se o IP da VM mudar, a conexão persiste pelo FQDN.

### 3. SSH Overwrite com PuTTY (`usuario@host` + `putty:`)
- **Padrão em Registros:** Quando uma entrada contém `putty:`, significa que deve ser aberta no software PuTTY utilizando a chave privada salva ou encaminhada via Pageant.
- **Porta:** 22 (ou porta customizada mapeada no inventário).
- **Exemplo de Execução:** `putty.exe -ssh pls@pls-doq-vm-db-protheus.netbird.selfhosted -P 22`.

### 4. MikroTik RouterOS com Winbox e Cloud DNS
- **Portas Homologadas:** Portas customizadas como `8205`, `8207` ou a padrão protegida `8291`.
- **Resolução Dinâmica:** Utilização do hostname MikroTik Cloud (`*.sn.mynetname.net`) em links que possuem IP público dinâmico.
- **Exemplo de Conexão no Winbox:** `prn-matriz.sn.mynetname.net:8205`.
