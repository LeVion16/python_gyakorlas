cat = {
    "name": "lajos",
    "age": 3,
}

user_input = input("Melyik adatot szeretnéd megváltoztatni? A macska nevét vagy életkorát? (NÉV / ÉLETKOR): ")
if user_input.lower() == "név":
    new_name = input("Mi legyen az új neve: ")
    cat.values("name", new_name)

print(cat)
