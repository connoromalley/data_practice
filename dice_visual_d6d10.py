import plotly.express as px

from die import Die

# create two d6
die_1 = Die()
die_2 = Die(10)

# make some rolls, and store results in a list
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
title = "Results of rolling a d6 and d10 50,000 times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# further customize chart
fig.update_layout(xaxis_dtick=1)

fig.show()

# save figure
# fig.write_html('dice_visual_d6d10.html')