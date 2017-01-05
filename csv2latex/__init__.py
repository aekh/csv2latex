import sys
import getopt
import csv

from . import help


def main():
    argv = sys.argv[1:]
    inputfile = ''
    outputfile = ''
    delimiter = ','
    quotechar = '\"'
    columns = []
    rows = []
    transpose = False

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
        "transpose"
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
    print(opts)
    print(args)

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
            rows = arg.split(",")
        elif opt in ("-c", "--columns"):
            columns = arg.split(",")
        elif opt in ("-t", "--transpose"):
            transpose = True
    print('Rows: ', rows)
    print('Cols: ', columns)

    if len(opts) == 0 or inputfile == '' or outputfile == '':
        help.help(0)
        sys.exit(2)

    with open(inputfile, 'r') as csvfile:
        csvdata = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        table = list(csvdata)
        if transpose:
            table = map(list, zip(*table))

        for row in table:
            print(' & '.join(row), end="")
            print(" \\\\")

    #outfiles = [outputfile + "-r" str(r) + "-c" + str(r) for r, _ in enumerate(rows)]

    #for r in rows:
    #    for c in columns:


    #except:
    #    print("No such file or directory: " + inputfile)

if __name__ == "__main__":
    main()