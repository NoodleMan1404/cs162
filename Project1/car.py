'''
Project 1 
9/28/23
Travis Santos

Description: A simple program designed to start, and drive an imaginary car.
'''

class Car:
    def __init__(self, doors, gear, engine):
        self.doors = doors
        self.gear = gear
        self.engine = engine

    def mainMenu(self):
        print('\n')
        print('------------------------------------')
        print(f'Engine Status: {self.engine}')
        print(f'Transmission Status: {self.gear}')
        print('------------------------------------')
        print('What would you like to do?\n\n')
        choice = input('(T)urn the key, (S)hift gears, or (G)et out of the car, never to return...: ')
        choice = choice.upper()
        if choice == 'T':
            if self.engine == True:
                print('You turn the key to the of position, and stop the engine. ')
                self.engine = False
                exitChoice = input('Would you like to get out of the car? (Y)es / (N)o: ')
                exitChoice = exitChoice.upper()
                if exitChoice == 'Y':
                    print('You open the door, and get out of the car...Goodbye')
                elif exitChoice == 'N':
                    input('Press any button to continue...')
                    self.mainMenu()
                self.mainMenu()
            elif self.engine == False:
                print('You turn the key to the on position, and start the engine.')
                self.engine = True
                driveChoice = input('Would you like change gears, and drive? (Y)es / (N)o: ')
                driveChoice = driveChoice.upper()
                if driveChoice == 'Y':
                    self.trans(self.gear)
                elif driveChoice == 'N':
                    self.mainMenu()
        self.drive(self.engine, self.gear)

    def drive(self):

        if self.engine == False:
            print('The engine is currently off. ')
        elif self.engine == True:
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
            self.drive()
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

my_car = Car(2, 'P', False)

# my_car.drive(my_car.engine, my_car.gear)
# my_car.trans('P')
my_car.mainMenu()