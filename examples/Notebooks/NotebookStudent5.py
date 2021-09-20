# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
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

# %% [markdown]
# Question 1
#
# a) Numpy array can contain words.  You can loop over the elements of a list. Run the code below to display a list of planets.

# %% nbgrader={"grade": true, "grade_id": "cell-a42a7f03915765f5", "locked": false, "points": 1, "schema_version": 3, "solution": true, "task": false}
import numpy as np

planets = np.array(['Jupiter', 'Earth', 'Mars', 'Venus', 'Pluto'])

for planet in planets:
    print (planet)

# %% [markdown]
# b) Write a statement in the cell below that will delete the element that does not belong in this list (hint: not a planet).

# %% nbgrader={"grade": false, "grade_id": "cell-00cc95148a616c15", "locked": false, "schema_version": 3, "solution": true, "task": false}
### BEGIN SOLUTION
planets = np.delete(planets, 4)
### END SOLUTION
