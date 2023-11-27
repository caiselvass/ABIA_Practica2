# Importació de llibreries
import numpy as np
import networkx as nx
from typing import Union
import matplotlib.pyplot as plt

# Definició de classe Book
class Book:
	def __init__(self, name: str, pages: int, goal: bool = False, read: bool = False):
		self.name: str = name
		self.pages: int = pages
		self.goal: bool = goal
		self.read: bool = read

	def __repr__(self) -> str:
		return f'{self.name}[{self.pages}]'
	
	def __eq__(self, other: 'Book') -> bool:
		return self.name == other.name
	
	def __hash__(self) -> int:
		return hash(self.name)
	

# Definició de funcions auxiliars
def has_cycle(graph: nx.DiGraph, u: Book, v: Book) -> bool:
	"""
	Retorna True si la aresta (u, v) crea un cicle en el graf, False en cas contrari.
	"""
	try:
		# Afegeix la arista (u, v) al graf i comprova si hi ha cicle
		graph.add_edge(u, v)
		if nx.find_cycle(graph, orientation='original'):
			return True
	except:
		pass
	finally:
		# Elimina la arista (u, v) del graf per restaurar l'estat inicial
		graph.remove_edge(u, v)
	return False

def add_edge_if_no_cycle(graph: nx.DiGraph, u: Book, v: Book, edge_name: str) -> None:
	assert edge_name in {'predecessor', 'parallel'}, "Error: El nom de l'aresta ha de ser 'predecessor' o 'parallel'."
	"""
	Afegeix l'aresta (u, v) al graf si no crea un cicle.
	"""
	if has_cycle(graph, u, v):
		print(f"    * L'aresta ({u} -> {v}) crearia un cicle. No s'ha afegit.")
	else:
		graph.add_edge(u, v, name=edge_name)
		print(f"    * Aresta ({u} -> {v}) afegida correctament.")


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
		n_tests: int = int(input(f"Introdueix el nombre de jocs de proves amb nivell d'extensió '{'B' if level == 0 else level}' que vols generar: ").replace(' ', ''))
		if n_tests < 1:
			raise ValueError
	except ValueError:
		print("Error: Introdueix un nombre enter >= 1.")
		continue
	break

# Inicialitzacions del les sagues de llibres famoses
graphs: list[nx.DiGraph] = [nx.DiGraph() for _ in range(n_tests)]

# Llibres de la saga de Harry Potter
hp_list: list[list[Union[str, int]]] = [
	['HP1_Harry_Potter_and_the_Philosopher\'s_Stone', 220],
	['HP2_Harry_Potter_and_the_Chamber_of_Secrets', 250],
	['HP3_Harry_Potter_and_the_Prisoner_of_Azkaban', 315],
	['HP4_Harry_Potter_and_the_Goblet_of_Fire', 635],
	['HP5_Harry_Potter_and_the_Order_of_the_Phoenix', 765],
	['HP6_Harry_Potter_and_the_Half-Blood_Prince', 605],
	['HP7_Harry_Potter_and_the_Deathly_Hallows', 605]
]
hp_books: list[Book] = [Book(name=n, pages=p) for n, p in hp_list]
hp_graph = nx.DiGraph()
hp_graph.add_nodes_from(hp_books)
for i in range(len(hp_books) - 1):
	hp_graph.add_edge(hp_books[i], hp_books[i+1], name='predecessor')

# Llibres de la saga del Senyor dels Anells
lr_list: list[list[Union[str, int]]] = [
	['LR1_The_Fellowship_of_the_Ring', 420],
	['LR2_The_Two_Towers', 350],
	['LR3_The_Return_of_the_King', 415]
]
lr_books: list[Book] = [Book(name, pages) for name, pages in lr_list]
lr_graph = nx.DiGraph()
lr_graph.add_nodes_from(lr_books)
for i in range(len(lr_books) - 1):
	lr_graph.add_edge(lr_books[i], lr_books[i+1], name='predecessor')

# Llibres de la saga dels Jocs de la Fam
hg_list: list[list[Union[str, int]]] = [
	['HG1_The_Hunger_Games', 370],
	['HG2_Catching_Fire', 390],
	['HG3_Mockingjay', 390]
]
hg_books: list[Book] = [Book(name, pages) for name, pages in hg_list]
hg_graph = nx.DiGraph()

for i in range(len(hg_books) - 1):
	hg_graph.add_edge(hg_books[i], hg_books[i+1], name='predecessor')

# Més preguntes a l'usuari
while True:
	try:
		books_list: list[str] = input("Introdueix les paraules clau de les sagues famoses de llibres separades per comes. Deixa-ho en blanc (buit) si no en vols incloure cap. [HELP per més detalls]:\n").replace(' ', '').split(',')
		for string in books_list:
			if string not in {'HP', 'LR', 'HG', 'HELP', 'help', ''}:
				raise ValueError
		if len(books_list) == 1 and books_list[0] in {'HELP', 'help'}:
			print(f"Pots escriure les següents paraules clau per incloure sagues famoses de llibres:\n    1) HP per incloure tots els 7 llibres de Harry Potter.\n    2) LR per incloure tots els 3 llibres del Senyor dels Anells (The Lord of the Rings).\n    3) HG per incloure tots els 3 llibres de la saga dels Jocs de la Fam (Hunger Games).")
			continue
		else:
			if 'HP' in books_list:
				for i, test_graph in enumerate(graphs):
					graphs[i] = nx.union(test_graph, hp_graph)
			if 'LR' in books_list:
				for i, test_graph in enumerate(graphs):
					graphs[i] = nx.union(test_graph, lr_graph)
			if 'HG' in books_list:
				for i, test_graph in enumerate(graphs):
					graphs[i] = nx.union(test_graph, hg_graph)
	except ValueError:
		print("Error: Els valors no són vàlids.")
		continue
	break

while True:
	try:
		max_addi_books: int = int(input("Introdueix el nombre màxim de llibres addicionals que vols generar per cada joc de proves: ").replace(' ', ''))
		if max_addi_books < 0:
			raise ValueError
		else:
			while True:
				try:
					seed: Union[int, None] = int(input("Introdueix la llavor per generar aleatòriament diferents nombres de llibres addicionals per cada joc de proves [0 per triar una llavor qualsevol]: ").replace(' ', ''))
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
	print(f"\nJOC DE PROVES [{i+1}] --> {num_addi_books} llibres addicionals afegits.")
	tmp_addi_books: list[Book] = []
	
	for b in range(num_addi_books):
		while True:
			tmp_pages: int = int(np.random.normal(400, 100))
			if 10 <= tmp_pages <= 800:
				break
		
		tmp_book: Book = Book(f'Book_{b+1}', tmp_pages)
		tmp_addi_books.append(tmp_book)
		test_graph.add_node(tmp_book)

	if level == 0:
		#Nivel básico: En el plan de lectura todos los libros tienen 0 o 1 predecesores y ningún paralelo.
		# El planner es capaz de encontrar un plan para poder llegar a leer los libros objetivo encadenando
		# libros, donde cada libro tiene solo uno o ningún predecesor.
		for b in tmp_addi_books:
			if np.random.choice([True, False]):
				while True:
					tmp_pred: Book = np.random.choice(np.array(tmp_addi_books))
					if tmp_pred != b:
						break
				add_edge_if_no_cycle(test_graph, tmp_pred, b, edge_name='predecessor')
		
	# elif level == 1:
	# 	#Extensión 1: Los libros pueden tener de 0 a N predecesores pero ningún paralelo. El planner
	# 	# es capaz de construir un plan para poder llegar a leer los libros objetivo, donde para todo
	# 	# libro que pertenece al plan, todos sus libros predecesores pertenecen al plan y están en meses anteriores.
	# elif level == 2:
	# 	#Extensión 2: Extensión 1 + los libros pueden tener de 0 a M libros paralelos. El planner es
	# 	# capaz de construir un plan para poder llegar a leer los libros objetivo, donde para todo libro
	# 	# que pertenece al plan, todos sus libros paralelos pertenecen al plan y están en el mismo mes o
		# en meses anteriores.
		
	elif level == 3:
		#Extensión 3: Los libros tienen además un número de páginas. El planificador controla que en
		# el plan generado no se superen las 800 páginas al mes.
		test_graph.add_edge(np.random.choice(list(test_graph.nodes)), list(test_graph.nodes)[-1], name=np.random.choice(['predecessor', 'parallel']))

# Mostra els grafs de cada joc de proves
for i, test_graph in enumerate(graphs):
	print(f"\n---------- JOC DE PROVES [{i+1}] ----------\n")
	print(f"    * {len(test_graph.nodes)} NODES: {list(test_graph.nodes)}\n")
	print(f"    * {len(list(e for e in test_graph.edges if test_graph.edges[e]['name'] == 'predecessor'))} ARESTES 'PREDECESSOR': {list(f'({e[0]} -> {e[1]})' for e in test_graph.edges if test_graph.edges[e]['name'] == 'predecessor')}\n")
	print(f"    * {len(list(e for e in test_graph.edges if test_graph.edges[e]['name'] == 'parallel'))} ARESTES 'PARALLEL': {list(f'({e[0]} -> {e[1]})' for e in test_graph.edges if test_graph.edges[e]['name'] == 'parallel')}\n")

	edge_colors = ['lightblue' if test_graph.edges[e]['name'] == 'predecessor' else 'red' for e in test_graph.edges]
	nx.draw(test_graph, with_labels=True, node_color='lightgray', edge_color=edge_colors, node_size=250, arrowstyle='->', arrowsize=35, font_size=6)
	plt.show()


# Generació dels jocs de proves
for i in range(n_tests):
	with open(f'./problems/problem_{i+1}.pddl', 'w') as file:
		# HEADER
		file.write(f'(define (problem reading_plan_problem_{i+1})\n\t(:domain reading_plan)\n')

		# OBJECTS
		books_str = ' '.join(list(str(n) for n in graphs[i].nodes))
		months = 'Past January February March April May June July August September October November December'
		file.write(f'\t;;Objects\n\t(:objects\n\t\t{months} - months\n\t\t{books_str} - books)\n\t)\n')

		# INIT
		file.write('\t;;Init\n\t(:init\n')
		
		# Order the months
		file.write('\t\t;;Order the months\n')
		file.write('\t\t(next_month January February)\n')
		file.write('\t\t(next_month February March)\n')
		file.write('\t\t(next_month March April)\n')
		file.write('\t\t(next_month April May)\n')
		file.write('\t\t(next_month May June)\n')
		file.write('\t\t(next_month June July)\n')
		file.write('\t\t(next_month July August)\n')
		file.write('\t\t(next_month August September)\n')
		file.write('\t\t(next_month September October)\n')
		file.write('\t\t(next_month October November)\n')
		file.write('\t\t(next_month November December)\n')

		# Initial number of months
		file.write('\t\t;;Initial number of months\n')
		file.write('\t\t(= (num_months_created) 1)\n')

		# Start on month 1
		file.write('\t\t;;Start on month 1\n')
		file.write('\t\t(current_month January)\n')
		file.write('\t\t(previous_month Past)\n')

		# Predecessors
		file.write('\t\t;;Predecessos\n')
		for e in graphs[i].edges:
			if graphs[i].edges[e]['name'] == 'predecessor':
				file.write(f'\t\t(predecessor {e[0]} {e[1]})\n')
		
		# Parallels
		file.write('\t\t;;Parallels\n')
		for e in graphs[i].edges:
			if graphs[i].edges[e]['name'] == 'parallel':
				file.write(f'\t\t(parallel {e[0]} {e[1]})\n')

		# Goal books
		file.write('\t\t;;Books the user would like to read\n')
		for b in np.random.choice(list(graphs[i].nodes), size=np.random.randint(1, len(list(graphs[i].nodes)) + 1), replace=False):
			file.write(f'\t\t(goal_book {b})\n')

		# Read books
		file.write('\t\t;;Books the user has already read\n')
		for b in np.random.choice(list(graphs[i].nodes), size=np.random.randint(1, len(list(graphs[i].nodes)) + 1), replace=False):
			file.write(f'\t\t(read {b})\n')
			file.write(f'\t\t(goal_book {b})')
			file.write(f'\t\t(assigned {b} Past)\n)')

		# Book pages
		file.write('\t\t;;Book pages\n')
		for n in graphs[i].nodes:
			file.write(f'\t\t(= (total_pages {n}) {n.pages})\n')

		# Initial pages read per month
		file.write('\t\t;;Initial pages read per month\n')
		for m in months.split():
			file.write(f'\t\t(= (pages_read {m}) 0)\n')

		file.write('\t)\n')

		# GOAL
		file.write('\t;;Goal\n\t(:goal\n')
		file.write('\t\t(and\n')
		file.write('\t\t\t(forall (?b - book) (imply (goal_book ?b) (read ?b)))\n\t\t)\n\t)\n')

		# METRICS
		file.write('\t;;Optimize the number of months\n\t(:metric minimize (num_months_created))\n')

		# FOOTER
		file.write(')')

# Pregunta a l'usuari si vol executar el planner
while True:
	try:
		execute_planner: Union[bool, str] = input("Vols executar el planner per tots els jocs de prova generats? [Y/N]: ").replace(' ', '')
		if execute_planner not in {'Y', 'y', 'N', 'n'}:
			raise ValueError
		else:
			if execute_planner in {'S', 's'}:
				execute_planner = True
			else:
				execute_planner = False
	except ValueError:
		print("Error: Introdueix només un dels següents valors: Y, N.")
		continue
	break

if execute_planner:
	# Optimitzar el nombre de mesos
	while True:
		try:
			optimize_months: Union[bool, str] = input("Vols aplicar l'optimitzador de nombre de mesos? [Y/N]: ").replace(' ', '')
			if optimize_months not in {'Y', 'y', 'N', 'n'}:
				raise ValueError
			else:
				if optimize_months in {'S', 's'}:
					optimize_months = True
				else:
					optimize_months = False
		except ValueError:
			print("Error: Introdueix només un dels següents valors: Y, N.")
			continue
		break

	# Execució del planner
	import platform #Per saber si estem a Windows, Linux o macOS
	import subprocess # Per executar el planner

	operative_system = platform.system()

	if operative_system not in {'Windows', 'Linux', 'Darwin'}:
		raise RuntimeError("El programa no ha pogut detectar quin és el vostre sistema operatiu. Siusplau, executeu el planner manualment.")

	if operative_system == 'Windows':
		for i in range(n_tests):
			if optimize_months:
				subprocess.run([f'./metricff -O -o ./domains/domain.pddl -f ./problems/problem_{i+1}.pddl'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			else:
				subprocess.run([f'./metricff -o ./domains/domain.pddl -f ./problems/problem_{i+1}.pddl'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	elif operative_system == 'Linux':
		for i in range(n_tests):
			if optimize_months:
				subprocess.run([f'./metricff -O -o ./domains/domain.pddl -f ./problems/problem_{i+1}.pddl'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			else:
				subprocess.run([f'./metricff -o ./domains/domain.pddl -f ./problems/problem_{i+1}.pddl'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	elif operative_system == 'Darwin':
		for i in range(n_tests):
			if optimize_months:
				subprocess.run([f'./metricff -O -o ./domains/domain.pddl -f ./problems/problem_{i+1}.pddl'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			else:
				subprocess.run([f'./metricff -o ./domains/domain.pddl -f ./problems/problem_{i+1}.pddl'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
