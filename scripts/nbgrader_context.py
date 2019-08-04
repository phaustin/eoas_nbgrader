"""
http://docs.python-guide.org/en/latest/writing/structure
"""
import os
import site
import sys
from pathlib import Path

curr_dir = Path(__file__).parent
# ~/repos/pythonlibs/diskinventory/notebooks/python/
if curr_dir.name == "python":
    root_dir = curr_dir.parents[1]
else:
    #~/repos/pythonlibs/diskinventory/notebooks
    root_dir = curr_dir.parent
#~/repos/pythonlibs/diskinventory/notebooks/datadir

data_dir = root_dir / 'data'
student_ids = data_dir /  "fakestudentnames.csv"
exchange_dir = root_dir / 'exchange'
assign_db = (root_dir / "gradebook.db").resolve()
sys.path.insert(0, root_dir)

sep = "*" * 30
print(
    (
        f"{sep}\ncontext imported. Front of path:\n"
        f"{sys.path[0]}\n{sys.path[1]}\n{sep}\n"
    )
)
site.removeduppaths()

