import streamlit as st
import sympy as sp
from streamlit.delta_generator import DeltaGenerator

from distributionsolver.utils import dotf

# Define symbols
x, lambda_ = sp.symbols("x lambda")


# Function to generate steps for Poisson Distribution
def poisson_distribution(lambda_: float, x: int) -> None:
    st.write("# Poisson Distribution")

    st.write(f"""
    Given:
    - λ (average number of successes in a given interval) = {dotf(lambda_)}
    - x (number of successes) = {x}
    """)


def distribution_function(lambda_: float, x: int) -> None:
    st.write("---\n### Poisson distribution function")

    st.latex(r"P(X = x) = \frac{\lambda^x e^{-\lambda}}{x!}")

    st.write("where")
    st.latex(r"x! = x \cdot (x - 1) \cdot (x - 2) \cdot \dots \cdot 1")

    st.write("Step 1: Substitute the values in the distribution function")

    st.latex(
        "P(X = {}) = \\frac{{{}^{}e^{{-{}}}}}{{{}!}}".format(
            dotf(x, 0), dotf(lambda_, 0), dotf(x, 0), dotf(lambda_, 0), dotf(x, 0)
        )
    )

    st.write("Step 2: Solve the equation")
    # term =

    st.latex(f"P(X = {x}) = {dotf((lambda_**x * sp.exp(-lambda_)) / sp.factorial(x))}")


def expected_value(lambda_: float, x: int) -> None:
    st.write("---\n### Expected Value")
    st.latex(r"E[X] = \lambda")

    st.write("Step 1: Substitute the value of lambda in the expected value formula")
    st.latex(f"E[X] = {dotf(lambda_)}")

    st.write("Step 2: Solve the equation")
    term = lambda_
    st.latex(f"E[X] = {dotf(term)}")


def variance(lambda_: float, x: int) -> None:
    st.write("---\n### Variance")
    st.latex(r"Var[X] = \lambda")

    st.write("Step 1: Substitute the value of lambda in the variance formula")
    st.latex(f"Var[X] = {dotf(lambda_)}")

    st.write("Step 2: Solve the equation")
    term = lambda_
    st.latex(f"Var[X] = {dotf(term)}")


def show_poisson_distribution(expander: DeltaGenerator):
    lambda_ = expander.number_input(
        "Enter value for lambda (average number of successes):", value=1.0, min_value=0.0, step=0.1
    )
    x = expander.number_input("Enter value for x (number of successes):", value=1, min_value=0, step=1)

    show_distribution_function = expander.checkbox("Show distribution function")
    show_expected_value = expander.checkbox("Show expected value")
    show_variance = expander.checkbox("Show variance")

    if expander.button("Solve"):
        poisson_distribution(lambda_, x)
        if show_distribution_function:
            distribution_function(lambda_, x)
        if show_expected_value:
            expected_value(lambda_, x)
        if show_variance:
            variance(lambda_, x)
