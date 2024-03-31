class Work:
    def __init__(self,driver_name,plate_number):
        self.driver_name = driver_name
        self.plate_number = plate_number 
        self.pickup_location = None
        self.destination_location = None
        self.distance = 0
        self.cosh = 0

    def cekinfodriver(self):
        print(f"name : {self.name} \nplate_number : {self.plate_number} \npickup_location : {self.pickup_location} \ndestination_location : {self.destination_location} \ncosh : {self.cosh} \nrating : {self.rating}")

    def PickUp(self):
        Pickup_Location = int(input("Masukan Lokasi Pick Up :"))
        self.pickup_location = Pickup_Location

    def DropOff(self):
        DropOff_Location = int(input("Masukan Lokasi Drop Off :"))
        self.destination_location = DropOff_Location

    def Distance(self):
        distance = self.pickup_location + self.destination_location
        self.distance = distance
        return distance

        
        