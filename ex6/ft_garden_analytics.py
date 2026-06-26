from typing import Self


class Plant:
    class Stats():
        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0

        def set_grow_count(self) -> None:
            self._grow_count += 1

        def set_age_count(self) -> None:
            self._age_count += 1

        def set_show_count(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, {self._show_count} show")

    def __init__(self, name: str, height: float,
                 days: int, growth_rate: float) -> None:
        self.name: str = name.capitalize()
        self._height: float = height if height >= 0 else 0
        self._days: int = days if days >= 0 else 0
        self.growth_rate: float = growth_rate if growth_rate > 0 else 0.01
        self.stats: Plant.Stats = Plant.Stats()

        if (height < 0):
            print("\033[31mInvalid negative height !"
                  "\nHeight set to default value\33[0m")
        if (days < 0):
            print("\33[31mInvalid negative age !"
                  "\nAge set to default value\033[0m")

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._days} days old")
        self.stats._show_count += 1

    def grow(self) -> None:
        for i in range(10):
            self._height = round(self._height + self.growth_rate, 2)
        self.stats._grow_count += 1

    def age(self) -> None:
        for i in range(20):
            self._days += 1
        self.stats._age_count += 1

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

    @staticmethod
    def check_age(days: int) -> None:
        if (days > 365):
            print(f"Is {days} days more than a year? -> True")
        else:
            print(f"Is {days} days more than a year? -> False")

    @classmethod
    def anonymous(cls) -> Self:
        return (cls("Unknown plant", 0.0, 0, 0))


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
        self._hasBloomed = True


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count: int = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

    def __init__(self, name: str, height: float,
                 days: int, growth_rate: float,
                 trunk_diameter: float) -> None:
        self._trunk_diameter: float = trunk_diameter
        super().__init__(name, height, days, growth_rate)
        self.stats: Tree.TreeStats = Tree.TreeStats()

    def produce_shade(self) -> None:
        print(f"Tree Oak now produces a shade of {self._height}cm long"
              f" and {self._trunk_diameter}cm wide.")
        self.stats._shade_count += 1

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


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 days: int, growth_rate: float, color: str) -> None:
        super().__init__(name, height, days, growth_rate, color)
        self.seeds_count = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds_count}")

    def bloom(self) -> None:
        super().bloom()
        self.seeds_count = 42


rose: Flower = Flower("rose", 15.0, 10, 0.8, "red")
sunflower: Seed = Seed("sunflower", 80.0, 45, 3.0, "yellow")
oak: Tree = Tree("oak", 200.0, 365, 0.54, 5.0)
anonymous: Plant = Plant.anonymous()

# ==========OUTPUT==========
print("=== Garden statistics ===")
print("=== Check year-old")
Plant.check_age(30)
Plant.check_age(400)
print("\n=== Flower")
rose.show()
print("[statistics for Rose]")
rose.stats.display()
print("[asking the rose to grow and bloom]")
rose.grow()
rose.bloom()
rose.show()
print("[statistics for Rose]")
rose.stats.display()
print("[statistics for Rose]")
rose.stats.display()
print("\n=== Tree")
oak.show()
print("[statistics for Oak]")
oak.stats.display()
print("[asking the oak to produce shade]")
oak.produce_shade()
print("[statistics for Oak]")
oak.stats.display()
print("\n=== Seed")
sunflower.show()
print("[make sunflower grow, age and bloom]")
sunflower.grow()
sunflower.age()
sunflower.bloom()
sunflower.show()
print("[statistics for Sunflower]")
sunflower.stats.display()
print("\n=== Anonymous")
anonymous.show()
print("[statistics for Unknown plant]")
anonymous.stats.display()
