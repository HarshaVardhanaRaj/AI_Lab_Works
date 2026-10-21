import pytholog as pl

# Knowledge Base
kb = {
    "american(west)",
    "missile(m1)",
    "owns(nono,m1)",
    "enemy(nono,america)",
    "sells(west,m1,nono)"
}

print("The knowledge base is implemented")

# Forward chaining
if "missile(m1)" in kb:
    kb.add("weapon(m1)")
    print("Derived: weapon(m1)")

if "enemy(nono,america)" in kb:
    kb.add("hostile(nono)")
    print("Derived: hostile(nono)")

if ("american(west)" in kb and
    "weapon(m1)" in kb and
    "sells(west,m1,nono)" in kb and
    "hostile(nono)" in kb):

    kb.add("criminal(west)")
    print("Derived: criminal(west)")


if "criminal(west)" in kb:
    print("\nYES - West is a Criminal")
else:
    print("\nNO - West is not a Criminal")
