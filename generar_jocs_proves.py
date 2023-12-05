# Importació de llibreries
import numpy as np
import networkx as nx
from typing import Union
import matplotlib.pyplot as plt
import os

# Comprovació de la correcta instal·lació del planner per MacOS
def correct_compilation_on_mac():
	return os.path.isfile('./executables/macos/ff')

# Definició de classe Book
class Book:
	def __init__(self, name: str, pages: Union[None, int] = None):
		self.name: str = name
		self.pages: Union[None, int] = pages

	def __repr__(self) -> str:
		return f'{self.name}'
	
	def __eq__(self, other: 'Book') -> bool:
		return self.name == other.name
	
	def __hash__(self) -> int:
		return hash(self.name)

# Definició de funcions auxiliars
def has_cycle(graph: nx.DiGraph, u: Book, v: Book, cycle_type: str = 'directed') -> bool:
	assert cycle_type in {'directed', 'undirected'}, "Error: El tipus de cicle ha de ser 'directed' o 'undirected'."
	"""
	Retorna True si la aresta (u, v) crea un cicle en el graf, False en cas contrari.
	"""
	try:
		# Afegeix la arista (u, v) al graf i comprova si hi ha cicle
		graph.add_edge(u, v)
		if cycle_type == 'directed':
			if nx.find_cycle(graph, orientation='original'):
				return True
		elif cycle_type == 'undirected':
			if nx.find_cycle(graph, orientation='ignore'):
				return True
	except:
		pass
	finally:
		# Elimina la arista (u, v) del graf per restaurar l'estat inicial
		graph.remove_edge(u, v)
	return False

def add_edge_if_no_cycle(graph: nx.DiGraph, u: Book, v: Book, edge_name: str, cycle_type: str = 'directed') -> bool:
	assert edge_name in {'predecessor', 'parallel'}, "Error: El nom de l'aresta ha de ser 'predecessor' o 'parallel'."
	assert cycle_type in {'directed', 'undirected'}, "Error: El tipus de cicle ha de ser 'directed' o 'undirected'."
	"""
	Afegeix l'aresta (u, v) al graf si no crea un cicle.
	"""
	if not has_cycle(graph, u, v, cycle_type=cycle_type):
		graph.add_edge(u, v, name=edge_name)
		print(f"\t* Aresta {edge_name.capitalize()}({u} -> {v}) afegida correctament (el graf no conté cicles).")
		return True
	return False
	
def parallel_chained_nodes(graph: nx.DiGraph, initial_node: Book) -> tuple:
	"""
	Retorna un conjunt amb tots els nodes que estan enllaçats amb el node inicial mitjançant arestes 'parallel' (incloent el node inicial).
	"""
	assert graph.number_of_nodes() > 0, "El graf no pot estar buit."
	assert graph.has_node(initial_node), "El node inicial ha d'estar en el graf."

	visited = set()

	def is_parallel(node1: Book, node2: Book):
		"""
		Retorna True si existeix una aresta 'parallel' que va de node1 a node2 o de node2 a node1, False en cas contrari.
		"""
		return (graph.get_edge_data(node1, node2, {}).get('name', '') == 'parallel' or
				graph.get_edge_data(node2, node1, {}).get('name', '') == 'parallel')

	def recursive(node: Book):
		"""
		Recorre el graf de forma recursiva per trobar tots els nodes que estan enllaçats amb el node inicial mitjançant arestes 'parallel'.
		"""
		if node in visited:
			return
		
		visited.add(node)

		for neighbor in graph.neighbors(node):
			if is_parallel(node, neighbor):
				recursive(neighbor)

		# Revisar también los nodos que apuntan a este con una arista 'parallel'
		for predecessor in graph.predecessors(node):
			if is_parallel(predecessor, node):
				recursive(predecessor)

	recursive(initial_node)
	
	list_visited = list(visited)
	list_visited.sort(key=lambda x: x.name)

	return tuple(list_visited)


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
hp_dict: dict = {
	'HP1_Harry_Potter_and_the_Philosophers_Stone': 220,
	'HP2_Harry_Potter_and_the_Chamber_of_Secrets': 250,
	'HP3_Harry_Potter_and_the_Prisoner_of_Azkaban': 315,
	'HP4_Harry_Potter_and_the_Goblet_of_Fire': 635,
	'HP5_Harry_Potter_and_the_Order_of_the_Phoenix': 800,
	'HP6_Harry_Potter_and_the_Half-Blood_Prince': 600,
	'HP7_Harry_Potter_and_the_Deathly_Hallows': 600
}
hp_books: dict = {n: Book(name=n, pages=p) for n, p in hp_dict.items()}
hp_graph = nx.DiGraph()
hp_graph.add_nodes_from(hp_books.values())
hp_graph.add_edge(hp_books['HP1_Harry_Potter_and_the_Philosophers_Stone'], hp_books['HP2_Harry_Potter_and_the_Chamber_of_Secrets'], name='predecessor')
hp_graph.add_edge(hp_books['HP2_Harry_Potter_and_the_Chamber_of_Secrets'], hp_books['HP3_Harry_Potter_and_the_Prisoner_of_Azkaban'], name='predecessor')
hp_graph.add_edge(hp_books['HP3_Harry_Potter_and_the_Prisoner_of_Azkaban'], hp_books['HP4_Harry_Potter_and_the_Goblet_of_Fire'], name='predecessor')
hp_graph.add_edge(hp_books['HP4_Harry_Potter_and_the_Goblet_of_Fire'], hp_books['HP5_Harry_Potter_and_the_Order_of_the_Phoenix'], name='predecessor')
hp_graph.add_edge(hp_books['HP5_Harry_Potter_and_the_Order_of_the_Phoenix'], hp_books['HP6_Harry_Potter_and_the_Half-Blood_Prince'], name='predecessor')
hp_graph.add_edge(hp_books['HP6_Harry_Potter_and_the_Half-Blood_Prince'], hp_books['HP7_Harry_Potter_and_the_Deathly_Hallows'], name='predecessor')

# Llibres de la saga del Senyor dels Anells
lr_dict: dict = {
	'LR1_The_Fellowship_of_the_Ring': 420,
	'LR2_The_Two_Towers': 350,
	'LR3_The_Return_of_the_King': 415
}
lr_books: dict = {n: Book(name=n, pages=p) for n, p in lr_dict.items()}
lr_graph = nx.DiGraph()
lr_graph.add_nodes_from(lr_books.values())
lr_graph.add_edge(lr_books['LR1_The_Fellowship_of_the_Ring'], lr_books['LR2_The_Two_Towers'], name='predecessor')
lr_graph.add_edge(lr_books['LR2_The_Two_Towers'], lr_books['LR3_The_Return_of_the_King'], name='predecessor')

# Llibres de la saga dels Jocs de la Fam
hg_dict: dict = {
	'HG1_The_Hunger_Games': 370,
	'HG2_Catching_Fire': 390,
	'HG3_Mockingjay': 390
}
hg_books: dict = {n: Book(name=n, pages=p) for n, p in hg_dict.items()}
hg_graph = nx.DiGraph()
hg_graph.add_nodes_from(hg_books.values())
hg_graph.add_edge(hg_books['HG1_The_Hunger_Games'], hg_books['HG2_Catching_Fire'], name='predecessor')
hg_graph.add_edge(hg_books['HG2_Catching_Fire'], hg_books['HG3_Mockingjay'], name='predecessor')

# Llibres inventats de la saga Marvel
mv_dict: dict = {
	'Avengers_1': 200,
	'Avengers_2': 250,
	'Avengers_3': 500,
	'Ironman': 300,
	'Hulk': 250,
	'Captain_America': 350,
	'Thor': 400,
	'Black_Widow': 300,
	'Hawkeye': 250,
	'Spiderman_1': 250,
	'Spiderman_2': 300,
	'Guardians_of_the_Galaxy_1': 300,
	'Guardians_of_the_Galaxy_2': 550,
	'Guardians_of_the_Galaxy_3': 250,
	'Groot': 400,
}
mv_books: dict = {n: Book(name=n, pages=p) for n, p in mv_dict.items()}
mv_graph = nx.DiGraph()
mv_graph.add_nodes_from(mv_books.values())
mv_graph.add_edge(mv_books['Avengers_1'], mv_books['Avengers_2'], name='predecessor')
mv_graph.add_edge(mv_books['Avengers_2'], mv_books['Avengers_3'], name='predecessor')
mv_graph.add_edge(mv_books['Guardians_of_the_Galaxy_1'], mv_books['Guardians_of_the_Galaxy_2'], name='predecessor')
mv_graph.add_edge(mv_books['Guardians_of_the_Galaxy_2'], mv_books['Guardians_of_the_Galaxy_3'], name='predecessor')
mv_graph.add_edge(mv_books['Spiderman_1'], mv_books['Spiderman_2'], name='predecessor')
mv_graph.add_edge(mv_books['Avengers_1'], mv_books['Ironman'], name='parallel')
mv_graph.add_edge(mv_books['Avengers_1'], mv_books['Hulk'], name='parallel')
mv_graph.add_edge(mv_books['Avengers_1'], mv_books['Captain_America'], name='parallel')
mv_graph.add_edge(mv_books['Avengers_1'], mv_books['Thor'], name='parallel')
mv_graph.add_edge(mv_books['Avengers_1'], mv_books['Black_Widow'], name='parallel')
mv_graph.add_edge(mv_books['Avengers_1'], mv_books['Hawkeye'], name='parallel')
mv_graph.add_edge(mv_books['Groot'], mv_books['Guardians_of_the_Galaxy_1'], name='parallel')

# Més preguntes a l'usuari
while True:
	set_strings_sagas: set[str] = {'HP', 'hp', 'LR', 'lr', 'HG', 'hg', 'HELP', 'help', ''} if level < 2 else {'HP', 'hp', 'LR', 'lr', 'HG', 'hg', 'MV', 'mv', 'HELP', 'help', ''}
	options_str: str = 'HP/LR/HG/HELP' if level < 2 else 'HP/LR/HG/MV/HELP'
	try:
		books_list: list[str] = input(f"Introdueix les paraules clau de les sagues famoses de llibres separades per comes. Deixa-ho en blanc (buit) si no en vols incloure cap. (HELP per més informació) [{options_str}]:\n").replace(' ', '').split(',')
		for string in books_list:
			if string not in set_strings_sagas:
				raise ValueError
		if 'HELP' in books_list or 'help' in books_list:
			print(f"Pots escriure les següents paraules clau per incloure sagues famoses de llibres:\n\t* HP per incloure tots els {len(hp_books)} llibres de Harry Potter.\n\t* LR per incloure tots els {len(lr_books)} llibres del Senyor dels Anells (The Lord of the Rings).\n\t* HG per incloure tots els {len(hg_books)} llibres de la saga dels Jocs de la Fam (Hunger Games).")
			if level >= 2:
				print(f"\t* MV per incloure tots els {len(mv_books)} llibres inventats de la saga Marvel.")
			continue
		else:
			if 'HP' in books_list or 'hp' in books_list:
				for i, test_graph in enumerate(graphs):
					graphs[i] = nx.union(test_graph, hp_graph)
			if 'LR' in books_list or 'lr' in books_list:
				for i, test_graph in enumerate(graphs):
					graphs[i] = nx.union(test_graph, lr_graph)
			if 'HG' in books_list or 'hg' in books_list:
				for i, test_graph in enumerate(graphs):
					graphs[i] = nx.union(test_graph, hg_graph)
			if 'MV' in books_list or 'mv' in books_list:
				for i, test_graph in enumerate(graphs):
					graphs[i] = nx.union(test_graph, mv_graph)
	except ValueError:
		print("Error: Els valors no són vàlids. Introdueix només un els següents valors: HP, LR, HG, HELP.")
		continue
	break

# Nombre de llibres addicionals
while True:
	try:
		num_addi_books: int = int(input("Introdueix el nombre de llibres addicionals que vols generar en els joc de proves: ").replace(' ', ''))
		if num_addi_books < 0:
			raise ValueError
		elif (not num_addi_books) and (not books_list):
			raise AssertionError
	except ValueError:
		print("Error: Introdueix un nombre enter >= 0.")
		continue
	except AssertionError:
		print("Error: No has inclòs cap saga famosa de llibres, així que has d'introduir un nombre enter >= 1 per evitar jocs de prova sense llibres.")
		continue
	break

# Percentatge de predecessors i paral·lels
if level >= 2 and num_addi_books > 1:
	while True:
		try:
			proportion_parallels_str: str = input("Introdueix el percentatge de llibres paral·lels respecte els predecessors (HELP per més informació): ").replace(' ', '').replace(',', '.')
			if proportion_parallels_str in {'HELP', 'help'}:
				print("El percentatge que introdueixis determinarà la quantitat de llibres paral·lels respecte la quantitat de llibres predecessors. Aquest percentatge no es complirà de manera totalment estricte, però s'intentarà aproximar el màxim possible.")
				continue
			chosen_proportion_parallels: float = float(proportion_parallels_str)
			if not (0 < chosen_proportion_parallels <= 100):
				raise ValueError
		except ValueError:
			print("Error: Introdueix un nombre real en l'interval (0, 100].")
			continue
		chosen_proportion_parallels /= 100
		break

# Percentatge de llibres que s'han de llegir aleatòriament
while True:
	try:
		proportion_to_read: float = float(input("Introdueix el percentatge de llibres que s'han de llegir aleatòriament: ").replace(' ', '').replace(',', '.'))
		if not (0 < proportion_to_read <= 100):
			raise ValueError
	except ValueError:
		print("Error: Introdueix un nombre real en l'interval (0, 100].")
		continue
	proportion_to_read /= 100
	break

# Llavor (seed) per generar les relacions entre els llibres addicionals
if num_addi_books > 1:
	while True:
		try:
			seed: Union[None, int] = int(input("Introdueix la llavor (seed) per realitzar els processos aleatoris (0 per triar una llavor qualsevol): ").replace(' ', ''))
			if seed < 0:
				raise ValueError
			elif seed == 0:
				seed = None		
		except ValueError:
			print("Error: Introdueix un nombre enter >= 0.")
			continue
		np.random.seed(seed)
		break

# Generació dels grafs per cada joc de proves
for i, test_graph in enumerate(graphs):
	print(f"\nJOC DE PROVES [{i+1}] --> {num_addi_books} llibres addicionals afegits.")
	
	# Afegir llibres addicionals (només en cas que n'hi hagi)
	if num_addi_books > 0:
		tmp_addi_books: list[Book] = []
		for b in range(num_addi_books):
			if level == 3:
				while True:
					tmp_pages: int = int(np.random.normal(275, 100))
					if 15 <= tmp_pages <= 800:
						break
			
				tmp_book: Book = Book(f'Book_{b+1}', tmp_pages)
			else:
				tmp_book: Book = Book(f'Book_{b+1}')
			tmp_addi_books.append(tmp_book)
			test_graph.add_node(tmp_book)
		
		# Afegir les arestes (predecessor/parallel) als llibres addicionals (només en cas que n'hi hagi més d'un) 
		if num_addi_books > 1:
			tmp_added_edges: int = 0

			if level == 0:
				# "Nivel básico: En el plan de lectura todos los libros tienen 0 o 1 predecesores y ningún paralelo.
				# El planner es capaz de encontrar un plan para poder llegar a leer los libros objetivo encadenando
				# libros, donde cada libro tiene solo uno o ningún predecesor."
				for b in tmp_addi_books:
					if tmp_added_edges >= num_addi_books - 1: # Un graf acíclic no pot tenir més arestes que nodes - 1
						break
					if np.random.choice([True, False]):
						while True:
							tmp_pred: Book = np.random.choice(np.array(tmp_addi_books))
							if tmp_pred != b:
								break
						added: bool = add_edge_if_no_cycle(graph=test_graph, u=tmp_pred, v=b, edge_name='predecessor', cycle_type='undirected')
						if added:
							tmp_added_edges += 1
				
			elif level == 1:
				# "Extensión 1: Los libros pueden tener de 0 a N predecesores pero ningún paralelo. El planner
				# es capaz de construir un plan para poder llegar a leer los libros objetivo, donde para todo
				# libro que pertenece al plan, todos sus libros predecesores pertenecen al plan y están en meses anteriores."
				for b in tmp_addi_books:
					if tmp_added_edges >= num_addi_books - 1: # Un graf acíclic no pot tenir més arestes que nodes - 1
						break
					for _ in range(np.random.randint(num_addi_books)):
						if np.random.choice([True, False]):
							while True:
								tmp_pred: Book = np.random.choice(np.array(tmp_addi_books))
								if tmp_pred != b:
									break
							added: bool = add_edge_if_no_cycle(graph=test_graph, u=tmp_pred, v=b, edge_name='predecessor', cycle_type='undirected')
							if added:
								tmp_added_edges += 1

			elif level == 2:
				# "Extensión 2: Extensión 1 + los libros pueden tener de 0 a M libros paralelos. El planner es
				# capaz de construir un plan para poder llegar a leer los libros objetivo, donde para todo libro
				# que pertenece al plan, todos sus libros paralelos pertenecen al plan y están en el mismo mes o
				# en meses anteriores."
				proportion_parallels: float = chosen_proportion_parallels # Restaurem el valor introduït per l'usuari
				proportion_predecessors: float = max(0, 1 - proportion_parallels)
				proportion_predecessors = round(proportion_predecessors / 2, 3)
				proportion_parallels = round(proportion_parallels / 2, 3)

				for b in tmp_addi_books:
					if tmp_added_edges >= num_addi_books - 1: # Un graf acíclic no pot tenir més arestes que nodes - 1
						break
					for _ in range(np.random.randint(num_addi_books)):
						random_value = np.random.choice(['predecessor', 'parallel', 'None'], p=[proportion_predecessors, proportion_parallels, round(1 - proportion_predecessors - proportion_parallels, 3)])
						if random_value == 'predecessor':
							while True:
								tmp_pred: Book = np.random.choice(np.array(tmp_addi_books))
								if tmp_pred != b:
									break
							added: bool = add_edge_if_no_cycle(graph=test_graph, u=tmp_pred, v=b, edge_name='predecessor', cycle_type='undirected')
							if added:
								tmp_added_edges += 1
						elif random_value == 'parallel':
							while True:
								tmp_parallel: Book = np.random.choice(np.array(tmp_addi_books))
								if tmp_parallel != b:
									break
							if tmp_parallel not in test_graph.neighbors(b):
								added: bool = add_edge_if_no_cycle(graph=test_graph, u=tmp_parallel, v=b, edge_name='parallel', cycle_type='undirected')
								if added:
									tmp_added_edges += 1
			
			elif level == 3:
				# Extensión 3: Los libros tienen además un número de páginas. El planificador controla que en
				# el plan generado no se superen las 800 páginas al mes.
				proportion_parallels: float = chosen_proportion_parallels # Restaurem el valor introduït per l'usuari
				proportion_predecessors: float = max(0, 1 - proportion_parallels)
				proportion_predecessors = round(proportion_predecessors / 2, 3)
				proportion_parallels = round(proportion_parallels / 2, 3)
				
				print(f"\t* Percentatge de predecessors: {proportion_predecessors * 100}%\n\t* Percentatge de paral·lels: {proportion_parallels * 100}%\n\t* Percentatge de llibres sense aresta: {(1 - proportion_predecessors - proportion_parallels) * 100}%\n")
				for b in tmp_addi_books:
					if tmp_added_edges >= num_addi_books - 1: # Un graf acíclic no pot tenir més arestes que nodes - 1
						break
					for _ in range(np.random.randint(num_addi_books)):
						random_value = np.random.choice(['predecessor', 'parallel', 'None'], p=[proportion_predecessors, proportion_parallels, round(1 - proportion_predecessors - proportion_parallels, 3)])
						if random_value == 'predecessor':
							while True:
								tmp_pred: Book = np.random.choice(np.array(tmp_addi_books))
								if tmp_pred != b:
									break
							added: bool = add_edge_if_no_cycle(graph=test_graph, u=tmp_pred, v=b, edge_name='predecessor', cycle_type='undirected')
							if added:
								tmp_added_edges += 1
						elif random_value == 'parallel':
							while True:
								tmp_parallel: Book = np.random.choice(np.array(tmp_addi_books))
								if tmp_parallel != b:
									break
							# Comprova que la suma de les pàgines dels llibres paral·lels no superi les 1600 pàgines (2 mesos amb un màxim de 800 pàgines cada mes)
							# Comprova que estiguin en un grup de paral·lels diferent. Si estan en el mateix grup, no cal afegir l'aresta perquè ja són paral·lels.
							if parallel_chained_nodes(graph=test_graph, initial_node=b) != parallel_chained_nodes(graph=test_graph, initial_node=tmp_parallel):
								if tmp_parallel not in test_graph.neighbors(b) \
									and (sum(p1.pages for p1 in parallel_chained_nodes(graph=test_graph, initial_node=b)) + sum(p2.pages for p2 in parallel_chained_nodes(graph=test_graph, initial_node=tmp_parallel))) <= 1600:
									added: bool = add_edge_if_no_cycle(graph=test_graph, u=tmp_parallel, v=b, edge_name='parallel', cycle_type='undirected')
									if added:
										tmp_added_edges += 1

# Mostra els grafs de cada joc de proves
for i, test_graph in enumerate(graphs):
	print(f"\n\n********** JOC DE PROVES {i+1} **********\n")
	print(f"\t* {len(test_graph.nodes)} NODES: {[(n.name, n.pages) if n.pages is not None else n.name for n in list(test_graph.nodes)]}\n")
	print(f"\t* {len(list(e for e in test_graph.edges if test_graph.edges[e]['name'] == 'predecessor'))} ARESTES 'PREDECESSOR': {list(f'({e[0]} -> {e[1]})' for e in test_graph.edges if test_graph.edges[e]['name'] == 'predecessor')}\n")
	print(f"\t* {len(list(e for e in test_graph.edges if test_graph.edges[e]['name'] == 'parallel'))} ARESTES 'PARALLEL': {list(f'({e[0]} -> {e[1]})' for e in test_graph.edges if test_graph.edges[e]['name'] == 'parallel')}\n")

	edge_colors = ['lightblue' if test_graph.edges[e]['name'] == 'predecessor' else 'red' for e in test_graph.edges]
	nx.draw(test_graph, with_labels=True, node_color='lightgray', edge_color=edge_colors, node_size=250, arrowstyle='->', arrowsize=35, font_size=8)
	plt.show()

# Generació dels jocs de proves
for i, test_graph in enumerate(graphs):
	with open(f'./problems/generated_problem_ext_{level}_v{i+1}.pddl', 'w') as file:
		print(f"\t* S'ha generat el fitxer 'generated_problem_ext_{level}_v{i+1}.pddl' en el directori 'problems' amb el joc de proves {i+1}.")

		# HEADER
		file.write(f'(define (problem generated_problem_ext_{level}_v{i+1})\n\t(:domain reading_plan)\n')

		# OBJECTS
		books_str = ' '.join(list(str(n) for n in test_graph.nodes))
		months = 'Past January February March April May June July August September October November December'
		file.write(f'\t;;Objects\n\t(:objects\n\t\t{months} - month\n\t\t{books_str} - book\n\t)\n')

		# INIT
		file.write('\t;;Init\n\t(:init\n')
		
		# Order the months
		file.write('\t\t;;Order the months\n')
		file.write('\t\t(next_month January February) (next_month February March) (next_month March April)\n')
		file.write('\t\t(next_month April May) (next_month May June) (next_month June July)\n')
		file.write('\t\t(next_month July August) (next_month August September) (next_month September October)\n')
		file.write('\t\t(next_month October November) (next_month November December)\n')

		# Start on month 1
		file.write('\t\t;;Start on month 1\n')
		file.write('\t\t(current_month January)\n')
		file.write('\t\t(previous_month Past)\n')

		# Predecessors
		file.write('\t\t;;Predecessors\n')
		for e in test_graph.edges:
			if test_graph.edges[e]['name'] == 'predecessor':
				file.write(f'\t\t(predecessor {e[0]} {e[1]})\n')
		
		# Goal books			
		goal_books: set = set(np.random.choice(list(test_graph.nodes), size=int(max(1, round(test_graph.number_of_nodes() * proportion_to_read, 0))), replace=False))
		
		if level >= 2:
			# Parallels
			parallel_groups: set = set()
			file.write('\t\t;;Parallels\n')
			for n in set(test_graph.nodes):
				parallel_groups.add(parallel_chained_nodes(graph=test_graph, initial_node=n))
			
			for group in parallel_groups:
				group_root = list(group)[0]
				for n in group:
					if n in goal_books:
						group_root = n
						break
			
				for n in group:
					if n != group_root:
						file.write(f'\t\t(parallel {group_root} {n})\n')

		# Goal books
		file.write('\t\t;;Books the user would like to read\n')
		for b in goal_books:
			file.write(f'\t\t(goal_book {b})\n')

		# Read books
		remaining_books: set = set(test_graph.nodes) - goal_books # No podem haver llegit llibres que ens volem llegir en un futur (seria una contradicció)
		num_remaining_books: int = len(remaining_books)
		if num_remaining_books > 0:
			file.write('\t\t;;Books the user has already read\n')
			for b in set(np.random.choice(list(remaining_books), size=np.random.randint(max(1, num_remaining_books), num_remaining_books + 1), replace=False)):
				file.write(f'\t\t(read {b})\n')
				file.write(f'\t\t(assigned {b} Past)\n')

		if level == 3:
			# Book pages
			file.write('\t\t;;Book pages\n')
			for n in test_graph.nodes:
				file.write(f'\t\t(= (total_pages {n}) {n.pages})\n')
			
			# Initial pages read per month
			file.write('\t\t;;Initial pages read per month\n')
			for m in months.split():
				file.write(f'\t\t(= (pages_read {m}) 0)\n')
			
			# Initial number of months
			file.write('\t\t;;Initial number of months\n')
			file.write('\t\t(= (num_months_created) 1)\n')

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
		execute_planner: Union[bool, str] = input("Vols executar automàticament el planner per tots els jocs de prova generats? (HELP per més informació) [Y/N/HELP]: ").replace(' ', '')
		if execute_planner not in {'Y', 'y', 'N', 'n', 'HELP', 'help'}:
			raise ValueError
		else:
			if execute_planner in {'HELP', 'help'}:
				print("L'execució automàtica només està disponible per Sistemes Operatius Windows (amb Powershell instal·lat) o MacOS (amb Xcode instal·lat). Es realitzarà amb els següents programes proporcionats per realitzar la pràcitca:\n\t* Windows: metricff.\n\t* MacOS: ff.\n\nSi voleu executar el planner manualment, executeu la següent comanda:\n\t* Windows:\n\t\t>>> powershell\n\t\t>>> ./executables/windows/metricff -o ./domains/default_domain_ext_X.pddl -f ./problems/generated_problem_ext_X_vY.pddl\n\t* MacOS:\n\t\t >>> ./executables/macos/ff -o ./domains/default_domain_ext_X.pddl -f ./problems/default_problem_ext_X_vY.pddl\n\n\tOn X és el nivell d'extensió del joc de proves que voleu executar i Y és el número del joc de proves que voleu executar. Els resultats de l'execució es guardaran a la carpeta 'results'.")			
				continue
			elif execute_planner in {'Y', 'y'}:
				execute_planner = True
			else:
				execute_planner = False
	except ValueError:
		print("Error: Introdueix només un dels següents valors: Y, N, HELP.")
		continue
	break

if execute_planner:
	# Optimitzar el nombre de mesos
	optimize_months: Union[bool, str] = False
	
	while True:
		try:
			optimize_months = input("Vols aplicar l'optimitzador de nombre de mesos? (HELP per més informació) [Y/N/HELP]: ").replace(' ', '')
			if optimize_months not in {'Y', 'y', 'N', 'n', 'HELP', 'help'}:
				raise ValueError
			else:
				if optimize_months in {'HELP', 'help'}:
					print("L'optimitzador de nombre de mesos afegeix el flag '-O' a l'execució. D'aquesta manera es garantitza que el nombre de mesos que es generen en el plan sigui el mínim possible, però el cost computacional i el temps d'execució són molt més alts.")
					continue
				elif optimize_months in {'Y', 'y'}:
					optimize_months = True
				else:
					optimize_months = False
		except ValueError:
			print("Error: Introdueix només un dels següents valors: Y, N, HELP.")
			continue
		break

	# Execució del planner
	import platform #Per saber si estem a Windows, Linux o MacOS
	import subprocess # Per executar el planner

	operative_system = platform.system()

	if operative_system not in {'Windows', 'Darwin'}:
		raise RuntimeError("El programa no ha pogut verificar que el vostre sistema operatiu sigui Windows o MacOS. Siusplau, executeu el planner manualment.")

	# Windows
	if operative_system == 'Windows':
		for i in range(n_tests):
			if optimize_months:
				with open(f'./results/generated_opt_result_ext_{level}_v{i+1}.txt', 'w') as result_file:
					execution = subprocess.run(['powershell', f'./executables/windows/metricff -O -o ./domains/default_domain_ext_{level}.pddl -f ./problems/generated_problem_ext_{level}_v{i+1}.pddl'], shell=True, stdout=result_file)
					print(f"\t* S'ha generat el fitxer 'generated_opt_result_ext_{level}_v{i+1}.txt' en el directori 'results' amb el resultat de l'execució del planner.")
			else:
				with open(f'./results/generated_result_ext_{level}_v{i+1}.txt', 'w') as result_file:
					execution = subprocess.run(['powershell', f'./executables/windows/metricff -o ./domains/default_domain_ext_{level}.pddl -f ./problems/generated_problem_ext_{level}_v{i+1}.pddl'], shell=True, stdout=result_file)
					print(f"\t* S'ha generat el fitxer 'generated_result_ext_{level}_v{i+1}.txt' en el directori 'results' amb el resultat de l'execució del planner.")
	
	# MacOS
	elif operative_system == 'Darwin':
		# Ejecutar el script de compilació del planner en cas que no estigui compilat
		if not correct_compilation_on_mac():
			subprocess.run('cd ./executables/macos && make ff', shell=True)
		
		for i in range(n_tests):
			if optimize_months:
				with open(f'./results/generated_opt_result_ext_{level}_v{i+1}.txt', 'w') as result_file:
					execution = subprocess.run([f'./executables/macos/ff -O -o ./domains/default_domain_ext_{level}.pddl -f ./problems/generated_problem_ext_{level}_v{i+1}.pddl'], shell=True, stdout=result_file)
					print(f"\t* S'ha generat el fitxer 'generated_opt_result_ext_{level}_v{i+1}.txt' en el directori 'results' amb el resultat de l'execució del planner.")
			else:
				with open(f'./results/generated_result_ext_{level}_v{i+1}.txt', 'w') as result_file:
					execution = subprocess.run([f'./executables/macos/ff -o ./domains/default_domain_ext_{level}.pddl -f ./problems/generated_problem_ext_{level}_v{i+1}.pddl'], shell=True, stdout=result_file)
					print(f"\t* S'ha generat el fitxer 'generated_result_ext_{level}_v{i+1}.txt' en el directori 'results' amb el resultat de l'execució del planner.")