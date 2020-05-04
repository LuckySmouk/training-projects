class View:

    def __init__ (self, name, age, height, wrist, iwt, txt):
        self.name = name
        self.age = age
        self.height = height
        self.wrist = wrist
        self.iwt = iwt
        self.txt = txt

    def chek_wrist(self):
        if self.wrist < 15:
            koff = 0.9
        elif 15 < self.wrist < 17:
            koff = 1
        elif self.wrist > 17:
            koff = 1.1
        self.iwt = (float(self.height) - 100 + int(self.age / 10)) * 0.9 * koff
        return print("\nПривет " + str(self.name) + "!\n" + "Твой лучший вес равен - " + str(self.iwt))

data_name = input("Your Name - ")
data_age = int(input("Age - "))
data_height = float(input("Your height - "))
data_wrist = float(input("Enter the size of the wrist (enter a point instead of a comma before the millimeters) - "))


user_1 = View(data_name, data_age, data_height, data_wrist, 0, 'text')
user_1.chek_wrist()
print(user_1.iwt)






