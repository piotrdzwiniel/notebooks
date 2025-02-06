from statsmodels.stats.power import TTestIndPower

# Define parameters
effect_size = 1.0  # Cohen's d (medium effect)
alpha = 0.05       # Significance level
sample_size = 20   # Number of participants per group

# Compute power
analysis = TTestIndPower()
power = analysis.solve_power(effect_size=effect_size, alpha=alpha, nobs1=sample_size)

"""
Power = 0.80 --> 80% chance of detecting a real effect
Power = 0.50 --> 50% chance (like flipping a coin - unreliable)
Power = 0.95 --> Very high chance of detectign an effect
"""

print(f"Power: {power:.4f}")  # Should be close to 0.8 for a typical study

