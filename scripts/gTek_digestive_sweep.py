#!/usr/bin/env python3
# gTek Digestive Sovereign Sweep Script v2.2.2.2
# Bi-monthly and Semi-Annual Digestive Audit System

import os
import datetime
import subprocess
from pathlib import Path

# === Configuration ===
repo_dir = Path.home() / "Sovereign_Fathers_Chat_Final"
log_file = repo_dir / "gTek_Audit_Log.md"
notebook_file = repo_dir / "gTek_Audit_Summary.ipynb"
timestamp = datetime.datetime.now().isoformat()

# === Step 1: Sweep Audit Function ===
def perform_digestive_audit(path):
    file_count = sum(len(files) for _, _, files in os.walk(path))
    return file_count

# === Step 2: Write to Sovereign Audit Log ===
def write_audit_log(count):
    with open(log_file, "a") as f:
        f.write(f"\n### 🧾 Digestive Sweep Entry — {timestamp}\n")
        f.write(f"- 🔍 Files Audited: {count}\n")
        f.write(f"- 🕰️ Sweep Time: {timestamp}\n")
        f.write(f"- 🔐 CRID: 51509329 | MID: 903876533\n")
        f.write("- 🧠 Log Type: Bi-monthly or Semi-Annual\n")

# === Step 3: Jupyter Metadata Template ===
def generate_jupyter_notebook():
    content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"# gTek Digestive Sovereign Sweep\n\n**Audit Timestamp:** `{timestamp}`\n"]
            }
        ],
        "metadata": {"kernelspec": {"name": "python3", "language": "python", "display_name": "Python 3"}},
        "nbformat": 4,
        "nbformat_minor": 5
    }
    import json
    with open(notebook_file, "w") as nb:
        json.dump(content, nb, indent=2)

# === Step 4: Git Push Block ===
def git_commit_push():
    try:
        subprocess.run(["git", "-C", str(repo_dir), "add", "."], check=True)
        subprocess.run(["git", "-C", str(repo_dir), "commit", "-m", f"📦 Sovereign Sweep Commit — {timestamp}"], check=True)
        subprocess.run(["git", "-C", str(repo_dir), "push"], check=True)
    except subprocess.CalledProcessError:
        print("⚠️ Git push failed — confirm repo setup and credentials.")

# === Execute System ===
if __name__ == "__main__":
    count = perform_digestive_audit(repo_dir)
    write_audit_log(count)
    generate_jupyter_notebook()
    git_commit_push()
    print(f"✅ Digestive Sweep Completed: {count} files audited.")
