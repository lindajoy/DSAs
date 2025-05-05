random_numbers = [1,2,3,4,5]
similar_numbers = [9,8,11,12,13]

random_numbers.extend(similar_numbers)
print('Extending my numbers here:', random_numbers)

random_numbers.extend(range(5)) # 0,1,2,3,4
print(random_numbers)

# Pop removes the last element from the list - but you can give an index of what index you would want removed.

cities = ["New York",  "Los Angeles", "Chicago",  "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
another_cities = ["Austin", "Jacksonville", "Houston", "Phoenix", "Fort Worth",  "Columbus", "Indianapolis"]

cities.pop()
print('Removed last city from cities', cities)

cities.pop(0)
print('Removed first city from cities', cities)

cities.insert(0, 'Nairobi')
print('Inserted Nairobi 🇰🇪', cities)

cities.remove('Chicago')
print('Removed first occurence of Chicago', cities)

#cities.remove('Cape Town')  # This should error out.
print('Trying to remove Cape Town...', cities)

cities.append('Chicago')
cities.append('Chicago')
cities.append('Chicago')
cities.append('Chicago')


print('Returns the number of chicago occurences', cities.count('Chicago'))

print('Reversing a list', cities.reverse())





