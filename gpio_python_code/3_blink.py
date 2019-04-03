# setup our output pins
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

# Turn LED's on 
print "lights on"
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
sleep(1) #sleep for 1 second

# Turn LED's off
print "lights off"
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
sleep(1) #sleep for 1 second

# Turn LED's on
print "lights on"
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
sleep(1) #sleep for 1 second

# Turn LED's off
print "lights off"
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
GPIO.cleanup()


