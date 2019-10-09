class PiezoElectricReader:
    '''
    Detects the presence based on GPIO readings and processing
    '''

    def detectPresence(self):
        gpioReading = self.readFromADC()
        detected = self.processADCReading(gpioReading)
        return detected

    '''
    Gets the reading from the ADC GPIO pin
    '''

    def readFromADC(self):
        # mock return
        return 512

    '''
    Processes the GPIO reading and determines if presence was detected
    '''

    def processADCReading(self, gpioReading):
        # mock return
        return True
