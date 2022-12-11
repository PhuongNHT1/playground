# Play with modules

from math import pi

# import a module from another path
from parent.child.child2.mymodule import add as plus

sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
for x in sample_dict:
    print(x)