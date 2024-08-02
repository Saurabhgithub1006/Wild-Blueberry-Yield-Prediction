# <span style="color: blue;">Wild Blueberry Yield Prediction</span>

 [Wild Blueberry streamlit app link](https://wild-blueberry-yield-prediction-bmjmre38bgfuvhkkn8ccbs.streamlit.app/)

 
![Image](https://github.com/Saurabhgithub1006/Wild-Blueberry-Yield-Prediction/blob/main/AppVideo-ezgif.com-video-to-gif-converter.gif?raw=true)


## About Dataset:
The dataset used for predictive modelling was generated by the Wild Blueberry Pollination Simulation Model, which is an open-source, spatially-explicit computer simulation program, that enables exploration of how various factors, including plant spatial arrangement, outcrossing and self-pollination, bee species compositions and weather conditions, in isolation and combination, affect pollination efficiency and yield of the wild blueberry agro-ecosystem.

The simulation model has been validated by the field observation and experimental data collected in Maine USA and Canadian Maritimes during the last 30 years and now is a useful tool for hypothesis testing and theory development for wild blueberry pollination researches. This simulated data provides researchers who have actual data collected from field observation and those who wants to experiment the potential of machine learning algorithms response to real data and computer simulation modelling generated data as input for crop yield prediction models.
![Image](https://github.com/Saurabhgithub1006/Wild-Blueberry-Yield-Prediction/blob/main/Screenshot%20(302).png?raw=true.jpg)

## Problem Statement:
The target feature is yield which is a continuous variable. The task is to classify this variable based on the other 17 features step-by-step by going through each day's task. The evaluation metrics will be RMSE score.
![Image]( https://img.freepik.com/free-vector/fresh-blueberries-with-water-drops-green-leaves-white-background-realistic-vector-illustration_1284-77363.jpg)


# Project Overview
This project aims to predict the yield of wild blueberries using data generated by the Wild Blueberry Pollination Simulation Model. The simulation model considers various factors such as plant spatial arrangement, bee species compositions, and weather conditions, affecting pollination efficiency and yield.

# Dataset
* Source: Wild Blueberry Pollination Simulation Model
* Description:
  + Open-source, spatially-explicit computer simulation program.
  + Validated by field observation and experimental data collected over the last 30 years in Maine, USA, and the Canadian Maritimes.
  + Useful for hypothesis testing and theory development in wild blueberry pollination research.
* Features: 17 features
* Instances: Simulated data for various environmental and soil conditions
* Target Feature: Yield (continuous variable)
# Objective
* To predict the yield of wild blueberries based on 17 features, using machine learning techniques, with the RMSE score as the evaluation metric.

# Approach
* Data Preprocessing:

 + Handled missing values.
 + Normalized features.
 + Created new variables to improve model performance.
* Feature Engineering:

Engineered features such as average temperature during the growing season and rainfall patterns.
Used SelectKBest for feature selection to identify the most impactful variables for yield prediction.
* Model Development:

Built and tuned several machine learning models, including:
Linear Regression
Random Forest
Decision Tree
Gradient Boosting
* Evaluation:

Evaluated model performance using cross-validation and testing on holdout datasets.
Optimized the model by tuning hyperparameters and validating on unseen data to prevent overfitting.
# Results
* Best Model: Random Forest
* Performance Metrics:
RMSE: 10
R-squared: 0.80
# Deployment
* Platform: Streamlit
* Functionality: Developed an interactive web application to visualize and predict wild blueberry yields.
# Conclusion
* The developed machine learning model effectively predicts wild blueberry yield based on environmental factors and soil properties, achieving a robust performance with an RMSE of 10 and an R-squared of 0.80.





