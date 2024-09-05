import math

import streamlit as st
import sympy as sp
from streamlit.delta_generator import DeltaGenerator

from distributionsolver.utils import dotf

# Define symbols
x = sp.symbols("x")
mu, sigma = sp.symbols("mu sigma")


# Function to generate steps for Normal Distribution
def normal_distribution(mu: float, sigma: float, x: float) -> None:
    st.write("# Normal Distribution")

    st.write(f"""
    Given:
    - mu (mean) = {mu}
    - sigma (standard deviation) = {sigma}
    - x (value at which to evaluate the PDF) = {x}
             """)


def pdf(mu: float, sigma: float, x: float) -> None:
    st.write("---\n### Probability Density Function (PDF)")

    st.latex(r"f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\dfrac{(x - \mu)^2}{2\sigma^2}}")

    st.write("where")
    st.latex(r"\mu = \text{mean}")
    st.latex(r"\sigma = \text{standard deviation}")

    st.write("Step 1: Substitute the values in the PDF")
    st.latex(
        f"f(x) = \\frac{{1}}{{{dotf(sigma)} \\sqrt{{2\\pi}}}} e^{{-\\dfrac{{(x - {dotf(mu)})^2}}{{2\\cdot {dotf(sigma)}^2}}}}"
    )

    st.write("Step 2: Solve the equation")
    term_1 = 1 / (sigma * math.sqrt(2 * math.pi))
    term_2 = math.exp(-((x - mu) ** 2) / (2 * sigma**2))
    term = term_1 * term_2
    st.latex(f"f({x}) = {dotf(term)}")
    st.write(f"Hence, f({x}) = {dotf(term)}")


def expected_value(mu: float, sigma: float, x: float) -> None:
    st.write("---\n### Expected Value")
    st.latex(r"E[X] = \mu")

    st.write("Step 1: Substitute the values in the expected value formula")
    st.latex(f"E[X] = {mu}")

    st.write("Step 2: Solve the equation")
    term = mu
    st.latex(f"E[X] = {dotf(term)}")


def variance(mu: float, sigma: float, x: float) -> None:
    st.write("---\n### Variance")
    st.latex(r"Var[X] = \sigma^2")

    st.write("Step 1: Substitute the values in the variance formula")
    st.latex(f"Var[X] = {sigma}^2")

    st.write("Step 2: Solve the equation")
    term = sigma**2
    st.latex(f"Var[X] = {dotf(term)}")


def show_normal_distribution(expander: DeltaGenerator):
    mu = expander.number_input("Enter value for mu (mean):", value=0.0)
    sigma = expander.number_input("Enter value for sigma (standard deviation):", value=1.0, min_value=0.0)
    x = expander.number_input("Enter value for x (value at which to evaluate the PDF):", value=0.0)

    show_pdf = expander.checkbox("Show PDF")
    show_expected_value = expander.checkbox("Show expected value")
    show_variance = expander.checkbox("Show variance")

    if expander.button("Solve"):
        normal_distribution(mu, sigma, x)
        if show_pdf:
            pdf(mu, sigma, x)
        if show_expected_value:
            expected_value(mu, sigma, x)
        if show_variance:
            variance(mu, sigma, x)
