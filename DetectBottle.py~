import RPi.GPIO as GPIO, time 

# setup function
def setup():
   global oldVal
   global pinNr
   oldVal = 0
   pinNr = 4
   GPIO.setmode(GPIO.BCM)


def RCtime():
   global pinNr
   global oldVal

   measurement = 0

   GPIO.setup(pinNr, GPIO.OUT)
   GPIO.output(pinNr, GPIO.LOW)
   time.sleep(0.1)

   GPIO.setup(pinNr, GPIO.IN)

   while(GPIO.input(pinNr)==GPIO.LOW):
      measurement += 1

   #return measurement
   if measurement>5000:
      if oldVal==0:
      	 print '1'
         execfile("Bottlemachine.py")
      oldVal = 1
   else:
      if oldVal==1:
         print '0'
      oldVal = 0

#main function
setup()
while True:
   RCtime()
