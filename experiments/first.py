"""Replay original oracles; do not duplicate the all-k theorem authority."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys,subprocess,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from source import checked_source
src=checked_source()
with TemporaryDirectory() as tmp:
    binary=str(Path(tmp)/'chord-check')
    subprocess.run(['g++','-std=c++17','-O2',str(src/'oracles/c2k/verify_chord_prefix_all8.cpp'),'-o',binary],check=True)
    output=subprocess.check_output([binary],text=True).splitlines()
recurrence=subprocess.check_output([sys.executable,str(src/'oracles/c14/chord_recurrence.py')],text=True).splitlines()
assert 'matchings=2027025 connected=593859 simple=593859 mismatches=0' in output[-2]
assert 'corrected_sigma7: 880865280' in recurrence
print(json.dumps({'domain':'all pairings through k=8; source recurrence through k=10',
    'matching_oracle':output,'recurrence_oracle':recurrence,
    'status':'source replay; k9/k10 recurrence-derived; no Q8 cycle enumeration or new all-k proof'},indent=2))
