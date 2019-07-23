#!/usr/bin/python3

# create a dictonary
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'ciscor'}

##display parts of the dictonary

print(switch['hostname'])
print(switch['ip'])

##request a 'fake' key
#print(switch['lynx'])


print( "First test - .get()" )
print( switch.get('lynx') )

print( " Second test - .get( )" )
print( switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!") )

print( "Third test - .get()" )
print( switch.get('version') )


print( "Ffourth test - .keys()" )
print( switch.keys() )

print( "Fifth test - .values()" )
print( switch.vaues() )


