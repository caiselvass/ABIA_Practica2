(define (problem reading_plan_problem_ext_2_5)
	(:domain reading_plan)
	;;Objects
	(:objects
		Past January February March April May June July August September October November December - month
		January_1 February_1 March_1 April_1 May_1 June_1 July_1 August_1 September_1 October_1 November_1 December_1 - month
		January_2 February_2 March_2 April_2 May_2 June_2 July_2 August_2 September_2 October_2 November_2 December_2 - month
		January_3 February_3 March_3 April_3 May_3 - month

		Book_1 Book_2 Book_3 Book_4 Book_5 Book_6 Book_7 Book_8 Book_9 Book_10 Book_11 Book_12 Book_13 Book_14 Book_15 - book
		Book_16 Book_17 Book_18 Book_19 Book_20 Book_21 Book_22 Book_23 Book_24 Book_25 Book_26 Book_27 Book_28 Book_29 Book_30 - book
		Book_31 Book_32 Book_33 Book_34 Book_35 Book_36 Book_37 Book_38 Book_39 Book_40 - book
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
		(next_month July_1 August_1) (next_month August_1 September_1) (next_month September_1 October_1)
		(next_month October_1 November_1) (next_month November_1 December_1) (next_month December_1 January_2)
		(next_month January_2 February_2) (next_month February_2 March_2) (next_month March_2 April_2)
		(next_month April_2 May_2) (next_month May_2 June_2) (next_month June_2 July_2)
		(next_month July_2 August_2) (next_month August_2 September_2) (next_month September_2 October_2)
		(next_month October_2 November_2) (next_month November_2 December_2) (next_month December_2 January_3)
		(next_month January_3 February_3) (next_month February_3 March_3) (next_month March_3 April_3)
		(next_month April_3 May_3) 
		;;Start on month 1
		(current_month January)
		(previous_month Past)
		;;Predecessors
		
		(predecessor Book_1 Book_2) (predecessor Book_2 Book_3) (predecessor Book_3 Book_4) (predecessor Book_4 Book_5)
		(predecessor Book_5 Book_6) (predecessor Book_6 Book_7) (predecessor Book_7 Book_8) (predecessor Book_8 Book_9)
		(predecessor Book_9 Book_10) (predecessor Book_10 Book_11) (predecessor Book_11 Book_12) (predecessor Book_12 Book_13)
		(predecessor Book_13 Book_14) (predecessor Book_14 Book_15) (predecessor Book_15 Book_16) (predecessor Book_16 Book_17)
		(predecessor Book_17 Book_18) (predecessor Book_18 Book_19) (predecessor Book_19 Book_20) (predecessor Book_20 Book_21)
		(predecessor Book_21 Book_22) (predecessor Book_22 Book_23) (predecessor Book_23 Book_24) (predecessor Book_24 Book_25)
		(predecessor Book_25 Book_26) (predecessor Book_26 Book_27) (predecessor Book_27 Book_28) (predecessor Book_28 Book_29)
		(predecessor Book_29 Book_30) (predecessor Book_30 Book_31) (predecessor Book_31 Book_32) (predecessor Book_32 Book_33)
		(predecessor Book_33 Book_34) (predecessor Book_34 Book_35) (predecessor Book_35 Book_36) (predecessor Book_36 Book_37)
		(predecessor Book_37 Book_38) (predecessor Book_38 Book_39) (predecessor Book_39 Book_40)


		;;Books the user would like to read
		(goal_book Book_40)
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
