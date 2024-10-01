# class Kucing:
#     def bersuara(self):
#         return "Meong!"

# class Anjing:
#     def bersuara(self):
#         return "Guk guk!"
    
# class Babi:
#     def bersuara(self):
#         return "Guik guik!"    

# class Persegi:
#     def luas(self):
#         return "s x s"
    
# class Segitiga:
#     def luas(self):
#         return "a x t / 2"

# # Polymorphism
# def suara_hewan(hewan):
#     print(hewan.bersuara())

# def luas_bangundatar(bangun_datar):
#     print(bangun_datar.luas())

# # # Membuat objek dari kelas Kucing dan Anjing
# kucing = Kucing()
# anjing = Anjing()
# babi = Babi()
# persegi = Persegi()
# segitiga = Segitiga()

# # Memanggil fungsi yang sama untuk kedua objek
# suara_hewan(kucing)  # Output: Meong!
# suara_hewan(anjing)  # Output: Guk guk!
# suara_hewan(babi)
# luas_bangundatar(persegi)
# luas_bangundatar(segitiga)

class Jett:
    def menyerang(self):
        return "Kunai"

class Phoenix:
    def menyerang(self):
        return "Membakar"

# Polymorphism
def agent_menyerang(agent):
    print(agent.menyerang())

#membuat class
phoenix = Phoenix() 
jett = Jett()   

#memanggil fungsi
agent_menyerang(jett)
agent_menyerang(phoenix)