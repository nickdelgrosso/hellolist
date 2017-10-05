
# coding: utf-8

# In[7]:

from bs4 import BeautifulSoup
from glob import glob



def get_ingredients(filename):
    """Returns List of Hello Fresh Ingredients from Recipe"""
    with open(filename, 'r') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'lxml')
    aa = soup.findAll(text='Zutaten')[1]
    ings = []
    for div in aa.parent.parent.parent.findAll('div'):
        if len(div.findAll('p')) > 2:
            ing = div.findAll('p')[:2]
            ings.append(tuple(i.text for i in ing)[::-1])
    ings = set(ings)
    return list(ings)


def combine_ingredients(ingredients):
    ingredients = sorted(ingredients)
    """Combines and adds list of ingredients [(name, 'amnt unit')]"""
    nings = []
    for idx, (ing1, ing2) in enumerate(zip(ingredients[:-1], ingredients[1:])):
        try:
            if ing1[0] == nings[-1][0]:
                continue
        except IndexError:
            pass
        if ing1[0] != ing2[0]:
            nings.append(ing1)
            continue
        if not ing1[1]:
            nings.append(ing1)
            continue
        amnt1 = ing1[1].split(' ')[0]
        amnt2 = ing2[1].split(' ')[0]
        amnt1 = .5 if amnt1 == '½' else float(amnt1)
        amnt2 = .5 if amnt2 == '½' else float(amnt2)
        total_amnt = amnt1 + amnt2
        nings.append((ing1[0], '{} {}'.format(total_amnt, ing1[1].split(' ')[1])))
    return nings

def full_merge(filenames):
    # Extract and merge ingredients
    ings = []
    for fname in filenames:
        ing = get_ingredients(fname)
        ings.extend(ing)
    all_ingredients = combine_ingredients(ings)
    return all_ingredients

if __name__ == '__main__':
    main()




