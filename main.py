def calculate_sharpe_ratio(returns, risk_free_rate, volatility):
    # Calculate excess returns
    excess_returns = returns - risk_free_rate

    # Calculate Sharpe ratio
    sharpe_ratio = excess_returns / volatility

    return sharpe_ratio

def get_user_inputs():
    try:
        returns = float(input("Enter the portfolio returns: "))
        risk_free_rate = float(input("Enter the risk-free rate: "))
        volatility = float(input("Enter the standard deviation or volatility: "))
        return returns, risk_free_rate, volatility
    except ValueError:
        print("Please enter valid numerical values.")
        return get_user_inputs()

if __name__ == "__main__":
    print("Calculate Sharpe Ratio")
    portfolio_returns, risk_free, portfolio_volatility = get_user_inputs()

    sharpe = calculate_sharpe_ratio(portfolio_returns, risk_free, portfolio_volatility)
    print(f"The Sharpe Ratio for the given inputs is: {sharpe}")
