# Enhanced Ensemble Methods for Wisconsin Breast Cancer Classification

## 🔬 Research Overview

This is an **optimized and elongated** version of the capstone research project on breast cancer classification using ensemble machine learning methods. The project analyzes the Wisconsin Breast Cancer Dataset (WBCD) to predict whether a tumor is benign or malignant based on 30 cytological characteristics.

**Author:** Derek Lankeaux
**Institution:** Rochester Institute of Technology (RIT)
**Program:** MS Applied Statistics
**Original Course:** STAT 790 - Capstone Project

---

## ✨ Enhancements Over Original Research

### 1. **Advanced Methodologies**
- ✅ **VIF Analysis** - Comprehensive multicollinearity assessment
- ✅ **SMOTE** - Synthetic Minority Over-sampling for class imbalance handling
- ✅ **Stratified Cross-Validation** - Better evaluation on imbalanced datasets
- ✅ **RFE** - Recursive Feature Elimination for optimal feature selection

### 2. **Additional Ensemble Methods**
- ✅ **XGBoost** - State-of-the-art gradient boosting
- ✅ **LightGBM** - Fast and efficient gradient boosting framework
- ✅ **Voting Classifier** - Soft voting ensemble combining multiple models
- ✅ **Stacking Classifier** - Meta-learning with Logistic Regression

### 3. **Comprehensive Evaluation**
- ✅ **ROC-AUC Analysis** - ROC curves and AUC scores for all models
- ✅ **Learning Curves** - Model performance vs. training set size
- ✅ **Feature Importance** - Analysis of most discriminative features
- ✅ **Multi-metric Comparison** - Accuracy, Precision, Recall, F1, ROC-AUC

### 4. **Code Quality & Production Readiness**
- ✅ **Modular Functions** - Reusable evaluation and visualization utilities
- ✅ **Model Persistence** - Saved models ready for deployment
- ✅ **Professional Visualizations** - Publication-quality plots and comparisons
- ✅ **Comprehensive Documentation** - Clear explanations and comments

---

## 📊 Dataset

**Wisconsin Diagnostic Breast Cancer (WDBC) Dataset**

- **Samples:** 569 (357 Benign, 212 Malignant)
- **Features:** 30 cytological characteristics
  - 10 mean features (radius, texture, perimeter, area, smoothness, etc.)
  - 10 standard error features
  - 10 worst/extreme features
- **Target:** Binary classification (Benign = 0, Malignant = 1)
- **Class Imbalance:** 1.68:1 (handled with SMOTE)

---

## 🚀 Getting Started

### Prerequisites

Python 3.8 or higher

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd EnsMethods
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook "STAT 790- CAPSTONE PROJECT (1).ipynb"
   ```

---

## 📁 Project Structure

```
EnsMethods/
├── STAT 790- CAPSTONE PROJECT (1).ipynb    # Main enhanced notebook
├── Original WBCD.csv                       # Dataset
├── Derek_Lankeaux_RIT_MS_Applied_Statistics_Capstone DRAFT.pdf
├── requirements.txt                        # Python dependencies
├── README.md                              # This file
├── FINAL_PUBLICATION.md                   # Research publication (source)
├── publish_outputs.py                     # Publication output generator
├── PUBLISHING_GUIDE.md                    # Publishing documentation
├── FINAL_PUBLICATION.html                 # Generated web version
├── FINAL_PUBLICATION_PDF_READY.html       # Generated PDF-ready version
├── COMPLETE_PROJECT_PUBLICATION.html      # Complete publication HTML
├── Enhanced Ensemble Methods.pdf          # Final PDF publication
└── models/                                # Saved models (generated after running)
    ├── best_model_*.pkl
    ├── scaler.pkl
    ├── feature_names.pkl
    └── *_model.pkl
```

---

## 📄 Publication Outputs

This project includes a comprehensive publication system for generating research outputs in multiple formats.

### Quick Start - Generate Publications

```bash
python3 publish_outputs.py
```

This generates:
- **Standard HTML** - For web viewing and sharing
- **PDF-Ready HTML** - Optimized for PDF conversion
- **Complete Publication** - Comprehensive standalone document

### Available Publications

1. **Research Paper** (`FINAL_PUBLICATION.md`)
   - Comprehensive 28-page academic publication
   - Complete methodology, results, and discussion
   - References and appendices included

2. **HTML Versions** (auto-generated)
   - Web-optimized format
   - PDF-ready format with print styles
   - Complete project publication

3. **PDF Version**
   - Generate from `FINAL_PUBLICATION_PDF_READY.html`
   - Open in browser → Print → Save as PDF
   - See `PUBLISHING_GUIDE.md` for details

### Converting to PDF

1. Open `FINAL_PUBLICATION_PDF_READY.html` in your browser
2. Press `Ctrl+P` (or `Cmd+P` on Mac)
3. Select "Save as PDF"
4. Use recommended settings (A4, default margins)
5. Save as `Enhanced Ensemble Methods for Wisconsin Breast Cancer Classification.pdf`

For more details, see [PUBLISHING_GUIDE.md](PUBLISHING_GUIDE.md)

---

## 🤖 Models Implemented

### Traditional Ensemble Methods
1. **Random Forest** - Bagging with decision trees
2. **Gradient Boosting** - Sequential weak learners
3. **AdaBoost** - Adaptive boosting
4. **Bagging Classifier** - Bootstrap aggregating

### Advanced Ensemble Methods
5. **XGBoost** - Extreme gradient boosting
6. **LightGBM** - Light gradient boosting machine
7. **Voting Classifier** - Soft voting ensemble
8. **Stacking Classifier** - Meta-learning approach

---

## 📈 Key Results

### Performance Highlights
- **Best Model:** Determined by ROC-AUC score
- **Typical Performance:** >95% accuracy, >0.98 ROC-AUC
- **Class Balance:** SMOTE improved minority class recall significantly
- **Feature Selection:** RFE identified 15 most important features

### Important Findings
- "Worst" features (maximum values) are most discriminative
- High multicollinearity exists among size-related features (VIF > 10)
- Ensemble methods consistently outperform single models
- SMOTE + Advanced ensembles provide best balance between precision and recall

---

## 📊 Notebook Sections

### Part 1: Original Analysis
1. Data Loading and Exploration
2. Descriptive Statistics
3. Data Visualization
4. Feature Scaling
5. PCA Analysis
6. Machine Learning (Original 4 models)
7. Model Evaluation

### Part 2: Enhanced Analysis
1. **Utility Functions** - Modular code for evaluation
2. **VIF Analysis** - Multicollinearity assessment
3. **SMOTE** - Class imbalance handling
4. **Feature Selection** - RFE and importance analysis
5. **Advanced Ensemble Methods** - XGBoost, LightGBM, Voting, Stacking
6. **Comprehensive Comparison** - ROC curves, learning curves, metrics
7. **Model Persistence** - Saving models for deployment
8. **Final Summary** - Research conclusions and recommendations

---

## 💾 Saved Model Artifacts

After running the notebook, the following files are generated in `models/`:

- `best_model_*.pkl` - Best performing model
- `scaler.pkl` - StandardScaler for feature normalization
- `feature_names.pkl` - List of feature names
- `*_model.pkl` - All trained models for comparison

### Loading Saved Models

```python
import joblib

# Load the best model
model = joblib.load('models/best_model_<name>.pkl')
scaler = joblib.load('models/scaler.pkl')
feature_names = joblib.load('models/feature_names.pkl')

# Make predictions on new data
X_new_scaled = scaler.transform(X_new)
predictions = model.predict(X_new_scaled)
probabilities = model.predict_proba(X_new_scaled)
```

---

## 📚 References

### Dataset
- **Source:** UCI Machine Learning Repository
- **Creators:** Dr. William H. Wolberg, W. Nick Street, Olvi L. Mangasarian
- **Year:** 1995

### Key Libraries
- scikit-learn - Machine learning framework
- XGBoost - Extreme gradient boosting
- LightGBM - Microsoft's gradient boosting framework
- imbalanced-learn - SMOTE and class imbalance handling
- SHAP - Model interpretability (optional)

---

## 🎯 Future Work

1. **Deep Learning Approaches** - Neural networks for comparison
2. **Hyperparameter Optimization** - Bayesian optimization, Optuna
3. **Ensemble Pruning** - Remove redundant models
4. **Feature Engineering** - Domain-specific feature creation
5. **Deployment** - REST API, web application, Docker containerization
6. **Monitoring** - Model drift detection, performance tracking
7. **Explainability** - SHAP values, LIME for clinical interpretability

---

## 📄 License

This project is for educational and research purposes.

---

## 👤 Contact

**Derek Lankeaux**
MS Applied Statistics
Rochester Institute of Technology

For questions or collaborations, please open an issue in the repository.

---

## 🙏 Acknowledgments

- Rochester Institute of Technology - MS Applied Statistics Program
- UCI Machine Learning Repository - For the WBCD dataset
- Dr. Wolberg, Street, and Mangasarian - Dataset creators
- scikit-learn, XGBoost, LightGBM communities - For excellent libraries

---

**Last Updated:** 2025-11-07
**Version:** 2.0 (Optimized and Elongated)
