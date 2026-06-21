# Q15. Create Device, Camera, Phone and SmartPhone classes. Demonstrate runtime polymorphism.
print("Q15. Create Device, Camera, Phone and SmartPhone classes. Demonstrate runtime polymorphism.")
class Device:
    def operate(self):
        print("Device operating.")

class Camera(Device):
    def operate(self):
        print("Camera taking photos.")

class Phone(Device):
    def operate(self):
        print("Phone making calls.")

class SmartPhone(Device):
    def operate(self):
        print("SmartPhone calling and taking photos.")

devices = [Camera(), Phone(), SmartPhone()]

for d in devices:
    d.operate()