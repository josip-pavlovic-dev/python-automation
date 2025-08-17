#ENG: Put project root on sys.path so `from src...` works in tests
#SR : Dodaj koren projekta na sys.path da `from src...` radi u testovima

from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
