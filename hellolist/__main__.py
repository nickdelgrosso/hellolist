
import sys
import pandas as pd

import tkinter as tk
from tkinter import filedialog

import hellolist

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    root = tk.Tk()
    root.withdraw()

    filenames = filedialog.askopenfilenames()
    all_ingredients = hellolist.full_merge(filenames)

    # Output file
    to='html'
    df = pd.DataFrame(sorted(all_ingredients), columns=['Ingredient', 'Amount'])
    df.to_excel('OurShoppingList.xlsx')


if __name__ == "__main__":
    main()

