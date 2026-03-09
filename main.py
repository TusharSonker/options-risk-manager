from src import pricing
def main():
	option_type = input("Enter the Option Type, C or P: ")
	stock_price = float(input("Enter the Stock Price: "))
	strike_price = float(input("Enter the Strike Price: "))
	time_of_expiry = float(input("Enter the Time of Expiration: "))
	risk_free_rate = float(input("Enter the Risk free rate: ")) / 100
	sigma = float(input("Enter the Volatility of the underlying: ")) /100
	print(pricing.option_pricing(stock_price,time_of_expiry,risk_free_rate,sigma,strike_price,option_type))

if __name__ == "__main__":
    main()