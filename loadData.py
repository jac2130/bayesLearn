import pandas as pd 
from Entro import Distance
import jsonpickle as jp

simple = pd.read_pickle("simple_models")
complex = pd.read_pickle("complex_models")

simple_score = {}

with open('simpleG', 'r') as f:
    simpleG = jp.decode(f.read())

with open('complexG', 'r') as f:
    complexG = jp.decode(f.read())

print simpleG


for key in simple:

    simple_score[key] = [Distance(simpleG["probs"], t) for t in simple[key]]
"""
for key in simple:
    print simple[key][6]
"""
key = simple.keys()[6]

print simple_score[key]
