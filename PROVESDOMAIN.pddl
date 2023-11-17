(define (domain reading-plan)
    (:requirements :strips :typing :equality :fluents)

    ;; Tipos
    (:types
        book
        month
    )

    ;; Predicados
    (:predicates
        (read ?b - book)
        (predecessor ?b1 - book ?b2 - book)  ; ?b1 es predecesor de ?b2
        (parallel ?b1 - book ?b2 - book)     ; ?b1 es paralelo de ?b2
    )

    ;; Funciones
    (:functions
        (pages_read)                 ; Total de páginas leídas en un mes
        (total_pages ?b - book)      ; Total de páginas de un libro
    )

    ;; Acciones
    (:action read_book
        :parameters (?b - book)
        :precondition (and
            (not (read ?b))
            (forall (?pre - book) (imply (predecessor ?pre ?b) (read ?pre)))
            (<= (+ (pages_read) (total_pages ?b)) 800)
        )
        :effect (and
            (read ?b)
            (increase (pages_read) (total_pages ?b))
            (when (= (+ (pages_read) (total_pages ?b)) 800)
                (assign (pages_read) 0)
            )
        )
    )
)
