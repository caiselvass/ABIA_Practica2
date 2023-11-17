(define (domain reading-plan)
    (:requirements :strips :typing :equality :fluents :conditional-effects)

    ;; Tipos
    (:types
        book month - object
    )

    ;; Predicados
    (:predicates
        (read ?b - book)
        (predecessor ?b1 - book ?b2 - book)  ; ?b1 es predecesor de ?b2
        (parallel ?b1 - book ?b2 - book)     ; ?b1 y ?b2 son paralelos
        (assigned ?b - book ?m - month)      ; Libro asignado a un mes
        (month_finished ?m - month)          ; Indica si un mes ya ha sido completado
    )

    ;; Funciones
    (:functions
        (pages_read ?m - month)          ; Páginas leídas en un mes
        (total_pages ?b - book)          ; Páginas totales de un libro
    )

    ;; Acciones
    (:action assign_book
        :parameters (?b - book ?m - month)
        :precondition (and
            (not (read ?b))
            (not (assigned ?b ?m))
            (forall (?pre - book) (imply (predecessor ?pre ?b) (read ?pre)))
            (forall (?par - book) (imply (parallel ?b ?par) (assigned ?par ?m)))
            (<= (+ (pages_read ?m) (total_pages ?b)) 800)
        )
        :effect (and
            (assigned ?b ?m)
            (increase (pages_read ?m) (total_pages ?b))
            (when (>= (+ (pages_read ?m) (total_pages ?b)) 800)
                (month_finished ?m))
        )
    )

    (:action finish_reading
        :parameters (?b - book ?m - month)
        :precondition (assigned ?b ?m)
        :effect (read ?b)
    )

    (:action finish_month
        :parameters (?m - month)
        :precondition (not (month_finished ?m))
        :effect (month_finished ?m)
    )
)
