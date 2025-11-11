#creating lists
planet_list = ["Mercury", "Mars"]
planet_list_2 = ["Neptune", "Urnaus"]

#func to add a planet using append()
def add_planet(planet):
    planet_list.append(planet)
    print(f"{planet} has been added to the list of planets")

#func to display the planets
def display_planets():
    print("Here is a list of planets:")
    for planet in planet_list:
        print(f"- {planet}")

#func to combine 2 lists using extend()
def add_more_planets():
    planet_list.extend(planet_list_2)
    print(f"{planet_list}")

#func to insert earth and venus in the proper positions using insert()
def insert_earth_and_venus_correctly():
    planet_list.insert(1,"Venus")
    planet_list.insert(2, "Earth")
    display_planets()

#func to add pluto using append again
def add_pluto():
    planet_list.append("Pluto")
    display_planets()

#func to separate the rocky planets into a separate list using slice()
def separate_the_rocky():
    x = slice(4)
    print(f"{planet_list[x]}")

#func to remove pluto using del operator
def remove_pluto():
   del planet_list[-1]
   display_planets()
    


add_planet("Jupiter")
add_planet("Saturn")
display_planets()
add_more_planets()
insert_earth_and_venus_correctly()
add_pluto()
separate_the_rocky()
remove_pluto()

# Example spacecraft list
spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
]

for planet in planet_list:
    visited_by = []

    for craft, visited_planet in spacecraft:
        if visited_planet == planet:
            visited_by.append(craft)

    if visited_by:
        for craft in visited_by:
            print(f"{craft} has visited")
            print("------------------------")
            print(planet)
            