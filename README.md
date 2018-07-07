# Notes

## Over-fitting
Overfitting refers to a model that models the training data too well.

## Feature Scaling
Standardize the range of independent variables. It is splitted into standardization and normalization.

### Standardization
![Standardization](resource/standardization.png)

### Normalization
![Normalization](resource/normalization.png)

### Simple Linear Regression

![SimpleLinearRegressionEquation](resource/simple-linear-regression.png)

![salary-linear-regression](resource/salary-linear-regression.png)
1. The Bias is basically where the line starts on the y-axis.

2. We plot a linear regression line with the training set of features and labels. When we apply the model to predict a value, the predicted value is calculated by the given feature in relation to that linear regression line. Basically with a given feature(X) we find where it lands on in the linear regression line which provides the label(Y). In other words, the linear regression line is a set of predicted values.

3. This model only works well when there is linear dependency. Which means the provided training set falls nicely along a linear regression line without outliers data points.

4. Positive Linear Relationship: The regression line slopes upward with the lower end of the line at the y intercept (axis) of the graph, and the upper end of line extending upward into the graph field, away from the x intercept (axis). In other words, the line goes upward

5. Negative Linear Relationship: The regression line slopes downward with the upper end of the line at the y intercept (axis) of the graph, and the lower end of line extending downward into the graph field, toward the x intercept (axis). In other words, the line goes downward 

6. No Relationship: There is no slope in the line, the line is flat.
