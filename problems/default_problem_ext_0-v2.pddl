(define (problem generated_problem_ext_0_v1)
	(:domain reading_plan)
	;;Objects
	(:objects
		Past January February March April May June July August September October November December - month
		Book_1 Book_2 Book_3 Book_4 Book_5 Book_6 Book_7 Book_8 Book_9 Book_10 - book
	)
	;;Init
	(:init
		;;Order the months
		(next_month January February) (next_month February March) (next_month March April)
		(next_month April May) (next_month May June) (next_month June July)
		(next_month July August) (next_month August September) (next_month September October)
		(next_month October November) (next_month November December)
        ;;Read books
        (read Book_2) 
        (read Book_6) 
		;;Start on month 1
		(current_month January)
		(previous_month Past)
		;;Predecessors
		(predecessor Book_1 Book_2)
		(predecessor Book_2 Book_3)
		(predecessor Book_3 Book_4)
        (predecessor Book_4 Book_5)

		(predecessor Book_6 Book_7)
		(predecessor Book_7 Book_8)
        (predecessor Book_8 Book_9)
        (predecessor Book_9 Book_10)
		;;Books the user would like to read
		(goal_book Book_5)
        (goal_book Book_10)
		;;Initialize num_months_created
		(= (num_months_created) 1)
	)
	;;Goal
	(:goal
		(and
			(forall (?b - book) (imply (goal_book ?b) (read ?b)))
		)
	)
	;;Optimize the number of months
	(:metric minimize (num_months_created))
)