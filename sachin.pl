predict(batsmen,Type):-
	batsmen(Type),
	iscrick(Type).
predict(cricketer,Type):-
	iscrick(Type).
batsmen(sachin).
iscrick(sachin).
batsmen(virat).
iscrick(virat).
iscrick(rahul).


 predict(batsmen,sachin).
true.

4 ?- predict(batsmen,virat).
true.

5 ?- 