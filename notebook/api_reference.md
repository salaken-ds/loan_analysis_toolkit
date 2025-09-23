# API Reference

This document provides an overview of the functions in the `schedule.py` file, including their arguments, descriptions, and return values.

---

## Functions

### 1. **`calculate_minimum_repayment`**
Calculates the minimum repayment amount for a loan using the compound interest formula.

#### Arguments:
- `principal` (float): The loan amount (principal).
- `annual_rate` (float): The annual interest rate (in percentage, e.g., 5 for 5%).
- `years` (int): The loan term in years.
- `months` (int): Additional months in the loan term.
- `repayment_frequency` (str): The repayment frequency. Valid values:
  - `'annual'`
  - `'monthly'`
  - `'quarterly'`
  - `'fortnightly'`
  - `'weekly'`

#### Returns:
- `float`: The minimum repayment amount per period.

---

### 2. **`calculate_daily_interest`**
Calculates the daily interest on the loan balance.

#### Arguments:
- `loan_balance` (float): The current loan balance.
- `annual_rate` (float): The annual interest rate (in percentage, e.g., 5 for 5%).

#### Returns:
- `float`: The daily interest amount.

---

### 3. **`find_relevant_dates`**
Generates a list of dates between a start date and an end date based on the specified frequency.

#### Arguments:
- `start_date` (datetime): The start date.
- `end_date` (datetime): The end date.
- `frequency` (str): The frequency of dates. Valid values:
  - `'daily'`
  - `'weekly'`
  - `'fortnightly'`
  - `'monthly'`
  - `'quarterly'`
  - `'annually'`

#### Returns:
- `list`: A list of `datetime` objects representing the dates.

---

### 4. **`calculate_end_date`**
Calculates the end date based on the start date, duration in years, and duration in months.

#### Arguments:
- `start_date` (datetime): The start date. Defaults to the current date.
- `years` (int): The duration in years.
- `months` (int): The duration in months.

#### Returns:
- `datetime`: The calculated end date.

---

### 5. **`generate_loan_transactions`**
Generates a loan schedule including repayments, interest charges, loan balance, and offset.

#### Arguments:
- `start_date` (datetime): The settlement date.
- `loan_amount` (float): The loan amount (principal).
- `annual_rate` (float): The annual interest rate (in percentage).
- `initial_offset_amount` (float): The initial amount in the offset account.
- `minimum_repayments` (float): The minimum repayment amount per period.
- `all_dates` (list): A list of all dates to iterate through (daily).
- `interest_charge_dates` (list): A list of dates when interest is charged (monthly).
- `repayment_dates` (list): A list of dates when repayments are made.
- `offset_contribution_dates` (list): A list of dates when offset contributions are made.
- `offset_contribution_regular_amount` (float): The regular contribution amount to the offset account.

#### Returns:
- `pd.DataFrame`: A DataFrame containing the loan schedule.

---

### 6. **`create_amortization_schedule`**
Generates loan transactions by passing required input to the daily routine.

#### Arguments:
- `start_date` (str): The settlement date in `YYYY-MM-DD` format.
- `loan_amount` (float): The loan amount (principal).
- `annual_rate` (float): The annual interest rate (in percentage).
- `loan_duration_years` (int): The loan term in years.
- `loan_duration_months` (int): Additional months in the loan term.
- `repayment_frequency` (str): The repayment frequency. Valid values:
  - `'weekly'`
  - `'fortnightly'`
  - `'monthly'`
- `initial_offset_amount` (float): The initial contribution to the offset account.
- `offset_contribution_frequency` (str): The frequency of offset contributions. Valid values:
  - `'weekly'`
  - `'fortnightly'`
  - `'monthly'`
- `regular_amount_offset_contribution` (float): The regular contribution amount to the offset account.

#### Returns:
- `pd.DataFrame`: A DataFrame containing the loan transactions.

---

### 7. **`create_monthly_summary`**
Creates a monthly summary of repayments made, interest charged, outstanding loan amount, and offset account balance.

#### Arguments:
- `transactions` (pd.DataFrame): A DataFrame containing all loan transactions.

#### Returns:
- `pd.DataFrame`: A DataFrame containing the monthly summary.
- `float`: The total interest charged over the loan term.
- `float`: The total repayments made over the loan term.

---

### 8. **`prepare_loan_summary`**
Creates a loan summary from loan details.

#### Arguments:
- `loan_params` (dict): A dictionary containing the following keys:
  - `start_date` (str): The settlement date in `YYYY-MM-DD` format.
  - `loan_amount` (float): The loan amount (principal).
  - `annual_rate` (float): The annual interest rate (in percentage).
  - `loan_duration_years` (int): The loan term in years.
  - `loan_duration_months` (int): Additional months in the loan term.
  - `repayment_frequency` (str): The repayment frequency.
  - `initial_offset_amount` (float): The initial contribution to the offset account.
  - `offset_contribution_frequency` (str): The frequency of offset contributions.
  - `offset_contribution_regular_amount` (float): The regular contribution amount to the offset account.
- `store_results` (bool): Whether to save the results to CSV files. Defaults to `False`.

#### Returns:
- `dict`: A dictionary containing:
  - `all_transactions` (pd.DataFrame): All loan transactions.
  - `monthly_summary` (pd.DataFrame): Monthly summary of the loan.
  - `total_interest_charged` (float): Total interest charged over the loan term.
  - `total_repayments` (float): Total repayments made over the loan term.

---

## Notes
- Ensure all required libraries (`datetime`, `timedelta`, `relativedelta`, `pandas`) are installed and imported.
- Handle exceptions for invalid inputs where applicable.