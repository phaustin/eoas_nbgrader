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
# Excercise 1
#
# a) Run the below code to see the plot.

# %%
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

# %% [markdown]
# b) What is the maximum voltage at time 0.25?  Write your answer in the cell below.

# %% {"nbgrader": {"schema_version": 3, "solution": true, "grade": true, "locked": false, "task": false, "points": 1, "grade_id": "cell-4d5a82b731481fe7"}}
