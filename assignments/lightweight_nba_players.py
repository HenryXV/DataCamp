import numpy as np
import hypothesis.strategies as st
from hypothesis import given
from hypothesis.strategies import lists


@given(weight_lb=lists(st.integers(min_value=120, max_value=200)),
       height_in=lists(st.integers(min_value=60, max_value=90)))
def lightweight_players(weight_lb, height_in):

    # Calculate the BMI: bmi
    np_height_m = np.array(height_in) * 0.0254
    np_weight_kg = np.array(weight_lb) * 0.453592
    try:
        bmi = np_weight_kg / np_height_m ** 2
    except ValueError:
        return None

    light = bmi < 21
    print(light)

    print(bmi[light])


if __name__ == '__main__':
    lightweight_players()
