import streamlit as st
import sympy as sp
from streamlit.delta_generator import DeltaGenerator

from distributionsolver.utils import dotf

# Define symbols
x = sp.symbols("x")
a, b = sp.symbols("a b")


# Function to generate steps for Uniform Distribution
def uniform_distribution(a: float, b: float, x: float) -> None:
    st.write("# Uniform Distribution")

    st.write(f"""
    Given:
    - a (lower bound of the distribution) = {a}
    - b (upper bound of the distribution) = {b}
    - x (value at which to evaluate the PDF) = {x}
             """)


def pdf(a: float, b: float, x: float) -> None:
    st.write("---\n### Probability Density Function (PDF)")

    st.latex(r"f(x) = \frac{1}{b - a}")

    st.write("where")
    st.latex(r"a = \text{lower bound of the distribution}")
    st.latex(r"b = \text{upper bound of the distribution}")

    st.write("Step 1: Substitute the values in the PDF")
    st.latex(f"f(x) = \\frac{{1}}{{{b} - {a}}}")

    st.write("Step 2: Solve the equation")
    if a <= x <= b:
        term = 1 / (b - a)
    else:
        term = 0
    st.latex(f"f({x}) = {dotf(term)}")
    st.write(f"Hence, f({x}) = {dotf(term)}")


def expected_value(a: float, b: float, x: float) -> None:
    st.write("---\n### Expected Value")
    st.latex(r"E[X] = \frac{a + b}{2}")

    st.write("Step 1: Substitute the values in the expected value formula")
    st.latex(f"E[X] = \\frac{{{a} + {b}}}{{2}}")

    st.write("Step 2: Solve the equation")
    term = (a + b) / 2
    st.latex(f"E[X] = {dotf(term)}")


def variance(a: float, b: float, x: float) -> None:
    st.write("---\n### Variance")
    st.latex(r"Var[X] = \frac{(b - a)^2}{12}")

    st.write("Step 1: Substitute the values in the variance formula")
    st.latex(f"Var[X] = \\frac{{({b} - {a})^2}}{{12}}")

    st.write("Step 2: Solve the equation")
    term = ((b - a) ** 2) / 12
    st.latex(f"Var[X] = {dotf(term)}")


def show_uniform_distribution(expander: DeltaGenerator):
    a = expander.number_input("Enter value for a (lower bound of the distribution):", value=0.0)
    b = expander.number_input("Enter value for b (upper bound of the distribution):", value=1.0)
    x = expander.number_input("Enter value for x (value at which to evaluate the PDF):", value=0.5)

    show_pdf = expander.checkbox("Show PDF")
    show_expected_value = expander.checkbox("Show expected value")
    show_variance = expander.checkbox("Show variance")

    if expander.button("Solve"):
        uniform_distribution(a, b, x)
        if show_pdf:
            pdf(a, b, x)
        if show_expected_value:
            expected_value(a, b, x)
        if show_variance:
            variance(a, b, x)
