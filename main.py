# Родительный класс животных
heaviest = 0
weight_count = 0
class Animal:
    type = None
    skills_status = False
    hungry = True
    heaviest = 0
    weight_count = 0
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        Animal.weight_count += int(self.weight)
        if Animal.heaviest < int(self.weight):
            Animal.heaviest = int(self.weight)



    def feed(self):
        while True:
            feed_animal = input('Чем будем кормить? ' )
            if self.forage != feed_animal:
                print('Животное ест только', self.forage)
            else:
                self.hungry = False
                break
        return 'Животное накормленно'

    def get_voise(self):
        return self.voise

    def use_skill(self):
        while True:
            answer = input('Будем ' + self.skills + ' у ' + self.type + ' ' + self.name + ' (y/n)? ')
            if answer == 'y':
                self.skills_status = True
                status = 'Сделано!'
                break
            elif answer == 'n':
                status = 'Тогда в другой раз'
                break
            else:
                print('Не понял...')
        return status
# Классы видов животных:
# Класс Коровы
class Cow(Animal):
    type = 'Корова'
    voise = 'Мууууу'
    skills = 'доить'
    forage = 'трава'

# Класс Гуся
class Goose(Animal):
    type = 'Гусь'
    voise = 'Га - га - га'
    skills = 'собирать яйца'
    forage = 'корм'

# Класс Овец
class Sheep(Animal):
    type = 'Овца'
    voise = 'Меее'
    skills = 'стрич'
    forage = 'трава'

# Класс Кур
class Chicken(Animal):
    type = 'Курица'
    voise = 'Ко - ко'
    skills = 'собирать яйца'
    forage = 'корм'

# Класс Коз
class Goat(Animal):
    type = 'Коза'
    voise = 'Беее'
    skills = 'доить'
    forage = 'трава'

# Класс Уток
class Duck(Animal):
    type = 'Утка'
    voise = 'Кря - Кря'
    skills = 'собирать яйца'
    forage = 'корм'

# print(Animal.display_count)
# Создаём животных нашей фермы
myCow = Cow('Манька', '500')
myGoose1 = Goose('Серый', '50')
myGoose2 = Goose('Белый', '55')
mySheep1 = Sheep('Борашек', '220')
mySheep2 = Sheep('Кудрявый', '235')
myChicken1 = Chicken('Ко-ко', '40')
myChicken2 = Chicken('Кукареку', '45')
myGoat1 = Goat('Рога', '180')
myGoat2 = Goat('Копыта', '185')
myDuck = Duck('Дональд', '60')



print('Масса всех животных %d' % Animal.weight_count)
print('Самый тяжёлый %d' % Animal.heaviest)

# print(myCow.type + ' по кличке ' + myCow.name + ': ее пора ' + myCow.skills + ', так как она весит уже ' + myCow.weight)
# print(myCow.get_voise())
# print(myCow.feed())
# print(myCow.use_skill())

# print(myGoose1.type + ' по кличке ' + myGoose1.name + ': у нее пора ' + myGoose1.skills + ', так как она весит уже ' + myGoose1.weight)
# print(myGoose1.get_voise())
# print(myGoose1.feed())
# print(myGoose1.use_skill())

# print(myGoose2.type + ' по кличке ' + myGoose2.name + ': у нее пора ' + myGoose2.skills + ', так как она весит уже ' + myGoose2.weight)
# print(myGoose2.get_voise())
# print(myGoose2.feed())
# print(myGoose2.use_skill())

# print(mySheep1.type + ' по кличке ' + mySheep1.name + ': ее пора ' + mySheep1.skills + ', так как она весит уже ' + mySheep1.weight)
# print(mySheep1.get_voise())
# print(mySheep1.feed())
# print(mySheep1.use_skill())

# print(mySheep2.type + ' по кличке ' + mySheep2.name + ': ее пора ' + mySheep2.skills + ', так как она весит уже ' + mySheep2.weight)
# print(mySheep2.get_voise())
# print(mySheep2.feed())
# print(mySheep2.use_skill())

# print(myChicken1.type + ' по кличке ' + myChicken1.name + ': у нее пора ' + myChicken1.skills + ', так как она весит уже ' + myChicken1.weight)
# print(myChicken1.get_voise())
# print(myChicken1.feed())
# print(myChicken1.use_skill())

# print(myChicken2.type + ' по кличке ' + myChicken2.name + ': у нее пора ' + myChicken2.skills + ', так как она весит уже ' + myChicken2.weight)
# print(myChicken2.get_voise())
# print(myChicken2.feed())
# print(myChicken2.use_skill())

# print(myGoat1.type + ' по кличке ' + myGoat1.name + ': ее пора ' + myGoat1.skills + ', так как она весит уже ' + myGoat1.weight)
# print(myGoat1.get_voise())
# print(myGoat1.feed())
# print(myGoat1.use_skill())

# print(myGoat2.type + ' по кличке ' + myGoat2.name + ': ее пора ' + myGoat2.skills + ', так как она весит уже ' + myGoat2.weight)
# print(myGoat2.get_voise())
# print(myGoat2.feed())
# print(myGoat2.use_skill())

print(myDuck.type + ' по кличке ' + myDuck.name + ': у нее пора ' + myDuck.skills + ', так как она весит уже ' + myDuck.weight)
print(myDuck.get_voise())
print(myDuck.feed())
print(myDuck.use_skill())