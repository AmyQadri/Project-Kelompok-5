class Work:
    def __init__(self,driver_name,plate_number,cosh):
        self.driver_name = driver_name
        self.plate_number = plate_number 
        self.pickup_location = None
        self.destination_location = None
        self.distance = 0
        self.cosh = cosh 
        self.rating = None

    def cekinfodriver(self):
        print(f"name : {self.name} \nplate_number : {self.plate_number} \npickup_location : {self.pickup_location} \ndestination_location : {self.destination_location} \ncosh : {self.cosh} \nrating : {self.rating}")

    def PickUp(self):
        print(f"PickUp : {self.pickup_location}")

    def DropOff(self):
        print(f"DropOff : {self.destination_location}")

    def setPickUp(self,location):
        self.pickup_location = location

    def setDropOff(self,location):
        self.destination_location = location

    def calculate_distance(self):
        return self.distance