import sys 
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
import pytest 
from calculator.core import add, subtract, multiplyy