# Módulo 05 — Infraestrutura, Hipervisores & Sistemas
## 05.3 Storage Corporativo e NAS (Synology, TrueNAS, QNAP)

Em nossos clientes de diagnóstico médico e hospitais (`092 - HOS`, `080 - CLN`, `112 - DIA`), o volume de arquivos de exames (raio-X, tomografia, ressonância em formato DICOM) atinge terabytes de informação sensível.

### Arquitetura de Armazenamento NAS
- **Protocolos Homologados:**
  - **SMB 3.1.1 com Criptografia:** Utilizado para compartilhamentos de estações Windows de radiologistas e recepção.
  - **NFS v4:** Utilizado para montagens de alta velocidade em servidores de aplicação Linux e clusters Docker.
  - **iSCSI:** Utilizado para fornecer LUNs diretas para hipervisores Proxmox ou VMware.

### Diretrizes de Segurança em Compartilhamentos NAS
1. **Desativação Completa do Protocolo SMBv1:** O SMBv1 possui vulnerabilidades críticas graves (como o EternalBlue / WannaCry). Homologamos estritamente SMBv2 e SMBv3.
2. **Isolamento de Contas Administrativas:** A conta `admin` padrão do storage deve ser desativada. O gerenciamento é feito por usuário nominal no cofre KeePass.
3. **Snapshots Locais Imutáveis:** Configuração de snapshots Btrfs ou ZFS no storage com retenção imutável de 14 dias (proteção contra ataques de Ransomware).
