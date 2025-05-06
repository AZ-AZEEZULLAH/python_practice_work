# This is a class named Animal
class Animal:
    # These are the properties that every animal will have
    color: str                 # color of the animal (like white, black)
    voice: str                 # the sound the animal makes (like bark, meow)
    number_of_legs: int = 4    # animals usually have 4 legs
    number_of_eyes: int = 2    # animals usually have 2 eyes
    number_of_ears: int = 2    # animals usually have 2 ears
    number_of_noses: int = 1   # animals usually have 1 nose

    # This is a special function that runs when we create a new animal
    def __init__(self, color: str, voice: str, number_of_legs: int = 4, number_of_eyes: int = 2,
                 number_of_ears: int = 2, number_of_noses: int = 1):
        # Set the color and voice given when creating the animal
        self.color = color
        self.voice = voice
        # Set the default or given number of body parts
        self.number_of_legs = number_of_legs
        self.number_of_eyes = number_of_eyes
        self.number_of_ears = number_of_ears
        self.number_of_noses = number_of_noses

    # This function adds a tail to the animal
    def add_tails(self):
        self.number_of_tails = 1  # Adds 1 tail
        return self.number_of_tails  # Gives back the number of tails


# Now we create animals

# A dog is created with color "white" and voice "bark"
dog = Animal("white", "bark")

# A cat is created with color "black" and voice "meow"
cat = Animal("black", "meow")

# Let's print details about the dog and cat
print("Dog color:", dog.color)     # prints dog's color
print("Dog voice:", dog.voice)     # prints dog's voice
print("Cat color:", cat.color)     # prints cat's color
print("Cat voice:", cat.voice)     # prints cat's voice

# Add a tail to the dog and print how many tails it has
print("Dog number of tails:", dog.add_tails())

# Print number of legs the dog has
print("Dog number of leg:", dog.number_of_legs)

# Make another animal - a cow
cow = Animal("brown", "moo")

# Add a tail to the cow and print it
print("Cow tail:", cow.add_tails())
