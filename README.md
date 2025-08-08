# Medical Insurance Cost Prediction with Linear Regression

[![Codespaces Prebuilds](https://github.com/4GeeksAcademy/gperdrizet-linear-regression/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/4GeeksAcademy/gperdrizet-linear-regression/actions/workflows/codespaces/create_codespaces_prebuilds)

A comprehensive machine learning project focused on predicting medical insurance costs using linear regression techniques. This project demonstrates essential data science skills including exploratory data analysis, feature engineering, model optimization, and performance evaluation with real-world healthcare data.


## Project Overview

This project analyzes medical insurance cost data to build predictive models that can estimate insurance charges based on policyholder characteristics. The dataset contains information about 1,338 insurance policyholders and provides hands-on experience with:

- Data loading and exploratory data analysis (EDA)
- Feature encoding and preprocessing
- Linear regression modeling
- Feature engineering and polynomial features
- Model optimization techniques
- Performance evaluation and comparison
- Data imbalance handling with over-sampling


## Getting Started

### Option 1: GitHub Codespaces (Recommended)

1. **Fork the Repository**
   - Click the "Fork" button on the top right of the GitHub repository page
   - 4Geeks students: set 4GeeksAcademy as the owner - 4Geeks pays for your codespace usage. All others, set yourself as the owner
   - Give the fork a descriptive name. 4Geeks students: I recommend including your GitHub username to help in finding the fork if you loose the link
   - Click "Create fork"
   - 4Geeks students: bookmark or otherwise save the link to your fork

2. **Create a GitHub Codespace**
   - On your forked repository, click the "Code" button
   - Select "Create codespace on main"
   - If the "Create codespace on main" option is grayed out - go to your codespaces list from the three-bar menu at the upper left and delete an old codespace
   - Wait for the environment to load (dependencies are pre-installed)

3. **Start Working**
   - Open `notebooks/mvp.ipynb` in the Jupyter interface for the assignment
   - Follow the step-by-step instructions in the notebook
   - Open `notebooks/solution.ipynb` to see the complete solution

### Option 2: Local Development

1. **Prerequisites**
   - Git
   - Python >= 3.10

2. **Fork the repository**
   - Click the "Fork" button on the top right of the GitHub repository page
   - Optional: give the fork a new name and/or description
   - Click "Create fork"

3. **Clone the repository**
   - From your fork of the repository, click the green "Code" button at the upper right
   - From the "Local" tab, select HTTPS and copy the link
   - Run the following commands on your machine, replacing `<LINK>` and `<REPO_NAME>`

   ```bash
   git clone <LINK>
   cd <REPO_NAME>
   ```

4. **Set Up Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Launch Jupyter & start the notebook**
   ```bash
   jupyter notebook notebooks/mvp.ipynb
   ```


## Project Structure

```
├── .devcontainer/           # Development container configuration
├── data/                    # Data directory
├── models/                  # Model artifacts directory
│
├── notebooks/               # Jupyter notebook directory
│   ├── helper_functions.py  # Custom utility functions
│   ├── mvp.ipynb            # Assignment notebook (MVP)
│   └── solution.ipynb       # Complete solution notebook
│
├── .gitignore              # Files/directories not tracked by git
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Dataset

The dataset contains medical insurance data with the following key features:

### Features:
- **age**: Age of the policyholder (18-64 years)
- **sex**: Gender (categorical: male/female)
- **bmi**: Body Mass Index (15.96-53.13)
- **children**: Number of children covered (0-5)
- **smoker**: Smoking status (categorical: yes/no)
- **region**: Geographic region (categorical: southeast, southwest, northeast, northwest)

### Target Variable:
- **charges**: Insurance charges in USD ($1,121 - $63,770)

### Dataset Characteristics:
- **Size**: 1,338 policyholders
- **Class Imbalance**: ~20% smokers vs 80% non-smokers
- **Target Distribution**: Highly right-skewed with outliers
- **Missing Values**: None

**Note**: This dataset is used for educational purposes to demonstrate machine learning concepts in healthcare cost prediction.


## Learning Objectives

### Part 1: Data Analysis
1. **Data Exploration**: Load and examine the medical insurance dataset
2. **Descriptive Statistics**: Analyze numerical and categorical feature distributions
3. **Feature Relationships**: Explore correlations between features and insurance costs
4. **Data Visualization**: Create histograms, scatter plots, and box plots

### Part 2: Model Development
5. **Data Preprocessing**: Handle categorical encoding and train-test splits
6. **Baseline Modeling**: Establish performance benchmarks
7. **Linear Regression**: Build and evaluate basic linear models
8. **Feature Engineering**: Apply transformations and create polynomial features

### Part 3: Optimization
9. **Feature Scaling**: Implement StandardScaler transformations
10. **Synthetic Features**: Generate polynomial and interaction terms
11. **Class Imbalance**: Address dataset imbalance with over-sampling
12. **Model Comparison**: Evaluate and compare multiple model variants

### Part 4: Evaluation
13. **Performance Metrics**: Calculate RMSE and R² scores
14. **Diagnostic Plots**: Create predicted vs actual and residual plots
15. **Business Impact**: Interpret results in healthcare context

## Model Performance

The project demonstrates progressive model improvement:

| Model | RMSE | R² | Key Insight |
|-------|------|----|-----------| 
| Baseline (Mean) | $12,101 | -0.00 | Simple average prediction |
| Linear Regression | $5,943 | 0.76 | Strong baseline performance |
| Engineered Features | $5,731 | 0.77 | Slight improvement with transformations |
| **Polynomial Features** | **$4,144** | **0.88** | **Best performance with interactions** |
| Over-sampled | $5,731 | 0.77 | Class balancing reduces overall performance |

The final model achieves 88% variance explained with ~31% relative error, demonstrating that feature interactions (especially involving smoking status) are crucial for accurate insurance cost prediction.

## Technologies Used

- **Python 3.11**: Core programming language
- **Pandas 2.3.1**: Data manipulation and analysis
- **NumPy 2.3.2**: Numerical computing
- **Scikit-learn 1.7.1**: Machine learning algorithms and preprocessing
- **Matplotlib 3.10.3**: Data visualization
- **Seaborn 0.13.2**: Statistical data visualization
- **Jupyter 1.1.1**: Interactive development environment

## Key Insights

1. **Smoking Impact**: Smoking status is the strongest predictor, with smokers having 3-4x higher costs
2. **Feature Interactions**: Polynomial features capture important non-linear relationships
3. **Age Effects**: Age shows accelerating cost increases, especially when combined with other risk factors
4. **Class Imbalance**: Over-sampling minority classes can hurt overall performance in regression tasks
5. **Model Complexity**: Simple linear models perform surprisingly well, but feature engineering provides significant gains

## Contributing

This is an educational project. Contributions for improving the analysis or adding new insights are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

