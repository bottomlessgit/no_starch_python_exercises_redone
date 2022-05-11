"""
Exercise demonstrates import modules by importing and using module
printing_functions.py to simulate printing a list of 3d models
"""
import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)