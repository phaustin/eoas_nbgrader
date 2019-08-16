# ---
# jupyter:
#   celltoolbar: Create Assignment
#   jupytext:
#     cell_metadata_filter: all
#     formats: ipynb,python//py:percent
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
# %% [markdown] {"nbgrader": {"grade": false, "grade_id": "cell-996c240bfb4138d2", "locked": true, "schema_version": 3, "solution": false, "task": false}}
# Exercise 2
#
# a) Run the below code to see the plot.
# %% {"scrolled": true}
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(
    xlabel="time (s)", ylabel="voltage (mV)", title="About as simple as it gets, folks"
)
ax.grid()

# %% [markdown] {"nbgrader": {"grade": false, "grade_id": "cell-e0cf901f2000dc5c", "locked": true, "schema_version": 3, "solution": false, "task": false}}
# b) What is the maximum voltage at time 0.25?  Write your answer in the cell below.

# %% {"nbgrader": {"grade": true, "grade_id": "cell-4d5a82b731481fe7", "locked": false, "points": 2, "schema_version": 3, "solution": true, "task": false}}
