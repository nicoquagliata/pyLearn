class Player:
    # init v.01
    #    def __init__(self, hit_points=50, mana=50, vocacion="sin vocacion", hechizo="Puff"):
    #        self.hit_points = hit_points
    #        self.mana = mana
    #        self.vocacion = vocacion
    #        self.hechizo = hechizo
    vocation = "no vocacion"
    spell = "Puff"
    movement_speed = "50"

# init v.02
    def __init__(self, **kwargs):
        self.name = input("Elige tu nombre: ")
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)

    def cast_spell(self):
        return self.spell

    def __str__(self):
        return ("{} is a {}: hit points: {} | mana: {} | Spell: {} | Movement Speed: {}".format(self.name, self.vocation, self.hit_points, self.mana, self.cast_spell(), self.movement_speed))


class Sorcerer(Player):
    vocation = "Sorcerer"
    spell = "Utevo lux"
    movement_speed = "20"

    def cast_spell(self):
        return "{} and Exura".format(self.spell)

class Knight(Player):
    vocation = "Knight"
    spell = "Exori"
    movement_speed = "60"

class Paladin(Player):
    vocation = "Paladin"
    spell = "Exana"
    movement_speed = "80"

class Druid(Player):
    vocation = "Druid"
    spell = "Exura sio"
    movement_speed = "30"

    def cast_spell(self):
        return "{} and Exura".format(self.spell)


class Troll:
    description = "Trolls are a human-like race that lives in small tribes in the holes and dungeons of Tibia. There they hunt animals and seek treasures over which they keep a jealous watch. They are weak and silly fighters, but as a squad they can become quite dangerous."
    type = "Troll"
    spell = "Puff"
    movement_speed = "50"

    def __init__(self, **kwargs):
        self.name = input("Pick Troll's name: ")
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",290)

    def __str__(self):
        return ("{} is a {}: hit points: {} | mana: {} |  Movement Speed: {}".format(self.name, self.type, self.hit_points, self.mana, self.movement_speed))
