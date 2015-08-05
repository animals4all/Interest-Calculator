def calculateSimpleInterest(principal, rate, time):
	'''Get interest only on principal'''

	interest = principal * rate * time
	balance = interest + principal
	return round(interest, 2), round(balance, 2)


def calculateCompoundInterest(principal, rate, time):
	'''Get interest on principal and old interest'''
	
	balance = principal * (1 + rate) ** time
	return round(balance, 2)


def main():
	quit = "n"

	# Continue looping until the player wants to quit
	while quit.lower() not in ("y", "yes"):
		print("")

		try:
			principal = float(input("Enter the principal: "))
		# Make sure the input isn't a string
		except ValueError:
			print("The principal must be a number.")
			continue
		print("")

		try:
			rate = float(input("Enter the interest rate as a percent: "))
		except ValueError:
			print("The interest rate must be a number.")
			continue
		# Convert the interest rate from a percent to a decimal
		rate /= 10
		print("")

		try:
			time = int(input("Enter the number of years you will be gaining interest: "))
		except ValueError:
			print("The number of years must be a number.")
			continue
		print("")

		simpleInterest, simpleBalance = calculateSimpleInterest(principal, rate, time)
		compoundBalance = calculateCompoundInterest(principal, rate, time)

		print("")
		print("Simple interest: " + str(simpleInterest))
		print("Final balance with simple interest: " + str(simpleInterest))
		print("Final balance with compound interest: " + str(compoundBalance))
		print("")

		quit = input("Do you want to quit? (y/n): ")


if __name__ == "__main__":
	main()
