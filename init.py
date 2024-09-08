# Skripta za inicijalizaciju repozitoriijuma,

from examGenerator import *
from sys import *

def main(rok, godina):
    if rok in validMonths and validYear(godina):
        os.rename('si1oe_xxx_xx-xx.tex', f'si1oe{rok}-{godina}.tex') # Rename si1oe rok
    else
        raise ValueError("Pogresan format roka ili godine!")

if __name__ == '__main__':
    args = p.parse_args()
    main(**vars(args))

    
