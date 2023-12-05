(define (problem reading_plan_problem_ext_2_5)
	(:domain reading_plan)
	;;Objects
	(:objects
		Past January February March April May June July August September October November December - month
		January_1 February_1 March_1 April_1 May_1 June_1 July_1 August_1 September_1 October_1 November_1 December_1 - month
		January_2 February_2 March_2 April_2 May_2 June_2 July_2 August_2 September_2 October_2 November_2 December_2 - month
		January_3 February_3 March_3 April_3 May_3 June_3 July_3 August_3 September_3 October_3 November_3 December_3 - month
		January_4 February_4 March_4 April_4 May_4 June_4 July_4 August_4 September_4 October_4 November_4 December_4 - month
		January_5 February_5 March_5 April_5 May_5 June_5 July_5 August_5 September_5 October_5 November_5 December_5 - month
		January_6 February_6 March_6 April_6 May_6 June_6 July_6 August_6 September_6 October_6 November_6 December_6 - month
		January_7 February_7 March_7 April_7 May_7 June_7 - month

		Book_1 Book_2 Book_3 Book_4 Book_5 Book_6 Book_7 Book_8 Book_9 Book_10 Book_11 Book_12 Book_13 Book_14 Book_15 - book
		Book_16 Book_17 Book_18 Book_19 Book_20 Book_21 Book_22 Book_23 Book_24 Book_25 Book_26 Book_27 Book_28 Book_29 Book_30 - book
		Book_31 Book_32 Book_33 Book_34 Book_35 Book_36 Book_37 Book_38 Book_39 Book_40 Book_41 Book_42 Book_43 Book_44 Book_45 - book
		Book_46 Book_47 Book_48 Book_49 Book_50 Book_51 Book_52 Book_53 Book_54 Book_55 Book_56 Book_57 Book_58 Book_59 Book_60 - book
		Book_61 Book_62 Book_63 Book_64 Book_65 Book_66 Book_67 Book_68 Book_69 Book_70 Book_71 Book_72 Book_73 Book_74 Book_75 - book
		Book_76 Book_77 Book_78 Book_79 Book_80 Book_81 Book_82 Book_83 Book_84 Book_85 Book_86 Book_87 Book_88 Book_89 Book_90 - book

	)
	;;Init
	(:init
		;;Order the months
		(next_month January February) (next_month February March) (next_month March April)
		(next_month April May) (next_month May June) (next_month June July)
		(next_month July August) (next_month August September) (next_month September October)
		(next_month October November) (next_month November December) (next_month December January_1)
		(next_month January_1 February_1) (next_month February_1 March_1) (next_month March_1 April_1)
		(next_month April_1 May_1) (next_month May_1 June_1) (next_month June_1 July_1)
		(next_month July_1 August_1) (next_month August_1 September_1) (next_month September_1 October_1)
		(next_month October_1 November_1) (next_month November_1 December_1) (next_month December_1 January_2)
		(next_month January_2 February_2) (next_month February_2 March_2) (next_month March_2 April_2)
		(next_month April_2 May_2) (next_month May_2 June_2) (next_month June_2 July_2)
		(next_month July_2 August_2) (next_month August_2 September_2) (next_month September_2 October_2)
		(next_month October_2 November_2) (next_month November_2 December_2) (next_month December_2 January_3)
		(next_month January_3 February_3) (next_month February_3 March_3) (next_month March_3 April_3)
		(next_month April_3 May_3) (next_month May_3 June_3) (next_month June_3 July_3)
		(next_month July_3 August_3) (next_month August_3 September_3) (next_month September_3 October_3)
		(next_month October_3 November_3) (next_month November_3 December_3) (next_month December_3 January_4)
		(next_month January_4 February_4) (next_month February_4 March_4) (next_month March_4 April_4)
		(next_month April_4 May_4) (next_month May_4 June_4) (next_month June_4 July_4)
		(next_month July_4 August_4) (next_month August_4 September_4) (next_month September_4 October_4)
		(next_month October_4 November_4) (next_month November_4 December_4) (next_month December_4 January_5)
		(next_month January_5 February_5) (next_month February_5 March_5) (next_month March_5 April_5)
		(next_month April_5 May_5) (next_month May_5 June_5) (next_month June_5 July_5)
		(next_month July_5 August_5) (next_month August_5 September_5) (next_month September_5 October_5)
		(next_month October_5 November_5) (next_month November_5 December_5) (next_month December_5 January_6)
		(next_month January_6 February_6) (next_month February_6 March_6) (next_month March_6 April_6)
		(next_month April_6 May_6) (next_month May_6 June_6) (next_month June_6 July_6)
		(next_month July_6 August_6) (next_month August_6 September_6) (next_month September_6 October_6)
		(next_month October_6 November_6) (next_month November_6 December_6) (next_month December_6 January_7)
		(next_month January_7 February_7) (next_month February_7 March_7) (next_month March_7 April_7)
		(next_month April_7 May_7) (next_month May_7 June_7)

		;;Start on month 1
		(current_month January)
		(previous_month Past)
		;;Predecessors
		
		(predecessor Book_1 Book_2) (predecessor Book_2 Book_3) (predecessor Book_3 Book_4) (predecessor Book_4 Book_5)
		(predecessor Book_5 Book_6) (predecessor Book_6 Book_7) (predecessor Book_7 Book_8) (predecessor Book_8 Book_9)
		(predecessor Book_9 Book_10) (predecessor Book_10 Book_11) (predecessor Book_11 Book_12) (predecessor Book_12 Book_13)
		(predecessor Book_13 Book_14) (predecessor Book_14 Book_15) (predecessor Book_15 Book_16) (predecessor Book_16 Book_17)
		(predecessor Book_17 Book_18) (predecessor Book_18 Book_19) (predecessor Book_19 Book_20) (predecessor Book_20 Book_21)
		(predecessor Book_21 Book_22) (predecessor Book_22 Book_23) (predecessor Book_23 Book_24) (predecessor Book_24 Book_25)
		(predecessor Book_25 Book_26) (predecessor Book_26 Book_27) (predecessor Book_27 Book_28) (predecessor Book_28 Book_29)
		(predecessor Book_29 Book_30) (predecessor Book_30 Book_31) (predecessor Book_31 Book_32) (predecessor Book_32 Book_33)
		(predecessor Book_33 Book_34) (predecessor Book_34 Book_35) (predecessor Book_35 Book_36) (predecessor Book_36 Book_37)
		(predecessor Book_37 Book_38) (predecessor Book_38 Book_39) (predecessor Book_39 Book_40) (predecessor Book_40 Book_41)
		(predecessor Book_41 Book_42) (predecessor Book_42 Book_43) (predecessor Book_43 Book_44) (predecessor Book_44 Book_45)
		(predecessor Book_45 Book_46) (predecessor Book_46 Book_47) (predecessor Book_47 Book_48) (predecessor Book_48 Book_49)
		(predecessor Book_49 Book_50) (predecessor Book_50 Book_51) (predecessor Book_51 Book_52) (predecessor Book_52 Book_53)
		(predecessor Book_53 Book_54) (predecessor Book_54 Book_55) (predecessor Book_55 Book_56) (predecessor Book_56 Book_57)
		(predecessor Book_57 Book_58) (predecessor Book_58 Book_59) (predecessor Book_59 Book_60) (predecessor Book_60 Book_61)
		(predecessor Book_61 Book_62) (predecessor Book_62 Book_63) (predecessor Book_63 Book_64) (predecessor Book_64 Book_65)
		(predecessor Book_65 Book_66) (predecessor Book_66 Book_67) (predecessor Book_67 Book_68) (predecessor Book_68 Book_69)
		(predecessor Book_69 Book_70) (predecessor Book_70 Book_71) (predecessor Book_71 Book_72) (predecessor Book_72 Book_73)
		(predecessor Book_73 Book_74) (predecessor Book_74 Book_75) (predecessor Book_75 Book_76) (predecessor Book_76 Book_77)
		(predecessor Book_77 Book_78) (predecessor Book_78 Book_79) (predecessor Book_79 Book_80) (predecessor Book_80 Book_81)
		(predecessor Book_81 Book_82) (predecessor Book_82 Book_83) (predecessor Book_83 Book_84) (predecessor Book_84 Book_85)
		(predecessor Book_85 Book_86) (predecessor Book_86 Book_87) (predecessor Book_87 Book_88) (predecessor Book_88 Book_89)
		(predecessor Book_89 Book_90) 


		;;Books the user would like to read
		(goal_book Book_90)
	)
	;;Goal
	(:goal
		(and
			(forall (?b - book) (imply (goal_book ?b) (read ?b)))
		)
	)
	;;Optimize the number of months
	(:metric minimize (num_months_created))
)
