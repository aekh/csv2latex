"""
Help text output
"""


def help(level):
    assert level >= 0
    if level >= 0:
        print("Usage: csv2latex -i <inputfile> -o <outputfile> [options]")
    if level == 0:
        print("\nFor more help, try: csv2latex -h")
    if level >= 1:
        print("\nOptions:\n"
              "  -h, --help \t\t Show available options\n"
              "  --more-help \t\t Show instructional help\n"
              "\n"
              "  -t, --transpose \t Transpose the CSV before splitting\n"
              "  --transpose-after \t Transpose after splitting \n"
              "                    \t (equivalent to -t if no splits)\n"
              "  --transpose-individual Step by step determine if the table should be\n"
              "                         transposed or not (Not available)\n"
              "  -r, -rows <rows> \t Indicate at which rows to split and start a new table\n"
              "  -c, -columns <colums> \t Indicate at which columns to split and start\n"
              "              \t\t a new table\n"
              "\n"
              "  -l, --literal \t Do not escape LaTeX syntax (Not available)\n"
              "  -p, --print \t\t Print resulting LaTeX table(s) to terminal instead\n"
              "              \t\t of to file. Ignores -o option")
    if level >= 2:
        print("\nInstructions:\n"
              "  -r 3,5,6 \t\t Splits into four row partitions\n"
              "           \t\t 0 to 2, 3 to 4, only row 5, and 6 to the final row")
        print("\nFor further help, visit https://github.com/aekh/csv2latex/wiki")
    if level > 0:
        print("\nReport bugs at https://github.com/aekh/csv2latex/issues.")