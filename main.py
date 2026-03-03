import numpy
import pandas
import matplotlib.pyplot as plt
import random

def plot(problems, solutions, predictions):
	plt.figure(figsize=(15, 6))
	plt.plot(problems, solutions, "ro")
	plt.plot(problems, predictions, "g")

	plt.show()





def linear_regression(a, b, problems):
	return a * problems + b




if __name__ == "__main__":
	house_prices_df = pandas.read_csv("prix_maisons.csv")

	# explication : normalisation standard <- # stats

	x_mean, x_std = house_prices_df["surface"].mean(), house_prices_df["surface"].std()
	y_mean, y_std = house_prices_df["prix"].mean(), house_prices_df["prix"].std()

	
	house_prices_df["surface"] = (house_prices_df["surface"] - x_mean )/ x_std
	house_prices_df["prix"] = (house_prices_df["prix"] - y_mean )/ y_std

	##### l'implémentation de notre optimizer
	a = random.random()
	b = random.random()
	
	predictions = linear_regression(a, b, house_prices_df["surface"])


	plot(problems=house_prices_df["surface"], solutions=house_prices_df["prix"], predictions=predictions)