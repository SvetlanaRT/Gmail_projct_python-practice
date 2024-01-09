import random
# CREATE LIST (** RANDOM LIST02)
# ------------------------------
list01=[x**2 for x in range(10)]
print(list01)

list02=[random.randint(10,15) for x in range(10)]
print(list02)

list03=[x+100 for x in list02]
print(list03)

# MODIFY (lambda+list):
# ---------------------------------
list04=list(map(lambda x: x+200,list01))
print(list04)
# ADD VAR TO LIST
# ---------------------------------