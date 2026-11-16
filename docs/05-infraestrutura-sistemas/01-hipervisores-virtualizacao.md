# Módulo 05 — Infraestrutura, Hipervisores & Sistemas
## 05.1 Hipervisores Corporativos: Proxmox VE, VMware ESXi e KVM

A virtualização moderna é a base dos servidores da Pulse TI. A migração de ambientes bare-metal para hipervisores do tipo bare-metal (Type 1) garante alta disponibilidade e agilidade em desastres.

### Comparativo Homologado na Pulse TI

| Hipervisor | Onde é Aplicado | Vantagens Homologadas | Ferramenta de Backup Nativa |
| :--- | :--- | :--- | :--- |
| **Proxmox VE (KVM/LXC)** | Datacenter Cloud Pulse (`123 - PLS`) e Clientes On-Premise | Código aberto, sem travas de licença, suporte a ZFS nativo, API REST. | Proxmox Backup Server (PBS) com deduplicação. |
| **VMware ESXi** | Ambientes Hospitalares (`092 - HOS`) e Legados de Grande Porte | Robustez corporativa, compatibilidade com appliances proprietários. | Veeam Backup & Replication ou scripts vzdump. |
| **KVM Nativo Linux** | Servidores dedicados leves (`080 - CLN`) | Performance máxima bare-metal com overhead de CPU próximo a zero. | Snapshots LVM e `qemu-img`. |

### Boas Práticas de Configuração no Proxmox VE
1. **ZFS com Mirror / RAIDZ:** Sempre utilizar ZFS com discos SSD corporativos (SAS ou NVMe), ativando compressão `lz4` nativa.
2. **Separação de Rede (Bridges):** Uma bridge (`vmbr0`) para a interface WAN pública e bridges dedicadas para VLANs internas de produção (`vmbr1.10`, `vmbr1.20`).
3. **VirtIO como Padrão de Disco e Rede:** Nunca usar emulação IDE ou E1000. VirtIO SCSI com `Discard=on` (TRIM) e VirtIO Net fornecem throughput até 3x superior.
