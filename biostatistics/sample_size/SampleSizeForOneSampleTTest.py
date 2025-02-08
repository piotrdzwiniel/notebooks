from statsmodels.stats.power import TTestPower

# Define parameters
effect_size = 0.5  # Cohen's d (medium effect); small = 0.2, medium = 0.5, large = 0.8
alpha = 0.05       # Significance level; (5% risk of false positives)
power = 0.8        # Power (1 - β); requires 80% power to detect the effect

analysis = TTestPower()
sample_size = analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power)

print(f"Required sample size: {int(sample_size)}")
