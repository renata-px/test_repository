import numpy as np

# === CONSTANTS ===
waste_coefficient = 0.88
volume_1_mol_normal_cond = 0.0224
mm_h2 = 2
mm_co2 = 44
mm_co = 28
mm_ch4 = 16
mm_n2 = 28
low_heat_value_const = 33
high_heat_value_const = 39.38
kwh_for_1_kg_h2 = 52
r_const = 8.31446

# === TEMPERATURE CALCULATIONS ===
def middle_temp_k(x1, x2, x3):
    return 700 + 19050 * x2 / (x1 * x3)

def middle_temp_c(x1, x2, x3):
    return middle_temp_k(x1, x2, x3) - 273.15

def normal_temp_c(x1, x2, x3):
    return middle_temp_c(x1, x2, x3) * 0.01917 + 726.59

# === GASIFICATION MODELS ===
def h2_vol(temp_c, model='poly'):
    if model == 'poly':
        return 8.64427756e+02 + (
            -1.11535475e-02) * temp_c ** 2 + 2.50417715e-05 * temp_c ** 3 + (
            -2.08318518e-08) * temp_c ** 4 + 6.09290570e-12 * temp_c ** 5
    return 0

def co2_vol(temp_c, model='poly'):
    if model == 'poly':
        return 7.88262261e+01 + (
            -1.42644743e-03) * temp_c ** 2 + 3.66824063e-06 * temp_c ** 3 + (
            -3.38728167e-09) * temp_c ** 4 + 1.07816591e-12 * temp_c ** 5
    return 0

def co_vol(temp_c, model='poly'):
    if model == 'poly':
        return -7.75058073e+02 + (1.12213487e-02) * temp_c ** 2 + (
            -2.59664968e-05) * temp_c ** 3 + (2.22417149e-08) * temp_c ** 4 + (
            -6.70159810e-12) * temp_c ** 5
    return 0

def ch4_vol(temp_c, model='poly'):
    if model == 'poly':
        return -1.35270631e+02 + 1.76696155e-03 * temp_c ** 2 + (
            -3.88540841e-06) * temp_c ** 3 + (3.15797384e-09) * temp_c ** 4 + (
            -9.02717242e-13) * temp_c ** 5
    return 0

def n2_vol(temp_c, model='poly'):
    if model == 'poly':
        return -1.92588105e+02 + 3.07852112e-03 * temp_c ** 2 + (
            -6.98410588e-06) * temp_c ** 3 + (5.91052625e-09) * temp_c ** 4 + (
            -1.75956783e-12) * temp_c ** 5
    return 0

# Volume / Mass helpers
def waste_volume(waste):
    return waste * waste_coefficient

def h2_m3(h2v, waste_vol):
    return h2v * waste_vol / 100

def h2_kg(h2_m3_val):
    h2_n = h2_m3_val / volume_1_mol_normal_cond
    return h2_n * mm_h2 / 1000

# Pyrolysis
def pyrolysis_temperature(energy):
    return (energy * 3.6 + 1.5591) / 0.0425

def pyrolysis_liquid_percent(temp):
    return 30.2507 + 0.0246 * temp - 0.000057833 * temp ** 2

print('✅ calculations.py fully loaded with core functions')