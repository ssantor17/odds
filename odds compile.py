from bs4 import BeautifulSoup
import urllib3
import pandas as pd
import numpy as np
import random
import sys

core = pd.read_pickle('games.pk1')
moves = pd.read_pickle('line_moves.pk1')


print(core)
print(moves)
