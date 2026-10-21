import pytholog as pl

kb = pl.KnowledgeBase("kb")

kb([
    "american(west)",
    "missile(m1)",
    "owns(nono, m1)",
    "enemy(nono, america)",
    "weapon(X) :- missile(X)",
    "hostile(X) :- enemy(X, america)",
    "criminal(X) :- american(X), weapon(Y), sells(X,Y,Z), hostile(Z)",
    "sells(west, m1, nono)"
])

print("The knowledge base is implemented")

print("Is West a Criminal?")

print(kb.query(pl.Expr("criminal(west)")))
