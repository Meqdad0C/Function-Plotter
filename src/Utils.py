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
    'pi': np.pi,
    'e': np.e,
}

utility_functions_names = list(utility_functions.keys())

converters = {
    'deg2rad': np.deg2rad,
    'rad2deg': np.rad2deg,
    'degrees': np.degrees,
    'radians': np.radians,
}

converters_names = list(converters.keys())

allowed_names = angular_functions_names + utility_functions_names


def find_close_bracket(func: str, start_index: int):
    """
    :param func: the function to search in
    :param start_index: the index of the opening bracket
    :return: the index of the closing bracket
    """
    open_brackets = 1
    for i in range(start_index + 1, len(func)):
        if func[i] == '(':
            open_brackets += 1
        elif func[i] == ')':
            open_brackets -= 1
        if open_brackets == 0:
            return i
    raise SyntaxError("Syntax Error: missing closing bracket")


def parse_function(func: str, angle_type='radian'):
    func = func.replace(" ", "")
    func = func.replace("^", "**")
    if angle_type == 'degree':
        for word in angular_functions_names:
            search_index = func.find(word + '(')
            print("search index", search_index)
            print("func", func)
            while search_index != -1:
                close_bracket_idx = find_close_bracket(func, func.find('(', search_index))
                print("close bracket index", close_bracket_idx)
                func = func[:close_bracket_idx] + ')' + func[close_bracket_idx:]
                print("func after adding a close bracket", func)
                func = func.replace(word + '(', word + '(radians(', 1)
                print("func after replacing", func)
                search_index = func[search_index + 1:].find(word + '(')
                print("search index", search_index)
    print(f"function after parsing {func}")
    return func


def eval_function(func):
    return eval(f"lambda x: {func}", {
        **angular_functions,
        **utility_functions,
        **converters,
    })


def validate_function(func, x_min, x_max):
    if func == '':
        raise SyntaxError("Syntax Error: empty function")
    for word in re.findall('[a-zA-Z_]+', func):
        if word not in allowed_names + converters_names + ['x']:
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
