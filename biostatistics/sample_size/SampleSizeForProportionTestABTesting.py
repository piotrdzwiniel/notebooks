from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Define expected proportions
p1 = 0.5  # Baseline conversion rate
p2 = 0.6  # Expected improvement

effect_size = proportion_effectsize(p1, p2)  # Compute effect size for proportions
analysis = NormalIndPower()
sample_size = analysis.solve_power(effect_size=effect_size, alpha=0.05, power=0.8, ratio=1)

print(f"Required sample size per group: {int(sample_size)}")
