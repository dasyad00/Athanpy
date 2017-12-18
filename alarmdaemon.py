#!/usr/bin/python
import sched, time
import datetime

class AlarmDaemon():
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        pass

    def alarm_action(self, athan_name):
        print('Time for ', athan_name, '!')

    def schedule_alarm(self, str_time, athan_name):
        hour = str_time[0:2]
        mins = str_time[3:]
        alarm_time = datetime.datetime.today()
        alarm_time = alarm_time.replace(
            hour=int(str_time[0:2]),
            minute=int(str_time[3:]),
            second=0
        )
        self.scheduler.enterabs(alarm_time.timestamp(), 1, self.alarm_action, argument={athan_name})
        print('Alarm set for:', alarm_time)

    def start_alarm(self):
        self.scheduler.run()

alarm = AlarmDaemon()
alarm.schedule_alarm('19:08', 'test')
alarm.start_alarm()
