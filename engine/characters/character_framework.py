class Npc:
    def __init__(self, health=10, alive=True, name = 'npc', defense = 0):
        self.health = health
        self.alive = alive
        self.name = name
        self.defense = defense
    def take_damage(self, amount):
        self.health -= (amount)
        if self.health <1:
            self.alive = False
            self.health = 0
    def is_alive(self):
        return self.alive
    

      



