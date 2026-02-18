import random


def prob_and_independent(pA: float, pB: float) -> float:
    return pA * pB


def prob_or_disjoint(pA: float, pB: float) -> float:
    return pA + pB


def conditional_probability(pA_and_B: float, pB: float) -> float:
    return pA_and_B / pB


def bayes_posterior_unnormalized(likelihood: float, prior: float) -> float:
    return likelihood * prior
