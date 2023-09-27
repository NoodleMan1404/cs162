class Car:

    def __init__(self, engine, transmission, doors, wheels):
        self.engine = engine
        self.transmission = transmission
        self.doors = doors
        self.wheels = wheels



    tank = 12

    def setStatus(status):
        print(f'The car is currently {status}... ')
        input('Press any key to continue ')
    
    def doorStatus(dStatus, pStatus): #dStatus = Driver, pStatus = Passenger Princess
        print(f'Driver door {dStatus} ')
        print(f'Passenger door {pStatus}')

    def drive():
        pass
    
    def displayInfo():
        print('---------------------------------------------')
        print('Information about the car you are driving ')
        print('Style', 'Coupe')
        print('Doors:', '2')
        print('Engine', '1.6 L')
        print('Transmission', '8 Speed Automatic')
        print('---------------------------------------------')

    displayInfo()