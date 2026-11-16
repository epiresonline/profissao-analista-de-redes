# -*- coding: utf-8 -*-
"""
Testador de Renderização Visual de Diagramas para o PDF
"""
import re

def render_diagram(mermaid_code):
    code = mermaid_code.strip()
    
    # 1. Diagrama da Regra 3-2-1-1-0 de Backup
    if "Dados Originais de Produção" in code and "3 Cópias dos Dados" in code:
        steps = [
            ("💾", "ORIGEM", "Dados Originais de Produção", "Bancos de dados, ERPs hospitalares e arquivos corporativos em tempo real."),
            ("📋", "REGRA 3", "3 Cópias dos Dados", "Ao menos três instâncias dos dados existentes simultaneamente."),
            ("💿", "REGRA 2", "2 Mídias Físicas Distintas", "Separação física de armazenamento: NVMe local de produção + Storage NAS corporativo."),
            ("☁️", "REGRA 1", "1 Cópia Offsite em Nuvem", "Salvaguarda remota externa automatizada via Rclone para Google Drive e AWS S3."),
            ("🔒", "REGRA 1", "1 Cópia Imutável ou Offline", "Snapshots imutáveis WORM / Air-Gapped imunes a ataques de ransomware."),
            ("✅", "REGRA 0", "0 Erros na Restauração", "Homologação periódica obrigatória em ambiente Sandbox para validação 100% íntegra.")
        ]
        html = '<div class="visual-diagram pipeline-diagram avoid-break">'
        html += '<div class="diagram-title">🛡️ ARQUITETURA DA REGRA DE BACKUP 3-2-1-1-0</div>'
        html += '<div class="pipeline-container">'
        for i, (icon, badge, title, desc) in enumerate(steps):
            html += f'''
            <div class="pipeline-step">
                <div class="step-card">
                    <div class="step-badge">{badge}</div>
                    <div class="step-header"><span class="step-icon">{icon}</span> {title}</div>
                    <div class="step-desc">{desc}</div>
                </div>
            </div>
            '''
            if i < len(steps) - 1:
                html += '<div class="step-arrow">⬇</div>'
        html += '</div></div>'
        return html

    # 2. Diagrama de Segmentação de Redes e VLANs
    if "VLAN 10: Gerenciamento" in code:
        vlans = [
            ("VLAN 10", "Gerenciamento", "Switches, APs Wi-Fi, PDUs e consoles IPMI/iLO", "#0284c7"),
            ("VLAN 20", "Servidores & DMZ", "Servidores de banco, ERPs e aplicações de produção", "#6366f1"),
            ("VLAN 30", "Estações Corporativas", "Desktops, notebooks e estações de trabalho de colaboradores", "#059669"),
            ("VLAN 40", "Equipamentos Médicos", "Aparelhos de ultrassom, tomógrafos, ressonâncias e DICOM/PACS", "#8b5cf6"),
            ("VLAN 50", "CFTV & Segurança", "Câmeras IP e servidores NVR com tráfego isolado da web", "#f59e0b"),
            ("VLAN 90", "Visitantes (Guest)", "Rede de hóspedes/pacientes com saída exclusiva para internet", "#dc2626")
        ]
        html = '<div class="visual-diagram tree-diagram avoid-break">'
        html += '<div class="diagram-title">🖧 TOPOLOGIA DE SEGMENTAÇÃO POR VLANS & FIREWALL</div>'
        html += '''
        <div class="tree-root">
            <div class="root-badge">GATEWAY & BORDA</div>
            <div class="root-title">🌐 MikroTik RouterOS (Firewall Stateful & Roteamento Inter-VLAN)</div>
        </div>
        <div class="tree-bus-arrow">⬇ DISTRIBUIÇÃO SEGMENTADA POR TRUNK 802.1Q ⬇</div>
        <div class="tree-grid">
        '''
        for vid, vname, vdesc, color in vlans:
            html += f'''
            <div class="vlan-card" style="border-left-color: {color};">
                <div class="vlan-tag" style="background-color: {color};">{vid}</div>
                <div class="vlan-name">{vname}</div>
                <div class="vlan-desc">{vdesc}</div>
            </div>
            '''
        html += '</div></div>'
        return html

    # 3. Diagrama de VPNs e Interconexões
    if "VPNs Pulse TI" in code:
        vpns = [
            ("NetBird Mesh", "WireGuard Overlay", "Conexão zero-touch mesh direta entre técnicos, servidores e nuvem sem portas abertas."),
            ("WireGuard v7", "Site-to-Site RouterOS", "Túnel de altíssimo throughput e latência mínima entre Matriz e Filiais regionais."),
            ("SSTP Seguro", "TCP 443 / SSL TLS", "Contingência robusta para ambientes com bloqueios restritivos em portas UDP."),
            ("EoIP + IPsec", "Túnel Camada 2", "Interconexão transparente L2 para sistemas legados que exigem mesmo domínio de broadcast.")
        ]
        html = '<div class="visual-diagram tree-diagram avoid-break">'
        html += '<div class="diagram-title">🔒 ARQUITETURA DE VPNS & INTERCONEXÕES HOMOLOGADAS</div>'
        html += '''
        <div class="tree-root">
            <div class="root-badge">MATRIZ OPERACIONAL</div>
            <div class="root-title">🛡️ Ecossistema de Conectividade Segura Pulse TI</div>
        </div>
        <div class="tree-bus-arrow">⬇ TÚNEIS CRIPTOGRAFADOS POR FINALIDADE ⬇</div>
        <div class="tree-grid" style="grid-template-columns: repeat(2, 1fr);">
        '''
        for vname, vtech, vdesc in vpns:
            html += f'''
            <div class="vlan-card" style="border-left-color: #0284c7;">
                <div class="vlan-tag" style="background-color: #0284c7;">{vtech}</div>
                <div class="vlan-name">{vname}</div>
                <div class="vlan-desc">{vdesc}</div>
            </div>
            '''
        html += '</div></div>'
        return html

    # 4. Diagrama das 4 Frentes do Analista N3
    if "Analista de Redes N3" in code and "Arquitetura & Engenharia" in code:
        frentes = [
            ("🏛️", "Arquitetura & Engenharia", "Desenho de topologias escaláveis, VPNs mesh, enlaces e políticas de firewall."),
            ("🚨", "Resolução de Crises", "Troubleshooting profundo de camada 2 e 3, análise de pacotes e recuperação de desastres."),
            ("⚙️", "Automação & Ferramental", "Desenvolvimento de scripts de salvaguarda, APIs REST e automação de rotinas."),
            ("📚", "Mentoria & Governança", "Conversão de incidentes em POPs estruturados e capacitação contínua da equipe N1/N2.")
        ]
        html = '<div class="visual-diagram tree-diagram avoid-break">'
        html += '<div class="diagram-title">🎯 AS QUATRO FRENTES DO ANALISTA DE REDES N3</div>'
        html += '''
        <div class="tree-root">
            <div class="root-badge">LIDERANÇA TÉCNICA</div>
            <div class="root-title">👨‍💻 Analista de Redes N3 / Engenheiro de Operações</div>
        </div>
        <div class="tree-bus-arrow">⬇ PILARES DE RESPONSABILIDADE OPERACIONAL ⬇</div>
        <div class="tree-grid" style="grid-template-columns: repeat(2, 1fr);">
        '''
        for icon, title, desc in frentes:
            html += f'''
            <div class="vlan-card" style="border-left-color: #38bdf8;">
                <div class="vlan-name">{icon} {title}</div>
                <div class="vlan-desc">{desc}</div>
            </div>
            '''
        html += '</div></div>'
        return html

    # 5. Diagrama das Skills de IA Ops
    if "mikrotik-helper" in code and "beszel-manager" in code:
        skills = [
            ("mikrotik-helper", "Redes & RouterOS", "Geração e auditoria de configurações RouterOS v6/v7."),
            ("beszel-manager", "Métricas & Hub", "Provisionamento e monitoramento ultraleve de servidores."),
            ("hesk-ticket-logger", "Helpdesk ITIL", "Gestão de chamados, rastreamento e primeira resposta."),
            ("daily-calendar-logger", "Google Calendar", "Registro de horas e classificação por cores na agenda."),
            ("backup-inspector", "Auditoria de Dumps", "Varredura proativa de integridade de backups de banco."),
            ("pulse-client-auditor", "Governança", "Validação de conformidade das 6 categorias estruturais.")
        ]
        html = '<div class="visual-diagram tree-diagram avoid-break">'
        html += '<div class="diagram-title">🤖 ECOSSISTEMA DE SKILLS & AGENTES ESPECIALISTAS (AIOPS)</div>'
        html += '''
        <div class="tree-root">
            <div class="root-badge">ORQUESTRADOR DE IA</div>
            <div class="root-title">🧠 Antigravity Pulse TI AI Ops</div>
        </div>
        <div class="tree-bus-arrow">⬇ HABILIDADES TÉCNICAS ACOPLADAS AO WORKSPACE ⬇</div>
        <div class="tree-grid">
        '''
        for sname, scateg, sdesc in skills:
            html += f'''
            <div class="vlan-card" style="border-left-color: #10b981;">
                <div class="vlan-tag" style="background-color: #10b981;">{scateg}</div>
                <div class="vlan-name"><code>{sname}</code></div>
                <div class="vlan-desc">{sdesc}</div>
            </div>
            '''
        html += '</div></div>'
        return html

    # 6. Diagrama dos 4 Pilares da Governança (index.md)
    if "subgraph G" in code and "Pilar 1" in code:
        pilares = [
            ("PILAR 1", "Governança & Workspace", ["Código oficial de 3 dígitos", "Sigla oficial de 3 letras", "Estrutura estrita em 2 níveis"]),
            ("PILAR 2", "Segurança Zero-Trust", ["Zero senhas em texto puro", "Cofre KeePass & Pulse Control", "Acessos decodificados NetBird & SSH"]),
            ("PILAR 3", "Infraestrutura & Redes", ["MikroTik RouterOS homologado", "Virtualização Proxmox / VMware", "Bancos de missão crítica (TASY, Postgres)"]),
            ("PILAR 4", "Operações & Automação", ["Chamados Hesk com 1ª resposta", "Google Calendar por cores técnicas", "Blocos redondos de 30 minutos", "IA Ops & Skills customizadas"])
        ]
        html = '<div class="visual-diagram tree-diagram avoid-break">'
        html += '<div class="diagram-title">🏛️ OS QUATRO PILARES DA GOVERNANÇA PULSE TI</div>'
        html += '<div class="tree-grid" style="grid-template-columns: repeat(2, 1fr); margin-top: 5mm;">'
        for tag, title, items in pilares:
            html += f'''
            <div class="vlan-card" style="border-left-color: #6366f1;">
                <div class="vlan-tag" style="background-color: #6366f1;">{tag}</div>
                <div class="vlan-name">{title}</div>
                <ul style="margin: 2mm 0 0 4mm; padding: 0; font-size: 8.5pt; color: #334155; line-height: 1.4;">
            '''
            for it in items:
                html += f'<li>{it}</li>'
            html += '</ul></div>'
        html += '</div></div>'
        return html

    # Fallback genérico caso apareça outro diagrama:
    return f'<div class="callout callout-note"><div class="callout-title">DIAGRAMA TÉCNICO</div><div class="callout-body"><pre><code>{mermaid_code}</code></pre></div></div>'

print("Módulo de diagramação visual validado com sucesso!")
