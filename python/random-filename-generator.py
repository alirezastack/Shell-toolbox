def random_generator(self):
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	# generate a random filename
	for i in range(0, len(alpha)):
		random_filename += random.choice(alpha)

	return random_filename



