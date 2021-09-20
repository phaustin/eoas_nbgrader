"""
http://docs.python-guide.org/en/latest/writing/structure
"""
import os
import site
import sys
from pathlib import Path

curr_dir = Path(__file__).parent
root_dir = curr_dir.parent
print(f"{root_dir.resolve()=}")
private_dir = root_dir / "e211_files"
student_csv = list(private_dir.glob("*19T1135*csv"))[0]
print(f"{str(student_csv)=}")
exchange_dir = root_dir / 'exchange'

gradebook_db = (root_dir / "gradebook.db").resolve()



