# Filename: using_tuple.py

zoo = ("wolf", "elephant", "penguin")
print("Number of animals in the zoo is", len(zoo))

new_zoo = ("monkey", "dolphin", zoo)
print("Number of animals in the new zoo is", len(new_zoo))
print("All animals in new zoo ate", new_zoo)
print("Animals brought from old zoo ate", new_zoo[2])
print("Last animal brought from old zoo is", new_zoo[2][2])
