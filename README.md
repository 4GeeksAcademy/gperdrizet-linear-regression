# Linear Regression: Health Insurance Cost Prediction

[![Codespace Prebuild](https://github.com/4GeeksAcademy/gperdrizet-linear-regression/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/4GeeksAcademy/gperdrizet-linear-regression/actions/workflows/codespaces/create_codespaces_prebuilds)

This repository contains a data science bootcamp assignment focused on linear regression using real-world health insurance data. Students will learn to:

- Build and evaluate linear regression models for cost prediction
- Perform comprehensive exploratory data analysis (EDA)
- Handle mixed data types (categorical and numerical features)
- Apply feature engineering techniques including one-hot encoding, scaling, and polynomial features
- Optimize models through feature transformations and synthetic feature generation
- Compare different modeling approaches including baseline, scaled, engineered, and polynomial models

## Dataset

The assignment uses a health insurance cost dataset containing 1,338 patient records with 7 features. The target variable is `charges` - the medical insurance cost for each patient. Features include:

- **age**: Age of the policyholder (numerical, 18-64 years)
- **sex**: Gender (categorical: male/female) 
- **bmi**: Body Mass Index (numerical, 15.96-53.13)
- **children**: Number of children covered (numerical, 0-5)
- **smoker**: Smoking status (categorical: yes/no) - strongly predictive of costs
- **region**: Geographic region (categorical: southeast, southwest, northeast, northwest)
- **charges**: Insurance charges - target variable (numerical, $1,121-$63,770)

## Repository Structure

- `notebooks/mvp.ipynb`: The main assignment notebook for students to complete.
- `notebooks/solution.ipynb`: The instructor's full solution for reference.
- `data/`: Contains raw, interim, and processed data folders (ignored by git).
- `models/`: Directory for saving trained models (ignored by git).
- `requirements.txt`: List of required Python packages.

## Getting Started

To complete this assignment, you can choose between two options: using GitHub Codespaces (recommended) or setting up a local development environment. Both methods will allow you to run the Jupyter notebook and complete the assignment.

### Option 1: GitHub Codespaces (Recommended)

1. **Fork the Repository**
   - Click the "Fork" button on the top right of the [GitHub repository page](https://github.com/4GeeksAcademy/gperdrizet-linear-regression)
   - This creates your own copy under your GitHub account

2. **Create a GitHub Codespace**
   - On your forked repository, click the "Code" button
   - Select "Create codespace on main" 
   - Wait for the environment to load (dependencies are pre-installed)

3. **Start Working**
   - Open `notebooks/mvp.ipynb` in the Jupyter interface
   - Follow the step-by-step instructions in the notebook

### Option 2: Local Development

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/gperdrizet-linear-regression.git
   cd gperdrizet-linear-regression
   ```

2. **Set Up Environment**
   ```bash
   # Create virtual environment (recommended)
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Launch Jupyter**
   ```bash
   jupyter notebook notebooks/mvp.ipynb
   ```

## Assignment Overview

The `mvp.ipynb` notebook guides you through:

1. **Data Loading & Inspection** - Load insurance data from URL, save local copy, and explore the dataset structure
2. **Exploratory Data Analysis (EDA)** - Analyze feature distributions and relationships with target variable
   - Descriptive statistics for numerical features
   - Distribution plots and categorical feature analysis
   - Feature-target correlation analysis
3. **Data Preparation** - Prepare data for machine learning
   - Train-test split (80/20)
   - One-hot encoding for categorical variables
4. **Model Training & Evaluation** - Build and compare different modeling approaches
   - Baseline model (mean prediction)
   - Standard linear regression
   - Feature scaling with StandardScaler
   - Feature engineering (transformations)
   - Polynomial features for capturing interactions
   - Optional: Over-sampling for class balance
5. **Model Comparison & Selection** - Compare performance across all models using RMSE and R²
6. **Final Model Evaluation** - Detailed analysis of the best-performing model with diagnostic plots

### Key Concepts Covered

- **Baseline Model Performance**: Using mean prediction as a performance benchmark
- **Feature Engineering**: One-hot encoding categorical variables, feature scaling with StandardScaler
- **Model Evaluation**: RMSE and R² metrics, predicted vs. actual plots, residual analysis
- **Advanced Feature Engineering**: Non-linear transformations, polynomial feature generation
- **Feature Interactions**: Capturing complex relationships between variables (age × smoking, BMI × smoking, etc.)
- **Class Imbalance Handling**: Over-sampling techniques for minority classes (smokers)
- **Data Visualization**: Comprehensive EDA using matplotlib and seaborn

## Working on the Assignment

- Complete the sections marked with comments asking for implementation (e.g., "Take a look at some descriptive statistics...")
- Run cells sequentially to maintain proper data flow
- Experiment with different feature engineering approaches in the optimization section
- Document your observations and findings in the provided markdown cells
- Pay attention to model performance improvements at each step
- The assignment progresses from simple baseline to advanced polynomial models

## Expected Learning Outcomes

By completing this assignment, you will:
- Understand how to establish and improve upon baseline model performance
- Learn effective EDA techniques for understanding feature-target relationships
- Master feature engineering techniques including encoding and scaling
- Gain experience with polynomial features and interaction terms
- Develop skills in model comparison and evaluation
- Learn to interpret residual plots and diagnostic visualizations

## Requirements

The environment is pre-configured with the following packages (see [`requirements.txt`](requirements.txt)):

- **pandas** (2.3.1) - Data manipulation and analysis
- **matplotlib** (3.10.3) - Basic plotting and visualization  
- **seaborn** (0.13.2) - Statistical data visualization
- **scikit-learn** (1.7.1) - Machine learning library
- **numpy** (2.3.2) - Numerical computing
- **scipy** (1.16.1) - Scientific computing
- **pyarrow** (21.0.0) - For reading Parquet files
- **ipykernel** (6.30.0) - Jupyter notebook kernel

## Instructor Solution

**For Students**: Try to complete the assignment on your own first before looking at the solution. The learning happens in the struggle!

If you need guidance or want to check your work, refer to the instructor's solution in [`notebooks/solution.ipynb`](notebooks/solution.ipynb).

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all packages from `requirements.txt` are installed
2. **Kernel Issues**: Restart the kernel if variables seem undefined  
3. **Data Loading**: The notebook downloads data from URL automatically, but ensure internet connection
4. **Feature Engineering**: Pay careful attention to train-test split - apply transformations fitted on training data only
5. **Polynomial Features**: Be aware that polynomial features create many new columns (can cause memory issues)

### Getting Help

- Review the instructor solution in `notebooks/solution.ipynb` if you're stuck
- Check the scikit-learn documentation for specific functions
- Pay attention to the data preparation steps, as proper feature engineering is crucial
- The `helper_functions.py` file contains utility functions for encoding and level counting
- Focus on understanding the progression from simple to complex models

## Additional Resources

- [Scikit-learn Linear Models](https://scikit-learn.org/stable/modules/linear_model.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
