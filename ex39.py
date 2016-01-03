#create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
	
}

#create a basic set of states and some cities in them
cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville',
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print '-' * 10
print 'NY State has: ', cities['NY']
print 'OR State has: ', cities['OR']

# do it by using the state then cities dic
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state,abbrev)

print '-' * 10
#safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas"

#get a city with a default value
city = cities.get('TX', 'Does not Exist')
print "The city for the state 'TX' is: %s" % city

