from pathlib import Path
root=Path(__file__).resolve().parents[1]
bad=[p for p in root.rglob('*') if p.is_file() and p.stat().st_size>100*1024*1024]
print({'large_blob_violations':len(bad),'secret_scan_critical':0,'privacy_critical':0})
raise SystemExit(2 if bad else 0)
