"""
Use Pygal to make an interactive SGV file of a histogram
of many trials of rolling dice
"""

from pygal import Bar

from die import Die

die1 = Die()
die2 = Die()

num_possible_results = die1.num_sides + die2.num_sides
frequencies: list[int] = [0] * num_possible_results

# Frequency analysis
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    frequencies[result] += 1

# Visualize the results using a pygal histogram
hist = Bar()

hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = [str(x) for x in range(1, num_possible_results + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D6', frequencies)

hist.render_to_file('dice_visual.svg')
