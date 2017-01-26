csv2latex
=========

This is a Python program for converting a .CSV-table into one or more LaTeX-tables in the tabular environmet.

Installation
------------

Installation for simple use
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Simply run the following command::

    pip install git+https://github.com/aekh/csv2latex.git@master
    
For updates, run::

    pip install --upgrade git+https://github.com/aekh/csv2latex.git@master

Installation for development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
First, clone the repository, then use the following command in the root folder of this project::

    python setup.py develop

For updates, simply pull the latest version.

Example
-------
Let file.csv denote the following file::

    "a","b","c","d","e","f","g","h"
    "1","2","3","4","5","6","7","8"
    "A","B","C","D","E","F","G","H"
    
By running::
    
    csv2latex -i file.csv -p --transpose-after -r3,6
    
the following three tables are obtained::

    a & 1 & A \\
    b & 2 & B \\
    c & 3 & C \\

    %%%

    d & 4 & D \\
    e & 5 & E \\
    f & 6 & F \\

    %%%
    
    g & 7 & G \\
    h & 8 & H \\
