family_1 = list(input())
family_2 = list(input())

if len(family_1) > len(family_2):
    print('First family bigger')
elif len(family_2) > len(family_1):
    print('Second family bigger')
else:
    print('Equal')