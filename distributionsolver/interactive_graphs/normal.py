import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from scipy.stats import norm

from distributionsolver.utils import dotf


# Function to calculate the Normal distribution
def normal_distribution(mu: float, sigma: float, num_points: int = 100) -> np.ndarray:
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, num_points)  # Adjust x range based on mean and sigma
    probabilities = norm.pdf(x, mu, sigma)
    return x, probabilities


# Function to plot the Normal distribution
def plot_normal_distribution(x: np.ndarray, probabilities: np.ndarray, mean: float, variance: float) -> None:
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

    # ax.set_xlim(mean - 4 * np.sqrt(variance), mean + 4 * np.sqrt(variance))  # Set x-axis limits to include 4 std devs
    ax.set_xlim(-50, 50)  # Set x-axis limits to include 4 std devs
    ax.set_ylim(0, 1)  # Set y-axis limit to constant value
    ax.set_xlabel("Value")
    ax.set_ylabel("Probability Density")
    ax.set_title("Normal Distribution")
    ax.legend()
    st.pyplot(fig)


# Function to calculate variance and expected value
def calculate_statistics(mu: float, sigma: float) -> None:
    mean = mu
    variance = sigma**2

    return mean, variance


# Streamlit app
def show_normal_distribution():
    st.write("### Normal Distribution")
    mu = st.slider("Mean (μ):", min_value=-50.0, max_value=50.0, value=0.0, step=0.1)
    sigma = st.slider("Standard Deviation (σ):", min_value=0.1, max_value=10.0, value=1.0, step=0.1)

    x_values, probabilities = normal_distribution(mu, sigma)

    mean, variance = calculate_statistics(mu, sigma)
    plot_normal_distribution(x_values, probabilities, mean, variance)
