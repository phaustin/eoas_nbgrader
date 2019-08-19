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
# a) Numpy array can contain words.  You can loop over the elements of a list. Run the code below to display a list of planets.

# %% {"nbgrader": {"schema_version": 3, "solution": true, "grade": true, "locked": false, "task": false, "points": 1, "grade_id": "cell-a42a7f03915765f5"}}
import numpy as np

planets = np.array(['Jupiter', 'Earth', 'Mars', 'Venus', 'Pluto'])

for planet in planets:
    print (planet)

# %% [markdown]
# b) Write a statement in the cell below that will delete the element that does not belong in this list (hint: not a planet).

# %% {"nbgrader": {"schema_version": 3, "solution": true, "grade": false, "locked": false, "task": false, "grade_id": "cell-00cc95148a616c15"}}
### BEGIN SOLUTION
planets = np.delete(planets, 5)
### END SOLUTION
