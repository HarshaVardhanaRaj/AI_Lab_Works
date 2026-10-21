from nltk.sem import Expression
from nltk.inference import ResolutionProver

read_expr = Expression.fromstring

kb = [
    read_expr("American(West)"),
    read_expr("Missile(M1)"),
    read_expr("Owns(Nono, M1)"),
    read_expr("Enemy(Nono, America)"),
    read_expr("all x (Missile(x) -> Weapon(x))"),
    read_expr("all x (Enemy(x, America) -> Hostile(x))"),
    read_expr("all x all y all z ((American(x) & Weapon(y) & Sells(x,y,z) & Hostile(z)) -> Criminal(x))"),
     read_expr("Sells(West, M1, Nono)")
]

goal = read_expr("-Criminal(West)")

print("Resolution Result: ", ResolutionProver().prove(goal, kb))
