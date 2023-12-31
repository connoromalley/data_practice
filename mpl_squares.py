import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

#plt.style.use('seaborn') why doesnt this work??

fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, color='green', s=10)
#ax.scatter(x_values, y_values, color=(0,0.3, .3), s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
#ax.plot(input_values, squares, linewidth=3)

# set chart title and lable axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)


# set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain') # this allows you to override default y axis


# set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()


#save plot with this command:
plt.savefig('squares_plot.png', bbox_inches='tight')

