import pandas as pd
import numpy as np


chat_id = 959806937 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    sum = 0
    for i in range(len(x)):
      sum += x[i]
    sr = sum / len(x)
    return 1 / (sr+34)
