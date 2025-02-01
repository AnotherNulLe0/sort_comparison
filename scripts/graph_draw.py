import matplotlib.pyplot as pyplot
from .cfg import DOT_SIZE, COLORS

def plot(efficiency, axes):
    colors = {}
    for func, color in zip(efficiency.keys(), COLORS):
        colors[func] = color
    for key in efficiency:
        # print(f"{key} = {color}")
        line, = axes.plot(efficiency[key][1], efficiency[key][0], color=colors[key])
        axes.scatter(efficiency[key][1], efficiency[key][0], color=colors[key], sizes=(DOT_SIZE,DOT_SIZE))
        line.set_label(key)
        axes.legend()



def draw(sorted_efficiency=None, unsorted_efficiency=None, sorted_memory=None, unsorted_memory=None):

    fig, ax = pyplot.subplots(ncols=2, nrows=2)
    ax1 = ax[0][1]
    ax2 = ax[0][0]
    ax3 = ax[1][0]
    ax4 = ax[1][1]

    ax1.set_ylabel("Время выполнения")
    ax1.set_xlabel("Длина массива")
    ax1.set_title("Отсортированного массива")

    ax2.set_ylabel("Время выполнения")
    ax2.set_xlabel("Длина массива")
    ax2.set_title("Неотсортированного массива")

    ax3.set_ylabel("Затраты памяти")
    ax3.set_xlabel("Длина массива")
    ax3.set_title("Неотсортированного массива")

    ax4.set_ylabel("Затраты памяти")
    ax4.set_xlabel("Длина массива")
    ax4.set_title("Отсортированного массива")

    plot(sorted_efficiency, ax1)
    plot(unsorted_efficiency, ax2)
    plot(unsorted_memory, ax3)
    plot(sorted_memory, ax4)

    slowest_time = max(ax1.get_ylim()[1], ax2.get_ylim()[1])
    ax1.set_ylim(0, slowest_time)
    ax2.set_ylim(0, slowest_time)

    biggest_mem = min(ax3.get_ylim()[1], ax4.get_ylim()[1])
    ax3.set_ylim(0, biggest_mem)
    ax4.set_ylim(0, biggest_mem)

    pyplot.show()
