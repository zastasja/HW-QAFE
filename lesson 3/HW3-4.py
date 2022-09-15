family_1 = input()
family_2 = input()

f1 = list(family_1.split(","))
f2 = list(family_2.split(","))

if len(f1) > len(f2):
    print('First family bigger')
elif len(f2) > len(f1):
    print('Second family bigger')
else:
    print('Equal')