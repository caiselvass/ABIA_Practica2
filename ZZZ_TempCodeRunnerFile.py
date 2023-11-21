# Generació dels jocs de proves
for i in range(n_tests):
	with open(f'problem{i}.pddl', 'w') as file:
		# HEADER
		file.write(f'(define (problem reading_plan_problem_{i})\n\t(:domain reading_plan)\n')

		# OBJECTS
		books_str = ' '.join(books)
		months = 'January February March April May June July August September October November December'

		file.write(f'\t;;Objects\n(:objects\n{months} - months\n{books_str} - books)\n')