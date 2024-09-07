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


def pdf_at_a_point(mu: float, sigma: float, x: float) -> None:
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


def pdf_for_a_range(mu_val: float, sigma_val: float, a: float, b: float) -> None:
    st.write("---\n### Probability Density Function (PDF) for a range")

    # Define the symbolic variables
    x, mu, sigma = sp.symbols("x mu sigma")

    # Define the PDF function using sympy functions
    # function = 1 / (sigma * sp.sqrt(2 * sp.pi)) * sp.exp(-((x - mu) ** 2) / (2 * sigma**2))

    st.latex(r"f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\dfrac{(x - \mu)^2}{2\sigma^2}}")

    st.write("Step 1: Probability for a range using integration")
    st.latex(
        r"P(a \leq X \leq b) = \int_a^b \frac{1}{\sigma \sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right) \, dx"
    )

    st.write("Step 2: Error Function Representation:")
    st.latex(
        r"P(a \leq X \leq b) = \frac{1}{2} \left[\text{erf}\left(\frac{b - \mu}{\sigma \sqrt{2}}\right) - \text{erf}\left(\frac{a - \mu}{\sigma \sqrt{2}}\right)\right]"
    )

    # Substitute the values for mu, sigma, a, and b
    z_a = (a - mu_val) / (sigma_val * sp.sqrt(2))
    z_b = (b - mu_val) / (sigma_val * sp.sqrt(2))

    st.write(f"Step 3: Substitute the Values for a = {a}, b = {b}, mu = {mu_val} and sigma = {sigma_val}")
    st.latex(
        f"P({{{a}}} \\leq X \\leq {{{b}}}) = \\frac{{1}}{{2}} \\left[\\text{{erf}}\\left(\\frac{{{b} - {mu_val}}}{{{sigma_val} \\sqrt{{2}}}}\\right) - \\text{{erf}}\\left(\\frac{{{a} - {mu_val}}}{{{sigma_val} \\sqrt{{2}}}}\\right)\\right]"
    )

    # Compute the error function values
    erf_a = sp.erf(z_a)
    erf_b = sp.erf(z_b)

    st.write("Step 4: Compute the Error Function Values:")
    st.latex(f"P({{{a}}} \\leq X \\leq {{{b}}}) = \\frac{{1}}{{2}} \\left[{dotf(erf_a, 4)} - {dotf(erf_b, 4)}\\right]")

    # Compute the final probability
    probability = 0.5 * (erf_b - erf_a)

    st.write("Step 5: Final Answer:")
    st.latex(f"P({{{a}}} \\leq X \\leq {{{b}}}) = {dotf(probability, 4)}")


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
    a = expander.number_input("Enter value for a (lower limit):", value=0.0)
    b = expander.number_input("Enter value for a (upper limit):", value=0.0)
    show_pdf_at_a_point = expander.checkbox("Show PDF at a point")
    show_pdf_for_a_range = expander.checkbox("Show PDF for a range")
    show_expected_value = expander.checkbox("Show expected value")
    show_variance = expander.checkbox("Show variance")

    if expander.button("Solve"):
        normal_distribution(mu, sigma, x)
        if show_pdf_at_a_point:
            pdf_at_a_point(mu, sigma, x)
        if show_pdf_for_a_range:
            pdf_for_a_range(mu, sigma, a, b)
        if show_expected_value:
            expected_value(mu, sigma, x)
        if show_variance:
            variance(mu, sigma, x)
