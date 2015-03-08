from celery import task
from models import Circuit

@task()
def toggleSwitch(circuit_id, state):
	circuit = Circuit.objects.get(pk=circuit_id)
	originalState = circuit.state

	if circuit.state != state:
		circuit.state = state
		circuit.changed = True
	circuit.save()

@task()
def testScheduler():
	print "OMG IT WORKS"