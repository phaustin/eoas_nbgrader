import os
from pathlib import Path

import nbgrader_context as nbcon

gradebook = os.environ["e213_gradebook"]
gradebook = "birwin_gradebook.db"
gradebook = "clm_gradebook.db"

assign_db = nbcon.root_dir / gradebook
exchange_dir = nbcon.root_dir / Path("exchange")

print(f"assignment db is {assign_db}")

c = get_config()  # noqa

c.CourseDirectory.db_url = f"sqlite:///{assign_db}"
c.CourseDirectory.root = str(nbcon.root_dir)
c.ExecutePreprocessor.timeout  = 300

c.Exchange.course_id = "e213"
c.Exchange.root = str(exchange_dir)
print(f"in nbgrader_config.py: setting exchange to {c.Exchange.root}")

# Apply this regular expression to the extracted file filename (absolute path)
c.FileNameCollectorPlugin.named_regexp = (
    r".*_(?P<student_id>\w+)_attempt_" "(?P<file_id>.*)"
)
