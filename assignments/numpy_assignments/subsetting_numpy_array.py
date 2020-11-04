import numpy as np
from hypothesis import given
from hypothesis.strategies import integers, floats, lists


@given(weight_kg=lists(integers(50, 120), min_size=110, max_size=200),
       height_m=lists(floats(1, 2, allow_nan=False), min_size=110, max_size=200))
def subsetting_numpy(weight_kg, height_m):
    np_weight_kg = np.array(weight_kg)
    np_height_m = np.array(height_m)

    print(np_weight_kg[50])
    print(np_height_m[100:111])


if __name__ == '__main__':
    subsetting_numpy()
