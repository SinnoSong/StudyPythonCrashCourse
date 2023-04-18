def format_city(city_name: str, country_name: str):
    return f"{city_name.title()}, {country_name.title()}"


def format_city(city_name: str, country_name: str, population: int = 0):
    if population == 0:
        return f"{city_name.title()}, {country_name.title()}"
    else:
        return f"{city_name.title()}, {country_name.title()} - population {population}"
