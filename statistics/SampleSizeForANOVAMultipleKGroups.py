from statsmodels.stats.power import FTestAnovaPower

# Define parameters
effect_size = 0.5  # Cohen's d (medium effect); small = 0.2, medium = 0.5, large = 0.8
alpha = 0.05       # Significance level; (5% risk of false positives)
power = 0.8        # Power (1 - β); requires 80% power to detect the effect
n_groups = 3      # Number of groups

analysis = FTestAnovaPower()
sample_size = analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, k_groups=n_groups)

print(f"Required sample size per group: {int(sample_size)}")
