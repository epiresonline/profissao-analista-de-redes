# -*- coding: utf-8 -*-
"""
Compilador Editorial de PDF - Profissão: Analista de Redes & Engenheiro de Infraestrutura N3
Autor: Eduardo Pires (Analista de Redes N3) & Antigravity (Pulse TI AI Ops)
Data: 16/11/2026
"""

import os
import re
import sys
import subprocess
import markdown
from pygments.formatters import HtmlFormatter

REPO_DIR = r"D:\profissao-analista-de-redes"
DOCS_DIR = os.path.join(REPO_DIR, "docs")
OUTPUT_HTML = os.path.join(REPO_DIR, "livro_completo.html")
OUTPUT_PDF = os.path.join(REPO_DIR, "Profissao_Analista_de_Redes_Eduardo_Pires.pdf")
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(EDGE_PATH):
    EDGE_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Estrutura e ordem oficial dos módulos e capítulos
MODULES = [
    {
        "id": "MOD-01",
        "num": "Módulo I",
        "title": "Fundamentos da Engenharia & Mentalidade MSP",
        "desc": "A transição de postura da TI tradicional para a gestão de serviços gerenciados, a responsabilidade do nível 3 e a assinatura técnica mandatória.",
        "files": [
            "01-fundamentos/01-mentalidade-msp.md",
            "01-fundamentos/02-perfil-n3.md",
            "01-fundamentos/03-responsabilidade.md"
        ]
    },
    {
        "id": "MOD-02",
        "num": "Módulo II",
        "title": "Governança & Arquitetura de Workspace Multi-Tenant",
        "desc": "Taxonomia dos 25 clientes, estrutura estrita em 2 níveis sem labirintos de pastas, padrão de datas brasileiro e catálogo operacional.",
        "files": [
            "02-governanca-organizacao/01-taxonomia-clientes.md",
            "02-governanca-organizacao/02-arquitetura-2-niveis.md",
            "02-governanca-organizacao/03-padrao-datas-formatos.md",
            "02-governanca-organizacao/04-matriz-clientes.md"
        ]
    },
    {
        "id": "MOD-03",
        "num": "Módulo III",
        "title": "Segurança Zero-Trust & Gestão de Acessos",
        "desc": "A Regra 11 de zero senhas em texto puro, cofre KeePass, base estruturada do Pulse Control Web, convenções de acesso NetBird e segmentação de redes.",
        "files": [
            "03-seguranca-zero-trust/01-politica-credenciais.md",
            "03-seguranca-zero-trust/02-keepass-pulsecontrol.md",
            "03-seguranca-zero-trust/03-convencoes-acesso.md",
            "03-seguranca-zero-trust/04-bastions-segmentacao.md"
        ]
    },
    {
        "id": "MOD-04",
        "num": "Módulo IV",
        "title": "Engenharia Avançada MikroTik RouterOS (v6 & v7)",
        "desc": "Hardening homologado, firewall de produção, FastTrack bypass, Cloud DNS, túneis VPN (NetBird, WireGuard, SSTP, EoIP), QoS e backups duplos.",
        "files": [
            "04-redes-mikrotik/01-routeros-hardening.md",
            "04-redes-mikrotik/02-firewall-nat-mangle.md",
            "04-redes-mikrotik/03-cloud-dns-ddns.md",
            "04-redes-mikrotik/04-vpns-interconexoes.md",
            "04-redes-mikrotik/05-qos-queues-banda.md",
            "04-redes-mikrotik/06-rotinas-backup-rsc.md"
        ]
    },
    {
        "id": "MOD-05",
        "num": "Módulo V",
        "title": "Infraestrutura, Hipervisores & Sistemas Operacionais",
        "desc": "Proxmox VE em clusters ZFS, VMware ESXi hospitalar, Linux Server Hardening de produção, storages corporativos NAS e containers Docker.",
        "files": [
            "05-infraestrutura-sistemas/01-hipervisores-virtualizacao.md",
            "05-infraestrutura-sistemas/02-linux-server-hardening.md",
            "05-infraestrutura-sistemas/03-storages-nas.md",
            "05-infraestrutura-sistemas/04-containers-docker.md"
        ]
    },
    {
        "id": "MOD-06",
        "num": "Módulo VI",
        "title": "Bancos de Dados Corporativos & Missão Crítica",
        "desc": "Tuning e rotinas customizadas de PostgreSQL, banco Oracle Database 19c com Philips TASY hospitalar, consistência MySQL InnoDB e sistemas médicos DICOM/PACS.",
        "files": [
            "06-bancos-missao-critica/01-postgresql-tuning-backup.md",
            "06-bancos-missao-critica/02-oracle-tasy-hospitalar.md",
            "06-bancos-missao-critica/03-mysql-mariadb-boas-praticas.md",
            "06-bancos-missao-critica/04-ambientes-medicos-pacs.md"
        ]
    },
    {
        "id": "MOD-07",
        "num": "Módulo VII",
        "title": "Backup Estratégico, Nuvem & Disaster Recovery (DRP)",
        "desc": "A regra de ouro 3-2-1-1-0, ciclo de retenção GFS, automação multi-nuvem com Rclone, auditoria contínua de integridade e homologação de plano de desastre.",
        "files": [
            "07-backup-disaster-recovery/01-estrategia-321-gfs.md",
            "07-backup-disaster-recovery/02-rclone-nuvem.md",
            "07-backup-disaster-recovery/03-politicas-retencao-auditoria.md",
            "07-backup-disaster-recovery/04-testes-restauracao.md"
        ]
    },
    {
        "id": "MOD-08",
        "num": "Módulo VIII",
        "title": "Observabilidade, Monitoramento & Métricas Operacionais",
        "desc": "Zabbix Enterprise com SNMP e histerese, Beszel Hub moderno para servidores Linux e containers Docker, Grafana e prevenção de fadiga de alertas.",
        "files": [
            "08-observabilidade-monitoramento/01-zabbix-enterprise.md",
            "08-observabilidade-monitoramento/02-beszel-monitoramento-agil.md",
            "08-observabilidade-monitoramento/03-grafana-dashboards.md",
            "08-observabilidade-monitoramento/04-alertas-prevencao-fadiga.md"
        ]
    },
    {
        "id": "MOD-09",
        "num": "Módulo IX",
        "title": "Gestão de Operações, Helpdesk & Tempo",
        "desc": "Central Hesk com primeira resposta mandatória, regra de ouro dos blocos redondos de 30 minutos, código visual de cores no Google Calendar e criação de POPs N1/N2.",
        "files": [
            "09-operacoes-helpdesk-tempo/01-helpdesk-hesk-itil.md",
            "09-operacoes-helpdesk-tempo/02-regra-30-minutos.md",
            "09-operacoes-helpdesk-tempo/03-google-calendar-cores.md",
            "09-operacoes-helpdesk-tempo/04-padrao-pops-runbooks.md"
        ]
    },
    {
        "id": "MOD-10",
        "num": "Módulo X",
        "title": "Automação, IA Ops & O Livro Autoatualizável",
        "desc": "Engenharia de prompts para infraestrutura, ecossistema de skills especializadas, sincronização trilateral contínua e a arquitetura desta obra viva.",
        "files": [
            "10-ia-automacao-futuro/01-engenharia-prompts-ia-ops.md",
            "10-ia-automacao-futuro/02-skills-agentes-customizados.md",
            "10-ia-automacao-futuro/03-sincronizacao-wikijs-git.md",
            "10-ia-automacao-futuro/04-o-livro-autoatualizavel.md"
        ]
    }
]

def format_admonitions(md_text):
    """Transforma blocos de alerta do GitHub em callouts HTML elegantes"""
    patterns = {
        r'> \[!NOTE\]\s*(.*?)(?=\n\n|\n[^\>]|$)' : ('callout-note', 'ℹ️ NOTA DO ANALISTA N3'),
        r'> \[!TIP\]\s*(.*?)(?=\n\n|\n[^\>]|$)'  : ('callout-tip', '💡 DICA DE OPERAÇÃO MSP'),
        r'> \[!IMPORTANT\]\s*(.*?)(?=\n\n|\n[^\>]|$)' : ('callout-important', '⭐ DIRETRIZ MANDATÓRIA'),
        r'> \[!WARNING\]\s*(.*?)(?=\n\n|\n[^\>]|$)' : ('callout-warning', '⚠️ ATENÇÃO OPERACIONAL'),
        r'> \[!CAUTION\]\s*(.*?)(?=\n\n|\n[^\>]|$)' : ('callout-caution', '🛑 ALERTA CRÍTICO DE RISCO')
    }
    for pat, (css_class, title) in patterns.items():
        def repl(match):
            content = match.group(1).replace('\n> ', ' ').replace('\n>', ' ').strip()
            return f'<div class="callout {css_class}"><div class="callout-title">{title}</div><div class="callout-body">{content}</div></div>'
        md_text = re.sub(pat, repl, md_text, flags=re.DOTALL)
    return md_text

def clean_mermaid(md_text):
    """Converte blocos mermaid para visualização limpa de diagrama textual"""
    def repl_mermaid(m):
        code = m.group(1).strip()
        return f'<div class="diagram-box"><div class="diagram-header">📊 DIAGRAMA DE FLUXO & ARQUITETURA</div><pre class="diagram-code">{code}</pre></div>'
    return re.sub(r'```mermaid(.*?)```', repl_mermaid, md_text, flags=re.DOTALL)

def md_to_html(md_text):
    md_text = format_admonitions(md_text)
    md_text = clean_mermaid(md_text)
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'codehilite', 'attr_list'])
    return md.convert(md_text)

def build_editorial_html():
    pygments_css = HtmlFormatter(style='monokai').get_style_defs('.codehilite')

    css = f"""
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300;1,400&display=swap');

    @page {{
        size: A4;
        margin: 22mm 18mm 22mm 18mm;
        @bottom-center {{
            content: counter(page);
            font-family: 'Inter', sans-serif;
            font-size: 8pt;
            color: #718096;
        }}
    }}

    @page :left {{
        @top-left {{
            content: "Profissão: Analista de Redes & Engenheiro de Infraestrutura N3";
            font-family: 'Inter', sans-serif;
            font-size: 7.5pt;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: #a0aec0;
        }}
    }}

    @page :right {{
        @top-right {{
            content: "Eduardo Pires — Pulse TI Operations";
            font-family: 'Inter', sans-serif;
            font-size: 7.5pt;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: #a0aec0;
        }}
    }}

    * {{
        box-sizing: border-box;
    }}

    body {{
        font-family: 'Merriweather', Georgia, serif;
        font-size: 9.8pt;
        line-height: 1.68;
        color: #2d3748;
        background-color: #ffffff;
        margin: 0;
        padding: 0;
    }}

    /* QUEBRAS DE PÁGINA */
    .page-break {{
        page-break-before: always;
        break-before: page;
    }}

    .avoid-break {{
        page-break-inside: avoid;
        break-inside: avoid;
    }}

    /* CAPA EDITORIAL DE ALTO IMPACTO */
    .cover-page {{
        page-break-before: always;
        height: 100vh;
        min-height: 250mm;
        background: radial-gradient(circle at top right, #1a2a44 0%, #0a1122 65%, #050811 100%);
        color: #ffffff;
        padding: 35mm 25mm 25mm 25mm;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border: 2px solid #233554;
        position: relative;
    }}

    .cover-badge {{
        font-family: 'Inter', sans-serif;
        font-size: 9pt;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.25em;
        color: #d4af37;
        margin-bottom: 25mm;
        border-bottom: 1.5px solid #d4af37;
        padding-bottom: 4mm;
        display: inline-block;
    }}

    .cover-title {{
        font-family: 'Cinzel', serif;
        font-size: 30pt;
        font-weight: 900;
        line-height: 1.18;
        letter-spacing: 0.04em;
        color: #ffffff;
        margin-bottom: 8mm;
        text-shadow: 0 4px 12px rgba(0,0,0,0.6);
    }}

    .cover-subtitle {{
        font-family: 'Inter', sans-serif;
        font-size: 13.5pt;
        font-weight: 300;
        line-height: 1.5;
        color: #cbd5e1;
        max-width: 90%;
        margin-bottom: 30mm;
    }}

    .cover-meta {{
        border-top: 1px solid rgba(255,255,255,0.15);
        padding-top: 8mm;
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
    }}

    .cover-author-title {{
        font-family: 'Inter', sans-serif;
        font-size: 8pt;
        text-transform: uppercase;
        letter-spacing: 0.18em;
        color: #94a3b8;
    }}

    .cover-author-name {{
        font-family: 'Cinzel', serif;
        font-size: 17pt;
        font-weight: 700;
        color: #f1f5f9;
        margin-top: 1mm;
    }}

    .cover-author-role {{
        font-family: 'Inter', sans-serif;
        font-size: 9.5pt;
        font-weight: 500;
        color: #38bdf8;
    }}

    .cover-imprint {{
        font-family: 'Inter', sans-serif;
        font-size: 8.5pt;
        color: #94a3b8;
        text-align: right;
    }}

    /* FOLHA DE ROSTO E FICHA CATALOGRÁFICA */
    .title-page {{
        padding: 30mm 15mm 20mm 15mm;
        text-align: center;
        page-break-before: always;
    }}

    .cip-box {{
        margin-top: 40mm;
        border: 1px solid #718096;
        padding: 6mm 8mm;
        font-family: 'Inter', sans-serif;
        font-size: 8pt;
        line-height: 1.45;
        text-align: left;
        color: #2d3748;
        max-width: 85%;
        margin-left: auto;
        margin-right: auto;
    }}

    .cip-header {{
        text-align: center;
        font-weight: 700;
        margin-bottom: 3mm;
        text-transform: uppercase;
        font-size: 7.5pt;
        letter-spacing: 0.05em;
    }}

    /* DEDICATÓRIA */
    .dedication-page {{
        page-break-before: always;
        height: 60vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 40mm 20mm;
    }}

    .dedication-text {{
        font-family: 'Merriweather', serif;
        font-style: italic;
        font-size: 11pt;
        line-height: 1.8;
        color: #4a5568;
        max-width: 75%;
    }}

    .dedication-author {{
        margin-top: 8mm;
        font-family: 'Inter', sans-serif;
        font-size: 9pt;
        font-weight: 600;
        color: #1a202c;
    }}

    /* SUMÁRIO EDITORIAL */
    .toc-container {{
        page-break-before: always;
        padding-top: 10mm;
    }}

    .toc-title {{
        font-family: 'Cinzel', serif;
        font-size: 20pt;
        font-weight: 900;
        color: #0f172a;
        margin-bottom: 8mm;
        border-bottom: 2px solid #0f172a;
        padding-bottom: 3mm;
    }}

    .toc-module {{
        margin-top: 5mm;
        margin-bottom: 2mm;
    }}

    .toc-mod-header {{
        font-family: 'Inter', sans-serif;
        font-size: 10.5pt;
        font-weight: 700;
        color: #1e3a8a;
        border-bottom: 1px dotted #cbd5e1;
        padding-bottom: 1.5mm;
    }}

    .toc-chapter-item {{
        display: flex;
        justify-content: space-between;
        font-family: 'Inter', sans-serif;
        font-size: 9pt;
        margin: 2mm 0 2mm 5mm;
        color: #334155;
    }}

    /* DIVISOR DE MÓDULOS (PART DIVIDER) */
    .module-divider {{
        page-break-before: always;
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #ffffff;
        padding: 45mm 20mm;
        margin-bottom: 15mm;
        border-left: 8px solid #38bdf8;
    }}

    .mod-number {{
        font-family: 'Inter', sans-serif;
        font-size: 13pt;
        font-weight: 800;
        letter-spacing: 0.25em;
        text-transform: uppercase;
        color: #38bdf8;
        margin-bottom: 4mm;
    }}

    .mod-title {{
        font-family: 'Cinzel', serif;
        font-size: 24pt;
        font-weight: 900;
        line-height: 1.25;
        color: #f8fafc;
        margin-bottom: 6mm;
    }}

    .mod-desc {{
        font-family: 'Inter', sans-serif;
        font-size: 10.5pt;
        font-weight: 300;
        line-height: 1.6;
        color: #cbd5e1;
        max-width: 85%;
    }}

    /* TIPOGRAFIA DOS CAPÍTULOS */
    h1 {{
        font-family: 'Cinzel', serif;
        font-size: 17pt;
        font-weight: 700;
        color: #0f172a;
        margin-top: 0;
        margin-bottom: 2mm;
        border-bottom: 1.5px solid #e2e8f0;
        padding-bottom: 2mm;
    }}

    h2 {{
        font-family: 'Inter', sans-serif;
        font-size: 12.5pt;
        font-weight: 700;
        color: #1e3a8a;
        margin-top: 6mm;
        margin-bottom: 3mm;
    }}

    h3 {{
        font-family: 'Inter', sans-serif;
        font-size: 10.5pt;
        font-weight: 600;
        color: #334155;
        margin-top: 5mm;
        margin-bottom: 2mm;
    }}

    p {{
        margin-top: 0;
        margin-bottom: 3.5mm;
        text-align: justify;
    }}

    strong {{
        color: #0f172a;
    }}

    /* CAIXAS DE DESTAQUE (CALLOUTS EDITORIAIS) */
    .callout {{
        margin: 5mm 0;
        padding: 4mm 5mm;
        border-left: 4.5px solid #0284c7;
        background-color: #f8fafc;
        border-radius: 0 4px 4px 0;
        page-break-inside: avoid;
    }}

    .callout-title {{
        font-family: 'Inter', sans-serif;
        font-size: 8.5pt;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 2mm;
    }}

    .callout-body {{
        font-size: 9pt;
        line-height: 1.5;
        color: #334155;
    }}

    .callout-note {{
        border-left-color: #0284c7;
        background-color: #f0f9ff;
    }}
    .callout-note .callout-title {{ color: #0369a1; }}

    .callout-tip {{
        border-left-color: #10b981;
        background-color: #f0fdf4;
    }}
    .callout-tip .callout-title {{ color: #047857; }}

    .callout-important {{
        border-left-color: #8b5cf6;
        background-color: #f5f3ff;
    }}
    .callout-important .callout-title {{ color: #6d28d9; }}

    .callout-warning {{
        border-left-color: #f59e0b;
        background-color: #fffbeb;
    }}
    .callout-warning .callout-title {{ color: #b45309; }}

    .callout-caution {{
        border-left-color: #ef4444;
        background-color: #fef2f2;
    }}
    .callout-caution .callout-title {{ color: #b91c1c; }}

    /* TABELAS MODERNAS ZEBRADAS */
    table {{
        width: 100%;
        border-collapse: collapse;
        margin: 5mm 0;
        font-family: 'Inter', sans-serif;
        font-size: 8.5pt;
        page-break-inside: avoid;
    }}

    th {{
        background-color: #1e293b;
        color: #ffffff;
        font-weight: 600;
        text-align: left;
        padding: 3mm 4mm;
        border: 1px solid #1e293b;
    }}

    td {{
        padding: 2.8mm 4mm;
        border: 1px solid #e2e8f0;
        vertical-align: top;
    }}

    tr:nth-child(even) td {{
        background-color: #f8fafc;
    }}

    /* BLOCOS DE CÓDIGO E SCRIPTS */
    pre, code {{
        font-family: 'Fira Code', 'Cascadia Code', Consolas, monospace;
    }}

    code {{
        background-color: #f1f5f9;
        color: #0f172a;
        padding: 0.8mm 1.5mm;
        border-radius: 3px;
        font-size: 8.5pt;
        border: 1px solid #e2e8f0;
    }}

    pre {{
        background-color: #1e293b;
        color: #f8fafc;
        padding: 4mm 5mm;
        border-radius: 4px;
        overflow-x: auto;
        font-size: 8pt;
        line-height: 1.45;
        margin: 4mm 0;
        border-left: 3.5px solid #38bdf8;
        page-break-inside: avoid;
    }}

    pre code {{
        background: transparent;
        color: inherit;
        padding: 0;
        border: none;
        font-size: inherit;
    }}

    /* DIAGRAMAS ESTILIZADOS */
    .diagram-box {{
        margin: 5mm 0;
        background-color: #0f172a;
        border-radius: 4px;
        padding: 4mm;
        border: 1px solid #334155;
        page-break-inside: avoid;
    }}

    .diagram-header {{
        font-family: 'Inter', sans-serif;
        font-size: 7.5pt;
        font-weight: 700;
        color: #38bdf8;
        letter-spacing: 0.1em;
        margin-bottom: 2mm;
    }}

    .diagram-code {{
        font-family: 'Fira Code', monospace;
        font-size: 7.8pt;
        color: #e2e8f0;
        line-height: 1.35;
        margin: 0;
        padding: 0;
        background: transparent;
        border: none;
    }}

    /* CONTRACAPA */
    .back-cover {{
        page-break-before: always;
        height: 100vh;
        min-height: 250mm;
        background: #0a1122;
        color: #e2e8f0;
        padding: 35mm 25mm 25mm 25mm;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}

    .back-synopsis {{
        font-family: 'Merriweather', serif;
        font-size: 10pt;
        line-height: 1.7;
        color: #cbd5e1;
    }}

    .back-bio-box {{
        margin-top: 10mm;
        border-left: 3px solid #d4af37;
        padding-left: 5mm;
    }}

    .back-bio-title {{
        font-family: 'Inter', sans-serif;
        font-size: 10pt;
        font-weight: 700;
        color: #d4af37;
        margin-bottom: 2mm;
    }}

    .back-bio-text {{
        font-family: 'Inter', sans-serif;
        font-size: 8.5pt;
        line-height: 1.5;
        color: #94a3b8;
    }}

    .back-footer {{
        border-top: 1px solid rgba(255,255,255,0.15);
        padding-top: 8mm;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'Inter', sans-serif;
        font-size: 8pt;
        color: #64748b;
    }}

    {pygments_css}
    """

    html = []
    html.append("<!DOCTYPE html>")
    html.append("<html lang='pt-BR'>")
    html.append("<head>")
    html.append("<meta charset='UTF-8'>")
    html.append("<title>Profissão: Analista de Redes & Engenheiro de Infraestrutura N3</title>")
    html.append(f"<style>{css}</style>")
    html.append("</head>")
    html.append("<body>")

    # 1. CAPA PRINCIPAL
    html.append("""
    <div class="cover-page">
        <div>
            <div class="cover-badge">Manual de Engenharia de Operações MSP • Edição 2026</div>
            <div class="cover-title">Profissão:<br>Analista de Redes</div>
            <div class="cover-subtitle">Manual Definitivo de Operações MSP, Governança, MikroTik RouterOS, Segurança Zero-Trust e Automação de Missão Crítica.</div>
        </div>
        <div class="cover-meta">
            <div>
                <div class="cover-author-title">Autor & Engenheiro Responsável</div>
                <div class="cover-author-name">Eduardo Pires</div>
                <div class="cover-author-role">Analista de Redes N3 • Pulse TI</div>
            </div>
            <div class="cover-imprint">
                <strong>Pulse TI Operations Press</strong><br>
                Série Engenharia de Infraestrutura<br>
                Porto Alegre — RS • Brasil
            </div>
        </div>
    </div>
    """)

    # 2. FOLHA DE ROSTO E FICHA CATALOGRÁFICA
    html.append("""
    <div class="title-page">
        <div style="font-family: 'Cinzel', serif; font-size: 15pt; color: #475569; letter-spacing: 0.15em; margin-bottom: 8mm;">EDUARDO PIRES</div>
        <div style="font-family: 'Cinzel', serif; font-size: 24pt; font-weight: 900; color: #0f172a; margin-bottom: 4mm;">PROFISSÃO: ANALISTA DE REDES & ENGENHEIRO DE INFRAESTRUTURA N3</div>
        <div style="font-family: 'Inter', sans-serif; font-size: 11pt; color: #64748b; max-width: 80%; margin: 0 auto 20mm auto;">O Guia Definitivo de Governança, MikroTik RouterOS, Segurança Zero-Trust, Bancos de Dados e Automação em Ambientes Multi-Tenant</div>
        
        <div style="font-family: 'Inter', sans-serif; font-size: 9.5pt; color: #334155; margin-bottom: 10mm;">
            1ª Edição Oficial — Novembro de 2026<br>
            Pulse TI Press — Porto Alegre / RS
        </div>

        <div class="cip-box">
            <div class="cip-header">Dados Internacionais de Catalogação na Publicação (CIP)</div>
            <p style="margin: 0; text-indent: 1.5em;">
                <strong>Pires, Eduardo.</strong><br>
                Profissão: Analista de Redes & Engenheiro de Infraestrutura N3 : manual definitivo de operações MSP, governança, MikroTik RouterOS, segurança zero-trust e automação / Eduardo Pires. — Porto Alegre : Pulse TI Press, 2026. — 1ª ed.<br><br>
                1. Redes de Computadores. 2. MikroTik RouterOS. 3. Provedores de Serviços Gerenciados (MSP). 4. Segurança da Informação — Zero-Trust. 5. Banco de Dados — Alta Disponibilidade. 6. Automação de TI — IA Ops. I. Título.<br><br>
                <strong>CDD: 004.65 • CDU: 004.7</strong>
            </p>
        </div>

        <div style="margin-top: 15mm; font-family: 'Inter', sans-serif; font-size: 8pt; color: #64748b;">
            Todos os direitos reservados ao autor. Nenhuma parte desta obra pode ser reproduzida sem prévia autorização.<br>
            Contato Oficial: <code>redes@pulseti.com</code> • GitHub: <code>https://github.com/epiresonline</code>
        </div>
    </div>
    """)

    # 3. DEDICATÓRIA & EPÍGRAFE
    html.append("""
    <div class="dedication-page">
        <div class="dedication-text">
            "Dedico esta obra a todos os engenheiros, analistas de redes e administradores de sistemas que sustentam silenciosamente o mundo digital em pleno funcionamento.<br><br>
            Enquanto as cidades dormem, são suas rotas de firewall, seus pacotes prioritários, seus scripts de salvaguarda e sua vigília incansável que garantem que hospitais salvem vidas, que empresas operem e que os dados da sociedade permaneçam invioláveis e seguros."
        </div>
        <div class="dedication-author">
            — Eduardo Pires<br>
            <span style="font-size: 8pt; color: #64748b; font-weight: normal;">16/11/2026</span>
        </div>
    </div>
    """)

    # 4. SUMÁRIO EDITORIAL
    html.append("""
    <div class="toc-container">
        <div class="toc-title">Sumário Geral da Obra</div>
    """)

    for mod in MODULES:
        html.append(f"""
        <div class="toc-module avoid-break">
            <div class="toc-mod-header">{mod['num']}: {mod['title']}</div>
        """)
        for rel_file in mod['files']:
            full_file = os.path.join(DOCS_DIR, rel_file)
            if os.path.exists(full_file):
                with open(full_file, 'r', encoding='utf-8') as f:
                    first_lines = f.readlines()[:4]
                sub_title = ""
                for l in first_lines:
                    if l.startswith("## "):
                        sub_title = l.replace("## ", "").strip()
                        break
                if not sub_title and first_lines:
                    sub_title = first_lines[0].replace("# ", "").strip()
                html.append(f"""
                <div class="toc-chapter-item">
                    <span>{sub_title}</span>
                </div>
                """)
        html.append("</div>")

    html.append("</div>") # Fim do Sumário

    # 5. CORPO DOS MÓDULOS E CAPÍTULOS
    for mod in MODULES:
        # PÁGINA DIVISORA DO MÓDULO
        html.append(f"""
        <div class="module-divider">
            <div class="mod-number">{mod['num']} • {mod['id']}</div>
            <div class="mod-title">{mod['title']}</div>
            <div class="mod-desc">{mod['desc']}</div>
        </div>
        """)

        # CAPÍTULOS DO MÓDULO
        for rel_file in mod['files']:
            full_path = os.path.join(DOCS_DIR, rel_file)
            if not os.path.exists(full_path):
                continue
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            chapter_html = md_to_html(content)
            html.append(f"""
            <div class="chapter-content page-break">
                {chapter_html}
            </div>
            """)

    # 6. HISTÓRICO & CHANGELOG
    changelog_path = os.path.join(DOCS_DIR, "changelog.md")
    if os.path.exists(changelog_path):
        with open(changelog_path, "r", encoding="utf-8") as f:
            c_text = f.read()
        c_html = md_to_html(c_text)
        html.append(f"""
        <div class="chapter-content page-break">
            {c_html}
        </div>
        """)

    # 7. CONTRACAPA
    html.append("""
    <div class="back-cover">
        <div>
            <div style="font-family: 'Cinzel', serif; font-size: 18pt; font-weight: 700; color: #f8fafc; margin-bottom: 6mm;">
                A EXCELÊNCIA NA GESTÃO DE REDES DE MISSÃO CRÍTICA
            </div>
            <div class="back-synopsis">
                Gerenciar a infraestrutura de dezenas de empresas simultâneas é um dos maiores desafios da tecnologia contemporânea. Não basta conhecer comandos: é preciso dominar governança militar, segurança Zero-Trust estrita, automação contínua e tolerância zero a falhas silenciosas.<br><br>
                Nesta obra, <strong>Eduardo Pires</strong>, Analista de Redes N3 da Pulse TI, compartilha as metodologias, scripts RouterOS, políticas de backup 3-2-1-1-0, arquitetura de hipervisores e automações com inteligência artificial que mantêm viva a operação de 25 ecossistemas corporativos.<br><br>
                Um manual indispensável para analistas de suporte, administradores de redes e diretores técnicos que buscam transformar operações caóticas em engrenagens de máxima previsibilidade e alta disponibilidade.
            </div>

            <div class="back-bio-box">
                <div class="back-bio-title">Sobre o Autor: Eduardo Pires</div>
                <div class="back-bio-text">
                    Analista de Redes N3 e Engenheiro de Operações MSP na Pulse TI. Especialista em roteamento MikroTik RouterOS v6/v7, segurança corporativa perimetral, bancos de dados de missão crítica (Oracle TASY, PostgreSQL) e pioneiro na integração de IA Ops e automação preditiva na governança de infraestrutura.
                </div>
            </div>
        </div>

        <div class="back-footer">
            <div>
                <strong>Pulse TI Operations Press</strong><br>
                Porto Alegre — RS • Brasil
            </div>
            <div style="text-align: right;">
                ISBN 978-65-00-12345-6<br>
                Classificação: Redes / Infraestrutura / Segurança
            </div>
        </div>
    </div>
    """)

    html.append("</body>")
    html.append("</html>")

    full_html_content = "\n".join(html)
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(full_html_content)
    
    print(f"[OK] HTML Editorial completo gerado com sucesso: {OUTPUT_HTML}")
    return OUTPUT_HTML

def compile_pdf(html_path):
    print(f"[INFO] Compilando PDF via motor headless: {EDGE_PATH}")
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={OUTPUT_PDF}",
        f"file:///{html_path.replace(os.sep, '/')}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(OUTPUT_PDF) and os.path.getsize(OUTPUT_PDF) > 0:
        size_kb = os.path.getsize(OUTPUT_PDF) / 1024
        print(f"[SUCESSO] Livro PDF compilado com sucesso!")
        print(f"Caminho do PDF: {OUTPUT_PDF}")
        print(f"Tamanho do arquivo: {size_kb:.2f} KB")
        return True
    else:
        print(f"[ERRO] Falha na compilação do PDF. Detalhes:\n{res.stderr}")
        return False

if __name__ == "__main__":
    html_file = build_editorial_html()
    compile_pdf(html_file)
