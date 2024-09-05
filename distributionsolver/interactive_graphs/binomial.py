import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from scipy.stats import binom

from distributionsolver.utils import dotf


# Function to calculate the binomial distribution
def binomial_distribution(n: int, p: float) -> np.ndarray:
    x = np.arange(0, n + 1)
    probabilities = binom.pmf(x, n, p)
    return x, probabilities


# Function to plot the binomial distribution
def plot_binomial_distribution(x: np.ndarray, probabilities: np.ndarray, mean: float, variance: float) -> None:
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
    ax.set_title("Binomial Distribution")
    ax.set_ylim(0, 1)  # Set y-axis limit to 1
    ax.legend()
    st.pyplot(fig)


# Function to calculate variance and expected value
def calculate_statistics(n: int, p: float) -> None:
    mean = n * p
    variance = n * p * (1 - p)

    return mean, variance


# Streamlit app
def show_binomial_distribution():
    st.write("### Binomial Distribution")
    n = st.slider("Number of trials (n):", min_value=1, max_value=100, value=10, step=1)
    p = st.slider("Probability of success (p):", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

    x_values, probabilities = binomial_distribution(n, p)

    mean, variance = calculate_statistics(n, p)
    plot_binomial_distribution(x_values, probabilities, mean, variance)
