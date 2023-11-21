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

books = set()

hp_books = [
	'pre',
    ['HP1_Harry_Potter_and_the_Philosopher\'s_Stone', 223],
    ['HP2_Harry_Potter_and_the_Chamber_of_Secrets', 251],
    ['HP3_Harry_Potter_and_the_Prisoner_of_Azkaban', 317],
    ['HP4_Harry_Potter_and_the_Goblet_of_Fire', 636],
    ['HP5_Harry_Potter_and_the_Order_of_the_Phoenix', 766],
    ['HP6_Harry_Potter_and_the_Half-Blood_Prince', 607],
    ['HP7_Harry_Potter_and_the_Deathly_Hallows', 607]
]

lr_books = [
	'pre',
    ['LR1_The_Fellowship_of_the_Ring', 423],
    ['LR2_The_Two_Towers', 352],
    ['LR3_The_Return_of_the_King', 416]
]

hg_books = [
	'pre',
    ['HG1_The_Hunger_Games', 374],
    ['HG2_Catching_Fire', 391],
    ['HG3_Mockingjay', 390]
]

while True:
	try:
		books_list = input("Introdueix les paraules clau de les sagues famoses de llibres separades per comes. Deixa-ho en blanc (buit) si no en vols incloure cap. [HELP per més detalls]:\n").replace(' ', '').split(',')
		if len(books_list) == 1 and books_list[0] in {'HELP', 'help'}:
			print(f"Pots escriure les següents paraules clau per incloure sagues famoses de llibres:\n    1) HP per incloure tots els 7 llibres de Harry Potter.\n    2) LR per incloure tots els 3 llibres del Senyor dels Anells (The Lord of the Rings).\n    3) HG per incloure tots els 3 llibres de la saga dels Jocs de la Fam (Hunger Games).")
			continue
		else:
			if 'HP' in books_list:
				books.add(hp_books)
			if 'LR' in books_list:
				books.add(lr_books)
			if 'HG' in books_list:
				books.add(hg_books)

	except ValueError:
		print("Error: Els valors no són vàlids.")
		continue
	break

while True:
	try:
		addi_books = int(input("Introdueix el nombre màxim de llibres addicionals que vols generar per cada joc de proves: "))
		if addi_books < 0:
			raise ValueError
		else:
			while True:
				try:
					seed = int(input("Introdueix la llavor per generar aleatòriament diferents nombres de llibres addicionals per cada joc de proves [0 per triar una llavor qualsevol]: "))
					if seed == 0:
						seed = None
					rng = random.Random(seed)
				except ValueError:
					print("Error: Introdueix un nombre enter.")
					continue
				break
			addi_books = rng.randint(0, addi_books)
	except ValueError:
		print("Error: Introdueix un nombre enter >= 0.")
		continue
	break

random_predecessors = ['pre']
random_parallels = ['par']
for i in range(1, addi_books + 1):
	if rng.choice([True, False]):
		random_predecessors.append(f'book_pre_{i}')
	else:
		random_parallels.append(f'book_par_{i}')
	
	if len(random_predecessors) > 1:
		books.add(random_predecessors)
	if len(random_parallels) > 1:
		books.add(random_parallels)

for group_books in books:
	print(group_books)

# Generació dels jocs de proves
for i in range(n_tests):
	with open(f'problem{i}.pddl', 'w') as file:
		# HEADER
		file.write(f'(define (problem reading_plan_problem_{i})\n\t(:domain reading_plan)\n')

		# OBJECTS
		books_str = ' '.join(books)
		months = 'Past January February March April May June July August September October November December'

		file.write(f'\t;;Objects\n(:objects\n{months} - months\n{books_str} - books)\n')

