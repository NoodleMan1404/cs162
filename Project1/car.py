class Car:

    def __init__(self, doors, gear, engine):
        self.doors = doors
        self.gear = gear
        self.engine = engine



    tank = 12

    def mainMenu(self):
        print('\nDirecting to drive function')
        self.drive(self.engine, self.gear)

    def drive(self, engine, gear):
        if self.engine == 'OFF':
            print('The engine is currently off. ')
        elif self.engine == 'ON':
            if self.gear == 'D':
                print("You start driving")
            elif self.gear == 'R':
                print('You start driving backwards')
            elif self.gear == 'N':
                print('Your engine starts revving because you\'re in neutral.')
            else:
                print('Either you selected something that wasn\'t an existing gear, or you\'re in park.')

    def setStatus(self, status):
        print(f'The car is currently {status}... ')
        input('Press any key to continue ')
    
    def doorStatus(self, dStatus, pStatus): #dStatus = Driver, pStatus = Passenger Princess
        print(f'Driver door {dStatus} ')
        print(f'Passenger door {pStatus}')

    def trans(self, gear): #Trans is short for transmission
        print(gear)
        self.gear = input(f'You are currently in {gear}\n\nWhat gear would you like to put it in? (P)ark, (R)everse, (N)uetral, (D)rive: ')
        self.gear = self.gear.upper()
        if self.gear == 'P':
            print('You have put the car in Park.\n')
            input('Press any button to continue...')
            self.mainMenu()
        elif self.gear == 'R':
            print('You have put the car in Reverse.\n')
            input('Press any button to continue...')
            self.mainMenu()
        elif self.gear == 'N':
            print('You have put the car in neutral.\n')
            input('Press any button to continue...')
            self.mainMenu()
        elif self.gear == 'D':
            print('You have put the car in Drive.\n')
            input('press any key to continue...')
            self.mainMenu()
        else: 
            print('Only enter a gear to drive. ')
            self.trans(self.gear)
    
    def displayInfo():
        print('---------------------------------------------')
        print('Information about the car you are driving ')
        print('Style', 'Coupe')
        print('Doors:', '2')
        print('Engine', '1.6 L')
        print('Transmission', '8 Speed Automatic')
        print('---------------------------------------------')

my_car = Car(2, 'P', 'ON')

# my_car.drive(my_car.engine, my_car.gear)
my_car.trans('P')