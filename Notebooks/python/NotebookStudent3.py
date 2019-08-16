# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# Excercise Playing with pyplot
#
# a) In the below code, insert a statement that will generate a plot from the following data:
#
# [1,2,3,4],[9,4,9,16]
#
# Go here (https://matplotlib.org/) to read more about Matplotlib.
#
# After inserting the statement, run the code to display the plot.
#

# %% {"nbgrader": {"schema_version": 3, "solution": true, "grade": true, "locked": false, "task": false, "points": 1, "grade_id": "cell-e96f567728b7bd7d"}}
import matplotlib.pyplot as plt
##insert your statement here##
plt.xlabel ('X')
plt.ylabel('Y')
plt.show()


# %% [markdown]
# b) Run the below code.  Nothing should be displayed.

# %% {"nbgrader": {"schema_version": 3, "solution": true, "grade": false, "locked": false, "task": false, "grade_id": "cell-f409ae4c0190c596"}}
import numpy as np  
import matplotlib.pyplot as plt  
def graph(formula, x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y)  
    plt.show()

# %% [markdown]
# c) Now run the following statement: graph('X', range(-10, 11)) in the cell below replacing x with any formula that you like.  For example, replace x with 'x**3+2*x-3'.
#
# This statement call the above script and insert a formula to be plotted.

# %% {"nbgrader": {"schema_version": 3, "solution": false, "grade": false, "locked": true, "task": true, "points": 1, "grade_id": "cell-fe5be254a7580a61"}}

# %%
