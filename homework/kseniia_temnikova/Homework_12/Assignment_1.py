from abc import abstractmethod


class Flower:

    def __init__(self, price, freshness, color, flower_life_expectancy):
        self.price = price
        self.freshness = freshness
        self.color = color
        self.flower_life_expectancy = flower_life_expectancy

    @abstractmethod
    def get_flower_name(self):
        pass

    def __repr__(self):
        return f' Name: {self.get_flower_name()}, price: {self.price}, ' \
               f' freshness level: {self.freshness}, color: {self.color}, ' \
               f' flower_life_expectancy {self.flower_life_expectancy} days.\n'


class Poppy(Flower):
    def __init__(self, price, freshness, color, flower_life_expectancy):
        super().__init__(price, freshness, color, flower_life_expectancy)

    def get_flower_name(self):
        return 'Poppy'


class Daisy(Flower):
    def __init__(self, price, freshness, color, flower_life_expectancy):
        super().__init__(price, freshness, color, flower_life_expectancy)

    def get_flower_name(self):
        return 'Daisy'


class Lavender(Flower):
    def __init__(self, price, freshness, color, flower_life_expectancy):
        super().__init__(price, freshness, color, flower_life_expectancy)

    def get_flower_name(self):
        return 'Lavender'


first_poppy = Poppy(20, 1, 'red', 7)
first_daisy = Daisy(8, 2, 'yellow', 3)
first_lavender = Lavender(33, 1, 'violet', 14)


class Bouquet:
    list_of_flowers = []

    def add_flower(self, flower: Flower):
        self.list_of_flowers.append(flower)
        return self.list_of_flowers

    def total_sum(self):
        prices = [flower.price for flower in self.list_of_flowers]
        return sum(prices)

    def avg_life_expectancy(self):
        total_life = sum([flower.flower_life_expectancy for flower in self.list_of_flowers])
        avg_life = total_life / len(self.list_of_flowers)
        return avg_life

    def sort_by_price(self):
        return sorted(self.list_of_flowers, key=lambda f: f.price)

    def sort_by_color(self):
        return sorted(self.list_of_flowers, key=lambda f: f.color)

    def search_by_price_more_than(self, number):
        return [flower for flower in self.list_of_flowers if flower.price > number]


new_bouquet = Bouquet()
new_bouquet.add_flower(first_daisy)
new_bouquet.add_flower(first_poppy)
new_bouquet.add_flower(first_lavender)
print(new_bouquet.list_of_flowers)
print(new_bouquet.total_sum())
print(new_bouquet.avg_life_expectancy())
print(new_bouquet.sort_by_price())
print(new_bouquet.sort_by_color())
print(new_bouquet.search_by_price_more_than(10))
