# python-homework
- Developer: Andrew Park

# Files
- src/pybank.py
- src/pyramen.py
- data/pybank/budget_data.csv
- data/pyramen/sales_data.csv
- data/pyramen/menu_data.csv

# Design Decisions
- Any input files (.csv's) are supplied through command-line options.
- The output file is also supplied through a command-line option.
- The design for the PyRamen portion that were initially provided was inefficient.
    That is, the efficiency provided by the initial design was O(M*N),
    where M is the number of rows in menu and N is the number of rows in sales.
    I modified the design to gather the distinct sale elements first.
    Then, I used dataframe aggregation techniques to do the calculations without having to iterate to each row.
    As a result, I was able to reduce the efficiency of the solution to O(P),
    where P is the number of DISTINCT sale items.
    For this dataset, the for-loop executed ~30 times.

# Usage
- python src/pybank.py -h / python src/pyramen.py -h
