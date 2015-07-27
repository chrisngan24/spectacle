"""
Helper/util functions
"""
import numpy as np

def metric(predict_y, true_y):
    assert len(predict_y) == len(true_y)

    n = len(predict_y)
    score = np.log(predict_y + 1) - np.log(true_y + 1)
    score = map(lambda x: pow(x,2), list(score))
    return np.sqrt(sum(score) / n)

if __name__ == '__main__':
    a = np.array([1,2])
    b = np.array([0.1,0.2])
    m_val = metric(a, b)
    import pdb; pdb.set_trace()

