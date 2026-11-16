# Módulo 03 — Segurança Zero-Trust & Gestão de Acessos
## 03.2 Cofres de Acesso: KeePass Corporativo & Pulse Control Web

A segurança das credenciais na Pulse TI baseia-se em duas ferramentas complementares:

### 1. O Cofre Oficial KeePass (`PASSWORD_DATABASE_PULSE.kdbx`)
- Localização oficial:  
  `002 - PTI - Pulse TI/05 - BACKUP E SEGURANCA/Controle de Acesso/Keepass/`
- Criptografia: AES-256 / ChaCha20 com chave mestre de alta entropia.
- Estrutura de grupos: Organizado rigorosamente segundo a taxonomia `<CODIGO> - <SIGLA> - <Nome>`.
- Campos customizados: Utiliza campos adicionais para registrar portas Winbox, URLs NetBird e IDs de ativos.

### 2. O Sistema Pulse Control Web (Inventário Ativo & REST API)
O **Pulse Control Web** é um sistema desenvolvido sob medida para a operação da Pulse TI, fornecendo um banco de dados SQLite 3 estruturado de alta performance (`D:\\PulseControl\\pulse-control-web\\pulsecontrol.db`) com busca full-text (FTS) e interface web em `http://localhost:3005`.

#### Estrutura de Dados das Entradas do Cofre
```sql
CREATE TABLE entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_code TEXT NOT NULL,      -- Ex: '112'
    client_name TEXT NOT NULL,      -- Ex: 'DiagCenter Diagnósticos'
    title TEXT NOT NULL,            -- Ex: 'MikroTik Borda Matriz'
    username TEXT NOT NULL,         -- Ex: 'pulse_admin'
    ip_address TEXT,                -- Ex: '100.81.222.10'
    port INTEGER,                   -- Ex: 8291
    protocol TEXT,                  -- Ex: 'Winbox', 'SSH', 'RDP'
    notes TEXT                      -- Metadados operacionais
);
```

#### Como Consultar Proativamente via Python
Quando um operador ou agente de IA precisa localizar um endereço IP ou porta de serviço de um cliente, ele consulta a base:

```python
import sqlite3

def buscar_ativo(codigo_cliente, termo):
    conn = sqlite3.connect(r'D:\PulseControl\pulse-control-web\pulsecontrol.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT title, username, ip_address, port, protocol FROM entries WHERE client_code = ? AND title LIKE ?",
        (codigo_cliente, f"%{termo}%")
    )
    return cursor.fetchall()
```
