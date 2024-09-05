import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from scipy.stats import expon

from distributionsolver.utils import dotf


# Function to calculate the Exponential distribution
def exponential_distribution(scale: float, num_points: int = 100) -> np.ndarray:
    x = np.linspace(0, 10 * scale, num_points)  # Fixed x-axis range to cover typical values
    probabilities = expon.pdf(x, scale=scale)
    return x, probabilities


# Function to plot the Exponential distribution
def plot_exponential_distribution(x: np.ndarray, probabilities: np.ndarray, mean: float, variance: float) -> None:
    fig, ax = plt.subplots()
    ax.plot(x, probabilities, color="skyblue")
    ax.fill_between(x, 0, probabilities, color="skyblue", alpha=0.5)

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

    ax.set_xlim(0, 10 * mean)  # Set x-axis limits to a fixed range based on the scale parameter
    ax.set_ylim(
        0, max(max(probabilities) * 1.1, 1)
    )  # Set y-axis limit to a fixed value slightly above the max probability
    ax.set_xlabel("Value")
    ax.set_ylabel("Probability Density")
    ax.set_title("Exponential Distribution")
    ax.legend()
    st.pyplot(fig)


# Function to calculate mean and variance
def calculate_statistics(scale: float) -> None:
    mean = scale
    variance = scale**2

    return mean, variance


# Streamlit app
def show_exponential_distribution():
    st.write("### Exponential Distribution")
    scale = st.slider("Scale (λ):", min_value=0.1, max_value=10.0, value=1.0, step=0.1)

    x_values, probabilities = exponential_distribution(scale)

    mean, variance = calculate_statistics(scale)
    plot_exponential_distribution(x_values, probabilities, mean, variance)
