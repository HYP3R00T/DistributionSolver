import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from scipy.stats import nbinom

from distributionsolver.utils import dotf


# Function to calculate the Negative Binomial distribution
def negative_binomial_distribution(r: int, p: float, max_x: int) -> np.ndarray:
    x = np.arange(0, max_x + 1)  # Negative Binomial distribution starts at x=0
    probabilities = nbinom.pmf(x, r, p)
    return x, probabilities


# Function to plot the Negative Binomial distribution
def plot_negative_binomial_distribution(x: np.ndarray, probabilities: np.ndarray, mean: float, variance: float) -> None:
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

    ax.set_xlabel("Number of Failures")
    ax.set_ylabel("Probability")
    ax.set_title("Negative Binomial Distribution")
    ax.set_ylim(0, 1)  # Set y-axis limit to 1
    ax.legend()
    st.pyplot(fig)


# Function to calculate variance and expected value
def calculate_statistics(r: int, p: float) -> None:
    mean = r * (1 - p) / p
    variance = r * (1 - p) / p**2

    return mean, variance


# Streamlit app
def show_negative_binomial_distribution():
    st.write("### Negative Binomial Distribution")
    r = st.slider("Number of successes (r):", min_value=1, max_value=50, value=10, step=1)
    p = st.slider("Probability of success (p):", min_value=0.01, max_value=1.0, value=0.5, step=0.01)
    max_x = st.slider("Maximum number of failures:", min_value=10, max_value=100, value=50, step=1)

    x_values, probabilities = negative_binomial_distribution(r, p, max_x)

    mean, variance = calculate_statistics(r, p)
    plot_negative_binomial_distribution(x_values, probabilities, mean, variance)
