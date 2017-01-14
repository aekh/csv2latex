from __future__ import print_function
import sys
import getopt
import csv
import os

from . import help, table

VERSION = "1.0.0"

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
    print_mode = False

    short_names = "h" \
                 "t" \
                 "p" \
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
        #"transpose-individual",
        "infile=",
        "outfile=",
        "print",
        "rows=",
        "columns=",
        "version"
    ]

    try:
        opts, args = getopt.getopt(argv,short_names,long_names)
    except getopt.GetoptError as err:
        print(str(err))
        help.help(0)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help.help(1)
            sys.exit()
        if opt == '--more-help':
            help.help(2)
            sys.exit()
        elif opt == '--version':
            print("Current version of csv2latex is " + VERSION)
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
                rows = [0] + list(map(int,arg.split(",")))
            except ValueError:
                print("option -r <rows> takes numbers separated by commas")
        elif opt in ("-c", "--columns"):
            try:
                columns = [0] + list(map(int, arg.split(",")))
            except ValueError:
                print("option -c <columns> takes numbers separated by commas")
        elif opt in ("-t", "--transpose"):
            transpose_before = True
        elif opt == "--transpose-after":
            if not transpose_individual:
                transpose_after = True
        #elif opt in ("--transpose-individual"):
        #    transpose_individual = True
        #    transpose_after = False
        elif opt in ('-p', '--print'):
            print_mode = True

    if len(opts) == 0 or inputfile == '' or (outputfile == '' and not print_mode):
        help.help(0)
        sys.exit(2)

    with open(inputfile, 'r') as csvfile:
        csvdata = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        matrix = list(csvdata)
        if transpose_before:
            matrix = list(map(list, zip(*matrix)))

    tables = []

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
                    tables.append(
                        table.Table(
                            slicer(matrix, srow=srow, erow=erow, scol=scol, ecol=ecol),
                            row + 1,
                            col + 1,
                            transpose_after
                        )
                    )
            else: # len(columns) = 1
                tables.append(
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
                tables.append(
                    table.Table(
                        slicer(matrix, scol=scol, ecol=ecol),
                        None,
                        col + 1,
                        transpose_after
                    )
                )
        else: # len(columns) = 1
            tables = [table.Table(matrix, None, None, transpose_after)]

    if not print_mode and len(tables) > 1:
        outputfile_base = os.path.splitext(outputfile)[0]
        outputfile_ext = os.path.splitext(outputfile)[1]
        outputfiles = ["" for _ in range(len(tables))]

        for i in range(len(tables)):
            outputfiles[i] = outputfile_base + "-" + str(i) + outputfile_ext

        print("The following files will be written:")
        if len(tables) > 3:
            print(outputfiles[0] + ", " + outputfiles[1] + ", ..., " + outputfiles[-1])
        else:
            for out in outputfiles:
                print(out, end=", ")
            print("")

        ans = ""
        while ans not in ('y', 'n'):
            ans = input("Do you want to continue? (y/n): ")

        if ans == 'n':
            sys.exit()

        for i in range(len(tables)):
            f = open(outputfiles[i], 'w')
            f.write(tables[i].write())
            f.close()

    else: # print_mode == True
        for tab in tables:
            print(tab.write())

def slicer(matrix, srow=0, erow=None, scol=0, ecol=None):
    if erow is None:
        erow = len(matrix)
    if ecol is None and len(matrix) > 0:
        ecol = len(matrix[1])
    return [row[scol:ecol] for row in matrix[srow:erow]]


if __name__ == "__main__":
    main()
