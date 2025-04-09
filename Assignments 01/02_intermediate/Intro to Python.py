MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    earth_weight = float(input("enter the weight of earth:"))
    planet = input("enter a planet").capitalize()
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity_constant = NEPTUNE_GRAVITY
    else:
        print("Planet not supported yet.")
        return
    planetary_weight = earth_weight * gravity_constant
    round_weight = round(planetary_weight , 2)
    print(f"the equivalent weight of {planet} is :{round_weight}")

main()