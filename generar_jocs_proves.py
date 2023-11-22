# Importació de llibreries
import numpy as np
import networkx as nx

# Definició de classe Book
class Book:
	def __init__(self, name: str, pages: int):
		self.name = name
		self.pages = pages

	def __repr__(self) -> str:
		return f'{self.name}'

# Nivell d'extensió dels jocs de proves
while True:
	try:
		level = input("Introdueix el nivell d'extensio dels jocs de proves que vols generar [B/1/2/3]: ").replace(' ', '')
		if level not in {'B', 'b', '1', '2', '3'}:
			raise ValueError
		else:
			if level in {'B', 'b'}:
				level = 0
			else:
				level = int(level)
	except ValueError:
		print("Error: Introdueix només un dels següents valors: B, 1, 2, 3.")
		continue
	break

# Nombre de jocs de proves a generar
while True:
	try:
		n_tests = int(input(f"Introdueix el nombre de jocs de proves amb nivell d'extensió '{'B' if level == 0 else level}' que vols generar: ").replace(' ', ''))
		if n_tests < 1:
			raise ValueError
	except ValueError:
		print("Error: Introdueix un nombre enter >= 1.")
		continue
	break

# Inicialitzacions del les sagues de llibres famoses
graphs = [nx.DiGraph() for _ in range(n_tests)]

# Llibres de la saga de Harry Potter
hp_list = [
    ['HP1_Harry_Potter_and_the_Philosopher\'s_Stone', 220],
    ['HP2_Harry_Potter_and_the_Chamber_of_Secrets', 250],
    ['HP3_Harry_Potter_and_the_Prisoner_of_Azkaban', 315],
    ['HP4_Harry_Potter_and_the_Goblet_of_Fire', 635],
    ['HP5_Harry_Potter_and_the_Order_of_the_Phoenix', 765],
    ['HP6_Harry_Potter_and_the_Half-Blood_Prince', 605],
    ['HP7_Harry_Potter_and_the_Deathly_Hallows', 605]
]
hp_books = [Book(name, pages) for name, pages in hp_list]
hp_graph = nx.DiGraph()
hp_graph.add_nodes_from(hp_books)
for i in range(len(hp_books) - 1):
	hp_graph.add_edge(hp_books[i], hp_books[i+1], name='predecessor')

# Llibres de la saga del Senyor dels Anells
lr_list = [
    ['LR1_The_Fellowship_of_the_Ring', 420],
    ['LR2_The_Two_Towers', 350],
    ['LR3_The_Return_of_the_King', 415]
]
lr_books = [Book(name, pages) for name, pages in lr_list]
lr_graph = nx.DiGraph()
lr_graph.add_nodes_from(lr_books)
for i in range(len(lr_books) - 1):
	lr_graph.add_edge(lr_books[i], lr_books[i+1], name='predecessor')

# Llibres de la saga dels Jocs de la Fam
hg_list = [
    ['HG1_The_Hunger_Games', 370],
    ['HG2_Catching_Fire', 390],
    ['HG3_Mockingjay', 390]
]
hg_books = [Book(name, pages) for name, pages in hg_list]
hg_graph = nx.DiGraph()
hg_graph.add_nodes_from(hg_books)
for i in range(len(hg_books) - 1):
	hg_graph.add_edge(hg_books[i], hg_books[i+1], name='predecessor')

# Més preguntes a l'usuari
while True:
	try:
		books_list = input("Introdueix les paraules clau de les sagues famoses de llibres separades per comes. Deixa-ho en blanc (buit) si no en vols incloure cap. [HELP per més detalls]:\n").replace(' ', '').split(',')
		for b in books_list:
			if b not in {'HP', 'LR', 'HG', 'HELP', 'help', ''}:
				raise ValueError
		if len(books_list) == 1 and books_list[0] in {'HELP', 'help'}:
			print(f"Pots escriure les següents paraules clau per incloure sagues famoses de llibres:\n    1) HP per incloure tots els 7 llibres de Harry Potter.\n    2) LR per incloure tots els 3 llibres del Senyor dels Anells (The Lord of the Rings).\n    3) HG per incloure tots els 3 llibres de la saga dels Jocs de la Fam (Hunger Games).")
			continue
		else:
			if 'HP' in books_list:
				for test_graph in graphs:
					test_graph = nx.compose(test_graph, hp_graph)
			if 'LR' in books_list:
				for test_graph in graphs:
					test_graph = nx.compose(test_graph, lr_graph)
			if 'HG' in books_list:
				for test_graph in graphs:
					test_graph = nx.compose(test_graph, hg_graph)
	except ValueError:
		print("Error: Els valors no són vàlids.")
		continue
	break

while True:
	try:
		max_addi_books = int(input("Introdueix el nombre màxim de llibres addicionals que vols generar per cada joc de proves: ").replace(' ', ''))
		if max_addi_books < 0:
			raise ValueError
		else:
			while True:
				try:
					seed = int(input("Introdueix la llavor per generar aleatòriament diferents nombres de llibres addicionals per cada joc de proves [0 per triar una llavor qualsevol]: ").replace(' ', ''))
					if seed == 0:
						seed = None
						np.random.seed(seed)
				except ValueError:
					print("Error: Introdueix un nombre enter.")
					continue
				break
			num_addi_books_list: list[int] = [np.random.randint(0, max_addi_books + 1) for _ in range(n_tests)]
	except ValueError:
		print("Error: Introdueix un nombre enter >= 0.")
		continue
	break

# Generació dels grafs per cada joc de proves
for i, test_graph in enumerate(graphs):
	num_addi_books: int = num_addi_books_list[i]
	
	for b in range(num_addi_books):
		while True:
			tmp_pages: int = int(np.random.normal(400, 100))
			if 10 <= tmp_pages <= 800:
				break

		test_graph.add_node(Book(f'Book_{b+1}', tmp_pages))

		if level == 0:
			
		elif level == 1:
		
		elif level == 2:
			
		elif level == 3:
			test_graph.add_edge(np.random.choice(list(test_graph.nodes)), list(test_graph.nodes)[-1], name=np.random.choice(['predecessor', 'parallel']))

# Mostra els grafs de cada joc de proves
for t, test_graph in enumerate(graphs):
	print(f"\n---------- JOC DE PROVES [{t+1}] ----------")
	for group_books in test_graph:
		print(group_books)
	

"""# Generació dels jocs de proves
for i in range(n_tests):
	with open(f'problem{i}.pddl', 'w') as file:
		# HEADER
		file.write(f'(define (problem reading_plan_problem_{i})\n\t(:domain reading_plan)\n')

		# OBJECTS
		books_str = ' '.join(books)
		months = 'Past January February March April May June July August September October November December'

		file.write(f'\t;;Objects\n(:objects\n{months} - months\n{books_str} - books)\n')"""

