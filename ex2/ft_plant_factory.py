class Plant:
    def __init__(self, name: str, height: float,
                 days: int, growth_rate: float):
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = growth_rate

    def show(self):
        capname: str = self.name.capitalize()
        print(f"{capname}: {self.height}cm, {self.days} days old")

    def grow(self):
        self.height = round(self.height + self.growth_rate, 2)

    def age(self):
        self.days += 1
        self.grow()


rose: Plant = Plant("rose", 25, 30, 0.8)
total: float = 0

print("=== Garden Plant Growth ===")
rose.show()
for i in range(7):
    print(f"=== Day {i + 1} ===")
    total += rose.growth_rate
    rose.age()
    rose.show()

print(f"Growth this week: {round(total, 2)}cm")
