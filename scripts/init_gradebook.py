"""
read a csv file with student ids and create the gradebook.db
"""
from nbgrader.api import Gradebook
import nbgrader_context as context
import sqlalchemy as dbsql
import pandas as pd
from gradelib.utils import make_canvas_index, make_id, find_possible
from gradelib.utils import calc_grades, merge_two, make_upload



db_name=f'sqlite:///{str(context.gradebook_db)}'
print(f'data base is {db_name}')

if context.gradebook_db.is_file():
    context.gradebook_db.unlink()

gb = Gradebook(db_name)

student_df = pd.read_csv(context.student_csv,index_col="ID")
print(student_df.head())
for the_id,first_name,last_name in student_df.to_records():
    student_dict={'first_name':first_name,'last_name':last_name}
    str_id = f"{the_id}"
    gb.add_student(str_id,**student_dict)

engine_in = dbsql.create_engine(db_name)
with engine_in.begin() as connection:
    df = pd.read_sql_table('student',connection)
print(df.head())
