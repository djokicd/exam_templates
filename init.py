# Skripta za inicijalizaciju repozitoriijuma,

from examGenerator import *
import os 
import glob

def main(rok, godina, datum, k = False, i = False, opcije = True):
    if rok in validMonths and validYear(godina):
        if not k^i:
            raise ValueError("Tip mora biti postavljen ili kao kolokvijum ili kao ispit")
        os.rename(glob.glob('si1oe_*.tex')[0], f'si1oe{rok}-{godina}.tex') # Rename si1oe rok
        
        with open("generics.tex", 'w', encoding='utf-8') as generics:
            generics.write(r"\newcommand{\datumIspita}{" + datum + " г}" + "\n")
            
            # U ispitnim rokovima posle februara, ne treba nuditi opcije za polaganje ispita
            # odnosno, polaže se samo integralni ispit. 
            if validMonths.index('FEB') < validMonths.index(rok):
                generics.write(r"\setboolean{\opcijeZaPolaganje}{true}" + "\n")    
            else:
                generics.write(r"\setboolean{\opcijeZaPolaganje}{false}" + "\n")

    else:
        raise ValueError("Pogresan format roka ili godine!")

if __name__ == '__main__':
    args = p.parse_args()
    main(**vars(args))

    
