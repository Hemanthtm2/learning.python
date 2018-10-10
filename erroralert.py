#!/usr/bin/python

alert_system='console'
error_severity='critical'
error_message='OMG'


if alert_system == 'console':
   print('error message')

elif alert_system == 'email':
    if error_severity == 'critical':
        print ("Immediatly send an email to system administrator")
    elif error_severity == 'warning':
        print("Send an email to first level support")
    else:
        print("Trigger a pagerduty")


