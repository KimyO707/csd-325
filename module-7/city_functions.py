def city_country(city, country, population=None, language=None):
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result


print(city_country("santiago", "chile"))
print(city_country("tokyo", "japan", 70760619))
print(city_country("paris", "france", 3215486, "french"))