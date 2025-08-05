# Linear Regression: Health Insurance Cost Prediction

[![Codespace Prebuild](https://github.com/4GeeksAcademy/gperdrizet-linear-regression/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/4GeeksAcademy/gperdrizet-linear-regression/actions/workflows/codespaces/create_codespaces_prebuilds)

This repository contains a data science bootcamp assignment focused on linear regression using real-world health insurance data. Students will learn to:

- Build and evaluate linear regression models for cost prediction
- Perform comprehensive exploratory data analysis (EDA)
- Handle mixed data types (categorical and numerical features)
- Apply feature engineering techniques including encoding and scaling
- Optimize models through feature selection and data transformations
- Compare baseline, single, and split model performance approaches

## Dataset

The assignment uses a health insurance cost dataset containing patient information and associated medical charges. The target variable is `charges` - the medical insurance cost for each patient. Features include demographic information (age, sex, region), health indicators (BMI, smoking status), and family information (number of children).

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

1. **Data Loading & Inspection** - Load and explore the health insurance dataset
2. **Exploratory Data Analysis (EDA)** - Analyze target variable and feature distributions, establish baseline model performance
3. **Feature Engineering** - Handle categorical variables, apply scaling, and prepare data for modeling
4. **Linear Model Training** - Build and evaluate linear regression models
5. **Model Optimization** - Explore advanced techniques like split modeling and feature transformations
6. **Final Evaluation** - Compare model performance and analyze results

### Key Concepts Covered

- **Baseline Model Performance**: Understanding simple prediction benchmarks
- **Feature Engineering**: One-hot encoding, standardization, and feature transformations
- **Model Evaluation**: RMSE calculation and residual analysis
- **Advanced Modeling**: Split model approaches based on categorical features (smoker vs. non-smoker)
- **Data Visualization**: Using matplotlib and seaborn for EDA and model evaluation

## Working on the Assignment

- Complete the sections marked with `# Your code here...`
- Run cells sequentially to maintain proper data flow
- Experiment with different feature engineering approaches
- Document your observations and findings in markdown cells

## Requirements

The environment is pre-configured with the following packages (see [`requirements.txt`](requirements.txt)):

- pandas - Data manipulation and analysis
- matplotlib - Basic plotting and visualization
- seaborn - Statistical data visualization
- scikit-learn - Machine learning library
- numpy - Numerical computing
- scipy - Scientific computing

## Instructor Solution

**For Students**: Try to complete the assignment on your own first before looking at the solution. The learning happens in the struggle!

If you need guidance or want to check your work, refer to the instructor's solution in [`notebooks/solution.ipynb`](notebooks/solution.ipynb).

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all packages from `requirements.txt` are installed
2. **Kernel Issues**: Restart the kernel if variables seem undefined

### Getting Help

- Review the instructor solution in `notebooks/solution.ipynb` if you're stuck
- Check the scikit-learn documentation for specific functions
- Pay attention to the data preparation steps, as proper feature engineering is crucial

## Additional Resources

- [Scikit-learn Linear Models](https://scikit-learn.org/stable/modules/linear_model.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
