validMonths = ["JAN", "FEB", "JUN", "JUL", "AUG", "SEP"]

def validYear(x):
    if len(x) != 5 or \
       x[2] != "-" or \
       not '0'< x[0] < '9' or \
       not '0'< x[1] < '9' or \
       not '0'< x[3] < '9' or \
       not '0'< x[4] < '9':
        raise ValueError("Pogresan format datum")
    return True

import argparse
p = argparse.ArgumentParser()
p.add_argument('rok')
p.add_argument('godina')