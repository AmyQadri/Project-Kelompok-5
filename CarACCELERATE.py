    def start_engine (self):
        self.status_engine = True

    def stop_engine (self):
        self.status_engine = False

    def accelerate (self,speed):
        if self.status_engine == True:
            self.speed = speed
            if speed > 0:
                self.position = (self.position[0] + speed, self.position[1])
            else:
                self.position = (self.position[0], self.position[1] - speed)
        else:
            print("Engine must be running to accelerate")