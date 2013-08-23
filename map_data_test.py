from models.models import *

def test(m):
	print("*************************** Testing...")
	print m
	# m.save()
	m.validate()
	print("*************************** Test complete...")

# Create the object
m = connection.Map()
# test(m)

# Add an email address
m.email = u'jono@dronedeploy.com'
# test(m)

# Add a name
m.name = u'Test Entry'
# test(m)


# Add a waypoint
wps = [	
	{'wp_no' : 0, 'lat' : 45.102, 'lng' : 20.213, 'alt' : 100, 'action' : "TAKEOFF"},
	{'wp_no' : 1, 'lat' : 45.103, 'lng' : 20.214, 'alt' : 100, 'action' : "GOTO"},
	{'wp_no' : 2, 'lat' : 45.104, 'lng' : 20.215, 'alt' : 100, 'action' : "GOTO"},
	{'wp_no' : 3, 'lat' : 45.105, 'lng' : 20.216, 'alt' : 100, 'action' : "LAND"},
 ]
m.waypoints = wps
test(m)

m.save()

