# Skripta za inicijalizaciju repozitoriijuma,

from examGenerator import *
import os 
import glob

def main(rok, godina, datum, k = False, i = False, opcije = True):
    if rok in validMonths and validYear(godina):
        if not bool(k)^bool(i):
            raise ValueError("Tip mora biti postavljen ili kao kolokvijum ili kao ispit")
        os.rename(glob.glob('si1oe_*.tex')[0], f'si1oe_{rok}-{godina}.tex') # Rename si1oe rok
        
        with open("generics.tex", 'w', encoding='utf-8') as generics:
            generics.write(r"\newboolean{opcijeZaPolaganje}" + "\n")
            generics.write(r"\newcommand{\datumIspita}{" + datum + " г}" + "\n")
            
            # U ispitnim rokovima posle februara, ne treba nuditi opcije za polaganje ispita
            # odnosno, polaže se samo integralni ispit. 
            if validMonths.index('FEB') < validMonths.index(rok):
                generics.write(r"\setboolean{opcijeZaPolaganje}{true}" + "\n")    
            else:
                generics.write(r"\setboolean{opcijeZaPolaganje}{false}" + "\n")

            generics.write(r"\newboolean{ispit}" + "\n" )

            if i:
                generics.write(r"\setboolean{ispit}{true}" + "\n")
                generics.write(r"\newcommand{\naslovFormulara}{ИСПИТ ИЗ ОСНОВА ЕЛЕКТРОНИКЕ}" + "\n") 
                generics.write(r"\newcommand{\tablicaPDF}{si1oe_tablica_ispit.pdf}" + "\n") 
            else:
                generics.write(r"\setboolean{ispit}{false}")
                generics.write(r"\newcommand{\tablicaPDF}{si1oe_tablica_kolokvijum.pdf}" + "\n") 
                if k == 1:
                    generics.write(r"\newcommand{\naslovFormulara}{ПРВИ КОЛОКВИЈУМ ИЗ ОСНОВА ЕЛЕКТРОНИКЕ}" + "\n")    
                elif k == 2:
                    generics.write(r"\newcommand{\naslovFormulara}{ДРУГИ КОЛОКВИЈУМ ИЗ ОСНОВА ЕЛЕКТРОНИКЕ}" + "\n")    
                elif k == 3:
                    generics.write(r"\newcommand{\naslovFormulara}{ТРЕЋИ КОЛОКВИЈУМ ИЗ ОСНОВА ЕЛЕКТРОНИКЕ}" + "\n")    
        with open('.vscode/settings.json', 'w') as settings:
            settings.write(f'''{{
    "name": "pdflatex",
    "command": "pdflatex",
    "args": [
        "--shell-escape", // if you want to have the shell-escape flag
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "--aux-directory=.aux",
        "si1oe_{rok}-{godina}.tex"
    ]
}}''')
    else:
        raise ValueError("Pogresan format roka ili godine!")

if __name__ == '__main__':
    args = p.parse_args()
    main(**vars(args))

    
