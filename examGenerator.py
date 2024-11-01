validMonths = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

monthsDict = {
    "JAN": "јануар",
    "FEB": "фебруар", 
    "MAR": "март", 
    "APR": "април", 
    "MAY": "мај",
    "JUN": "јун",
    "JUL": "јул",
    "AUG": "август",
    "SEP": "септембар",
    "OCT": "октобар",
    "NOV": "новембар",
    "DEC": "децембар"
}

def validYear(x):
    if len(x) != 5 or \
       x[2] != "-" or \
       not '0'<= x[0] <= '9' or \
       not '0'<= x[1] <= '9' or \
       not '0'<= x[3] <= '9' or \
       not '0'<= x[4] <= '9':
        raise ValueError("Pogresan format datum")
    return True

import argparse
p = argparse.ArgumentParser()
p.add_argument('rok')
p.add_argument('godina')
p.add_argument('datum')
p.add_argument('--kolokvijum', dest='k', default=False)
p.add_argument('--ispit', dest='i', action='store_true', default=False)

