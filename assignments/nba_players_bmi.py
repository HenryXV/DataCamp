# Import numpy
import numpy as np
import hypothesis.strategies as st
from hypothesis import given
from hypothesis.strategies import lists


@given(weight_lb=lists(st.integers(min_value=50, max_value=150)),
       height_in=lists(st.integers(min_value=50, max_value=150)))
def players_bmi(weight_lb, height_in):

    # Create array from height_in with metric units: np_height_m
    np_height_m = np.array(height_in) * 0.0254

    # Create array from weight_lb with metric units: np_weight_kg
    np_weight_kg = np.array(weight_lb) * 0.453592
    print(f'meters: {np_height_m}, kg: {np_weight_kg}')
    # Calculate the BMI: bmi
    try:
        bmi = (np_weight_kg / np_height_m ** 2)
        print(f'BMI: {bmi}')
    except ValueError:
        pass


if __name__ == '__main__':
    players_bmi()
