import streamlit as st
import sympy as sp
from streamlit.delta_generator import DeltaGenerator

from distributionsolver.utils import dotf

# Define symbols
x, p = sp.symbols("x p")


# Function to generate steps for geometric distribution
def geometric_distribution(p: float, x: int) -> None:
    st.write("# Geometric Distribution")

    st.write(f"""
    Given:
    - p (probability of success) = {p}
    - x (number of trials until first success) = {x}
    """)


def distribution_function(p: float, x: int) -> None:
    st.write("---\n### Geometric distribution function")

    st.latex(r"P(X = x) = (1 - p)^{x-1} \cdot p")

    st.write("Step 1: Substitute the values in the distribution function")

    st.latex(r"P(X = {}) = (1 - {})^{{{}-1}} \cdot {}".format(dotf(x, 0), dotf(p), dotf(x, 0), dotf(p)))

    st.write("Step 2: Solve the equation")
    term_1 = (1 - p) ** (x - 1)
    term_2 = p
    st.latex(f"P(X = {x}) = {dotf(term_1)} \\cdot {dotf(term_2)}")

    st.write("Hence,")
    st.latex(f"P(X = {x}) = {dotf(term_1 * term_2)}")


def expected_value(p: float) -> None:
    st.write("---\n### Expected Value")
    st.latex(r"E[X] = \frac{1}{p}")

    st.write("Step 1: Substitute the value of p in the formula")
    st.latex(f"E[X] = \\frac{{1}}{{{p}}}")

    st.write("Step 2: Solve the equation")
    term = 1 / p
    st.latex(f"E[X] = {dotf(term)}")


def variance(p: float) -> None:
    st.write("---\n### Variance")
    st.latex(r"Var[X] = \frac{1 - p}{p^2}")

    st.write("Step 1: Substitute the value of p in the formula")
    st.latex(f"Var[X] = \\frac{{1 - {p}}}{{{p}^2}}")

    st.write("Step 2: Solve the equation")
    term = (1 - p) / p**2
    st.latex(f"Var[X] = {dotf(term)}")


def show_geometric_distribution(expander: DeltaGenerator):
    p = expander.number_input(
        "Enter value for p (probability of success):", value=0.5, min_value=0.0, max_value=1.0, step=0.01
    )
    x = expander.number_input("Enter value for x (number of trials until first success):", value=1, min_value=1, step=1)

    show_distribution_function = expander.checkbox("Show distribution function")
    show_expected_value = expander.checkbox("Show expected value")
    show_variance = expander.checkbox("Show variance")

    if expander.button("Solve"):
        geometric_distribution(p, x)
        if show_distribution_function:
            distribution_function(p, x)
        if show_expected_value:
            expected_value(p)
        if show_variance:
            variance(p)
