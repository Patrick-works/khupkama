import random
code,val=["diamond","spade","clubs","heart"],[]
for i in range(11):
    val.append(str(i))
val.append("Jack")
val.append("Queen")
val.append("King")
val.append("Ace")
cards,card=[],[]
for i in code:
    for j in val:
        card=[i+"-"+j]
        cards.append(card)
        card=[]
random.shuffle(cards)
print(cards)

