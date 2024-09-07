import sympy as sp


def dotf(value: float | int, precision: int = 3) -> str:
    return f"{value:.{precision}f}"


def format_integral(latex_expr, lower_bound, upper_bound, wrt):
    # This function manually formats the integral expression with bounds
    return f"\\int_{{{lower_bound}}}^{{{upper_bound}}} {latex_expr} d{{{wrt}}}"


def sub_but_not_solved(expression, symbols):
    print(expression)
    latex_expression = sp.latex(expression)
    for key, value in symbols.items():
        latex_expression = latex_expression.replace(key, f"({value})")
    return latex_expression
