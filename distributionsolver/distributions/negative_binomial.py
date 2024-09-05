import streamlit as st
import sympy as sp
from streamlit.delta_generator import DeltaGenerator

from distributionsolver.utils import dotf

# Define symbols
x = sp.symbols("x")


# Function to generate steps for Negative Binomial Distribution
def negative_binomial_distribution(r: int, p: float, x: int) -> None:
    st.write("# Negative Binomial Distribution")

    st.write(f"""
    Given:
    - r (number of successes) = {r}
    - p (probability of success in each trial) = {p}
    - x (number of failures before achieving r successes) = {x}
             """)


def distribution_function(r: int, p: float, x: int) -> None:
    st.write("---\n### Negative Binomial distribution function")

    st.latex(r"P(X = x) = \binom{x + r - 1}{r - 1}~p^r~(1 - p)^x")

    st.write("where")
    st.latex(r"\binom{x + r - 1}{r - 1} = \frac{(x + r - 1)!}{(r - 1)! \cdot x!} ")

    st.write("Step 1: Substitute the values in the distribution function")
    st.latex(f"P(X = {x}) = \\binom{{{x + r - 1}}}{{{r - 1}}}~{p}^{r}~(1 - {p})^{x}")

    st.write("Step 2: Solve the equation")
    binomial_coefficient = sp.factorial(x + r - 1) / (sp.factorial(r - 1) * sp.factorial(x))
    term_1 = p**r
    term_2 = (1 - p) ** x
    st.latex(f"P(X = {x}) = {dotf(binomial_coefficient)}\\cdot{dotf(term_1)}\\cdot{dotf(term_2)}")
    st.write("Hence,")
    st.latex(f"P(X = {x}) = {dotf(binomial_coefficient * term_1 * term_2)}")


def expected_value(r: int, p: float, x: int) -> None:
    st.write("---\n### Expected Value")
    st.latex(r"E[X] = \frac{r \cdot (1 - p)}{p}")

    st.write("Step 1: Substitute the values in the distribution function")
    st.latex(f"E[X] = \\frac{{{r} \\cdot (1 - {p})}}{{{p}}}")

    st.write("Step 2: Solve the equation")
    term = (r * (1 - p)) / p
    st.latex(f"E[X] = {dotf(term)}")


def variance(r: int, p: float, x: int) -> None:
    st.write("---\n### Variance")
    st.latex(r"Var[X] = \frac{r \cdot (1 - p)}{p^2}")

    st.write("Step 1: Substitute the values in the distribution function")
    st.latex(f"Var[X] = \\frac{{{r} \\cdot (1 - {p})}}{{{p}^2}}")

    st.write("Step 2: Solve the equation")
    term = (r * (1 - p)) / (p**2)
    st.latex(f"Var[X] = {dotf(term)}")


def show_negative_binomial_distribution(expander: DeltaGenerator):
    r = expander.number_input("Enter value for r (number of successes):", value=1, min_value=1, step=1)
    p = expander.number_input(
        "Enter value for p (probability of success in each trial):", value=0.5, min_value=0.0, max_value=1.0
    )
    x = expander.number_input(
        "Enter value for x (number of failures before achieving r successes):", value=1, min_value=0, step=1
    )

    show_distribution_function = expander.checkbox("Show distribution function")
    show_expected_value = expander.checkbox("Show expected value")
    show_variance = expander.checkbox("Show variance")
    if expander.button("Solve"):
        negative_binomial_distribution(r, p, x)
        if show_distribution_function:
            distribution_function(r, p, x)
        if show_expected_value:
            expected_value(r, p, x)
        if show_variance:
            variance(r, p, x)
