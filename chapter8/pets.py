def describe_pet(pet_name, animal_type="cat"):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("dabing", "cat")
describe_pet(animal_type="cat", pet_name="dabing")
describe_pet("dabing")
