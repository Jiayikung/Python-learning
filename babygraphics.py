"""
File: babygraphics.py
Name: Doris Kung
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]  # File names for baby data
CANVAS_WIDTH = 1000  # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600  # Height of drawing canvas in pixels
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,  # The years to be displayed
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20  # The margin size between the canvas edge and the graph line
COLORS = ['red', 'purple', 'green', 'blue']  # The color of the line
TEXT_DX = 2  # The distance between the text and the line
LINE_WIDTH = 2  # The width of the line
MAX_RANK = 1000  # The maximum rank of the baby name


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE + (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS) * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # draw the lower horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # draw the upper horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)   
    # draw the vertical lines
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    # draw the lines
    for i, name in enumerate(lookup_names):
        if name in name_data:
            for j, year in enumerate(YEARS):
                x = get_x_coordinate(CANVAS_WIDTH, j)
                if str(YEARS[j]) in name_data[name]:  # if the year is in the name_data[name]
                    y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK * int(name_data[name][str(year)])  # calculate the y coordinate
                    canvas.create_text(x + TEXT_DX, y, text=name + ' ' + name_data[name][str(year)], anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
                else:  # if the year is not in the name_data[name]
                    y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_text(x + TEXT_DX, y, text=name + ' *', anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
                if j != len(YEARS) - 1:  # if the year is the last year
                    x2 = get_x_coordinate(CANVAS_WIDTH, j+1)
                    if str(YEARS[j+1]) in name_data[name]:
                        y2 = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK * int(name_data[name][str(YEARS[j+1])])
                        canvas.create_line(x, y, x2, y2, width=LINE_WIDTH, fill=COLORS[i % len(COLORS)])
                    else:
                        y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                        canvas.create_line(x, y, x2, y2, width=LINE_WIDTH, fill=COLORS[i % len(COLORS)])
        

# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
