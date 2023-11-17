(define (problem reading-plan-problem) (:domain reading-plan)
    ;; Objetos
    (:objects
        book1 book2 book3 book4 book5 - book
    )

    ;; Estado inicial
    (:init
        ;; Predecesores
        (predecessor book1 book2)  ; Se debe leer book1 antes de book2
        (predecessor book2 book3)  ; Se debe leer book2 antes de book3
        ;; No hay predecesores para book4 y book5

        ;; Páginas por libro
        (= (total_pages book1) 300)  ; Book1 tiene 300 páginas
        (= (total_pages book2) 250)  ; Book2 tiene 250 páginas
        (= (total_pages book3) 200)  ; Book3 tiene 200 páginas
        (= (total_pages book4) 150)  ; Book4 tiene 150 páginas
        (= (total_pages book5) 100)  ; Book5 tiene 100 páginas

        ;; Límite de páginas por mes (ejemplo: 500 páginas)
        (= (pages_read) 0)
        ;; Suponiendo que el límite mensual es 500 páginas
    )

    ;; Objetivo
    (:goal
        (and
            (read book1)
            (read book2)
            (read book3)
            (read book4)
            (read book5)
        )
    )
)
