(define (problem reading_plan_problem_ext_2_5)
	(:domain reading_plan)
	;;Objects
	(:objects
		Past January February March April May June July August September October November December - month
		January_1 February_1 March_1 April_1 May_1 June_1 July_1 August_1 - month

		Book_1 Book_2 Book_3 Book_4 Book_5 Book_6 Book_7 Book_8 Book_9 Book_10 Book_11 Book_12 Book_13 Book_14 Book_15 - book
		Book_16 Book_17 Book_18 Book_19 Book_20 - book
	)
	;;Init
	(:init
		;;Order the months
		(next_month January February) (next_month February March) (next_month March April)
		(next_month April May) (next_month May June) (next_month June July)
		(next_month July August) (next_month August September) (next_month September October)
		(next_month October November) (next_month November December) (next_month December January_1)
		(next_month January_1 February_1) (next_month February_1 March_1) (next_month March_1 April_1)
		(next_month April_1 May_1) (next_month May_1 June_1) (next_month June_1 July_1)
		(next_month July_1 August_1)

		;;Start on month 1
		(current_month January)
		(previous_month Past)
		;;Predecessors
		
		(predecessor Book_1 Book_2) (predecessor Book_2 Book_3) (predecessor Book_3 Book_4) (predecessor Book_4 Book_5)
		(predecessor Book_5 Book_6) (predecessor Book_6 Book_7) (predecessor Book_7 Book_8) (predecessor Book_8 Book_9)
		(predecessor Book_9 Book_10) (predecessor Book_10 Book_11) (predecessor Book_11 Book_12) (predecessor Book_12 Book_13)
		(predecessor Book_13 Book_14) (predecessor Book_14 Book_15) (predecessor Book_15 Book_16) (predecessor Book_16 Book_17)
		(predecessor Book_17 Book_18) (predecessor Book_18 Book_19) (predecessor Book_19 Book_20)


		;;Books the user would like to read
		(goal_book Book_20)
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
