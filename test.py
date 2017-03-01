import random

rng = random.randint(1, 10)
a1 = (''.join([random.choice(list('QWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(rng)]))
a2 = (''.join([random.choice(list('123456789')) for x in range(rng)]))
a3 = (''.join([random.choice(list('#$%*)@!~+')) for x in range(random.randint(1, 15))]))
b = int(a2)+1
Sn1 = a1+a2
Sn2 = a1+str(b)
SnrBoard11 = "NoRead", " ", Sn1, a3
SnrBoard12 = "NoRead", " ", Sn2, a3

SnrBoard1 = random.choice(list(SnrBoard11))
SnrBoard2 = random.choice(list(SnrBoard12))
SnrBoard = SnrBoard1, SnrBoard2
print(SnrBoard)