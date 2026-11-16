# Módulo 06 — Bancos de Dados Corporativos & Missão Crítica
## 06.4 Ambientes Médicos, PACS Optix, Mobilemed e DICOM

A Pulse TI possui vasta especialização na gestão de clínicas de radiologia e medicina diagnóstica (`053 - WAG`, `099 - CIT`, `112 - PRN`, `121 - MED`).

### O Ecossistema de Diagnóstico por Imagem
- **PACS (Picture Archiving and Communication System):** Servidores responsáveis pelo armazenamento, transmissão e exibição de exames médicos (ex.: Optix PACS, Mobilemed).
- **Protocolo DICOM (Digital Imaging and Communications in Medicine):** Protocolo de rede que comunica tomógrafos, aparelhos de ultrassom e ressonâncias magnéticas com o servidor PACS.

### Desafios de Engenharia em Redes DICOM
1. **Latência e Throughput:** Um exame de tomografia computadorizada moderno pode conter mais de 2.000 fatias de imagem de alta resolução em um único estudo (pesando centenas de megabytes). A rede local das estações de laudo deve operar em Gigabit Ethernet puro ou 10 GbE.
2. **Conformidade Legal de Guarda:** No Brasil, a legislação do CFM e ANVISA exige a guarda segura de exames e laudos médicos por **no mínimo 20 anos**. Portanto, a estratégia de armazenamento exige replicação multi-nuvem imutável (AWS S3 Glacier ou Wasabi Cloud).
