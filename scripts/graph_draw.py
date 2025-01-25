import matplotlib.pyplot as pyplot
from utils import SORTING_FUNCTIONS

def plot(efficiency, axes):
    colors = {}
    for func, color in zip(SORTING_FUNCTIONS, [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 0.88, 0), (0.65, 0.2, 0.75), (0, 1, 1), (0, 0, 0)]):
        colors[func.__name__] = color
    for key in efficiency:
        # print(f"{key} = {color}")
        line, = axes.plot(efficiency[key][1], efficiency[key][0], color=colors[key])
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
