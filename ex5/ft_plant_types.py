class Plant:
    def __init__(self, name: str, height: float,
                 days: int, growth_rate: float) -> None:
        self.name: str = name.capitalize()
        self._height: float = height if height >= 0 else 0
        self._days: int = days if days >= 0 else 0
        self.growth_rate: float = growth_rate if growth_rate > 0 else 0.01

        if (height < 0):
            print("\033[31mInvalid negative height !"
                  "\nHeight set to default value\33[0m")
        if (days < 0):
            print("\33[31mInvalid negative age !"
                  "\nAge set to default value\033[0m")

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._days} days old")

    def grow(self) -> None:
        self._height = round(self._height + self.growth_rate, 2)

    def age(self) -> None:
        self._days += 1
        self.grow()

    def set_height(self, value: float) -> None:
        if (value < 0):
            print(f"\033[31m{self.name}: Error, height can’t be negative")
            return (print("Height update rejected\n\33[0m"))
        self._height = value
        print(f"Height updated: {value}cm")

    def set_age(self, value: int) -> None:
        if (value < 0):
            print(f"\033[31m{self.name}: Error, age can’t be negative")
            return (print("Age update rejected\n\033[0m"))
        self._days = value
        print(f"Age updated: {value} days")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._days)


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 days: int, growth_rate: float, color: str) -> None:
        self._color: str = color
        self._hasBloomed: bool = False
        super().__init__(name, height, days, growth_rate)

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if (self._hasBloomed):
            print("Rose is blooming beautifully!")
        else:
            print("Rose has not bloomed yet")

    def bloom(self) -> None:
        self._hasBloomed = not self._hasBloomed


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 days: int, growth_rate: float,
                 trunk_diameter: float) -> None:
        self._trunk_diameter: float = trunk_diameter
        super().__init__(name, height, days, growth_rate)

    def produce_shade(self) -> None:
        print(f"Tree Oak now produces a shade of {self._height}cm long"
              f" and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 days: int, growth_rate: float,
                 harvest_season: str) -> None:
        self.harvest_season: str = harvest_season.capitalize()
        self._nutritional_value: int = 0
        super().__init__(name, height, days, growth_rate)

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


rose: Flower = Flower("rose", 15, 10, 0.8, "red")
oak: Tree = Tree("oak", 200.0, 365, 1.82, 5.0)
tomato: Vegetable = Vegetable("tomato", 5.0, 10, 2.1, "april")

# ================  OUTPUT  ===================
print("=== Garden Plant Types ===")
print("=== Flower")
rose.show()
print("[asking the rose to bloom]")
rose.bloom()
rose.show()

print("\n=== Tree")
oak.show()
print("[asking the oak to produce shade]")
oak.produce_shade()
print("\n=== Vegetable")
tomato.show()
print("[make tomato grow and age for 20 days]")
for i in range(20):
    tomato.age()
tomato.show()
