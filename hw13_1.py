class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def add(self, other_country):
        combined_name = f'{self.name} {other_country.name}'
        combined_population = self.population + other_country.population
        return Country(combined_name, combined_population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)


print(f'Combined_name: {bosnia_herzegovina.name}')
print(f'Combined population: {bosnia_herzegovina.population}')
