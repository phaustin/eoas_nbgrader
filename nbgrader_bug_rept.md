---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# EOSC211 NBgrader Workflow

Summary of steps to create EOSC211 course in the nbgrader framework, and bugs along the way (some solved, some not). The goal here is to create a smoothly operating NBgrader workflow where instructors can upload, distribute, collect, autograde, manually grade, and re-distribute assignments. I managed to parse 1 assignment (albeit not smoothly), before opting to start from scratch and build the NBgrader-ized version of the course from the ground up.

The E211 git repository is organized by week, with each folder generally containing 2 worksheets and one laboratory assignment (exceptions for holidays, midterm week, etc.). Worksheets are done in class, on paper, so do not need any autograding. Labs are self contained, meaning that the lab folder contains all the necessary data, image files, and a .ipynb file with the lab assignment. 

**NBgrader Docs:**

https://nbgrader.readthedocs.io/en/stable/index.html

**Contact Info**

andrew.loeppky@gmail.com

+++

### Step 1

Course as it was run in fall 2021 is at https://nbgrader.eoastest.xyz/tree on the `students2021` branch.

```
$ git checkout students2021
```

Note this branch contains real student information, so the hub is password protected and the git repo is not on github, just commit locally (the coursework is backed up elsewhere). The branch `start_from_scratch` contains a made up classlist and has been purged of any real student info/work.

```
$ git checkout start_from_scratch
```

### Step 2

Clear out *everything* except `nbgrader_config.py` and `docker_compose.yml`

### Step 3

Create `classlist.csv` in the following format. Note only the `id` column is required, additional columns may include `last_name`, `first_name`, `email` and nothing else. 

```
id, last_name, first_name
59944305, Turing, Alan
60507264, Rossum, Guido
96512060, Torvalds, Linus
73109324, Wozniak, Steven
```

**Bug:** the csv reader sometimes randomly adds "$\cdot$" characters in the headers for unknown reasons. Solution is to edit the csv in a plain text editor (jupyterhub's text editor works)

### Step 4 

Manually add and remove students. This is a mandatory feature to make sure works because students will inevitably join late or drop the course. Manage students either from the GUI:

`Formgrader` $\rightarrow$ `Manage Students` $\rightarrow$ `+ Add new student`

**Bug:** there is no way to delete students from the GUI...

or from the command line:

```
$ nbgrader db student add <id>
$ nbgrader db student remove <id>
```

**Bug:** you can only remove students that were part of the original `classlist.csv`, not students that were added manually after the fact

### Step 5

Create a directory called `exchange/` in the location specified by `nbgrader_config.py`, and one called `source/`  and `release/`. `source/` is "raw" assignments will go, `release/` is where the student versions go once the metadata has been added. 

**Bug:** the GUI `add new assignment` button just initializes a link to nowhere... 

### Step 6

Time to begin creating assignments. The assumed workflow is to design assignment ipynb's in some other folder and import them into NBgrader. Upload the assignment and all associated files into a folder one level below `source/`. 

**Example:** We have an assignment called `lab_wk2.ipynb`, and image files `open_jhub.png` and `insert_new_cell.png`. Create a folder called `LAB_WK2`, and inside it place `lab_wk2.ipynb`, `open_jhub.png` and `insert_new_cell.png`.

**Bug:** (more of a warning) if your notebooks are paired with MyST, use the `.ipynb`, NOT the `.md` version for generating assignments

### Step 7

Open your assignment on with the nbgrader env active. Then do:

`View` $\rightarrow$ `Cell Toolbar`$\rightarrow$ `Create Assignment`

Use the drop down menus to configure each cell as read only, autograded, or manual graded. More on that here:

https://nbgrader.readthedocs.io/en/stable/user_guide/creating_and_grading_assignments.html

**Note:** NBgrader adds `# YOUR CODE HERE` lines automatically. Some of the E211 assignments contain redundant comments, these should be deleted.

### Step 8

Open the Formgrader tab and press `Generate` (the hat icon). This *should* create the assignment and place it in `release/`

**Bug:** Something is wrong with the filepath, an extra `/./` gets inserted and the released assignment folder tries to land in a directory which does not exist. 


+++

## How it is Supposed to Work

### Assignment Life Cycle

### Step 1 

Develop the assignment. Current iteration of e211 lives at https://github.com/phaustin/eosc211. (Private repo, ask Phil for an invite). Assignments are uploaded here as `.md` files (they are easier to version control), but need to be converted to `.ipynb` using jupytext:

`File` $\rightarrow$ `Jupytext` $\rightarrow$ check both `pair notebook with .ipynb` and `pair notebook with MyST markdown`

Include solutions with the following syntax (case sensitive):

+++

#### Question XX

Create a variable "radius" with a value of 6000

```{code-cell} ipython3
### BEGIN SOLUTION
radius = 6000
### END SOLUTION
```

### Step 2

Upload assignment to NBgrader (https://nbgrader.eoastest.xyz/). Place the .ipynb version of the assignment in the `source/` directory. Select `Manage Assignments` $\rightarrow$ `Release` (hat icon). Assignment now appears in `release/` directory with answers stripped

+++

### Step 3

Distribute assignments to students. Some ambiguity at this stage -- either upload to Canvas for students to download and work on locally, or put the assignment on Jupyterhub. Tools for this at:

https://ubc-dsci.github.io/rudaux/content/preface.html

+++

### Step 4

Students do the assignment and submit via Canvas. Assignments get renamed with unique student identifiers (see `nbgrader_config.py`). Again, this step is somewhat ambiguous, but the completed assignments need to get to the `submitted/` directory.

+++

### Step 5

From `Formgrader`, press `autograde` to autograde each assignment. Graded files will be placed in the `feedback/` directory, organized by student number

```
feedback/12345678/lab1-andrew/lab1.ipynb
                 /lab2-andrew/lab2.ipynb
```

+++

### Step 6

Select `Generate Feedback` to complete the manual grading component of each assignment.

+++

### Step 7

Select `Share Feedback` to copy fully graded files into the `exchange/` directory. They need to get converted to HTML (so graded assignments are un-editable) and uploaded to Canvas where students can see their corrected assignments. Again, [Rudeaux](https://ubc-dsci.github.io/rudaux/content/preface.html) can probably achieve this
