import streamlit as st
import sympy as sp
from streamlit.delta_generator import DeltaGenerator

from distributionsolver.utils import dotf

# Define symbols
x = sp.symbols("x")


# Function to generate steps for Binomial Distribution
def binomial_distribution(n: int, p: float, x: int) -> None:
    st.write("# Binomial Distribution")

    st.write(f"""
    Given:
    - n (number of trials) = {n}
    - p (probability of success in each trial) = {p}
    - x (number of successes) = {x}
             """)


def distribution_function(n: int, p: float, x: int) -> None:
    st.write("---\n### Binomial distribution function")

    st.latex(r"b (x;~n,~p) = \binom{n}{x}~p^x~(1-p)^{n-x}")

    st.write("where")
    st.latex(r"\binom{n}{x} = \frac{n!}{x!(n-x)!} ")

    st.write("Step 1: Substitute the values in the distribution function")
    st.latex(f"b ({x};~{n},~{p}) = \\binom{{{n}}}{{{x}}}~{p}^{x}~(1-{p})^{n-x}")

    st.write("Step 2: Solve the equation")
    binomial_coefficient = sp.factorial(n) / (sp.factorial(x) * sp.factorial(n - x))
    term_1 = p**x
    term_2 = (1 - p) ** (n - x)
    st.latex(f"b ({x};~{n},~{p}) = {dotf(binomial_coefficient)}\\cdot{dotf(term_1)}\\cdot{dotf(term_2)}")
    st.write("Hence,")
    st.latex(f"b ({x};~{n},~{p}) = {dotf(binomial_coefficient*term_1*term_2)}")


def expected_value(n: int, p: float, x: int) -> None:
    st.write("---\n### Expected Value")
    st.latex(r"E[X] = np")

    st.write("Step 1: Substitute the values in the distribution function")
    st.latex(f"E[X] = {n}\\cdot{p}")

    st.write("Step 2: Solve the equation")
    term = n * p
    st.latex(f"E[X] = {dotf(term)}")


def variance(n: int, p: float, x: int) -> None:
    st.write("---\n### Variance")
    st.latex(r"Var[X] = np (1 - p)")

    st.write("Step 1: Substitute the values in the distribution function")
    st.latex(f"Var[X] = {n} \\cdot {p} \\cdot ( 1 - {p})")

    st.write("Step 2: Solve the equation")
    term = n * p * (1 - 0)
    st.latex(f"Var[X] = {dotf(term)}")


def show_binomial_distribution(expander: DeltaGenerator):
    n = expander.number_input("Enter value for n (number of trials):", value=1)
    p = expander.number_input(
        "Enter value for p (probability of success in each trial):", value=0.5, min_value=0.0, max_value=1.0
    )
    x = expander.number_input("Enter value for x (number of successes):", value=1, max_value=n)
    show_distribution_function = expander.checkbox("Show distribution function")
    show_expected_value = expander.checkbox("Show expected value")
    show_variance = expander.checkbox("Show variance")
    if expander.button("Solve"):
        binomial_distribution(n, p, x)
        if show_distribution_function:
            distribution_function(n, p, x)
        if show_expected_value:
            expected_value(n, p, x)
        if show_variance:
            variance(n, p, x)
