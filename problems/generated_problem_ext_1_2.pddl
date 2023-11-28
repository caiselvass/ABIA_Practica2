(define (problem reading_plan_problem_ext_1_2)
	(:domain reading_plan)
	;;Objects
	(:objects
		Past January February March April May June July August September October November December - month
		Book_1 Book_2 Book_3 Book_4 Book_5 Book_6 Book_7 Book_8 Book_9 - book
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
		(predecessor Book_2 Book_5)
		(predecessor Book_4 Book_1)
		(predecessor Book_6 Book_3)
		(predecessor Book_6 Book_8)
		(predecessor Book_7 Book_3)
		(predecessor Book_8 Book_5)
		(predecessor Book_9 Book_4)
		(predecessor Book_9 Book_5)
		;;Books the user would like to read
		(goal_book Book_4)
		(goal_book Book_6)
		(goal_book Book_8)
		(goal_book Book_9)
		(goal_book Book_3)
		(goal_book Book_2)
		;;Books the user has already read
		(read Book_5)
		(goal_book Book_5)
		(assigned Book_5 Past)
		(read Book_7)
		(goal_book Book_7)
		(assigned Book_7 Past)
		(read Book_1)
		(goal_book Book_1)
		(assigned Book_1 Past)
	)
	;;Goal
	(:goal
		(and
			(forall (?b - book) (imply (goal_book ?b) (read ?b)))
		)
	)
)