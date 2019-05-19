import numpy as np

a = [1,2,3,4,5,6]
b = np.mean(a)
print(b)

destinations = ["Paris, France","Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
def get_destination_index(destination):
  for i in range(0,len(destinations)):
    if destinations[i] == destination:
        destination_index = i
        return destination_index

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

attractions = [[], [], [], [], []]

def add_attraction(destination,attraction):
    try:
        destination_index = get_destination_index(destination)
    except SyntaxError:
        return
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return 

add_attraction('Los Angeles, USA',['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination,interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for i in attractions_in_city:
    possible_attraction = i
    attraction_tags = i[1]
    for interest in interests:
      if interest == attraction_tags[0]:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest
  
la_arts = find_attractions('Los Angeles, USA',['art'])
print(la_arts)
  






