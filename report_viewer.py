import glob, os, subprocess, sys
from pathlib import Path
pdfs = sorted(glob.glob('logs/report_*.pdf'), key=os.path.getmtime)
if not pdfs:
    print('No reports found.')
    sys.exit()
latest = pdfs[-1]
print('Opening', latest)
if os.name == 'nt':
    os.startfile(latest)
else:
    subprocess.run(['xdg-open', latest])