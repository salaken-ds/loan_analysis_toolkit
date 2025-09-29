from loan_analysis_toolkit.schedule import prepare_loan_summary
import pandas as pd


if __name__ == "__main__":
    # loan parameters
    loan_amount = 650_000  # Loan amount in dollars
    annual_rate = 5.34     # Annual interest rate in percentage
    loan_duration_years = 30          # Loan term in years
    loan_duration_months = 0          # Additional months in loan term
    start_date = '2025-10-05'  # Loan settlement date
    repayment_frequency = 'fortnightly'  # Repayment frequency
    initial_offset_amount = 20_000  # Initial offset account balance in dollars
    offset_contribution_frequency = 'monthly'  # Offset contribution frequency
    offset_contribution_regular_amount = 500  # Offset contribution amount in dollars
    extra_repayments_frequency = 'annually'  # Extra repayments frequency
    extra_repayments_regular_amount = 5_000  # Extra repayments amount in dollars
    # Whether to capture daily and monthly interest accruals in the transactions
    # Default is False
    capture_interest_accrual = False

    loan_parameters_base = {
        'loan_amount' : loan_amount,
        'annual_rate' : annual_rate,
        'loan_duration_years' : loan_duration_years,
        'loan_duration_months' : loan_duration_months,
        'start_date' : start_date,
        'repayment_frequency' : repayment_frequency,
        'initial_offset_amount' : 0,
        'offset_contribution_frequency' : offset_contribution_frequency,
        'offset_contribution_regular_amount' : 0,
        'extra_repayments_frequency' : extra_repayments_frequency, 
        'extra_repayments_regular_amount' : 0,
        'capture_interest_accrual' : capture_interest_accrual
        }
    loan_parameters_offsetonly = {
        'loan_amount' : loan_amount,
        'annual_rate' : annual_rate,
        'loan_duration_years' : loan_duration_years,
        'loan_duration_months' : loan_duration_months,
        'start_date' : start_date,
        'repayment_frequency' : repayment_frequency,
        'initial_offset_amount' : initial_offset_amount,
        'offset_contribution_frequency' : offset_contribution_frequency,
        'offset_contribution_regular_amount' : offset_contribution_regular_amount,
        'extra_repayments_frequency' : extra_repayments_frequency, 
        'extra_repayments_regular_amount' : 0,
        'capture_interest_accrual' : capture_interest_accrual
        }
    
    loan_parameters_extratxnonly = {
        'loan_amount' : loan_amount,
        'annual_rate' : annual_rate,
        'loan_duration_years' : loan_duration_years,
        'loan_duration_months' : loan_duration_months,
        'start_date' : start_date,
        'repayment_frequency' : repayment_frequency,
        'initial_offset_amount' : 0,
        'offset_contribution_frequency' : offset_contribution_frequency,
        'offset_contribution_regular_amount' : 0,
        'extra_repayments_frequency' : extra_repayments_frequency, 
        'extra_repayments_regular_amount' : extra_repayments_regular_amount,
        'capture_interest_accrual' : capture_interest_accrual
        }
    loan_parameters_both= {
        'loan_amount' : loan_amount,
        'annual_rate' : annual_rate,
        'loan_duration_years' : loan_duration_years,
        'loan_duration_months' : loan_duration_months,
        'start_date' : start_date,
        'repayment_frequency' : repayment_frequency,
        'initial_offset_amount' : initial_offset_amount,
        'offset_contribution_frequency' : offset_contribution_frequency,
        'offset_contribution_regular_amount' : offset_contribution_regular_amount,
        'extra_repayments_frequency' : extra_repayments_frequency, 
        'extra_repayments_regular_amount' : extra_repayments_regular_amount,
        'capture_interest_accrual' : capture_interest_accrual
        }

    res_basic = prepare_loan_summary(loan_parameters_base, store_results = False)['total_interest_charged']
    res_offset = prepare_loan_summary(loan_parameters_offsetonly, store_results = False)['total_interest_charged']
    res_extracontrib = prepare_loan_summary(loan_parameters_extratxnonly, store_results = False)['total_interest_charged']
    res_both = prepare_loan_summary(loan_parameters_both, store_results = False)['total_interest_charged']

    # total_interest_paid_by_customer = res['total_interest_charged']
    print()
    print("Total interested payable by the customer: ")
    print("     - No offset, no extra repayments: ${}".format(round(res_basic,2) ))
    print("     - Offset with, no extra repayments: ${}".format(round(res_offset, 2)))
    print("     - No offset, with extra repayments: ${}".format(round(res_extracontrib, 2)))
    print("     - With offset, with extra repayments: ${}".format(round(res_both, 2)))
    print()

    # Total interested payable by the customer: 
    #  - No offset, no extra repayments: $647093.34
    #  - Offset with, no extra repayments: $423561.75
    #  - No offset, with extra repayments: $495545.42
    #  - With offset, with extra repayments: $353294.29
