class Plant:
    def __init__(self, name: str, height: float,
                 days: int, growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = growth_rate

    def show(self) -> None:
        capname: str = self.name.capitalize()
        print(f"{capname}: {self.height}cm, {self.days} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 2)

    def age(self) -> None:
        self.days += 1
        self.grow()


rose: Plant = Plant("rose", 25, 30, 0.8)
oak: Plant = Plant("oak", 200, 365, 0.54)
cactus: Plant = Plant("cactus", 5, 90, 0.05)
sunflower: Plant = Plant("sunflower", 80, 45, 1.77)
fern: Plant = Plant("fern", 15, 120, 0.12)

print("=== Plant Factory Output ===")
print("Created: ", end="")
rose.show()
print("Created: ", end="")
oak.show()
print("Created: ", end="")
cactus.show()
print("Created: ", end="")
sunflower.show()
print("Created: ", end="")
fern.show()
