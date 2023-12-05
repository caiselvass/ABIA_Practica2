(define (problem generated_problem_ext_0_v1)
	(:domain reading_plan)
	;;Objects
	(:objects
		Past January February March April May June July August September October November December - month
		Book_1 Book_2 Book_3 Book_4 Book_5 Book_6 Book_7 Book_8 Book_9 Book_10 Book_11 Book_12 Book_13 Book_14 Book_15 - book
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
		;;Predecessors
		(parallel Book_1 Book_2)
		(parallel Book_1 Book_3)
		(parallel Book_1 Book_4)
		(parallel Book_1 Book_5)
		(parallel Book_1 Book_6)
		
		(parallel Book_10 Book_7)
		(parallel Book_10 Book_8)
		(parallel Book_10 Book_9)

		(predecessor Book_10 Book_11)
		(predecessor Book_11 Book_12)
		(predecessor Book_12 Book_13)
		(predecessor Book_13 Book_14)
		(predecessor Book_14 Book_15)
		;;Books the user would like to read
		(goal_book Book_1)
		(goal_book Book_15)

        ;; Pages of each book
        (= (total_pages Book_1) 250)
        (= (total_pages Book_2) 200)
        (= (total_pages Book_3) 150)
        (= (total_pages Book_4) 300)
        (= (total_pages Book_5) 250)
        (= (total_pages Book_6) 400)
        (= (total_pages Book_7) 550)
        (= (total_pages Book_8) 200)
        (= (total_pages Book_9) 150)
        (= (total_pages Book_10) 450)
        (= (total_pages Book_11) 600)
        (= (total_pages Book_12) 500)
        (= (total_pages Book_13) 250)
        (= (total_pages Book_14) 300)
        (= (total_pages Book_15) 450)

        ;; Initial pages read per month
        (= (pages_read January) 0)
        (= (pages_read February) 0)
        (= (pages_read March) 0)
        (= (pages_read April) 0)
        (= (pages_read May) 0)
        (= (pages_read June) 0)
        (= (pages_read July) 0)
        (= (pages_read August) 0)
        (= (pages_read September) 0)
        (= (pages_read October) 0)
        (= (pages_read November) 0)
        (= (pages_read December) 0)
        

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