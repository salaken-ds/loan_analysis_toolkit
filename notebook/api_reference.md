# API Reference: Loan Analysis Toolkit

This document provides an API reference for the functions available in this package.

---

## `calculate_minimum_repayment`

**Description**  
Calculates the minimum repayment amount for a loan using the compound interest formula.

**Arguments**  
- `principal` (float): The loan amount (principal).  
- `annual_rate` (float): The annual interest rate (in percentage, e.g., 5 for 5%).  
- `years` (int): The loan term in years.  
- `months` (int): Additional loan term in months.  
- `repayment_frequency` (str): The repayment frequency (`'annual'`, `'monthly'`, `'quarterly'`, etc.).

**Returns**  
- `float`: The minimum repayment amount per period.

---

## `calculate_daily_interest`

**Description**  
Calculates the daily interest on the loan balance.

**Arguments**  
- `loan_balance` (float): The current loan balance.  
- `annual_rate` (float): The annual interest rate (in percentage, e.g., 5 for 5%).

**Returns**  
- `float`: The daily interest amount.

---

## `find_relevant_dates`

**Description**  
Generates a list of dates between `start_date` and `end_date` based on the specified frequency.

**Arguments**  
- `start_date` (datetime): The start date.  
- `end_date` (datetime): The end date.  
- `frequency` (str): The frequency of dates (`'daily'`, `'weekly'`, `'monthly'`, etc.).

**Returns**  
- `list`: A list of `datetime` objects representing the dates.

---

## `calculate_end_date`

**Description**  
Calculates the end date based on the start date, duration in years, and duration in months.

**Arguments**  
- `start_date` (datetime): The start date. Defaults to the current date.  
- `years` (int): The duration in years.  
- `months` (int): The duration in months.

**Returns**  
- `datetime`: The calculated end date.

---

## `generate_loan_transactions`

**Description**  
Generates a loan schedule including repayments, interest charges, loan balance, and offset.

**Arguments**  
- `start_date` (datetime): The settlement date.  
- `loan_amount` (float): The loan amount (principal).  
- `annual_rate` (float): The annual interest rate.  
- `initial_offset_amount` (float): The initial amount in the offset account.  
- `minimum_repayments` (float): The minimum repayment amount per period.  
- `all_dates` (list): A list of all dates to iterate through (daily).  
- `interest_charge_dates` (list): Dates when interest is charged (monthly).  
- `repayment_dates` (list): Dates when repayments are made.  
- `offset_contribution_dates` (list): Dates when offset contributions are made.  
- `offset_contribution_regular_amount` (float): Regular offset contribution amount.  
- `extra_repayments_dates` (list): Dates for extra repayments.  
- `extra_repayments_regular_amount` (float): Regular extra repayment amount.  
- `capture_interest_accrual` (bool): Whether to capture daily and monthly interest accruals.

**Returns**  
- `pd.DataFrame`: A DataFrame containing the loan schedule.

---

## `create_amortization_schedule`

**Description**  
Generates loan transactions by passing required input to the daily routine.

**Arguments**  
- `start_date` (str): The settlement date in `YYYY-MM-DD` format.  
- `loan_amount` (float): The loan amount (principal).  
- `annual_rate` (float): The annual interest rate.  
- `loan_duration_years` (int): Loan duration in years.  
- `loan_duration_months` (int): Additional loan duration in months.  
- `repayment_frequency` (str): Frequency of repayments (`'weekly'`, `'monthly'`, etc.).  
- `initial_offset_amount` (float): Initial offset account contribution.  
- `offset_contribution_frequency` (str): Frequency of offset contributions.  
- `regular_amount_offset_contribution` (float): Regular offset contribution amount.  
- `extra_repayments_frequency` (str): Frequency of extra repayments.  
- `extra_repayments_regular_amount` (float): Regular extra repayment amount.  
- `capture_interest_accrual` (bool): Whether to capture daily and monthly interest accruals.

**Returns**  
- `pd.DataFrame`: A DataFrame containing the loan transactions.

---

## `create_monthly_summary`

**Description**  
Creates a monthly summary of repayments, interest charged, outstanding loan amount, and offset account balance.

**Arguments**  
- `transactions` (pd.DataFrame): A DataFrame containing loan transactions.

**Returns**  
- `pd.DataFrame`: A DataFrame containing the monthly summary.  
- `float`: Total interest charged over the loan period.  
- `float`: Total repayments made over the loan period.

---

## `prepare_loan_summary`

**Description**  
Creates a loan summary from loan details.

**Arguments**  
- `loan_params` (dict): A dictionary containing loan parameters.  
- `store_results` (bool): Whether to store results as CSV files.

**Returns**  
- `dict`: A dictionary containing:  
  - `all_transactions` (pd.DataFrame): All loan transactions.  
  - `monthly_summary` (pd.DataFrame): Monthly summary of the loan.  
  - `total_interest_charged` (float): Total interest charged.  
  - `total_repayments` (float): Total repayments made.

---