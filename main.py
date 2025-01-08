ismlar = [
    {
        "Ism": "Sherbek",
        "Yosh": 18
    },
    {
        "Ism": "Aziz",
        "Yosh": 38
    },
    {
        "Ism": "Asror",
        "Yosh": 19
    },
]

# Bizga eng yoshi kattasi kimligini aniqlab beradi 
oldest = ismlar[0]
for ism in ismlar[1:]:
    if oldest['Yosh'] < ism['Yosh']:
        oldest = ism

# Natijani chiqaramiz 

print(f"Eng yoshi kattasi: {oldest['Ism']}, yoshi: {oldest['Yosh']}")