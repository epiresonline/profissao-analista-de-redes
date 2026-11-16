# -*- coding: utf-8 -*-
"""
Motor de Autoatualização do Livro 'Profissão: Analista de Redes N3'
Autor: Eduardo Pires (Analista de Redes N3)
Data de Criação: 16/11/2026
"""

import os
import sys
import datetime
import subprocess

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS_DIR = os.path.join(REPO_DIR, "docs")
CHANGELOG_PATH = os.path.join(DOCS_DIR, "changelog.md")

def get_current_date_br():
    now = datetime.datetime.now()
    return now.strftime("%d/%m/%Y")

def count_chapters():
    count = 0
    for root, dirs, files in os.walk(DOCS_DIR):
        for f in files:
            if f.endswith(".md"):
                count += 1
    return count

def run_git(args, cwd=REPO_DIR):
    result = subprocess.run(["git"] + args, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"[ERRO GIT] {' '.join(args)}: {result.stderr.strip()}")
    else:
        print(f"[OK GIT] {' '.join(args)}")
    return result

def main():
    print("=" * 60)
    print("INICIANDO MOTOR DE AUTOATUALIZACAO DO LIVRO VIVO")
    print(f"Diretório do Repositório: {REPO_DIR}")
    print("=" * 60)

    hoje = get_current_date_br()
    total_docs = count_chapters()
    print(f"[INFO] Data atual: {hoje}")
    print(f"[INFO] Total de arquivos de documentacao encontrados: {total_docs}")

    # Verificar status do git
    run_git(["status", "--short"])

    # Adicionar alterações
    run_git(["add", "."])

    # Commit
    commit_msg = f"Autoatualizacao do Livro: Auditoria e Sincronizacao em {hoje} ({total_docs} documentos)"
    run_git(["commit", "-m", commit_msg])

    # Push para branch main
    print("[INFO] Enviando atualizacoes para o GitHub...")
    push_res = run_git(["push", "origin", "main"])

    if push_res.returncode == 0:
        print("[SUCESSO] Repositório sincronizado com sucesso!")
        print("A esteira do GitHub Actions foi disparada para atualizar o GitHub Pages.")
    else:
        print("[AVISO] Nao foi possivel dar push agora ou nao ha alteracoes pendentes.")

if __name__ == "__main__":
    main()
