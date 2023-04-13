import pandas as pd
import numpy as np

from hyppo.ksample import MMD

chat_id = 1105798394 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.03
    m="rbf"
    g=1
    pval=MMD(compute_kernel=m, gamma=g).test(x,y).pvalue
    return p_value < alpha # Ваш ответ, True или False
