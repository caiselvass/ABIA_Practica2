(define (domain reading_plan)
    ;; Types
    (:types
        book month - object
    )

    ;; Predicates
    (:predicates
        (read ?b - book)
        (predecessor ?b1 - book ?b2 - book)
        (goal_book ?b - book) ; New predicate for goal books
        (assigned ?b - book ?m - month)
        (current_month ?m - month)
        (next_month ?m1 - month ?m2 - month)
        (previous_month ?m - month)
    )

    ;; Actions
    (:action assign_book
        :parameters (?b - book ?actualm - month ?prevm - month)
        :precondition (and
            (not (read ?b))
            (or (goal_book ?b) (exists (?x - book) (predecessor ?b ?x)))
            (current_month ?actualm)
            (previous_month ?prevm)
            ;; The predecessors must have been read before the book's month
            (or (not (exists (?pre - book) (predecessor ?pre ?b))) 
                (and (exists (?pre - book) (predecessor ?pre ?b)) (read ?pre) (not (assigned ?pre ?actualm))))
        )
        :effect (and
            (read ?b)
            (assigned ?b ?actualm)
        )
    )



    (:action start_month
        :parameters (?nextm - month ?actualm - month ?prevm - month)
        :precondition (and 
            (current_month ?actualm)
            (previous_month ?prevm)
            (next_month ?actualm ?nextm)
        )
        :effect (and
            (not (current_month ?actualm))
            (current_month ?nextm)
            (previous_month ?actualm)
            (not (previous_month ?prevm))
        )
    )
)
