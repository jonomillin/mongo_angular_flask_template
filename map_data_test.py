from models.models import Map

def test(m):
	print m
	# m.save()
	m.validate()


m = Map()
test(m)

wps = [
	{wp_no : 0, lat : 45.102, lng : 20.213, alt : 100, action : "FLY"}
]

