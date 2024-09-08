# Skripta za inicijalizaciju repozitoriijuma,

from examGenerator import *
import os 

def main(rok, godina, datum, k = False, i = False, opcije = True):
    if rok in validMonths and validYear(godina):
        #os.rename('si1oe_xxx_xx-xx.tex', f'si1oe{rok}-{godina}.tex') # Rename si1oe rok

        with open("generics.tex", 'w', encoding='utf-8') as generics:
            generics.write(r"\newcommand{\datumIspita}{" + datum + " г}" + "\n")
            if opcije:
                generics.write(r"\setboolean{\opcijeZaPolaganje}{true}" + "\n")    
            else:
                generics.write(r"\setboolean{\opcijeZaPolaganje}{false}" + "\n")

    else:
        raise ValueError("Pogresan format roka ili godine!")

if __name__ == '__main__':
    args = p.parse_args()
    main(**vars(args))

    
