class Bot:
    def __init__(self, name, age=0, energy=0, shield=0):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield

    def display_name(self):
        print("Your name is {}".format(self.name))

    def display_age(self):
        print("You are {} years old".format(self.age))

    def display_energy(self):
        print("Your energy level is at {} %".format(self.energy))

    def display_shield(self):
        print("Your shield level is at {} %".format(self.shield))

    def display_summary(self):
        print("Name: {}\nAge: {}\nEnergy: {}\nShield: {}".format(self.name, self.age, self.energy, self.shield))

    def __str__(self):
        bot.display_summary()

bot = Bot("Pedro", 19, 68, 100)

bot.__str__()