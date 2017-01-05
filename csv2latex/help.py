"""
Help text output
"""


def help(level):
    assert level >= 0
    if level >= 0:
        print("Usage: csv2latex -i <inputfile> -o <outputfile> [options]")
    if level == 0:
        print("\nFor more help, type: csv2latex -h")
    if level >= 1:
        print("\nOptions:\n"
              "  -h, --help \t\t Show available options\n"
              "  --more-help \t\t Show instructional help\n"
              "\n"
              "  -r=\"<rows>\" \t\t asdf \n"
              "  -l, --literal \t Do not escape LaTeX syntax")
    if level >= 2:
        print("\nInstructions:\n"
              "  asdf")
        print("\nFor further help, visit https://github.com/aekh/csv2latex/wiki")
    print("\nReport bugs at https://github.com/aekh/csv2latex/issues.")