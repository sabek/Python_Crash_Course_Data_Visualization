from die import Die
import pygal


num_die = 3

# Create D6
die1 = Die()
die2 = Die()
die3 = Die()

rolls = 50000

# Roll
results = []
for roll_num in range(rolls):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

# analyze results
frequencies = []
max_result = die1.num_sides + die2.num_sides + die3.num_sides

for value in range (num_die, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visual the results
hist = pygal.Bar()

hist.title = "Results of rolling 2 D6 " + str(rolls) + " times."
hist.x_labels = [x for x in range(num_die, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')
