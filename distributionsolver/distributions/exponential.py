import math

import streamlit as st
import sympy as sp
from streamlit.delta_generator import DeltaGenerator

from distributionsolver.utils import dotf

# Define symbols
x = sp.symbols("x")
lambda_ = sp.symbols("lambda")


# Function to generate steps for Exponential Distribution
def exponential_distribution(lambda_: float, x: float) -> None:
    st.write("# Exponential Distribution")

    st.write(f"""
    Given:
    - lambda (rate parameter) = {lambda_}
    - x (value at which to evaluate the PDF) = {x}
             """)


def pdf(lambda_: float, x: float) -> None:
    st.write("---\n### Probability Density Function (PDF)")

    st.latex(r"f(x) = \lambda e^{-\lambda x}")

    st.write("where")
    st.latex(r"\lambda = \text{rate parameter}")

    st.write("Step 1: Substitute the values in the PDF")
    st.latex(f"f(x) = {lambda_} e^{{- {lambda_}\\times{x}}}")

    st.write("Step 2: Solve the equation")
    term = lambda_ * math.exp(-lambda_ * x)
    st.latex(f"f({x}) = {dotf(term)}")
    st.write(f"Hence, f({x}) = {dotf(term)}")


def expected_value(lambda_: float, x: float) -> None:
    st.write("---\n### Expected Value")
    st.latex(r"E[X] = \frac{1}{\lambda}")

    st.write("Step 1: Substitute the values in the expected value formula")
    st.latex(f"E[X] = \\frac{{1}}{{{lambda_}}}")

    st.write("Step 2: Solve the equation")
    term = 1 / lambda_
    st.latex(f"E[X] = {dotf(term)}")


def variance(lambda_: float, x: float) -> None:
    st.write("---\n### Variance")
    st.latex(r"Var[X] = \frac{1}{\lambda^2}")

    st.write("Step 1: Substitute the values in the variance formula")
    st.latex(f"Var[X] = \\frac{{1}}{{{lambda_}^2}}")

    st.write("Step 2: Solve the equation")
    term = 1 / (lambda_**2)
    st.latex(f"Var[X] = {dotf(term)}")


def show_exponential_distribution(expander: DeltaGenerator):
    lambda_ = expander.number_input("Enter value for lambda (rate parameter):", value=1.0, min_value=0.0)
    x = expander.number_input("Enter value for x (value at which to evaluate the PDF):", value=0.0)
    show_pdf = expander.checkbox("Show PDF")
    show_expected_value = expander.checkbox("Show expected value")
    show_variance = expander.checkbox("Show variance")

    if expander.button("Solve"):
        exponential_distribution(lambda_, x)
        if show_pdf:
            pdf(lambda_, x)
        if show_expected_value:
            expected_value(lambda_, x)
        if show_variance:
            variance(lambda_, x)
