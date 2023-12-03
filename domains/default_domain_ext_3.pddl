(define (domain reading_plan)
    (:requirements :typing :negative-preconditions :disjunctive-preconditions :existential-preconditions :universal-preconditions :fluents)

    ;; Types
    (:types
        book month - object
    )

    ;; Predicates
    (:predicates
        (read ?b - book)
        (predecessor ?b1 - book ?b2 - book)
        (parallel ?b1 - book ?b2 - book)
        (goal_book ?b - book) ; New predicate for goal books
        (assigned ?b - book ?m - month)
        (current_month ?m - month)
        (next_month ?m1 - month ?m2 - month)
        (previous_month ?m - month)
    )

    ;; Functions
    (:functions
        (pages_read ?m - month)
        (total_pages ?b - book)
        (num_months_created)
    )

    ;; Actions
    (:action assign_book
        :parameters (?b - book ?actualm - month ?prevm - month)
        :precondition (and
            (not (read ?b))
            (or (goal_book ?b) (exists (?x - book) (predecessor ?b ?x)) (exists (?y - book) (parallel ?y ?b)))
            (current_month ?actualm)
            (previous_month ?prevm)
            ;; The predecessors must have been read before the book's month
            (forall (?pre - book) (imply (predecessor ?pre ?b) (and (read ?pre) (not (assigned ?pre ?actualm)))))
            ;; The parallel books must be a goal to be read before the book's month or in the same month
            (forall (?par - book) (imply (and (parallel ?b ?par) (not (assigned ?par Past))) (or (assigned ?par ?actualm) (assigned ?par ?prevm))))

            (<= (+ (pages_read ?actualm) (total_pages ?b)) 800)
        )
        :effect (and
            (read ?b)
            (assigned ?b ?actualm)
            (increase (pages_read ?actualm) (total_pages ?b))
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
            (increase (num_months_created) 1) 
        )
    )
)
