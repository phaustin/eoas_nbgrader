# ---
# jupyter:
#   celltoolbar: Create Assignment
#   jupytext:
#     cell_metadata_filter: all
#     formats: ipynb,py:percent
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% trusted=true
from numpy.testing import assert_allclose

# %% [markdown] nbgrader={"grade": false, "grade_id": "cell-09bcef57c063b32d", "locked": true, "schema_version": 3, "solution": false, "task": false}
# Excercise 1
#
# a) Create a variable t with a value of 5

# %% nbgrader={"grade": false, "grade_id": "variable", "locked": false, "schema_version": 3, "solution": true, "task": false} trusted=true
# enter you answer below this line
### BEGIN SOLUTION
t = 5
### END SOLUTION

# %% [markdown] nbgrader={"grade": false, "grade_id": "cell-a2a1bee4128b0b73", "locked": true, "schema_version": 3, "solution": false, "task": false}
# b) The code below should run without error

# %% nbgrader={"grade": true, "grade_id": "cell-d4a12ebfd43a43ba", "locked": true, "points": 1, "schema_version": 3, "solution": false, "task": false} trusted=true
s = 10/t
assert_allclose(s, 2.0, rtol=1e-2)
