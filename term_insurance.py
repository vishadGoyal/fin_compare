"""Methods to compare various term insurance payment plans"""


def compound_interest(principle: int, rate_pp: float, years: int) -> float:
    """Returns compound interest."""
    # print(principle, rate_pp, years)
    amount = principle * (pow((1 + rate_pp / 100), years))
    # print("amount: ", amount)
    return amount - principle


def calculate_returns(
    investment_amount: int,
    expected_annual_return_percentage_points: float,
    years_of_investment: int,
    expected_tax_rate_percentage_points: float,
) -> float:
    """Calculates expected returns on investment."""
    gains = compound_interest(
        investment_amount, expected_annual_return_percentage_points, years_of_investment
    )
    # print("gains: ", gains)
    return investment_amount + gains * (1 - expected_tax_rate_percentage_points / 100)


def calculate_wealth_in_hand_at_retirement(
    disposable_yearly_income: int,
    expected_annual_return_pp: float,
    yearly_premium: int,
    premium_paying_years: int,
    current_age: int,
    retirement_age: int = 60,
) -> float:
    """Calculates total wealth at 85 with the given payment plan params."""
    # TODO: Consider better ways to handle retirement and compare plans
    # rather than deducting outstanding amount after retirement.
    years_till_retirement = retirement_age - current_age
    wealth = 0
    if premium_paying_years > years_till_retirement:
        wealth -= (premium_paying_years - years_till_retirement) * yearly_premium
    for i in range(retirement_age):
        wealth += calculate_returns(
            disposable_yearly_income - yearly_premium
            if i < premium_paying_years
            else disposable_yearly_income,
            expected_annual_return_pp,
            years_till_retirement - i,
            15,
        )
    return wealth


print(
    "Monthly, till 85",
    calculate_wealth_in_hand_at_retirement(
        2400000, 10, 10178 * 12, premium_paying_years=60, current_age=25
    ),
)
print(
    "Yearly, till 85",
    calculate_wealth_in_hand_at_retirement(
        2400000, 10, 115650, premium_paying_years=60, current_age=25
    ),
)
print(
    "Monthly, till 60",
    calculate_wealth_in_hand_at_retirement(
        2400000, 10, 11137 * 12, premium_paying_years=35, current_age=25
    ),
)
print(
    "Yearly, till 60",
    calculate_wealth_in_hand_at_retirement(
        2400000, 10, 126555, premium_paying_years=35, current_age=25
    ),
)
print(
    "Monthly, till 35",
    calculate_wealth_in_hand_at_retirement(
        2400000, 10, 28561 * 12, premium_paying_years=10, current_age=25
    ),
)
print(
    "Yearly, till 35",
    calculate_wealth_in_hand_at_retirement(
        2400000, 10, 324554, premium_paying_years=10, current_age=25
    ),
)
