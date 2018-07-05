import os
import sys
path_abs=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path_abs)
from core import src
if __name__ == '__main__':
    src.run()