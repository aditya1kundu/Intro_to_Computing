# Creating list and input words separated by '-' as elements.
items=[n for n in input("Enter sentence here: ").split('-')]


items.sort()    # arranging alphabetically

print('-'.join(items))
