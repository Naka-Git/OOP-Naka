class Attackable:
    def attack(self, target):
        return 0
class BangunDatar:
    def __init__(self, nama, sisi):
        """
        Membuat sebuah object bangun datar dengan nama dan sisi
        :param nama: nama dari object
        :param sisi: bisa berupa jari jari atau sisi dari bangun datar
        """
        self.nama = nama
        self.sisi = sisi
    
    def luas(self):
        return 0;

    def keliling(self):
        return 0;

class Persegi(BangunDatar):
    def luas(self):
        return self.sisi * self.sisi

    def keliling(self):
        return self.sisi * 4;

class Lingkaran(BangunDatar):
    def luas(self):
        return 3.14 * self.sisi * self.sisi

    def keliling(self):
        return 2 * 3.14 * self.sisi


class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target):
        return 0;
    
    def magicAttack(self, target):
        return 0;

    def __str__(self):
        return f"Hero name: {self.name}\n{self.name} health: {self.health}"

class Warrior(Hero):
    def attack(self, target: Hero):
        print(f"Warrior {self.name} attacking {target.name}")
        target.health -= 10
    def magicAttack(self, target: Hero):
        print(f"Warrior {self.name} using magic attack to {target.name}")
        target.health -= 5

class Mage(Hero):
    def attack(self, target: Hero):
        print(f"Mage {self.name} attacking {target.name}")
        target.health -= 5
    def magicAttack(self, target: Hero):
        print(f"Mage {self.name} using magic attack to {target.name}")
        target.health -= 20

        
a = Lingkaran('Lingkaran A', 8)
print(f"Luas dari instance a {a.luas()}")
print(f"Keliling dari instance a {a.keliling()}")

b = Persegi('Persegi B', 8)
print(f"Luas dari instance b {b.luas()}")
print(f"Keliling dari instance b {b.keliling()}")

warrior_a = Warrior('Warrior A', 100)
warrior_b = Warrior('Warrior b', 100)
mage_a = Mage('Mage A', 100)
mage_b = Mage('Mage B', 100)

bilangan = 15

print(warrior_a)
print(warrior_b)
print(mage_a)
print(mage_b)

print("==========")
warrior_a.attack(warrior_b)
print(warrior_b)
mage_a.attack(warrior_b)
print(warrior_b)
mage_a.magicAttack(mage_a)
print(warrior_b)

# print(warrior_a)
# print(warrior_b)
