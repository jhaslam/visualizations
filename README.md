# Studies in Python Graphing and Visualization
This is my personal workspace to try out data visualization libraries
in Python. The libraries featured are matplotlib and pygal.

## Project Configuration Instructions
- Install Python >= 3.9
- `python -m venv project_env`
- `./project_env/Scripts/activate`
- `pip install -r requirements.txt`


## `mpl_squares.py`

![screenshot](docs/mpl_squares.png)

Demonstrates one of the most basic uses of matplotlib. This is essentially
a HelloWorld of this graphing library.  

To run:  
`python mpl_squares.py`


## `rw_visual.py`

![screenshot](docs/rw_visual.png)

Visualizes a random walk using the gradient feature of matplotlib.  
  
To run:  
`python rw_visual.py`


## `dice_visual.py`

<img src="docs/dice_visual.svg" width="400">

Use Pygal to make an interactive SGV file of a histogram
of many trials of rolling dice

To run:  
`python dice_visual.py`


## `highs_lows.py`

![screenshot](docs/highs_lows.png)

Reads data in CSV format and plots it out using matplotlib pyplot

To run:  
`python highs_lows.py`


## `world_polulation.py`

<img src="docs/world_population.svg" width="400">

Uses pygal to make an interactive SVG of world population by country.

To run:  
`python -m population`


## `python_repos.py`

<img src="docs/python_repos.svg" width="400">

Uses the GitHub public API to chart the most starred public Python repos

To run:  
`python -m apis/python_repos.py`