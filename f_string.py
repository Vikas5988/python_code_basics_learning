#F String exercise

City="Kanpur"
State="UP"
place="The City {} is in the Sate of {}"


print(place.format(City,State))    #without F string

print(place.format(State,City))    #without F string, Wrong order

print(f"{City} is in {State}")

