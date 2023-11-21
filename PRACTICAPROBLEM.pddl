(define (problem reading_plan_problem)
    (:domain reading_plan)
    ;; Objects
    (:objects
        book1 book2 book3 book4 book5 book6 book7 book8 book9 book10 book11 book12 book13 book14 book15 - book
        month0 month1 month2 month3 month4 month5 month6 month7 month8 month9 month10 month11 month12 - month
    )

    ;; Initial State
    (:init
        ;; Order the months
        (next_month month1 month2) (next_month month2 month3) (next_month month3 month4)
        (next_month month4 month5) (next_month month5 month6) (next_month month6 month7)
        (next_month month7 month8) (next_month month8 month9) (next_month month9 month10)
        (next_month month10 month11) (next_month month11 month12)

        ;; Predecessors and parallel books
        (predecessor book1 book2)
        (predecessor book2 book3)
        (predecessor book3 book4)
        (parallel book5 book1)
        (parallel book5 book6)
        (parallel book5 book8)

        ;; Books the user would like to read
        (goal_book book5)
        (goal_book book6)
        (goal_book book8)



        ;; Read books
        (assigned book1 month0)
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
            ;; Imply goal_read -> read for each book
            (forall (?b - book) (imply (goal_book ?b) (read ?b)))
        )
    )

    ;; Optimize the number of months
    (:metric minimize (num_months_created))
)
