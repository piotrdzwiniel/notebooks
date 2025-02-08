from statsmodels.stats.power import TTestIndPower

# Define parameters
effect_size = 1.0  # Cohen's d (medium effect); small = 0.2, medium = 0.5, large = 0.8
alpha = 0.01       # Significance level; (5% risk of false positives)
power = 0.8        # Power (1 - β); requires 80% power to detect the effect
ratio = 1.0        # Assumes equal group sizes

# Compute required sample size per group
analysis = TTestIndPower()
sample_size = analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, ratio=ratio)

print(f"Required sample size per group: {int(sample_size)}")