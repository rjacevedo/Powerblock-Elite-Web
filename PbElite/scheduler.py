from djcelery.models import PeriodicTask, CrontabSchedule
from models import Circuit
from models import Schedule
import datetime
import json

def updateSchedule(schedule_id, start_date, end_date):
	schedule = Schedule.objects.get(pk=schedule_id)
	
	start_crontab = CrontabSchedule(day_of_month=start_date.day, month_of_year=start_date.month,
		hour=start_date.hour, minute=start_date.minute)
	end_crontab = CrontabSchedule(day_of_month=end_date.day, month_of_year=end_date.month,
		hour=end_date.hour, minute=end_date.minute)

	start_schedule = schedule.start_id
	end_schedule = schedule.end_id
	
	if start_schedule.crontab != start_crontab:
		start_crontab.save()
		start_schedule.crontab = start_crontab

	if end_schedule.crontab != end_crontab:
		end_crontab.save()
		end_schedule.crontab = end_crontab

	schedule.start_id = start_schedule
	schedule.end_id = end_schedule
	schedule.save()

def scheduleToggleTask(circuit_id, desired_state, crontab_obj):
	periodic_task = PeriodicTask(
		name='%s_%s' % ('toggleSwitch', datetime.datetime.now()),
    	task='PbElite.tasks.toggleSwitch',
    	crontab=crontab_obj,
    	args=json.dumps([circuit_id, desired_state])
	)
	periodic_task.save()
	return periodic_task

def createUserSchedule(schedule_id, desired_state):
	schedule = Schedule.objects.get(pk=schedule_id)
	circuit = schedule.circuit
	originalState = circuit.state
	start_date = schedule.start_time
	end_date = schedule.end_date

	# Schedule the start time (desired_state)
	start_crontab = CrontabSchedule(day_of_month=start_date.day, month_of_year=start_date.month,
		hour=start_date.hour, minute=start_date.minute)
	start_crontab.save()
	schedule.start_id = scheduleToggleTask(circuit.pk, desired_state, start_crontab)

	# Schedule the end time (original_state)
	end_crontab = CrontabSchedule(day_of_month=end_date.day, month_of_year=end_date.month,
		hour=end_date.hour, minute=end_date.minute)
	end_crontab.save()
	schedule.end_id = scheduleToggleTask(circuit.pk, originalState, end_crontab)

	#Save the id's to the Schedule table to delete later
	schedule.save()


def scheduleTest():
	crontab_obj = CrontabSchedule()
	crontab_obj.save()

	periodic_task = PeriodicTask(
		name='test',
		task="PbElite.tasks.testScheduler",
		crontab=crontab_obj
	)
	periodic_task.save()