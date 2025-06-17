import os
import zipfile
import hashlib
import shutil
import mimetypes
import stat
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import datetime

# === CONFIGURATION ===
ZIP_DIR = "./zips"
EXTRACT_DIR = "./extracted_zips"
AUDIT_DIR = "./Sovereign_Audit_Organized"
AUDIT_LOG = os.path.join(AUDIT_DIR, "gTek_KeyAuditLog.txt")
ENV_KEY_VAR = "GTEK_MASTER_KEY"

load_dotenv()

def get_key():
    key = os.getenv(ENV_KEY_VAR)
    return Fernet(key.encode())

def decrypt_pass(enc_path, fernet):
    with open(enc_path, 'rb') as f:
        return fernet.decrypt(f.read()).decode()

def extract_zips():
    os.makedirs(EXTRACT_DIR, exist_ok=True)
    for file in os.listdir(ZIP_DIR):
        if file.endswith(".zip"):
            with zipfile.ZipFile(os.path.join(ZIP_DIR, file), 'r') as zip_ref:
                zip_ref.extractall(EXTRACT_DIR)

def file_permissions(path):
    try:
        return oct(os.stat(path).st_mode)[-3:]
    except Exception:
        return "???"

def organize_file(path):
    type_folder = mimetypes.guess_type(path)[0]
    type_folder = type_folder.split('/')[0] if type_folder else os.path.splitext(path)[1].lower().replace('.', '') or "unknown"
    target_dir = os.path.join(AUDIT_DIR, type_folder)
    os.makedirs(target_dir, exist_ok=True)
    shutil.copy2(path, os.path.join(target_dir, os.path.basename(path)))

def audit_files():
    os.makedirs(AUDIT_DIR, exist_ok=True)
    with open(AUDIT_LOG, 'a') as log:
        log.write(f"\n\nAudit Log: {datetime.datetime.now()}\n{'='*70}\n")
        for root, _, files in os.walk(EXTRACT_DIR):
            for f in files:
                path = os.path.join(root, f)
                try:
                    size = os.path.getsize(path)
                    sha = hashlib.sha256(open(path, 'rb').read()).hexdigest()
                    created = datetime.datetime.fromtimestamp(os.path.getctime(path)).isoformat()
                    modified = datetime.datetime.fromtimestamp(os.path.getmtime(path)).isoformat()
                    filetype, _ = mimetypes.guess_type(path)
                    perms = file_permissions(path)

                    log.write(
                        f"{path}\n"
                        f" ├─ Size: {size} bytes\n"
                        f" ├─ SHA-256: {sha}\n"
                        f" ├─ Created: {created}\n"
                        f" ├─ Modified: {modified}\n"
                        f" ├─ Type: {filetype or 'unknown'}\n"
                        f" └─ Permissions: {perms}\n\n"
                    )
                    organize_file(path)
                except Exception as e:
                    log.write(f"[ERROR] Failed to audit {path}: {str(e)}\n")

if __name__ == "__main__":
    extract_zips()
    audit_files()
    print("Audit complete. Log saved to:", AUDIT_LOG)
