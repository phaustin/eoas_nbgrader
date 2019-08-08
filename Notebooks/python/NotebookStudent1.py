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
#       format_version: '1.2'
#       jupytext_version: 1.2.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---
# %% [markdown]
# Demo Manually graded answer
#
# Please state Newton's three law of motion:
# %% {"nbgrader": {"grade": true, "grade_id": "newton_law_motion", "locked": false, "points": 1, "schema_version": 3, "solution": true, "task": false}}
# %% [markdown]
# Demo Autograded answer
#
# Please write the Linear Momentum formula in the below cell:
# %% [markdown] {"nbgrader": {"grade": false, "grade_id": "momentum_formula", "locked": false, "schema_version": 3, "solution": true, "task": false}}
### BEGIN SOLUTION
# p = mv
### END SOLUTION
# %% [markdown]
# Demo Autograder tests
# %% {"nbgrader": {"grade": true, "grade_id": "cell-d4a12ebfd43a43ba", "locked": true, "points": 1, "schema_version": 3, "solution": false, "task": false}}
### BEGIN HIDDEN TESTS
a = 5
assert a == 5
### END HIDDEN TESTS

# %% [markdown]
# Demo Read-only

# %% {"nbgrader": {"grade": false, "grade_id": "cell-0ab772a9f6f882ef", "locked": true, "schema_version": 3, "solution": false, "task": false}}
a = 1 + 1
assert a == 2

# %% [markdown]
# Manually graded task

# %% [markdown] {"nbgrader": {"grade": true, "grade_id": "cell-f007c5d5b4e88524", "locked": false, "points": 1, "schema_version": 1, "solution": true, "task": true}, "trusted": true}
# Describe the task here!
