class Pokemon:
    def __init__(self, name, typ):
        self.name = name
        self.level = 1
        self.typ = typ
        self.max_health = self.level * 10
        self.current_health = self.max_health
        self.is_knocked_out = False

    # remove health points
    def lose_health(self, hit_amount):
        self.current_health -= hit_amount
        return "{} now has {} health".format(self.name, self.current_health)

    # regains health
    def gain_health(self, gain_amount):
        self.current_health += gain_amount
        return "{} now has {} health".format(self.name, self.current_health)

    # knok out pokemon
    def knock_out(self):
        self.current_health = 0
        self.is_knocked_out = True
        return "{} is knocked out!".format(self.name)

    # reviving knocked out pokemon
    def revive_knocked_out(self):
        self.current_health = self.max_health
        self.is_knocked_out = False
        return "{} is revived with {} health points".format(self.name, self.current_health)

    # attack method - calculate damage based on type and level
    def attack(self, other_pokemon):
        # types = ["Water", "Fire", "Grass"]
        if self.typ == other_pokemon.typ:
            damage = self.level
        elif self.typ == "Water":
            if other_pokemon.typ == "Grass":
                damage = self.level * 0.5
            elif other_pokemon.typ == "Fire":
                damage = self.level * 2
        elif self.typ == "Grass":
            if other_pokemon.typ == "water":
                damage = self.level * 2
            elif other_pokemon.typ == "Fire":
                damage = self.level * 0.5
        elif self.typ == "Fire":
            if other_pokemon.typ == "Grass":
                damage = self.level * 2
            elif other_pokemon.typ == "water":
                damage = self.level * 0.5
        return other_pokemon.lose_health(damage)


class Trainer:
    def __init__(self, name, pokemons, potions):
        self.name = name
        if len(pokemons) > 6:
            print("Maximum pokemon amount is 6!")
        self.pokemons = pokemons
        self.potions = potions
        self.current_pokemon = 0

    def use_potion(self):
        if self.potions == 0:
            print("No potion in inventory!")
        else:
            print("Using 1 health potion on {}".format(self.pokemons[self.current_pokemon]))
            self.potions -= 1
            self.pokemons[self.current_pokemon].gain_health(20)

    def attack_other_trainer(self, other_trainer):
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        print("Attacking {trainer}'s {pokemon}".format(trainer=other_trainer, pokemon=their_pokemon))
        self.pokemons[self.current_pokemon].attack(other_trainer.current_pokemon)

    def switch_pokemon(self, pokemon):
        pokemon_index = self.pokemons.index(pokemon)
        print("Switching from {} to {}".format(self.current_pokemon, pokemon))
        self.current_pokemon = pokemon_index


pokemon_A = Pokemon("Pokemon A", "Grass")
pokemon_B = Pokemon("Pokemon B", "Water")
pokemon_C = Pokemon("Pokemon C", "Fire")
pokemon_D = Pokemon("Pokemon D", "Water")
pokemon_E = Pokemon("Pokemon E", "Grass")
pokemon_F = Pokemon("Pokemon F", "Fire")

trainer_one = Trainer("T one", [pokemon_A, pokemon_B, pokemon_C], 2)
trainer_two = Trainer("T two", [pokemon_D, pokemon_E, pokemon_F], 2)

trainer_one.attack_other_trainer(trainer_two)














