# Módulo 04 — Engenharia Avançada MikroTik RouterOS
## 04.6 Rotinas de Backup Automatizado (.backup e .rsc)

Um dos erros mais graves de um administrador de redes júnior é salvar apenas o arquivo `.backup` binário da MikroTik. O `.backup` só pode ser restaurado no mesmo modelo de hardware com a mesma versão de firmware. Se a RouterBOARD queimar e precisar ser substituída por outro modelo, o arquivo `.backup` torna-se inútil.

### A Regra Dupla de Backup MikroTik Pulse TI

Todo backup de MikroTik deve obrigatoriamente gerar dois arquivos:
1. **O binário `.backup`:** Restauração rápida 1:1 no mesmo equipamento (preserva senhas criptografadas e certificados).
2. **O script legível `.rsc` (`export compact`):** Export textual em texto limpo de todos os comandos de configuração. Permite importar as configurações em qualquer equipamento substituto, mesmo de modelo ou arquitetura diferente.

### Script de Backup Agendado no RouterOS
```routeros
# ========================================================
# SCRIPT DE EXPORT E BACKUP DIÁRIO PULSE TI
# ========================================================
:local devicename [/system identity get name]
:local sysdate [/system clock get date]
:local datestring ([:pick $sysdate 7 11] . "-" . [:pick $sysdate 0 3] . "-" . [:pick $sysdate 4 6])
:local backupfile ($devicename . "-" . $datestring . ".backup")
:local scriptfile ($devicename . "-" . $datestring . ".rsc")

# Gerar arquivo binário
/system backup save name=$backupfile

# Gerar arquivo de script legível
/export compact file=$scriptfile

:log info ("Backup e Export gerados com sucesso: " . $backupfile)
```
