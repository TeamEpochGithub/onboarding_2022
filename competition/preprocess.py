import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import pickle
import hashlib
import py_compile

# py_compile.compile("evaluate_todelete.py", "evaluate_todelete.pyc", None, True)

from evaluate_public import score_submission
print(score_submission("../data/ford_test.csv"))