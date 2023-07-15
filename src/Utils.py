import re

import numpy as np

angular_functions = {
    'sin': np.sin,
    'cos': np.cos,
    'tan': np.tan,
    'asin': np.arcsin,
    'acos': np.arccos,
    'atan': np.arctan
}

angular_functions_names = list(angular_functions.keys())

utility_functions = {
    'sqrt': np.sqrt,
    'log': np.log,
    'exp': np.exp,
    'abs': np.abs,
    # 'deg2rad': np.deg2rad,
    # 'rad2deg': np.rad2deg,
    # 'degrees': np.degrees,
    # 'radians': np.radians,
    'pi': np.pi,
    'e': np.e,
}

utility_functions_names = list(utility_functions.keys())

allowed_names = angular_functions_names + utility_functions_names


def parse_function(func: str):
    func = func.replace(" ", "")
    func = func.replace("^", "**")
    print(f"function after parsing {func}")
    return func


def eval_function(func):
    return eval(f"lambda x: {func}", {
        **angular_functions,
        **utility_functions,
    })


def validate_function(func, x_min, x_max):
    if func == '':
        raise SyntaxError("Syntax Error: empty function")
    for word in re.findall('[a-zA-Z_]+', func):
        if word not in allowed_names + ['x']:
            raise SyntaxError(f"Syntax Error: unexpected '{word}'")
    if x_min == '':
        raise SyntaxError("Syntax Error: empty x_min")
    if x_max == '':
        raise SyntaxError("Syntax Error: empty x_max")
    try:
        x_min = float(x_min)
        x_max = float(x_max)
    except ValueError:
        return ValueError("Min and max values must be numbers")
    try:
        return eval_function(func), x_min, x_max
    except SyntaxError as e:
        raise SyntaxError(f"Syntax Error: {e}")
    except NameError as e:
        raise NameError(f"Name Error: {e}")
    except Exception as e:
        raise Exception(f"Unexpected Error: {e}")
