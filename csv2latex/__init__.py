import sys
import getopt
import csv

from . import help, table


def main():
    argv = sys.argv[1:]
    inputfile = ''
    outputfile = ''
    delimiter = ','
    quotechar = '\"'
    columns = []
    rows = []
    transpose_before = False
    transpose_after = False
    transpose_individual = False

    short_names = "h" \
                 "t" \
                 "i:" \
                 "o:" \
                 "d:" \
                 "q:" \
                 "r:" \
                 "c:"

    long_names = [
        "help",
        "more-help",
        "transpose",
        "transpose-after",
        "transpose-individual",
        "infile=",
        "outfile=",
        "rows=",
        "columns="
    ]

    try:
        opts, args = getopt.getopt(argv,short_names,long_names)
    except getopt.GetoptError as err:
        print(str(err))
        help.help(0)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            help.help(1)
            sys.exit()
        if opt == '--more-help':
            help.help(2)
            sys.exit()
        elif opt in ("-i", "--infile"):
            inputfile = arg
        elif opt in ("-o", "--outfile"):
            outputfile = arg
        elif opt in ("-d", "--delimiter"):
            delimiter = arg
        elif opt in ("-q", "--quotechar"):
            quotechar = arg
        elif opt in ("-r", "--rows"):
            try:
                rows  = [0] + list(map(int,arg.split(",")))
            except ValueError:
                print("option -r <rows> takes numbers separated by commas")
        elif opt in ("-c", "--columns"):
            try:
                columns = [0] + list(map(int, arg.split(",")))
            except ValueError:
                print("option -c <columns> takes numbers separated by commas")
        elif opt in ("-t", "--transpose"):
            transpose_before = True
        elif opt in ("--transpose-after"):
            if transpose_individual == False:
                transpose_after = True
        elif opt in ("--transpose-individual"):
            transpose_individual = True
            transpose_after = False

    if len(opts) == 0 or inputfile == '' or outputfile == '':
        help.help(0)
        sys.exit(2)

    with open(inputfile, 'r') as csvfile:
        csvdata = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        matrix = list(csvdata)
        if transpose_before:
            matrix = map(list, zip(*matrix))

    Tables = []

    if len(rows) > 1:
        for row in range(len(rows)):
            srow = rows[row]
            if row + 1 == len(rows):
                erow = None
            else:
                erow = rows[row + 1]
            if len(columns) > 1:
                for col in range(len(columns)):
                    scol = columns[col]
                    if col + 1 == len(columns):
                        ecol = None
                    else:
                        ecol = columns[col + 1]
                    Tables.append(
                        table.Table(
                            slicer(matrix, srow=srow, erow=erow, scol=scol, ecol=ecol),
                            row + 1,
                            col + 1,
                            transpose_after
                        )
                    )
            else: # len(columns) = 1
                Tables.append(
                    table.Table(
                        slicer(matrix, srow=srow, erow=erow),
                        row + 1,
                        None,
                        transpose_after
                    )
                )
    else: # len(row) = 1
        if len(columns) > 1:
            for col in range(len(columns)):
                scol = columns[col]
                if col + 1 == len(columns):
                    ecol = None
                else:
                    ecol = columns[col + 1]
                Tables.append(
                    table.Table(
                        slicer(matrix, scol=scol, ecol=ecol),
                        None,
                        col + 1,
                        transpose_after
                    )
                )
        else: # len(columns) = 1
            Tables = [table.Table(matrix, None, None, transpose_after)]

    for tab in Tables:
        tab.write(outputfile)


def slicer(matrix, srow=0, erow=None, scol=0, ecol=None):
    if erow == None:
        erow = len(matrix)
    if ecol == None and len(matrix) > 0:
        ecol = len(matrix[1])
    return [row[scol:ecol] for row in matrix[srow:erow]]


if __name__ == "__main__":
    main()