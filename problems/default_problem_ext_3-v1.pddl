(define (problem reading_plan_problem)
    (:domain reading_plan)
    ;; Objects
    (:objects
		Past January February March April May June July August September October November December - month
		Book_1 Book_2 Book_3 Book_4 Book_5 Book_6 Book_7 Book_8 Book_9 Book_10 Book_11 Book_12 Book_13 Book_14 Book_15 - book
	)

        ;; Initial State
        (:init
            ;; Order the months
            (next_month January February) (next_month February March) (next_month March April)
            (next_month April May) (next_month May June) (next_month June July)
            (next_month July August) (next_month August September) (next_month September October)
            (next_month October November) (next_month November December)

           

            ;; Books the user would like to read
            (goal_book Book_1)
            (goal_book Book_2)
            (goal_book Book_3)
            (goal_book Book_4)
            (goal_book Book_5)
            (goal_book Book_6)
            (goal_book Book_7)
            (goal_book Book_8)
            (goal_book Book_9)
            (goal_book Book_10)
            (goal_book Book_11)
            (goal_book Book_12)
            (goal_book Book_13)
            (goal_book Book_14)
		    (goal_book Book_15)

            ;; Pages of each book
            (= (total_pages Book_1) 100)
            (= (total_pages Book_2) 100)
            (= (total_pages Book_3) 100)
            (= (total_pages Book_4) 100)
            (= (total_pages Book_5) 100)
            (= (total_pages Book_6) 100)
            (= (total_pages Book_7) 100)
            (= (total_pages Book_8) 100)
            (= (total_pages Book_9) 200)
            (= (total_pages Book_10) 200)
            (= (total_pages Book_11) 200)
            (= (total_pages Book_12) 200)
            (= (total_pages Book_13) 400)
            (= (total_pages Book_14) 400)
            (= (total_pages Book_15) 500)

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
            
            ;; Initial Number of months
            (= (num_months_created) 1)

            ;; Start on month 1
            (current_month January)

            ;; Give an initial previous month (just for simplifying the code)
            (previous_month Past)
        )

        ;; Goal
        (:goal
            (and
                ;; Imply goal_read -> read for each book
                (forall (?b - book) (imply (goal_book ?b) (read ?b)))
            )
        )

        ;; Optimize the number of months
        (:metric minimize (num_months_created))
    )
