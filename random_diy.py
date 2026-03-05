import time
from hashlib import sha256


class RandomGenerator:
	def __init__(self, seed=None):
		if seed == None:
			self.seed = time.time()
		else:
			self.seed = seed



	def generate_random_number(self, max_value, recur=True):
		random_number = int(f'0x{sha256(str(self.seed).encode("utf-8")).hexdigest()}',16) % max_value
		if recur:
			self.seed += self.generate_random_number(max_value, recur=False)
		return random_number


random_generator_object = RandomGenerator(seed=42)
for _ in range(10):
	random_number = random_generator_object.generate_random_number(max_value=100)
	print(random_number)