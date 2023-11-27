(define (problem reading_plan_problem)
    (:domain reading_plan)
    ;; Objects
    (:objects
        book1 book2 book3 book4 book5 book6 book7 book8 book9 book10 book11 book12 book13 book14 book15 - book
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
        (predecessor book4 book5)
        (predecessor book6 book7)
        (predecessor book10 book11)


        ;; Books the user would like to read
        (goal_book book5)
        (goal_book book6)
        (goal_book book11)



        ;; Read books
        (assigned book1 Past)
        (read book1)
        (goal_book book1)

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
)
