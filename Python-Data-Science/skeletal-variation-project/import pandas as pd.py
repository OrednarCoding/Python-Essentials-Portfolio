import os
os.system("cls")
import pandas as pd
print(pd.__version__)
import matplotlib.pyplot as plt
plt.plot([1,2,3,],[1,2,1])
from sklearn.datasets import load_iris
print(load_iris().data.shape)
