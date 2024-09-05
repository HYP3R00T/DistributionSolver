import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from distributionsolver.interactive_graphs.binomial import show_binomial_distribution
from distributionsolver.interactive_graphs.exponential import show_exponential_distribution
from distributionsolver.interactive_graphs.geometric import show_geometric_distribution
from distributionsolver.interactive_graphs.hypergeometric import show_hypergeometric_distribution
from distributionsolver.interactive_graphs.negative_binomial import show_negative_binomial_distribution
from distributionsolver.interactive_graphs.normal import show_normal_distribution
from distributionsolver.interactive_graphs.poisson import show_poisson_distribution
from distributionsolver.interactive_graphs.uniform import show_uniform_distribution

expander: DeltaGenerator = st.expander("Probability Distribution Visualizer")

# Dropdown for distribution selection
options: list = [
    "Binomial",
    "Hypergeometric",
    "Geometric",
    "Poisson",
    "Negative Binomial",
    "Uniform",
    "Normal",
    "Exponential",
]
chart = expander.selectbox("Select a distribution", options)

if chart == "Binomial":
    show_binomial_distribution()
elif chart == "Hypergeometric":
    show_hypergeometric_distribution()
elif chart == "Geometric":
    show_geometric_distribution()
elif chart == "Poisson":
    show_poisson_distribution()
elif chart == "Negative Binomial":
    show_negative_binomial_distribution()
elif chart == "Uniform":
    show_uniform_distribution()
elif chart == "Normal":
    show_normal_distribution()
elif chart == "Exponential":
    show_exponential_distribution()
