class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        capname: str = self.name.capitalize()
        print(f"{capname}: {self.height}cm, {self.age} days old")


rose: Plant = Plant("rose", 25, 30)
sunflower: Plant = Plant("sunflower", 80, 45)
cactus: Plant = Plant("cactus", 15, 120)

rose.show()
sunflower.show()
cactus.show()
