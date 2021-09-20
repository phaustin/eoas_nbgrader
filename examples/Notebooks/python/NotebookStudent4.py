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
# Question 1
#
# a) pyplot can produce polar graph.  The format to use the method is objectname.method(variable1, variable2).  Enter a statement in the cell below that will create a polar graph.  Please run the code with your statement to display the graph.
#
#

# %% {"nbgrader": {"schema_version": 3, "solution": true, "grade": true, "locked": false, "task": false, "points": 1, "grade_id": "cell-a98f885f7f0fb08f"}}
import numpy as np
import matplotlib.pyplot as plt
cos = np.cos
pi = np.pi

a = 5
e = 0.3
theta = np.linspace(0,2*pi, 360)
r = (a*(1-e**2))/(1+e*cos(theta))
##enter your statement here##

plt.show()

