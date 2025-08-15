# Project Title

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

Predicting stock returns is a fundamental challenge in quantitative finance. However, using machine learning can better inform predictions and generate excess returns through the utilization of historical data, specifically momentum and volatility patterns. This project aims to test whether certain machine learning models can outperform a benchmark (ex. S&P 500) in predicting daily/weekly stock returns, and potentially identify which features of stocks are most predictive. This project is significant because it shows the practical applications of machine learning in the world of finance. In addition, hedge funds and traders use similar approaches for algorithmic trading.

## Stakeholder & User

The primary stakeholders of this project would be portfolio managers and algorithmic traders, and students who are studying financial engineering or quantitative finance could be users. The model predictions from this project can be used for market pre-screenings, and the model outputs can be useful in informing buy/sell/hold decisions in a simulated environment.

## Useful Answer & Decision

The type of useful answer this project's model outputs would give is predictive (classification or regression), and some possible metrics could be Sharpe ratio, accuracy or recall (if using binary classification), or mean squared error (if using regression). 

The artifact to deliver for this project would be a trained machine learning model (e.g. XGBoost, Random Forest), along with backtested results against a benchmark and potentially feature importance analysis.

## Assumptions & Constraints

- Data used for this project will be limited to free data sources such as Yahoo Finance or Bloomberg, and only to daily/weekly data. 

- The machine learning models will only be run on my local machine

- There won't be any analysis of real-time data (latency constraint)

- There won't be any actual trading being done with these model outputs (compliance constraint). 

## Known Unknowns / Risks

- Model may fail in volatile periods such as crashes.

  - Test across multiple time periods (e.g., include COVID-19 data)

- There is high risk and potential for overfitting with noisy financial data

  - Use validation and regularization

- The models may underperform simple benchmarks such as moving averages

  - Compare against baseline

## Lifecycle Mapping
Goal → Stage → Deliverable

- Define scope & success metrics → Stage 1: Problem Framing & Scoping → Problem Framing & Scoping

- Acquire & clean data → Stage 2: Data Engineering → Processed dataset 

- Train & evaluate models	→ Stage 3: Modeling → Code for models and evaluation written in Python 

- Backtest strategy	→ Stage 4: Validation → Performance report using aforementioned metrics and validation methods

- Present findings → Stage 5: Presentation → Slide deck or written report


## Repo Plan
/data/, /src/, /notebooks/, /docs/ ; cadence for updates