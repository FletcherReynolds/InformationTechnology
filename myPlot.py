import matplotlib.pyplot as plt

xlist = [10, 25, 28, 60, 20, 66, 69, 34, 16, 34]
ylist = ['joe', 'sam', 'alexa', 'yuri', 'graham', 'scott', 'morgan', 'greg', 'wallace', 'jay']

plt.xlabel('This is X')
plt.ylabel('This is Y')

plt.title('This is a plot')

plt.pie(xlist)

plt.show()