import numpy as np

def metric(predict_y, true_y):
    assert len(predict_y) == len(true_y)
    n = float(len(predict_y))
    score = sum(predict_y == true_y) / n
    return score

if __name__ == '__main__':
    print 'start'
    a = np.array([1,2,2])
    b = np.array([1,2,1])
    print a == b
    import pdb; pdb.set_trace()
    m_val = metric(a, b)
    import pdb; pdb.set_trace()
    print m_val

