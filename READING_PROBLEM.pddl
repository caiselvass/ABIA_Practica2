(define (problem reading_plan_problem) (:domain reading_plan)
    ;; Objects
    (:objects
        book1 book2 book3 book4 book5 book6 book7 book8 book9 book10 - book
        month0 month1 month2 month3 month4 month5 month6 month7 month8 month9 month10 month11 month12 - month
    )

    ;; Initial State
    (:init
        ;; Order the months
        (next_month month1 month2) (next_month month2 month3) (next_month month3 month4)
        (next_month month4 month5) (next_month month5 month6) (next_month month6 month7)
        (next_month month7 month8) (next_month month8 month9) (next_month month9 month10)
        (next_month month10 month11) (next_month month11 month12)

        ;; Precedessors and parallel books
        (predecessor book1 book2)
        (predecessor book2 book3)
        (predecessor book3 book4)
        (predecessor book4 book5)
        (predecessor book5 book6)
        (predecessor book6 book7)

        ;; Read books
        (assigned book4 month0)
        (read book4)


        ;; Pages of each book
        (= (total_pages book1) 700)
        (= (total_pages book2) 550)
        (= (total_pages book3) 200)
        (= (total_pages book4) 150)
        (= (total_pages book5) 100)
        (= (total_pages book6) 180)
        (= (total_pages book7) 220)

        ;; Initial pages read per month
        (= (pages_read month1) 0)
        (= (pages_read month2) 0)
        (= (pages_read month3) 0)
        (= (pages_read month4) 0)
        (= (pages_read month5) 0)
        (= (pages_read month6) 0)
        (= (pages_read month7) 0)
        (= (pages_read month8) 0)
        (= (pages_read month9) 0)
        (= (pages_read month10) 0)
        (= (pages_read month11) 0)
        (= (pages_read month12) 0)
        
        ;; Initial Number of months
        (= (num_months_created) 1)

        ;; Start on month 1
        (actual_month month1)

        ;; Give an initial previous month (just for simplifying the code)
        (previous_month month0)
    )

    ;; Goal
    (:goal
        (and
            ;; Books that the user would like to read
            (read book7)
        )
    )

    ;; Optimize the number of months
    (:metric minimize (num_months_created))
)
