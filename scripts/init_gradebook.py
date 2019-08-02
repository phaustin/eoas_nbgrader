import pprint

import nbgrader
import numpy as np
import pandas as pd
from nbgrader.apps import NbGraderAPI
from traitlets.config import Config
from context import data_dir, exchange_dir

# create a custom config object to specify options for nbgrader
config = Config()
config.Exchange.course_id = "course101"
config.Exchange.root = str(exchange_dir)

api = NbGraderAPI(config=config)


df_gradebook = pd.read_csv(data_dir / 'fakestudentnames.csv')

the_grades = nbgrader.api.Gradebook("sqlite:///grades.db")

# # print(df_merged)

# for row in df_merged.iterrows():
#     the_dict = row[1].to_dict()
#     values = row[1][["ID", "Surname", "Preferred Name", "SIS User ID"]].to_dict()
#     new_dict = {}
#     rename = [
#         ("ID", "the_id"),
#         ("Surname", "last_name"),
#         ("Preferred Name", "first_name"),
#     ]
#     for old, new in rename:
#         new_dict[new] = values[old]
#     the_id = new_dict["the_id"]
#     del new_dict["the_id"]
#     the_grades.add_student(the_id, **new_dict)

#     pprint.pprint(new_dict)

# students = the_grades.students
# print(students)
# the_grades.close()

# # pdb.set_trace()
