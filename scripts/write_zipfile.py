from gradelib.make_zip import write_collect
import nbgrader_context as nc
zipfile = nc.private_dir / 'week2_lab/submissions.zip'
new_zip = nc.private_dir / 'week2_extracted.zip'
assign_name="wk2_lab"
notebook_name="jupyter_intro.ipynb"
write_collect(zipfile, new_zip, assign_name, notebook_name)

