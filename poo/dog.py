class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def sit(self) -> None:
        print(f"{self.name} is sitting down")

    def roll_over(self) -> None:
        print(f"{self.name} rolling over")