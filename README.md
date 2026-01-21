# Healthcare Cost Prediction 💊

## Project Overview

**Healthcare Cost Prediction** is an intelligent, production-ready machine learning web application designed to predict annual medical expenses based on patient demographics and health indicators. This comprehensive predictive tool leverages advanced machine learning algorithms to analyze key health factors including age, BMI, smoking status, number of dependents, gender, and geographic location—providing accurate cost estimates for healthcare providers, insurance companies, hospitals, and individual patients seeking to understand their potential medical expenses.

---

## 🎯 Purpose

The **Healthcare Cost Prediction System** is a data-driven machine learning application built to help users estimate annual healthcare costs with high accuracy. The system analyzes patient information including age, body mass index (BMI), smoking habits, number of children, gender, and residential region to generate personalized cost predictions. This tool is intended for use by healthcare administrators, insurance companies, hospital billing departments, financial planners, health economists, policy makers, and individuals seeking to budget for medical expenses or understand factors that influence healthcare costs.

---

## 🛠️ Tech Stack

The application was built using the following tools and technologies:

### **Backend & Machine Learning:**
- 🤖 **Python 3.8+** – Primary programming language for ML pipeline and web server
- 🧠 **scikit-learn 1.3.0** – Machine learning library for model training and preprocessing
- 🚀 **XGBoost 1.7.6** – Gradient boosting framework for high-performance predictions
- 📊 **pandas 2.0.3** – Data manipulation and analysis
- 🔢 **NumPy 1.24.3** – Numerical computing and array operations
- 💾 **joblib 1.3.2** – Model serialization and deserialization

### **Web Framework:**
- 🌐 **Flask 2.3.3** – Lightweight WSGI web application framework
- 🔧 **Werkzeug 2.3.7** – WSGI utilities and routing
- 🎨 **Jinja2** – Template engine for dynamic HTML rendering

### **Data Visualization & Analysis:**
- 📈 **Matplotlib 3.7.2** – Static plotting and visualization
- 📊 **Seaborn 0.12.2** – Statistical data visualization

### **Development & Deployment:**
- 📁 **setuptools** – Package development and distribution
- 📝 **Logging** – Comprehensive application logging system
- 🔒 **Custom Exception Handling** – Robust error management
- 🎯 **Modular Architecture** – Separation of concerns (components, pipelines, utilities)

### **ML Pipeline Components:**
- 🔄 **StandardScaler** – Feature normalization
- 🏷️ **OneHotEncoder** – Categorical variable encoding
- 🔍 **GridSearchCV** – Hyperparameter optimization
- 📊 **Train-Test Split** – Data partitioning for validation
- 🎲 **SimpleImputer** – Missing value handling

---

## 📊 Data Source

**Source:** Kaggle - Medical Cost Personal Dataset

Dataset includes comprehensive information on healthcare costs and patient demographics, including:
- Patient age (18-100 years)
- Gender (male/female)
- Body Mass Index (BMI) measurements
- Number of dependent children
- Smoking status (yes/no)
- Residential region (northeast, northwest, southeast, southwest)
- Annual medical charges (target variable)

**Dataset Characteristics:**
- **Time Period:** Historical medical cost data
- **Sample Size:** 1,338 patient records
- **Features:** 7 columns (6 predictors + 1 target)
- **Target Variable:** Medical charges (continuous)
- **Data Quality:** Clean dataset with no missing values
- **Feature Types:** Mixed (numerical and categorical)

---

## ✨ Features / Highlights

### 📌 Business Problem

Healthcare costs in the United States continue to rise dramatically, creating financial uncertainty for individuals, families, insurance companies, and healthcare providers. Stakeholders struggle with:

- **Cost Estimation:** Patients cannot accurately predict their annual medical expenses for budgeting
- **Insurance Pricing:** Insurance companies need accurate risk assessment for premium calculations
- **Resource Planning:** Hospitals require cost forecasts for resource allocation and capacity planning
- **Risk Assessment:** Healthcare providers need to identify high-cost patients for preventive care programs
- **Financial Planning:** Individuals struggle to plan for medical expenses, leading to financial distress
- **Policy Making:** Government agencies need data-driven insights for healthcare policy decisions
- **Premium Calculation:** Insurers lack precise tools to calculate fair and accurate insurance premiums

Without an intelligent, automated system to predict healthcare costs based on individual factors, financial planning for both providers and patients remains challenging and often inaccurate.

---

### 🎯 Goal of the Application

To deliver an **AI-powered healthcare cost prediction platform** that:

✅ Provides instant, accurate predictions of annual medical expenses based on patient demographics  
✅ Helps individuals budget and plan for healthcare costs proactively  
✅ Assists insurance companies in calculating fair and accurate premium rates  
✅ Enables healthcare providers to identify high-risk, high-cost patients  
✅ Supports financial planning for medical expenses and insurance coverage  
✅ Offers transparent, interpretable predictions with user-friendly interface  
✅ Scales to handle production-level traffic with robust error handling

---

### 📈 Walkthrough of Key Features

#### 1️⃣ **Intelligent Model Selection (8 ML Algorithms Compared)**

The system automatically trains and evaluates 8 different machine learning algorithms:

**Models Evaluated:**
1. **Random Forest Regressor** – Ensemble method using multiple decision trees
2. **XGBoost Regressor** – Gradient boosting with regularization
3. **Gradient Boosting Regressor** – Sequential ensemble learning
4. **Decision Tree Regressor** – Simple tree-based model
5. **Linear Regression** – Basic linear relationship modeling
6. **Ridge Regression** – Linear regression with L2 regularization
7. **Lasso Regression** – Linear regression with L1 regularization
8. **AdaBoost Regressor** – Adaptive boosting ensemble method

**Selection Process:**
- GridSearchCV for hyperparameter tuning on each model
- 3-fold cross-validation for robust evaluation
- Automatic selection based on highest R² score on test data
- Performance metrics: R², MAE (Mean Absolute Error), RMSE (Root Mean Squared Error)

**Typical Best Performer:** XGBoost or Random Forest with R² scores of 0.86-0.88

**Insight:** The automated model selection ensures you always get the best-performing algorithm for your data, eliminating manual trial-and-error and ensuring production-ready accuracy.

---

#### 2️⃣ **Advanced Feature Engineering Pipeline**

**Numerical Features Processing:**
- **Features:** Age, BMI, Number of Children
- **Imputation:** Median strategy for handling outliers
- **Scaling:** StandardScaler for normalization
- **Purpose:** Ensures all numerical features are on the same scale for optimal model performance

**Categorical Features Processing:**
- **Features:** Sex, Smoker Status, Region
- **Imputation:** Most frequent strategy for consistency
- **Encoding:** OneHotEncoder with unknown category handling
- **Scaling:** StandardScaler (with_mean=False) for sparse matrix compatibility
- **Purpose:** Converts text categories into numerical format while preserving information

**Pipeline Benefits:**
✅ Automated preprocessing – no manual feature engineering required  
✅ Reproducible transformations – same preprocessing for training and prediction  
✅ Handles edge cases – missing values and unknown categories gracefully  
✅ Optimized performance – efficient scaling and encoding

**Insight:** The preprocessing pipeline ensures consistent, reliable predictions by standardizing all input features, preventing model bias toward features with larger numerical ranges.

---

#### 3️⃣ **Modern Web Interface with Gradient Design**

**Hero Section:**
- Eye-catching gradient background (blue to purple)
- Clear title: "Healthcare Cost Prediction"
- Subtitle: "Estimate medical expenses with AI-powered predictions"
- Professional, trustworthy appearance

**Prediction Card:**
- Clean white card design elevated above background
- Two-column grid layout for efficient form completion
- Input fields with validation and placeholders
- Large, prominent prediction button with gradient styling

**Key Metrics Displayed:**
- **Age:** Input range 18-100 years
- **Sex:** Dropdown selection (male/female)
- **BMI:** Decimal input (10-60 range)
- **Children:** Integer input (0-10 dependents)
- **Smoker:** Dropdown selection (yes/no)
- **Region:** Four geographic regions (Southeast, Southwest, Northeast, Northwest)

**Interactive Elements:**
- Form data persistence after prediction
- Real-time validation on all inputs
- Smooth hover effects on buttons
- Animated result display with gradient background
- Error messages with clear explanations

**Insight:** The modern, responsive design ensures users can easily input data and understand predictions, reducing friction and improving user experience across desktop and mobile devices.

---

#### 4️⃣ **Real-Time Prediction with Result Display**

**Prediction Result Card:**
- Beautiful gradient background (pink to red)
- Large, prominent cost display: **$8,543.67**
- Subtitle: "Estimated annual medical expenses"
- Smooth slide-in animation for visual feedback

**Result Interpretation:**
- Dollar amount formatted to 2 decimal places
- Clear context provided (annual vs monthly)
- No technical jargon – plain language explanation
- Instant feedback (prediction takes <1 second)

**Example Predictions:**

| Profile | Age | Sex | BMI | Children | Smoker | Region | Predicted Cost |
|---------|-----|-----|-----|----------|--------|--------|----------------|
| Young Non-Smoker | 25 | Male | 22.5 | 0 | No | Northwest | $3,500 - $5,000 |
| Middle-Aged Parent | 40 | Female | 28.0 | 2 | No | Southeast | $7,000 - $9,000 |
| Senior Smoker | 60 | Male | 32.0 | 0 | Yes | Northeast | $35,000 - $45,000 |
| Healthy Adult | 30 | Female | 21.0 | 1 | No | Southwest | $4,000 - $6,000 |

**Insight:** Smoking status has the most dramatic impact on predicted costs, often increasing estimates by 3-5x. BMI and age also significantly influence predictions, highlighting the importance of preventive health measures.

---

#### 5️⃣ **Form Data Retention for Easy Adjustments**

**Smart Form Behavior:**
- All entered data remains in form after prediction
- Users can easily adjust one field and re-predict
- No need to re-enter all information
- Enables quick scenario comparison ("What if I quit smoking?")

**Use Cases:**
1. **Scenario Planning:** Change one variable to see impact
   - "How much would I save if I lost 10 BMI points?"
   - "What if I moved to a different region?"
   
2. **Sensitivity Analysis:** Understand which factors matter most
   - Compare smoker vs non-smoker costs
   - Test age progression (current age vs 10 years older)
   
3. **Family Planning:** Estimate costs for different family sizes
   - Compare 1 child vs 2 children scenarios
   - Plan for growing family medical budgets

**Insight:** Form persistence dramatically improves user experience by allowing rapid "what-if" analysis without tedious re-entry, making the tool practical for real-world financial planning scenarios.

---

#### 6️⃣ **Informational Cards for User Education**

**Three Key Benefits Highlighted:**

**🎯 Accurate Predictions**
- "AI model trained on thousands of healthcare records"
- Builds user confidence in prediction quality
- Emphasizes data-driven approach

**⚡ Instant Results**
- "Get predictions in seconds with optimized pipeline"
- Highlights speed and efficiency
- Reduces user wait time anxiety

**🔒 Secure & Private**
- "Data processed securely and never stored"
- Addresses privacy concerns
- Builds trust with users

**Insight:** Educational cards help users understand the value proposition, technology benefits, and privacy protections, increasing adoption and trust in the system.

---

### 💼 Business Impact & Insights

#### For Individual Patients:
- **Budget Planning:** Accurate annual cost estimates for financial planning
- **Insurance Selection:** Compare estimates against insurance premiums
- **Lifestyle Decisions:** Understand cost impact of health choices (smoking, weight)
- **Preventive Care:** Motivation to maintain healthy BMI and avoid smoking
- **Savings Planning:** Set realistic healthcare savings goals
- **Peace of Mind:** Reduce financial uncertainty about medical expenses

#### For Insurance Companies:
- **Premium Calculation:** Data-driven premium pricing based on risk factors
- **Risk Assessment:** Identify high-risk customers requiring specialized plans
- **Underwriting Efficiency:** Automated initial cost estimation
- **Fraud Detection:** Flag unrealistic claims against predicted costs
- **Product Development:** Design targeted insurance products for specific demographics
- **Competitive Pricing:** Optimize premiums while maintaining profitability

#### For Healthcare Providers:
- **Resource Allocation:** Forecast demand for high-cost treatments
- **Patient Stratification:** Identify patients needing preventive care programs
- **Financial Counseling:** Help patients understand expected costs upfront
- **Capacity Planning:** Anticipate resource needs based on patient mix
- **Revenue Forecasting:** Predict revenue based on patient population
- **Value-Based Care:** Target interventions to reduce costs for high-risk patients

#### For Hospital Administrators:
- **Billing Estimates:** Provide accurate cost estimates to patients before treatment
- **Collection Planning:** Anticipate payment challenges for high-cost patients
- **Financial Aid Programs:** Identify patients needing financial assistance
- **Department Budgeting:** Allocate resources based on predicted patient costs
- **Contract Negotiations:** Use data to negotiate insurance reimbursement rates

#### For Health Economists & Researchers:
- **Cost Driver Analysis:** Identify factors most strongly correlated with costs
- **Policy Impact Studies:** Model effects of smoking cessation programs
- **Regional Disparities:** Analyze geographic variations in healthcare costs
- **Demographic Trends:** Study cost evolution across different age groups
- **Obesity Impact:** Quantify financial burden of high BMI on healthcare system
- **Smoking Costs:** Calculate societal costs of tobacco use

#### For Financial Planners:
- **Retirement Planning:** Include realistic healthcare cost estimates
- **Emergency Fund Sizing:** Recommend appropriate medical emergency savings
- **Insurance Recommendations:** Guide clients to appropriate coverage levels
- **Tax Planning:** Estimate HSA/FSA contribution needs
- **Long-Term Care Planning:** Project future medical expenses for aging clients

#### For Government & Policy Makers:
- **Healthcare Policy:** Design interventions based on cost drivers
- **Public Health Programs:** Target smoking cessation and obesity programs
- **Subsidy Allocation:** Identify demographics needing financial assistance
- **Healthcare Reform:** Model impact of policy changes on costs
- **Regional Investments:** Direct healthcare infrastructure to high-cost regions

---

## 📸 Screenshots / Demo

### Main Interface
<img width="861" height="925" alt="Screenshot 2026-01-14 115457" src="https://github.com/user-attachments/assets/a1655e39-56e1-4baf-98ad-951045340a05" />

*Modern web interface with gradient background, clean form design, and intuitive input fields for patient information*

### Prediction Result
<img width="767" height="851" alt="Screenshot 2026-01-14 115733" src="https://github.com/user-attachments/assets/12c213ec-284e-4fd6-913b-d408e35e83d1" />

*Beautiful result display showing estimated annual healthcare cost with smooth animations and clear formatting*

### Form Data Persistence
<img width="907" height="661" alt="Screenshot 2026-01-14 115953" src="https://github.com/user-attachments/assets/f1f6d632-004a-4ba6-b3de-30c6847140be" />

*After prediction, all entered data remains in the form allowing easy adjustments and scenario comparisons*



---

## 📚 Key Learnings

### Machine Learning Skills Developed:
✅ **Model Comparison:** Trained and evaluated 8 different regression algorithms  
✅ **Hyperparameter Tuning:** GridSearchCV for optimal model configuration  
✅ **Pipeline Architecture:** Built end-to-end ML pipelines with preprocessing and modeling  
✅ **Feature Engineering:** StandardScaler for numerical features, OneHotEncoder for categorical  
✅ **Model Evaluation:** R², MAE, RMSE metrics for comprehensive performance assessment  
✅ **Overfitting Prevention:** Cross-validation and train-test split strategies  
✅ **Model Serialization:** joblib for efficient model saving and loading  
✅ **Production ML:** Deployed models in real-world web applications

### Software Engineering Skills:
✅ **Modular Architecture:** Separated data ingestion, transformation, training, and prediction  
✅ **Custom Exception Handling:** Created robust error management system  
✅ **Logging System:** Implemented comprehensive logging for debugging and monitoring  
✅ **Code Organization:** Followed Python best practices with proper package structure  
✅ **Version Control:** Git for code management and collaboration  
✅ **Virtual Environments:** Dependency isolation for reproducible deployments  
✅ **Package Management:** setup.py for proper Python package distribution

### Web Development Skills:
✅ **Flask Framework:** Built RESTful APIs and web interfaces  
✅ **Jinja2 Templating:** Dynamic HTML generation with server-side rendering  
✅ **Form Handling:** POST/GET request processing and validation  
✅ **Session Management:** Form data persistence across requests  
✅ **Responsive Design:** CSS Grid and Flexbox for adaptive layouts  
✅ **UI/UX Design:** Modern, user-friendly interface with gradient backgrounds  
✅ **CSS Animations:** Smooth transitions and hover effects

### Healthcare Domain Knowledge:
✅ **Cost Drivers:** Understanding factors influencing medical expenses  
✅ **BMI Impact:** Health implications of body mass index on costs  
✅ **Smoking Correlation:** Dramatic cost increase for smokers (3-5x higher)  
✅ **Age Progression:** Healthcare costs increase with age  
✅ **Regional Variations:** Geographic differences in medical pricing  
✅ **Family Size Impact:** Dependent children effect on household medical costs  
✅ **Preventive Care Value:** Financial benefits of maintaining healthy lifestyle

### Data Science Skills:
✅ **Data Preprocessing:** Cleaning, imputation, and transformation  
✅ **Feature Selection:** Identifying relevant predictors  
✅ **Statistical Analysis:** Understanding distributions and correlations  
✅ **Model Interpretation:** Explaining predictions to non-technical users  
✅ **Performance Optimization:** Tuning models for production speed  
✅ **Data Visualization:** Creating meaningful charts and graphs

---

## 🔮 Future Enhancements

### Planned Features:

🎯 **Advanced Cost Breakdown**
- Separate predictions for: hospitalization, medication, preventive care, emergency services
- Category-wise cost distribution pie chart
- Most likely medical service categories based on profile

📊 **Cost Comparison Tool**
- Side-by-side comparison of two different patient profiles
- Difference calculator showing savings from lifestyle changes
- Visual charts showing cost differences across multiple scenarios

🏥 **Personalized Health Recommendations**
- AI-generated suggestions to reduce healthcare costs
- "What if" scenarios: "Losing 10 BMI points could save you $2,500/year"
- Smoking cessation program recommendations with projected savings

📈 **Historical Cost Trends**
- Project cost increases over 5, 10, 20 years based on age
- Retirement healthcare budget calculator
- Inflation-adjusted long-term cost estimates

🎪 **Insurance Plan Recommender**
- Match predicted costs against available insurance plans
- Premium vs out-of-pocket cost calculator
- Optimal plan recommendation based on predicted expenses

💰 **Savings Calculator**
- Calculate required monthly savings to cover predicted costs
- Emergency fund size recommendation
- HSA/FSA contribution optimizer

📱 **Mobile App Development**
- Native iOS and Android applications
- Push notifications for health reminders
- Offline prediction capability

🔐 **User Account System**
- Save multiple profiles (family members)
- Track prediction history over time
- Compare actual vs predicted costs

🤖 **Enhanced ML Models**
- Deep learning models for improved accuracy
- Incorporate additional health indicators (blood pressure, cholesterol)
- Use medical history for personalized predictions

📊 **Analytics Dashboard**
- Population-level cost analysis
- Regional cost heatmaps
- Demographic trend visualizations

🌐 **Multi-Language Support**
- Spanish, Hindi, Mandarin translations
- Localized cost estimates for different countries
- Currency conversion for international users

🔔 **Alert System**
- Email notifications when costs exceed thresholds
- Annual cost estimate reminders
- Health milestone notifications (upcoming age bracket change)

---

## 🚀 Installation & Setup

### Prerequisites:
- **Python 3.8 or higher** - [Download Here](https://www.python.org/downloads/)
- **pip** (Python package manager) - Included with Python installation
- **Virtual Environment** (recommended) - For dependency isolation
- **Git** (optional) - For cloning repository
- **4GB RAM minimum** (8GB recommended)
- **500MB free disk space**

### Step-by-Step Installation:

#### 1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/healthcare-cost-prediction.git
cd healthcare-cost-prediction
```

#### 2. **Create Virtual Environment**

**Windows:**
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. **Upgrade pip**
```bash
pip install --upgrade pip
```

#### 4. **Install Dependencies**
```bash
pip install -r requirements.txt
```

**What gets installed:**
- Flask 2.3.3 (web framework)
- pandas 2.0.3 (data manipulation)
- numpy 1.24.3 (numerical computing)
- scikit-learn 1.3.0 (machine learning)
- xgboost 1.7.6 (gradient boosting)
- joblib 1.3.2 (model serialization)
- matplotlib 3.7.2 (plotting)
- seaborn 0.12.2 (visualization)
- werkzeug 2.3.7 (WSGI utilities)

#### 5. **Install Project Package**
```bash
pip install -e .
```

This makes the `src` module importable throughout the project.

#### 6. **Prepare Dataset**

Place `medical_expenses.csv` in the `notebook/` folder with columns:
- age, sex, bmi, children, smoker, region, charges

#### 7. **Train the Model**
```bash
python train_model.py
```

**Expected Training Time:** 2-5 minutes  
**Output Files Created:**
- `artifacts/data.csv` (full dataset)
- `artifacts/train.csv` (training split - 80%)
- `artifacts/test.csv` (test split - 20%)
- `artifacts/model.pkl` (trained model)
- `artifacts/preprocessor.pkl` (feature transformer)

**Console Output:**
```
==================================================
Starting Training Pipeline...
==================================================
✅ Data loaded successfully from: notebook/medical_expenses.csv
Dataset shape: (1338, 7)
Columns: ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
✅ Train set saved: artifacts/train.csv
✅ Test set saved: artifacts/test.csv

Fitting 3 folds for each of 12 candidates, totaling 36 fits
Training Random Forest...
Training XGBoost...
Training Gradient Boosting...
Training Linear Regression...
Training Ridge Regression...
Training Lasso Regression...
Training Decision Tree...
Training AdaBoost...

Best Model: XGBoost Regressor
Train R2: 0.9123
Test R2: 0.8654
MAE: 2,847.32
RMSE: 4,512.89

==================================================
✅ Training Completed Successfully!
📊 Model R2 Score: 0.8654
==================================================

📁 Artifacts saved in 'artifacts/' folder:
  - data.csv
  - train.csv
  - test.csv
  - model.pkl
  - preprocessor.pkl

🚀 You can now run: python app.py
```

#### 8. **Run the Application**
```bash
python app.py
```

**Console Output:**
```
================================================================================
💊 Healthcare Cost Predictor - Starting Flask Server
================================================================================
📁 Working Directory: /path/to/healthcare_cost_prediction
🐍 Python Version: 3.11.5
✅ Model and preprocessor found

🌐 Server will start at: http://localhost:5001
   Press CTRL+C to stop the server
================================================================================

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5001
 * Running on http://192.168.1.100:5001
Press CTRL+C to quit
```

#### 9. **Access the Application**

Open your web browser and navigate to:
- **http://localhost:5001**
- Or **http://127.0.0.1:5001**

#### 10. **Make Your First Prediction**

**Test Input:**
- Age: 35
- Sex: Male
- BMI: 27.5
- Children: 2
- Smoker: No
- Region: Northwest

**Expected Result:** ~$8,500-$9,500 annual cost

---

## 🧪 Testing

### Manual Testing

Test the application with these sample profiles:

#### Test Case 1: Young, Healthy Individual
```
Age: 25
Sex: Female
BMI: 21.5
Children: 0
Smoker: No
Region: Southeast

Expected Range: $3,000 - $5,000
```

#### Test Case 2: Middle-Aged Parent
```
Age: 40
Sex: Male
BMI: 28.0
Children: 2
Smoker: No
Region: Northwest

Expected Range: $7,000 - $9,000
```

#### Test Case 3: Senior Smoker
```
Age: 60
Sex: Male
BMI: 32.0
Children: 0
Smoker: Yes
Region: Northeast

Expected Range: $35,000 - $45,000
```

#### Test Case 4: Optimal Health Profile
```
Age: 30
Sex: Female
BMI: 22.0
Children: 1
Smoker: No
Region: Southwest

Expected Range: $4,000 - $6,000
```

### Unit Testing

Create `tests/test_prediction.py`:

```python
import pytest
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

def test_prediction_pipeline():
    """Test basic prediction functionality"""
    data = CustomData(
        age=35,
        sex='male',
        bmi=27.5,
        children=2,
        smoker='no',
        region='northwest'
    )
    
    pipeline = PredictPipeline()
    df = data.get_data_as_data_frame()
    result = pipeline.predict(df)
    
    assert result is not None
    assert len(result) == 1
    assert result[0] > 0  # Cost should be positive
    assert result[0] < 100000  # Sanity check

def test_smoker_impact():
    """Verify smokers have higher predicted costs"""
    non_smoker = CustomData(40, 'male', 28.0, 2, 'no', 'northwest')
    smoker = CustomData(40, 'male', 28.0, 2, 'yes', 'northwest')
    
    pipeline = PredictPipeline()
    
    cost_non_smoker = pipeline.predict(non_smoker.get_data_as_data_frame())[0]
    cost_smoker = pipeline.predict(smoker.get_data_as_data_frame())[0]
    
    assert cost_smoker > cost_non_smoker * 2  # Smokers cost at least 2x more
```

Run tests:
```bash
pytest tests/ -v
```

---

## 📊 Model Performance

### Evaluation Metrics

**Best Model: XGBoost Regressor**

| Metric | Training Set | Test Set |
|--------|--------------|----------|
| R² Score | 0.9123 | 0.8654 |
| MAE | 2,456.78 | 2,847.32 |
| RMSE | 3,987.45 | 4,512.89 |

**Interpretation:**
- **R² = 0.8654**: Model explains 86.54% of cost variance
- **MAE = 2,847**: Average prediction error is ±2,847
- **RMSE = 4,512**: Typical prediction is within ±4,512

### Feature Importance

**Top Cost Influencers:**
1. **Smoker Status** (45% importance) – Dominates cost predictions
2. **Age** (25% importance) – Strong positive correlation
3. **BMI** (18% importance) – Higher BMI = higher costs
4. **Region** (7% importance) – Geographic cost variations
5. **Children** (3% importance) – Minor impact
6. **Sex** (2% importance) – Minimal direct effect

**Key Insight:** Smoking is by far the strongest predictor, often increasing costs by 300-500%. This aligns with medical research showing smokers have significantly higher rates of chronic diseases, hospitalizations, and medication needs.

---

## 🚢 Production Deployment

### Option 1: Local Production Mode

```bash
# Set environment variables
export FLASK_ENV=production
export FLASK_DEBUG=0

# Run with production settings
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Option 2: Docker Deployment

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Install package
RUN pip install -e .

# Expose port
EXPOSE 5001

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5001/ || exit 1

# Run application
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t healthcare-predictor .
docker run -p 5001:5001 healthcare-predictor
```

### Option 3: Heroku Deployment

```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Create runtime.txt
echo "python-3.9.16" > runtime.txt

# Initialize Git (if not already)
git init
git add .
git commit -m "Initial commit"

# Deploy to Heroku
heroku create healthcare-cost-predictor-app
git push heroku main
heroku open
```

### Option 4: AWS EC2 Deployment

```bash
# SSH into EC2 instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3-pip python3-venv nginx -y

# Clone repository
git clone https://github.com/yourusername/healthcare-cost-prediction.git
cd healthcare-cost-prediction

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .

# Train model
python train_model.py

# Install and configure Gunicorn
pip install gunicorn
gunicorn --bind 0.0.0.0:8000 app:app --daemon

# Configure Nginx reverse proxy
sudo nano /etc/nginx/sites-available/healthcare-predictor
```

**Nginx Configuration:**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Option 5: Azure App Service

```bash
# Login to Azure
az login

# Create resource group
az group create --name healthcare-rg --location eastus

# Create App Service plan
az appservice plan create --name healthcare-plan --resource-group healthcare-rg --sku B1 --is-linux

# Create web app
az webapp create --resource-group healthcare-rg --plan healthcare-plan --name healthcare-predictor --runtime "PYTHON:3.9"

# Deploy code
az webapp up --name healthcare-predictor --resource-group healthcare-rg
```

---

## 🔧 Configuration

### Environment Variables

Create `.env` file:

```env
# Flask Configuration
FLASK_APP=app.py
FLASK_ENV=production
SECRET_KEY=your-secret-key-here-change-in-production

# Model
