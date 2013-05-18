import time
import spidev
import RPi.GPIO as GPIO

class ShiftOutputSPI:
    
    BCM = None
    OUT = None
    
    def __init__(self, num_channels=8, S_ST=22):

	self.state = 0x00

        self.spi = spidev.SpiDev(0,0)

        self.S_ST = S_ST
	GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.S_ST, GPIO.OUT, initial=GPIO.LOW)
    
    def setup(self, *args, **kwargs):
        pass
    
    def setmode(self, *args, **kwargs):
        pass
    
    def output(self, chan, state, commit=True):
        bit = (1 << chan)
        if state:
            self.state |= bit
        else:
            self.state &= ~bit
        if (commit):
            self._commit()
        
    def _commit(self):
        GPIO.output(self.S_ST, False)
	# self.spi.writebytes([self.state])
	self.spi.writebytes(list(divmod(self.state, 0x100)))
        GPIO.output(self.S_ST, True)

