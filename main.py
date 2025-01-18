import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Common setup
np.random.seed(42)
n_samples = 100
outliers1 = 95 ## values that you need to modify to change outliers proportion
outliers2 = 80
X_raw = np.random.normal(size=n_samples)
X = sm.add_constant(X_raw)  # Add intercept

def run_regressions_and_plot(Y, ax, title_suffix):
    # Fit LAD (Robust Linear Model)
    lad_model = sm.RLM(Y, X, M=sm.robust.norms.HuberT())
    lad_results = lad_model.fit()
    Y_pred_lad = lad_results.predict(X)
    
    # Fit OLS (Ordinary Least Squares)
    ols_model = sm.OLS(Y, X)
    ols_results = ols_model.fit()
    Y_pred_ols = ols_results.predict(X)
    
    # Plot on the provided axes
    ax.scatter(X_raw, Y, label='Data', alpha=0.7)
    ax.plot(X_raw, Y_pred_lad, color='red', label='LAD Fit')
    ax.plot(X_raw, Y_pred_ols, color='blue', linestyle='--', label='OLS Fit')
    ax.set_title(f"Regression Comparison ({title_suffix})")
    ax.set_xlabel("Predictor")
    ax.set_ylabel("Response")
    ax.legend()

# Scenario 1: Outliers at Y[95:]
Y1 = 2 * X[:, 1] + np.random.normal(size=n_samples)
Y1[outliers1:] += 20  # Introduce outliers in the last 5 points

# Scenario 2: Outliers at Y[70:]
Y2 = 2 * X[:, 1] + np.random.normal(size=n_samples)
Y2[outliers2:] += 20  # Introduce outliers in the last 30 points

# Create subplots (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Run regressions and plot on both subplots
run_regressions_and_plot(Y1, ax1, "Outliers from index "+ str(outliers1) +" to end")
run_regressions_and_plot(Y2, ax2, "Outliers from index "+str(outliers2)+ " to end")

# Show the plots
plt.tight_layout()
plt.show()
