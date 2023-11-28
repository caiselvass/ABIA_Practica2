(define (problem reading_plan_problem_ext_1_3)
	(:domain reading_plan)
	;;Objects
	(:objects
		Past January February March April May June July August September October November December - month
		Book_1 Book_2 Book_3 - book
	)
	;;Init
	(:init
		;;Order the months
		(next_month January February) (next_month February March) (next_month March April)
		(next_month April May) (next_month May June) (next_month June July)
		(next_month July August) (next_month August September) (next_month September October)
		(next_month October November) (next_month November December)
		;;Start on month 1
		(current_month January)
		(previous_month Past)
		;;Predecessos
		(predecessor Book_2 Book_3)
		;;Books the user would like to read
		(goal_book Book_1)
		;;Books the user has already read
		(read Book_3)
		(goal_book Book_3)
		(assigned Book_3 Past)
		(read Book_2)
		(goal_book Book_2)
		(assigned Book_2 Past)
	)
	;;Goal
	(:goal
		(and
			(forall (?b - book) (imply (goal_book ?b) (read ?b)))
		)
	)
)