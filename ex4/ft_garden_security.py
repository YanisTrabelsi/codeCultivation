class Plant:
    def __init__(self, name: str, height: float,
                 days: int, growth_rate: float) -> None:
        self.name: str = name.capitalize()
        self._height: float = height if height >= 0 else 0
        self._days: int = days if days >= 0 else 0
        self.growth_rate: float = growth_rate if growth_rate > 0 else 0.01

        if(height < 0):
            print("Invalid negative height !\nHeight set to default value")
        if(days < 0):
            print("Invalid negative age !\nAge set to default value")
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._days} days old")

    def grow(self) -> None:
        self._height = round(self._height + self.growth_rate, 2)

    def age(self) -> None:
        self._days += 1
        self.grow()

    def set_height(self, value: float) -> None:
        if (value < 0):
            print(f"{self.name}: Error, height can’t be negative")
            return (print("Height update rejected\n"))
        self._height = value
        print(f"Height updated: {value}cm")

    def set_age(self, value: int) -> None:
        if (value < 0):
            print(f"{self.name}: Error, age can’t be negative")
            return (print("Age update rejected\n"))
        self._days = value
        print(f"Age updated: {value} days")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._days)


print("=== Garden Security System ===")
rose: Plant = Plant("rose", 25, 30, 0.8)
rose.set_age(-5)
print("Current state: ", end="")
rose.show()
