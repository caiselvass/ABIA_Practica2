# Importació de llibreries
import random

# Preguntes inicials a l'usuari
while True:
	try:
		n_tests = int(input("Introdueix el nombre de jocs de proves que vols generar: "))
		if n_tests < 1:
			raise ValueError
	except ValueError:
		print("Error: Introdueix un nombre enter >= 1.")
		continue
	break

while True:
	try:
		user_random_str = input("Vols generar els jocs de proves aleatoriament? [Y/N]: ")
		if user_random_str in {'Y', 'y', 'N', 'n'}:
			random_bool = user_random_str in {'Y', 'y'}
		else:
			raise ValueError
	except ValueError:
		print("Error: Introdueix Y o N.")
		continue
	break

if random_bool:
	while True:
		try:
			n_books = int(input("Introdueix el nombre màxim de llibres que vols generar per cada joc de proves: "))
			if n_books < 1:
				raise ValueError
			else:
				n_books = random.randint(1, n_books)
		except ValueError:
			print("Error: Introdueix un nombre enter >= 1.")
			continue
		break

# Generació dels jocs de proves
for i in range(n_tests):
	with open(f'problem{i}.pddl', 'w') as file:
		# HEADER
		file.write(f'(define (problem reading_plan_problem_{i})\n\t(:domain reading_plan)\n')

		# OBJECTS
		file.write('\t;;Objects\n(:objects\n')

