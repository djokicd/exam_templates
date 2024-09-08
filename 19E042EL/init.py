# Skripta za inicijalizaciju repozitoriijuma,

from examGenerator import *
import os 
import glob

def main(rok, godina, datum, k = False, i = False, opcije = True):
    if rok in validMonths and validYear(godina):
        if not bool(k)^bool(i):
            raise ValueError("Tip mora biti postavljen ili kao kolokvijum ili kao ispit")
        os.rename(glob.glob('el_*.tex')[0], f'el_{rok}-{godina}.tex') # Rename si1oe rok
        
        with open("generics.tex", 'w', encoding='utf-8') as generics:
            generics.write(r"\newcommand{\datumIspita}{" + datum + " г}" + "\n")


            generics.write(r"\newcommand{\footerCenter}{" + monthsDict[rok].capitalize() + " " + \
                          "20" + godina[0:1] + "/20" + godina[-2:-1] + "}")
            generics.write(r"\newboolean{ispit}" + "\n" )
            
            if i:
                generics.write(r"\setboolean{ispit}{true}" + "\n") 
                generics.write(r"\newcommand{\trajanjeIspita}{180}" + "\n") 
            else:
                generics.write(r"\setboolean{ispit}{false}" + "\n")
                generics.write(r"\newcommand{\trajanjeIspita}{120}" + "\n") 

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
        "el_{rok}-{godina}.tex"
    ]
}}''')
    else:
        raise ValueError("Pogresan format roka ili godine!")

if __name__ == '__main__':
    args = p.parse_args()
    main(**vars(args))

    
