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

idcol="SIS User ID"
df_canvas = pd.read_csv(context.student_csv)
df_canvas = pd.DataFrame(make_id(df_canvas,idcol),copy=True)
possible_row_canvas = find_possible(df_canvas)
idcol = "Student Number"
df_fsc = pd.read_csv(context.fsc_csv)
df_fsc = pd.DataFrame(make_id(df_fsc,idcol),copy=True)

for the_id,row  in df_canvas.iterrows():
    try:
        canvas_id = f"{int(row['ID']):d}"
        first_name, last_name = df_fsc.loc[the_id]['Preferred Name'], df_fsc.loc[the_id]['Surname']
        student_dict={'first_name':first_name,'last_name':last_name}
        gb.add_student(canvas_id,**student_dict)
    except (KeyError,ValueError):
        print(f"skipping row id {the_id}")

engine_in = dbsql.create_engine(db_name)
with engine_in.begin() as connection:
    df = pd.read_sql_table('student',connection)
print(df.head())
