from nbgrader.api import Gradebook
import nbgrader_context as context
import sqlalchemy as dbsql
import pandas as pd

db_name=f'sqlite:///{str(context.assign_db)}'
print(f'data base is {db_name}')

if context.assign_db.is_file():
    context.assign_db.unlink()

gb = Gradebook(db_name)


student_df = pd.read_csv(context.student_ids,index_col="ID")

for the_id,first_name,last_name in student_df.to_records():
    student_dict={'first_name':first_name,'last_name':last_name}
    str_id = f"{the_id}"
    gb.add_student(str_id,**student_dict)

engine_in = dbsql.create_engine(db_name)
with engine_in.begin() as connection:
    df = pd.read_sql_table('student',connection)
print(df.head())
