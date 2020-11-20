

def main():

    x_coords = []

    x_lines = ["side 1 G", "side 1 5", "side 1 10", "side 1 15", "side 1 20", "side 1 25", "side 1 30", "side 1 35",
               "side 1 40", "side 1 45", "50", "side 2 45", "side 2 40", "side 2 35", "side 2 30", "side 2 25",
               "side 2 20", "side 2 15", "side 2 10", "side 2 5", "side 2 G"]

    for i, line in enumerate(x_lines):
        if i < 10:
            if i > 0:
                x_coords += ["{0} outside the {1}".format(x, line) for x in range(4, 0, -1)]

            x_coords.append("on the {0}".format(line))
            x_coords += ["{0} inside the {1}".format(x, line) for x in range(1, 4)]
        elif i == 10:
            x_coords += ["{0} outside the {1} on side 1".format(x, line) for x in range(4, 0, -1)]

            x_coords.append("on the {0}".format(line))
            x_coords += ["{0} outside the {1} on side 2".format(x, line) for x in range(1, 5)]
        else:

            x_coords += ["{0} inside the {1}".format(x, line) for x in range(3, 0, -1)]

            x_coords.append("on the {0}".format(line))

            if i + 1 < len(x_lines):
                x_coords += ["{0} outside the {1}".format(x, line) for x in range(1, 5)]

    y_coords = []

    y_coords.append("on the front sideline")
    y_coords += ["{0} behind the front sideline".format(x) for x in range(1, 50)]
    y_coords += ["{0} in front of the front hash".format(x) for x in range(50, 0, -1)]
    y_coords.append("on the front hash")
    y_coords += ["{0} behind the front hash".format(x) for x in range(1, 50)]
    y_coords += ["{0} in front of the back hash".format(x) for x in range(50, 0, -1)]
    y_coords.append("on the back hash")
    y_coords += ["{0} behind the back hash".format(x) for x in range(1, 50)]
    y_coords += ["{0} in front of the back sideline".format(x) for x in range(50, 0, -1)]
    y_coords.append("on the back sideline")

    output = ""

    for x in x_coords:
        for y in y_coords:
            output += "{0}, {1}. \n".format(x, y)

    with open("output.txt", "w") as out:
        out.write(output)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
