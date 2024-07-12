# Linear Regression Using Normal Equation (easy)

Write a Python function that performs linear regression using the normal equation. The function should take a matrix X (features) and a vector y (target) as input, and return the coefficients of the linear regression model. Round your answer to four decimal places, -0.0 is a valid result for rounding a very small number.

# Learn 
Linear regression aims to model the relationship between a scalar dependent variable and one or more explanatory variables (or independent variables). The normal equation provides an analytical solution to finding the coefficients that minimize the cost function for linear regression. Given a matrix (with each row representing a training example and each column a feature) and a vector (representing the target values), the normal equation is:

![Image](//Easy/Linear%20Regression%20Using%20Normal%20Equation/screenshot.png")

# Practical Implementation
A practical implementation involves augmenting X with a column of ones to account for the intercept term and then applying the normal equation directly to compute  $\theta$.