import matplotlib.pyplot as pyplot
from .cfg import SORTING_FUNCTIONS, DOT_SIZE, COLORS

def plot(efficiency, axes):
    colors = {}
    for func, color in zip(SORTING_FUNCTIONS, COLORS):
        colors[func.__name__] = color
    for key in efficiency:
        # print(f"{key} = {color}")
        line, = axes.plot(efficiency[key][1], efficiency[key][0], color=colors[key])
        axes.scatter(efficiency[key][1], efficiency[key][0], color=colors[key], sizes=(DOT_SIZE,DOT_SIZE))
        line.set_label(key)
        axes.legend()



def draw(sorted_efficiency=None, unsorted_efficiency=None):

    fig, ax = pyplot.subplots(ncols=2, nrows=1)

    ax[0].set_ylabel("Время выполнения")
    ax[0].set_xlabel("Длина массива")
    ax[0].set_title("Неотсортированного массива")

    ax[1].set_ylabel("Время выполнения")
    ax[1].set_xlabel("Длина массива")
    ax[1].set_title("Отсортированного массива")

    plot(unsorted_efficiency, ax[0])
    plot(sorted_efficiency, ax[1])

    slowest_time = max(ax[0].get_ylim()[1], ax[1].get_ylim()[1])
    ax[0].set_ylim(0, slowest_time)
    ax[1].set_ylim(0, slowest_time)

    pyplot.show()
