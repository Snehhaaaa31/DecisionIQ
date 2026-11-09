# DecisionIQ – AI-Powered Business Intelligence & Decision Support Platform

DecisionIQ is an AI-powered Business Intelligence and Decision Support platform developed using Python and Streamlit. It transforms raw business datasets into meaningful insights through interactive dashboards, automated data analysis, sales forecasting, and AI-generated recommendations.

The platform provides a centralized environment where users can upload datasets, explore business performance, identify trends, forecast future outcomes, and make data-driven decisions.

## 🚀 Features

### 1. Dataset Upload & Analysis
- Upload datasets in CSV and Excel formats.
- Automatically analyze uploaded datasets.
- Display dataset previews and structural information.
- Identify missing values and duplicate records.
- Generate statistical summaries.
- Explore individual columns, data types, and unique values.

### 2. Interactive Business Dashboard
- Display important business KPIs.
- Analyze total sales and profit.
- Visualize sales trends over time.
- Compare sales across different categories.
- Analyze regional distribution.
- Apply interactive filters for customized analysis.
- Explore relationships between numerical variables.

### 3. Sales Forecasting
- Forecast future sales using Facebook Prophet.
- Analyze historical sales patterns.
- Visualize actual and predicted sales.
- Display forecast confidence intervals.
- Analyze forecast components and trends.

### 4. AI-Powered Business Insights
- Generate AI-driven insights from business data.
- Identify important patterns and trends.
- Obtain recommendations to support business decisions.
- Integrate Groq API for AI-powered analysis.

### 5. Reports & Downloads
- Generate analytical reports.
- Download processed datasets.
- Export forecasting results.
- Access useful analytical information for further evaluation.

## 🖥️ Application Screenshots

### 1. Home Page
The home page introduces DecisionIQ and provides navigation to its major features.

![Home Page](screenshots/home.png)

### 2. Dataset Upload & Analysis
Upload a dataset and explore its structure, statistics, missing values, and column information.

![Dataset Upload](screenshots/upload.png)

### 3. Interactive Dashboard
Visualize business KPIs, sales trends, category performance, regional distribution, and other important metrics.

![Dashboard](screenshots/dashboard.png)

### 4. Sales Forecasting
Generate future sales predictions using historical data and visualize forecasting results.

![Forecasting](screenshots/forecasting.png)

### 5. AI-Powered Insights
Generate AI-based business insights and recommendations to understand dataset patterns.

![AI Insights](screenshots/ai-insights.png)

### 6. Reports
Generate and download analytical reports and forecasting results.

![Reports](screenshots/reports.png)

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application development |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computations |
| Plotly | Interactive data visualization |
| Facebook Prophet | Time-series forecasting |
| Groq API | AI-powered insights |
| CSS | Custom application styling |
| Git & GitHub | Version control |

## 📁 Project Structure

```text
DecisionIQ/
│
├── .streamlit/
│   └── config.toml
│
├── data/
│   └── superstore.csv
│
├── notebook/
│   └── Day1_EDA.ipynb
│
├── pages/
│   ├── _1Upload_Dataset.py
│   ├── _2Dashboard.py
│   ├── _3Forecasting.py
│   ├── _4AI_Insights.py
│   └── _5Reports.py
│
├── styles/
│   └── style.css
│
├── screenshots/
│   ├── home.png
│   ├── upload.png
│   ├── dashboard.png
│   ├── forecasting.png
│   ├── ai-insights.png
│   └── reports.png
│
├── utils/
│   ├── ai.py
│   ├── ai_snapshot.py
│   ├── dashboard.py
│   ├── download.py
│   ├── explorer.py
│   ├── forecasting.py
│   ├── loader.py
│   ├── metrics.py
│   ├── missing.py
│   ├── preview.py
│   ├── report.py
│   ├── statistics.py
│   └── summary.py
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/DecisionIQ.git
```

### Step 2: Navigate to the Project Directory

```bash
cd DecisionIQ
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure Groq API

Configure your Groq API key securely using Streamlit secrets or environment variables, according to your application configuration.

Do not upload API keys or other credentials to GitHub.

### Step 6: Run the Application

```bash
streamlit run app.py
```

The application will launch in your default web browser.

## 📊 Sample Dataset

DecisionIQ includes a sample Superstore sales dataset for exploring its business analytics capabilities.

The dataset supports analysis of:
- Sales and profitability
- Product categories and sub-categories
- Customer segments
- Regional performance
- Order trends
- Discounts and shipping costs

Users can also upload their own CSV and Excel datasets.

## 🔄 Application Workflow

1. Upload a business dataset.
2. Process and explore the uploaded data.
3. Analyze dataset quality and statistical summaries.
4. View business KPIs through interactive dashboards.
5. Generate future sales forecasts.
6. Obtain AI-powered business insights.
7. Generate reports and download analytical results.

## 🔮 Future Enhancements

- Advanced customer segmentation.
- Automated anomaly detection.
- More predictive analytics models.
- Additional AI-powered recommendations.
- Support for more data sources and formats.
- Cloud deployment and user authentication.

## 🎯 Project Objective

The objective of DecisionIQ is to simplify business intelligence by integrating data analysis, interactive visualization, predictive forecasting, and artificial intelligence into a single platform.

It aims to reduce manual analytical effort and help users transform raw business data into actionable insights for smarter decision-making.

## 👩‍💻 Author

**Sneha Sachan**

B.Tech – Electronics and Computer Engineering

Interests: Data Analytics | Artificial Intelligence | Machine Learning | Business Intelligence

---

**DecisionIQ – Turning Raw Data into Meaningful Insights and Smarter Decisions.**
