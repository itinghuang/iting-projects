"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

To search the name in the database and print out all ranks of the name.
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
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    column = (width-2*GRAPH_MARGIN_SIZE)/len(YEARS) #the column calculated the average width
    x_coordinate = GRAPH_MARGIN_SIZE+column*year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas
    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        index = get_x_coordinate(CANVAS_WIDTH, i) #the x coordinate of every index
        canvas.create_line(index, GRAPH_MARGIN_SIZE,index, CANVAS_HEIGHT)
        canvas.create_text(index+TEXT_DX,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text= YEARS[i],anchor=tkinter.NW)
    canvas.create_line(CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)


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
    draw_fixed_lines(canvas) # draw the fixed background grid
    # Write your code below this line
    #################################
    for i in range(len(lookup_names)): # check every names in lookup_names
        name = lookup_names[i]
        if i > len(COLORS)-1:
            aa = i % len(COLORS) #the remainder of tha number of colors will decide the color of every name
            color = COLORS[aa]
        else:
            color = COLORS[i] #the index is smaller than the number of colors
        for j in range(len(YEARS)): #check every years in the dict of same name
            if j < (len(YEARS)-1): #if j is not the last year
                year = str(YEARS[j])
                year2 = str(YEARS[j+1])
                index = get_x_coordinate(CANVAS_WIDTH,j) #the x coodrinate of the first year
                if year in name_data[name]:
                    rank = int(name_data[name][year])
                    rank_position = rank*(CANVAS_HEIGHT/MAX_RANK)+GRAPH_MARGIN_SIZE #the position was shorted in canvas
                    name_card = [name, rank] #set the name card to print in the graph
                else:
                    rank_position = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE #if cannot found, put the graph in the bottom
                    name_card = [name, '*']
                index2 = get_x_coordinate(CANVAS_WIDTH, j+1) #the x coodrinate of the second year
                if year2 in name_data[name]:
                    rank2 = int(name_data[name][year2])
                    rank2_position = rank2*(CANVAS_HEIGHT/MAX_RANK)+GRAPH_MARGIN_SIZE #the shorten position
                else:
                    rank2_position = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                canvas.create_line(index, rank_position,index2, rank2_position, width = LINE_WIDTH, fill=color)
                canvas.create_text(index + TEXT_DX, rank_position, text=name_card, anchor=tkinter.SW, fill=color)
            else: # draw the last year, the last year will show the first coordinate only
                year = str(YEARS[j])
                index = get_x_coordinate(CANVAS_WIDTH, j)
                if year in name_data[name]:
                    rank = int(name_data[name][year])
                    rank_position = rank*(CANVAS_HEIGHT/MAX_RANK)+GRAPH_MARGIN_SIZE
                    name_card = [name, rank]
                else:
                    rank_position = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    name_card = [name, '*']
                canvas.create_text(index + TEXT_DX, rank_position, text=name_card, anchor=tkinter.SW, fill=color)


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
