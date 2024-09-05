import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from scipy.stats import hypergeom

from distributionsolver.utils import dotf


# Function to calculate the hypergeometric distribution
def hypergeometric_distribution(N: int, n: int, a: int) -> np.ndarray:
    x = np.arange(0, min(a, n) + 1)
    probabilities = hypergeom.pmf(x, N, a, n)
    return x, probabilities


# Function to plot the hypergeometric distribution
def plot_hypergeometric_distribution(x: np.ndarray, probabilities: np.ndarray, mean: float, variance: float) -> None:
    fig, ax = plt.subplots()
    ax.bar(x, probabilities, color="skyblue", edgecolor="black")

    # Plot mean line
    ax.axvline(mean, color="red", linestyle="dashed", linewidth=1, label=f"Mean: {dotf(mean)}")

    # Plot variance boundaries
    left_boundary = mean - np.sqrt(variance)
    right_boundary = mean + np.sqrt(variance)
    ax.axvline(
        left_boundary, color="green", linestyle="dotted", linewidth=1, label=f"Lower Bound: {dotf(left_boundary)}"
    )
    ax.axvline(
        right_boundary, color="blue", linestyle="dotted", linewidth=1, label=f"Upper Bound: {dotf(right_boundary)}"
    )

    ax.set_xlabel("Number of Successes")
    ax.set_ylabel("Probability")
    ax.set_title("Hypergeometric Distribution")
    ax.set_ylim(0, 1)  # Set y-axis limit to 1
    ax.legend()
    st.pyplot(fig)


# Function to calculate variance and expected value
def calculate_statistics(N: int, n: int, a: int) -> None:
    mean = n * a / N
    variance = n * (a / N) * ((N - a) / N) * ((N - n) / (N - 1))

    return mean, variance


# Streamlit app
def show_hypergeometric_distribution():
    st.write("### Hypergeometric Distribution")
    N = st.slider("Total size of the population (N):", min_value=1, max_value=1000, value=50, step=1)
    n = st.slider("Number of trials (n):", min_value=1, max_value=N, value=10, step=1)
    a = st.slider("Number of successes in the population (a):", min_value=0, max_value=N, value=5, step=1)

    x_values, probabilities = hypergeometric_distribution(N, n, a)

    mean, variance = calculate_statistics(N, n, a)
    plot_hypergeometric_distribution(x_values, probabilities, mean, variance)
