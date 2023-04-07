import pandas as pd
import numpy as np
 from scipy.stats import poisson
 from sklearn.metrics import mean_squared_error

chat_id = 767766291 # Ваш chat ID, не меняйте название переменной


def solution(x: np.array) -> float:
   #   Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return x.mean() / 12 # Ваш ответ

 for i in [10, 100, 1000]:
    lb = 10.0
     y_pred = []
    for j in range(100):
        x = poisson.rvs(12 * lb, size=i)
        y_pred.append(solution(x))
    print(i, mean_squared_error([lb] * 100, y_pred))
