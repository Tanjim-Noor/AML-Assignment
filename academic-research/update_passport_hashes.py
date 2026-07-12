"""Refresh SHA-256 values for existing relative Research Passport artifacts."""

import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PASSPORT = ROOT / "academic-research/research-passport.yaml"
lines = PASSPORT.read_text(encoding="utf-8").splitlines()

current_path: Path | None = None
updates = 0
for index, line in enumerate(lines):
    match = re.match(r'^(\s*)path:\s*"([^"]+)"\s*$', line)
    if match:
        raw = match.group(2)
        candidate = Path(raw)
        current_path = None if candidate.is_absolute() else ROOT / candidate
        continue
    hash_match = re.match(r'^(\s*)sha256:\s*"[0-9a-fA-F]+"\s*$', line)
    if hash_match and current_path and current_path.is_file():
        value = hashlib.sha256(current_path.read_bytes()).hexdigest()
        lines[index] = f'{hash_match.group(1)}sha256: "{value}"'
        updates += 1
        current_path = None

PASSPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
print(f"Updated {updates} relative artifact hashes")
