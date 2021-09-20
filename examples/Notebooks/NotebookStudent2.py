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

# %% nbgrader={"grade": true, "grade_id": "cell-4d5a82b731481fe7", "locked": false, "points": 1, "schema_version": 3, "solution": true, "task": false}
