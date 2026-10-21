import pytholog as pl

kb = pl.KnowledgeBase("kb")

kb([
    "american(west)",
    "missile(m1)",
    "owns(nono,m1)",
    "enemy(nono,america)",
    "weapon(X) :- missile(X)",
    "hostile(X) :- enemy(X,america)",
    "criminal(X) :- american(X), weapon(Y), sells(X,Y,Z), hostile(Z)",
    "sells(west,m1,nono)"
])

print("The knowledge base is implemented")

result = kb.query(pl.Expr("criminal(west)"))

if result[0] == "Yes":
    print("YES - West is a Criminal")
else:
    print("NO - West is not a Criminal")
