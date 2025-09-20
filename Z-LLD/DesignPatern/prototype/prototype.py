import copy

# Prototype with nested objects
class Skill:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return f"{self.name}({self.power})"

class Character:
    def __init__(self, name, level, skills):
        ## Heavy calculation + api call
        self.name = name
        self.level = level
        self.skills = skills  # list of Skill objects

    def __str__(self):
        skills_str = ", ".join(str(skill) for skill in self.skills)
        return f"{self.name} (Level {self.level}) with skills: [{skills_str}]"

    def clone(self):
        # Deep copy ensures nested objects are copied, not shared
        return copy.deepcopy(self)

# Original object with nested skills
prototype = Character("Warrior", 5, [Skill("Slash", 50), Skill("Shield", 30)])

# Clone character
char1 = prototype.clone()
char1.name = "Warrior A"
char1.skills[0].power = 60  # modifies only char1, prototype unaffected

char2 = prototype.clone()
char2.name = "Warrior B"
char2.skills[1].name = "Barrier"  # modifies only char2

print(prototype)
print(char1)
print(char2)

#
# Warrior (Level 5) with skills: [Slash(50), Shield(30)]
# Warrior A (Level 5) with skills: [Slash(60), Shield(30)]
# Warrior B (Level 5) with skills: [Slash(50), Barrier(30)]