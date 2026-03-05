import numpy

surfaces = numpy.array([100, 200 ,300])

def sum_dia2(array):
	total = 0 
	for value in array:
		total += value
	return total 


def len_dia2(array):
	index = 0
	while True:
		try:
			array[index]
			index += 1
		except:
			return index


def mean_dia2(array):
	return sum_dia2(array)/len_dia2(array)


def std_dia2(array):
	"""
	ecart moyen à la moyenne
	"""
	mean_array = mean_dia2(array)
	distances_to_mean = [] 

	for value in array: 
		distances_to_mean.append((value - mean_array)**2)

	return mean_dia2(distances_to_mean)**(1/2)


def standard_normalisation_dia2(array):
	standard_array = []
	mean_array = mean_dia2(array)
	std_array = std_dia2(array)

	for value in array:
		standard_value = (value - mean_array) / std_array
		standard_array.append(float(standard_value))

	return standard_array, mean_array, std_array

















standard_surface, mean_surface, std_surface = standard_normalisation_dia2(surfaces)
print(surfaces)
print("mean : ", mean_dia2(surfaces))
print("std : ", std_dia2(surfaces))
print("_"*20)
print(standard_surface)
print("mean : ", mean_dia2(standard_surface))
print("std : ", std_dia2(standard_surface))








