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
add_attraction("Paris, France", ["The Louvre", ["art", "museum"]])
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
  possible_attractions = []
  for i in attractions_in_city:
    possible_attraction = i
    print(possible_attraction[0])
    for x in possible_attraction[1]:
      attraction_tags = x
      for interest in interests:
        if interest == attraction_tags:
          attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest
  
la_arts = find_attractions('Los Angeles, USA',['art','beach'])
print(la_arts)

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = \
  find_attractions(traveler_destination,traveler_interests)
  print(traveler_attractions)
  places = ''
  for i in range(0,len(traveler_attractions)):
    if i == len(traveler_attractions) - 1:
      places += str(traveler_attractions[i]) + "."
    else:
      places += str(traveler_attractions[i]) + ", "
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination +': '+ places
  return interests_string
print(get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['art','monument']]))
  





