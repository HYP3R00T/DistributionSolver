import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from scipy.stats import geom

from distributionsolver.utils import dotf


# Function to calculate the geometric distribution
def geometric_distribution(p: float, max_x: int) -> np.ndarray:
    x = np.arange(1, max_x + 1)  # Geometric distribution starts at x=1
    probabilities = geom.pmf(x, p)
    return x, probabilities


# Function to plot the geometric distribution
def plot_geometric_distribution(x: np.ndarray, probabilities: np.ndarray, mean: float, variance: float) -> None:
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

    ax.set_xlabel("Number of Trials")
    ax.set_ylabel("Probability")
    ax.set_title("Geometric Distribution")
    ax.set_ylim(0, 1)  # Set y-axis limit to 1
    ax.legend()
    st.pyplot(fig)


# Function to calculate variance and expected value
def calculate_statistics(p: float) -> None:
    mean = 1 / p
    variance = (1 - p) / (p**2)

    return mean, variance


# Streamlit app
def show_geometric_distribution():
    st.write("### Geometric Distribution")
    p = st.slider("Probability of success (p):", min_value=0.01, max_value=1.0, value=0.5, step=0.01)
    max_x = st.slider("Maximum number of trials:", min_value=10, max_value=100, value=50, step=1)

    x_values, probabilities = geometric_distribution(p, max_x)

    mean, variance = calculate_statistics(p)
    plot_geometric_distribution(x_values, probabilities, mean, variance)
