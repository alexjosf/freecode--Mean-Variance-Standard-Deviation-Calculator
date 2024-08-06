import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    else:
        array = np.array(list).reshape(3, 3)

    mean = [(array.mean(axis=0).tolist()), (array.mean(axis=1).tolist()),
            (array.flatten().mean())]

    var = [(array.var(axis=0).tolist()), (array.var(axis=1).tolist()),
           (array.flatten().var())]

    std = [(array.std(axis=0).tolist()), (array.std(axis=1).tolist()),
           (array.flatten().std())]

    max = [(array.max(axis=0).tolist()), (array.max(axis=1).tolist()),
           (array.flatten().max())]

    min = [(array.min(axis=0).tolist()), (array.min(axis=1).tolist()),
           (array.flatten().min())]

    sum = [(array.sum(axis=0).tolist()), (array.sum(axis=1).tolist()),
           (array.flatten().sum())]

    calculations = {
        "mean": mean,
        "variance": var,
        "standard deviation": std,
        "max": max,
        "min": min,
        "sum": sum,
    }

    return calculations