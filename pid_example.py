#!/usr/bin/python

"""
PID Tutorial
Author: James Irwin
This file contains a class with a simple PID implementation,
and a main function demonstrating how to use it.
It assumes that you already have functions for reading motor speed
and controlling a motor via PWM.
"""

import time

class PID:
	def __init__(self, P=0, I=0, D=0):
		self.P = P
		self.I = I
		self.D = D
		self.error_integral = 0 #accumulated error (integral of error)
		self.previous_error = 0 #store previous error for simple derivative calculation

	def update(self, error):
		#calculate control due to proportional error
		p_control = error * self.P

		#update the integral
		self.error_integral += error

		#calculate control due to integral of error
		i_control = self.error_integral * self.I

		#calculate derivative (simple method)
		derivative = error - self.previous_error
		self.previous_error = error

		#calculate control due to derivative of error
		d_control = derivative * self.D

		#return proper control action
		return p_control + i_control + d_control


def get_motor_speed():
	#insert actual code to read motor speed
	motor_speed = 0
	return 0

def set_motor_pwm(duty_cycle):
	#sanitize results from controller
	#can't have duty cycle less than 0 or greater that 100
	if(duty_cycle > 100):
		duty_cycle = 100
	if(duty_cycle < 0):
		duty_cycle = 0

	#send pwm to motor
	print "motor PWM:", duty_cycle

def main():
	pid = PID(3,1,0)
	desired_speed = 10

	while 1:
		motor_speed = get_motor_speed()
		error = desired_speed - motor_speed
		
		control = pid.update(error)
		
		set_motor_pwm(control)
		
		time.sleep(1)



if __name__=="__main__":
	main()
