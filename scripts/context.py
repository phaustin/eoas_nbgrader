"""
http://docs.python-guide.org/en/latest/writing/structure
"""
import os
import site
import sys
from pathlib import Path

root_dir = Path(__file__).parents[1]
data_dir = root_dir / 'data'
exchange_dir = root_dir / 'exchange'
sys.path.insert(0, root_dir)

sep = "*" * 30
print(
    (
        f"{sep}\ncontext imported. Front of path:\n"
        f"{sys.path[0]}\n{sys.path[1]}\n{sep}\n"
    )
)
site.removeduppaths()

