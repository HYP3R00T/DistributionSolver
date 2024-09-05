import streamlit as st
import sympy as sp
from streamlit.delta_generator import DeltaGenerator

from distributionsolver.utils import dotf

# Define symbols
x = sp.symbols("x")


# Function to generate steps for hypergeometric Distribution
def hypergeometric_distribution(N: int, n: int, a: int, x: int) -> None:
    st.write("# Hypergeometric Distribution")

    st.write(f"""
    Given:
    - N (total size of the population) = {N}
    - n (size of the sample drawn from the population) = {n}
    - a (number of successes in the population) = {a}
    - x (number of successes in the sample) = {x}
             """)


def distribution_function(N: int, n: int, a: int, x: int) -> None:
    st.write("---\n### Hypergeometric distribution function")

    st.latex(r"b (x;~n,~a,~N) = \dfrac{\dbinom{a}{x}\dbinom{N - a}{n - x}}{\dbinom{N}{n}}")

    st.write("where")
    st.latex(r"\binom{n}{x} = \frac{n!}{x!(n-x)!} ")

    st.write("Step 1: Substitute the values in the distribution function")

    st.latex(
        "b ({};~{},~{},~{}) = \\dfrac{{\\dbinom{}{}\\dbinom{}{}}}{{\\dbinom{}{}}}".format(
            dotf(x, 0),
            dotf(n, 0),
            dotf(a, 0),
            dotf(N, 0),
            dotf(a, 0),
            dotf(x, 0),
            dotf(N - a, 0),
            dotf(n - x, 0),
            dotf(N, 0),
            dotf(n, 0),
        )
    )

    st.write("Step 2: Solve the equation")
    term_1 = sp.factorial(a) / (sp.factorial(x) * sp.factorial(a - x))
    term_2 = sp.factorial(N - a) / (sp.factorial(n - x) * sp.factorial(N - a - (n - x)))
    term_3 = sp.factorial(N) / (sp.factorial(n) * sp.factorial(N - n))

    st.latex(
        "b ({};~{},~{},~{}) = \\dfrac{{{}\\cdot{}}}{{{}}}".format(
            dotf(x, 0), dotf(n, 0), dotf(a, 0), dotf(N, 0), dotf(term_1, 0), dotf(term_2, 0), dotf(term_3, 0)
        )
    )

    st.write("Hence,")
    st.latex(f"b ({x};~{n},~{a},~{N}) = {dotf(term_1*term_2/term_3)}")


def expected_value(N: int, n: int, a: int, x: int) -> None:
    st.write("---\n### Expected Value")
    st.latex(r"E[X] = \frac{n \cdot a}{N}")

    st.write("Step 1: Substitute the values in the distribution function")
    st.latex(f"E[X] = \\frac{{{n} \\cdot {a}}}{{{N}}}")

    st.write("Step 2: Solve the equation")
    term = (n * a) / N
    st.latex(f"E[X] = {dotf(term)}")


def variance(N: int, n: int, a: int, x: int) -> None:
    st.write("---\n### Variance")
    st.latex(r"Var[X] = n \cdot \frac{a}{N} \cdot \frac{N - a}{N} \cdot \frac{N - n}{N - 1}")

    st.write("Step 1: Substitute the values in the distribution function")
    st.latex(
        f"Var[X] = {n} \\cdot \\frac{{{a}}}{{{N}}} \\cdot \\frac{{{N} - {a}}}{{{N}}} \\cdot \\frac{{{N} - {n}}}{{{N} - 1}}"
    )

    if N == 1:
        st.write("Step 2: Variance is undefined when N = 1 (division by zero)")
        st.latex(r"\text{Variance is undefined for } N = 1.")
    else:
        st.write("Step 2: Solve the equation")
        term = n * (a / N) * ((N - a) / N) * ((N - n) / (N - 1))
        st.latex(f"Var[X] = {dotf(term)}")


def show_hypergeometric_distribution(expander: DeltaGenerator):
    N = expander.number_input("Enter value for N (total size of the set):", value=1, min_value=1, step=1)
    n = expander.number_input(
        "Enter value for n (size of the sample drawn from the total set):", value=1, min_value=1, max_value=N, step=1
    )
    a = expander.number_input(
        "Enter value for a (number of successes in the total set):", value=1, min_value=0, max_value=N, step=1
    )
    x = expander.number_input(
        "Enter value for x (number of successes in the sample):", value=1, min_value=0, max_value=min(a, n), step=1
    )

    show_distribution_function = expander.checkbox("Show distribution function")
    show_expected_value = expander.checkbox("Show expected value")
    show_variance = expander.checkbox("Show variance")
    if expander.button("Solve"):
        hypergeometric_distribution(N, n, a, x)
        if show_distribution_function:
            distribution_function(N, n, a, x)
        if show_expected_value:
            expected_value(N, n, a, x)
        if show_variance:
            variance(N, n, a, x)
