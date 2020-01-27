# In Dictionary each key is separated from its value by a colon, the items are separated by commas
# and the whole thing is enclosed in curly braces.
# Indexed by unique keys that must be immutable objects

# definition of dictionary
europe = { 'spain':'madrid', 'france': 'paris', 'germany': 'berlin', 'norway':'oslo' }

# Accessing values in dictionary
# europe['norway']

# Updating dictionary
# europe['norway'] = 'otracosa'

# Deleting Dictionary
#   removinig entry with key
#   del europe['france']
#
#   removing all entries
#   europe.clear()
#
#   delete entire dictionary
#   del europe

#print out the dictionary
print(europe)

#print out the keys in europe
print(europe.keys())

#print out value that belongs to key 'norway'
print(europe['norway'])

# Add italy and poland to europe
europe['italy'] = 'rome'
europe['poland'] = 'warsaw'

# Print out italy in europe
print('italy' in europe)
