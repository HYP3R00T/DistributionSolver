import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

from distributionsolver.utils import dotf


# Function to calculate the Uniform distribution
def uniform_distribution(a: float, b: float, num_points: int = 100) -> np.ndarray:
    x = np.linspace(-100, 100, num_points)  # Constant range for x-axis
    probabilities = np.zeros_like(x)
    probabilities[(x >= a) & (x <= b)] = 1 / (b - a)  # Uniform probability density
    return x, probabilities


# Function to plot the Uniform distribution
def plot_uniform_distribution(x: np.ndarray, probabilities: np.ndarray, mean: float, variance: float) -> None:
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

    ax.set_xlim(-100, 100)  # Set x-axis limit to constant range
    ax.set_ylim(0, 1)  # Set y-axis limit to constant value
    ax.set_xlabel("Value")
    ax.set_ylabel("Probability Density")
    ax.set_title("Uniform Distribution")
    ax.legend()
    st.pyplot(fig)


# Function to calculate variance and expected value
def calculate_statistics(a: float, b: float) -> None:
    mean = (a + b) / 2
    variance = (b - a) ** 2 / 12

    return mean, variance


# Streamlit app
def show_uniform_distribution():
    st.write("### Uniform Distribution")
    a = st.slider("Lower bound (a):", min_value=-100.0, max_value=100.0, value=-1.0, step=0.1)
    b = st.slider("Upper bound (b):", min_value=-100.0, max_value=100.0, value=1.0, step=0.1)

    # Ensure that b > a
    if b <= a:
        st.error("Upper bound must be greater than lower bound.")
        return

    x_values, probabilities = uniform_distribution(a, b)

    mean, variance = calculate_statistics(a, b)
    plot_uniform_distribution(x_values, probabilities, mean, variance)
