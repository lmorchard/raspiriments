import time
import RPi.GPIO as GPIO

class ShiftOutputGPIO:
    
    BCM = None
    OUT = None
    
    def __init__(self, num_channels=8, S_DS=23, S_ST=24, S_SH=25):
        
        self.num_channels = num_channels
        self.S_DS = S_DS
        self.S_ST = S_ST
        self.S_SH = S_SH
        
        self.state = [0 for idx in range(0, self.num_channels)]
        
        for p in (self.S_DS, self.S_ST, self.S_SH):
            GPIO.setup(p, GPIO.OUT, initial=GPIO.LOW)
    
    def setup(self, *args, **kwargs):
        pass
    
    def setmode(self, *args, **kwargs):
        pass
    
    def output(self, chan, state, commit=True):
        self.state[self.num_channels - 1 - chan] = state
        if (commit):
            self._commit()
        
    def _commit(self):
        GPIO.output(self.S_ST, 0)
        for bit in self.state:
            GPIO.output(self.S_DS, int(bit))
            GPIO.output(self.S_SH, 1)
            GPIO.output(self.S_SH, 0)
        GPIO.output(self.S_ST, 1)
        #time.sleep(0.01)