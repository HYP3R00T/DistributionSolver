import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from scipy.stats import poisson

from distributionsolver.utils import dotf


# Function to calculate the Poisson distribution
def poisson_distribution(lambda_: float, max_x: int) -> np.ndarray:
    x = np.arange(0, max_x + 1)  # Poisson distribution starts at x=0
    probabilities = poisson.pmf(x, lambda_)
    return x, probabilities


# Function to plot the Poisson distribution
def plot_poisson_distribution(x: np.ndarray, probabilities: np.ndarray, mean: float, variance: float) -> None:
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

    ax.set_xlabel("Number of Events")
    ax.set_ylabel("Probability")
    ax.set_title("Poisson Distribution")
    ax.set_ylim(0, 1)  # Set y-axis limit to 1
    ax.legend()
    st.pyplot(fig)


# Function to calculate variance and expected value
def calculate_statistics(lambda_: float) -> None:
    mean = lambda_
    variance = lambda_

    return mean, variance


# Streamlit app
def show_poisson_distribution():
    st.write("### Poisson Distribution")
    lambda_ = st.slider("Lambda (rate of occurrence):", min_value=0.1, max_value=20.0, value=5.0, step=0.1)
    max_x = st.slider("Maximum number of events:", min_value=10, max_value=100, value=50, step=1)

    x_values, probabilities = poisson_distribution(lambda_, max_x)

    mean, variance = calculate_statistics(lambda_)
    plot_poisson_distribution(x_values, probabilities, mean, variance)
