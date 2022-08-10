# This class is used to generate the ennemies.
# A ennemy is a random enemy scaled by the level of the character and the difficulty.
# It has a name, health, energy, stats, and loot.
# The loot is generated randomly scaled by the level of the character.
# The ennemy can be an orc, a demon, a dragon, a goblin, a skeleton, a zombie, a skeleton
import random
import string


class Ennemy:
    # The constructor of the class
    def __init__(self, name, health, energy, stats, ennemyType, loot):
        self.name = name
        self.health = health
        self.energy = energy
        self.stats = stats
        self.type = ennemyType
        self.loot = loot
        self.isAlive = True

    # This method is used to generate the ennemies.
    # A ennemy is a random enemy scaled by the level of the character and the difficulty.
    # It has a name, health, energy, stats, and loot.
    # The loot is generated randomly scaled by the level of the character.
    # The ennemy can be an orc, a demon, a dragon, a goblin, a skeleton, a zombie, a skeleton

    def generateEnnemy(self, level, difficulty):
        # The ennemy can be an orc, a demon, a dragon, a goblin, a skeleton, a zombie, a skeleton
        ennemyType = self.generateType()
        # The name of the ennemy is random
        name = self.generateName(ennemyType)
        # The health of the ennemy is random scaled by the level of the character
        health = self.generateHealth(level)
        # The energy of the ennemy is random scaled by the level of the character
        energy = self.generateEnergy(level)
        # The stats of the ennemy is random scaled by the level of the character
        stats = self.generateStats(level)
        # The loot of the ennemy is random scaled by the level of the character
        loot = self.generateLoot(level)
        # The ennemy is created
        ennemy = Ennemy(name, health, energy, stats, ennemyType, loot)
        return ennemy

    # This method generates the type of the ennemy
    def generateType(self):
        choice = random.randint(1, 7)
        if choice == 1:
            self.type = 'Orc'
        elif choice == 2:
            self.type = 'Demon'
        elif choice == 3:
            self.type = 'Dragon'
        elif choice == 4:
            self.type = 'Goblin'
        elif choice == 5:
            self.type = 'Skeleton'
        elif choice == 6:
            self.type = 'Zombie'
        elif choice == 7:
            self.type = 'Skeleton'
        return self.type

    def generateName(self, ennemyType):
        self.name = ''.join(random.choice(string.ascii_uppercase) for _ in range(random.randint(5, 10))) + ' The '
        if ennemyType == 1:
            self.name += 'Orc'
        elif ennemyType == 2:
            self.name += 'Demon'
        elif ennemyType == 3:
            self.name += 'Dragon'
        elif ennemyType == 4:
            self.name += 'Goblin'
        elif ennemyType == 5:
            self.name += 'Skeleton'
        elif ennemyType == 6:
            self.name += 'Zombie'
        elif ennemyType == 7:
            self.name += 'Skeleton'
        return self.name
