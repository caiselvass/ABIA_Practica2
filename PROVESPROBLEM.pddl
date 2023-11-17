(define (problem reading-plan-problem) (:domain reading-plan)
    ;; Objetos
    (:objects
        book1 book2 book3 book4 book5 book6 book7 - book
        mes1 mes2 mes3 mes4 - month
    )

    ;; Estado inicial
    (:init
        ;; Predecesores
        (predecessor book1 book2)  ; book1 debe leerse antes de book2
        (predecessor book2 book3)  ; book2 debe leerse antes de book3

        ;; Libros Paralelos
        (parallel book4 book5)     ; book4 y book5 son paralelos
        (parallel book5 book4)

        ;; Páginas por libro
        (= (total_pages book1) 300)
        (= (total_pages book2) 250)
        (= (total_pages book3) 200)
        (= (total_pages book4) 150)
        (= (total_pages book5) 100)
        (= (total_pages book6) 180)
        (= (total_pages book7) 220)

        ;; Páginas leídas inicialmente en cada mes
        (= (pages_read mes1) 0)
        (= (pages_read mes2) 0)
        (= (pages_read mes3) 0)
        (= (pages_read mes4) 0)
    )

    ;; Objetivo
    (:goal
        (and
            (read book1)
            (read book2)
            (read book3)
            (read book4)
            (read book5)
            (read book6)
            (read book7)
        )
    )
)
