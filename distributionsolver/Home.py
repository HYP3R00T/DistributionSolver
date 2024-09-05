import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from distributionsolver.distributions.binomial import show_binomial_distribution
from distributionsolver.distributions.exponential import show_exponential_distribution
from distributionsolver.distributions.geometric import show_geometric_distribution
from distributionsolver.distributions.hypergeometric import show_hypergeometric_distribution
from distributionsolver.distributions.negative_binomial import show_negative_binomial_distribution
from distributionsolver.distributions.normal import show_normal_distribution
from distributionsolver.distributions.poisson import show_poisson_distribution
from distributionsolver.distributions.uniform import show_uniform_distribution

expander: DeltaGenerator = st.expander("Probability Distribution Solver")

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
distribution = expander.selectbox("Select a distribution", options)

if distribution == "Binomial":
    show_binomial_distribution(expander)
elif distribution == "Hypergeometric":
    show_hypergeometric_distribution(expander)
elif distribution == "Geometric":
    show_geometric_distribution(expander)
elif distribution == "Poisson":
    show_poisson_distribution(expander)
elif distribution == "Negative Binomial":
    show_negative_binomial_distribution(expander)
elif distribution == "Uniform":
    show_uniform_distribution(expander)
elif distribution == "Normal":
    show_normal_distribution(expander)
elif distribution == "Exponential":
    show_exponential_distribution(expander)
