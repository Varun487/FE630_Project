# FE630 Project

## Goal

The goal of this project to build and compare 2 a factor-based long short allocation models with constraints on their betas.

## Components in the project

### Data

Download data of chosen instruments and time period.

### Regression

There are 2 regressions to be completed for each asset
- Regress asset's excess return on the factor model in order to get the coefficients for gathering our expected returns. 
- Regress asset's returns on the SPY to obtain the betas of each asset compared to our benchmark. 

### Expected returns

Calculate expected returns based on the French Fama model.

### Portfolio optimization

Solves objective function given for both strategies and returns optimal portfolio weights.

### Backtest

Calculate returns based on portfolio optimization and re-balances the portfolio every week. Then calculates cumulative returns.

## Build the project

- Initialize

```commandline
git clone git@github.com:Varun487/FE630_Project.git
cd FE630_Project
pip3 install -r requirements.txt
```

- Run

```commandline
python3 main.py
```

## Project members

###### All members are at Stevens Institute of Technology Fall 2022

1. Varun Seshu
2. Sriram Bharadwaj
3. Prakhyath Shivappa
4. Darsh Sharma
