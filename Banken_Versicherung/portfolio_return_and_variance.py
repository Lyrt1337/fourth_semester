import numpy as np

E_R_A = 0.08        # Expected return of Asset A
E_R_B = 0.12        # Expected return of Asset B
W_A = 0.5           # Weight of Asset A in the portfolio
W_B = 0.5           # Weight of Asset B in the portfolio
sigma2_A = 0.04     # Variance of Asset A
sigma2_B = 0.09     # Variance of Asset B
Cov_AB = 0.02       # Covariance between Asset A and Asset B

std_A = np.sqrt(0.04)   # Standard Deviation of Asset A
std_B = np.sqrt(0.09)   # Standard Deviation of Asset B


# slide example + naming
# E(rp) = W_b * E(r_B) + w_S * (E)r_S
# rp = wBrB + wSrS
# rp = portfolio return
# wB = bond weight
# rB = bond return
# wS = stock weight
# rS = stock return

# Expected rate of return on the portfolio

E_R_P = W_A * E_R_A + W_B * E_R_B


# variance of the portfolio
sigma2_P = (W_A ** 2 * sigma2_A) + (W_B ** 2 * sigma2_B) + (2 * W_A * W_B * std_A * std_B * Cov_AB)

print("task 1")
print("Expected Return: ", E_R_P*100)
print("Variance: ", sigma2_P*100)

# Task 2
# Calculated Return and Variance using Python (png = missing_slide2_task2)

# E_R_A = 0.05
# E_R_B = 0.08
# E_R_C = 0.12
# E_R_D = 0.10
# E_R_E = 0.07
# E_R_F = 0.09

E_R = [0.05, 0.08, 0.12, 0.1, 0.07, 0.09]
# weights
# W_A = 0.1
# W_B = 0.2
# W_C = 0.25
# W_D = 0.15
# W_E = 0.2
# W_F = 0.1

W = [0.1, 0.2, 0.25, 0.15, 0.2, 0.1]

# Variances
# sigma2_A = 0.02
# sigma2_B = 0.03
# sigma2_C = 0.04
# sigma2_D = 0.035
# sigma2_E = 0.025
# sigma2_F = 0.03

sigma2 = [0.02, 0.03, 0.04, 0.035, 0.025, 0.03]

# Assuming all covariance betweeen different assets are 0.02 for simplification
Cov = [[0.02 if i != j else sigma2[i] for j in range(6)] for i in range(6)]

# calculating
# E_R_P = W_A * E_R_A + W_B * E_R_B + W_C * E_R_C + W_D * E_R_D + W_E * E_R_E + W_F * E_R_F
E_R_P = sum(W[i] * E_R[i] for i in range(6))
sigma2_P = sum(W[i] * W[j] * Cov[i][j] for i in range(6) for j in range(6))

print("--------------------")
print("task 2")
print(f"Expected Return: {E_R_P*100}%")
print(f"Variance: {sigma2_P * 100}%")
