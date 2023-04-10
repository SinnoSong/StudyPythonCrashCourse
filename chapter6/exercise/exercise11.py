cities = {"beijing": {
    "country": "china",
    "population": 3000_0000,
    "fact": "old city"
},
    "zhengzhou": {
    "country": "china",
    "population": 1000_0000,
    "fact": "old city"
},
    "chengdu": {
    "country": "china",
    "population": 2000_0000,
    "fact": "old city"
}
}
for key in cities:
    print(f"{key} : {cities[key]}")
