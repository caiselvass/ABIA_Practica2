(define (domain reading_plan)
    (:requirements :strips :typing :equality :fluents :conditional-effects)

    ;; Types
    (:types
        book month - object
    )

    ;; Predicates
    (:predicates
        (read ?b - book)
        (predecessor ?b1 - book ?b2 - book)
        (parallel ?b1 - book ?b2 - book)
        (assigned ?b - book ?m - month)
        (month_finished ?m - month)
        (actual_month ?m - month)
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
            (not (assigned ?b ?actualm))
            (not (read ?b))
            (actual_month ?actualm)
            (previous_month ?prevm)
            ;; The predecessors must have been read before the book's month
            (forall (?pre - book) (imply (predecessor ?pre ?b) (and (read ?pre) (not (assigned ?pre ?actualm)))))
            ;; The parallel books must have been read before the book's month or in the same month
            (forall (?par - book) (imply (or (parallel ?b ?par) (parallel ?par ?b)) (or (assigned ?par ?actualm) (and (assigned ?par ?prevm) (read ?par)))))
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
            (actual_month ?actualm)
            (previous_month ?prevm)
            (next_month ?actualm ?nextm)
            ;; Change the actual month only if the previous month is finished
            (forall (?b - book) (imply (assigned ?b ?actualm) (read ?b)))
        )
        :effect (and
            (month_finished ?actualm)
            (not (actual_month ?actualm))
            (actual_month ?nextm)
            (previous_month ?actualm)
            (not (previous_month ?prevm))
            (increase (num_months_created) 1) 
        )
    )

)
