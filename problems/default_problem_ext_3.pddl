(define (problem reading_plan_problem)
    (:domain reading_plan)
    ;; Objects
    (:objects
        book1 book2 book3 book4 book5 book6 book7 book8 book9 book10 book11 book12 book13 book14 book15 book16 book17 book18 book19 book20 book21 book22 book23 book24 book25 - book
        Past January February March April May June July August September October November December - month
    )

        ;; Initial State
        (:init
            ;; Order the months
            (next_month January February) (next_month February March) (next_month March April)
            (next_month April May) (next_month May June) (next_month June July)
            (next_month July August) (next_month August September) (next_month September October)
            (next_month October November) (next_month November December)

            ;; Predecessors and parallel books
            (predecessor book1 book2)
            (predecessor book2 book3)
            (predecessor book3 book4)
            (predecessor book4 book5)
            (predecessor book5 book6)
            (predecessor book6 book7)
            (parallel book10 book9)
            (parallel book10 book11)
            (parallel book10 book12)
            (parallel book25 book16)
            (parallel book25 book17)
            (parallel book25 book18)
            (predecessor book21 book22)
            (predecessor book22 book23)
            (predecessor book23 book24)

            ;; Books the user would like to read
            (goal_book book7)
            (goal_book book8)
            (goal_book book10)
            (goal_book book15)
            (goal_book book24)
            (goal_book book16)
            (goal_book book17)
            (goal_book book18)
            (goal_book book19)
            (goal_book book20)
            (goal_book book25)


            ;; Read books
            (assigned book1 Past)
            (read book1)
            (goal_book book1)

            ;; Pages of each book
            (= (total_pages book1) 700)
            (= (total_pages book2) 350)
            (= (total_pages book3) 200)
            (= (total_pages book4) 150)
            (= (total_pages book5) 100)
            (= (total_pages book6) 180)
            (= (total_pages book7) 220)
            (= (total_pages book8) 320)
            (= (total_pages book9) 410)
            (= (total_pages book10) 275)
            (= (total_pages book11) 300)
            (= (total_pages book12) 250)
            (= (total_pages book13) 200)
            (= (total_pages book14) 150)
            (= (total_pages book15) 100)
            (= (total_pages book16) 400)
            (= (total_pages book17) 350)
            (= (total_pages book18) 300)
            (= (total_pages book19) 250)
            (= (total_pages book20) 450)
            (= (total_pages book21) 400)
            (= (total_pages book22) 350)
            (= (total_pages book23) 300)
            (= (total_pages book24) 250)
            (= (total_pages book25) 450)

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