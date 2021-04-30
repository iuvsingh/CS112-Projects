class Device:
    def __init__(self, name, watts=100, on=False):
        self.name=name
        self.watts=watts
        self.on=on

    def __str__(self):
        if self.on==True:
            x='(+' + str(self.watts) + 'W: ' + self.name +')'
            return x
        else:
            x='(+0W: ' + self.name +')'
            return x

    def __repr__(self):
        x="Device('" + self.name + "', " + str(self.watts) + ", " + str(self.on) +")"
        return x

    def __eq__(self,other):
        if (self.name==other.name) and (self.watts==other.watts) and (self.on==other.on):
            return True
        else:
            return False

    def turn_on (self):	
        self.on=True

    def turn_off(self):
        self.on=False

    def toggle (self):
        if self.on==False:
            self.on=True
        else:
            self.on=False


class Outlet:
    def __init__(self, devices=None):
        if self.devices==None:
            self.devices=[]
        else:
            self.devices=devices

    def __str__(self):
        x = "Outlet(["
        for i in range(len(self.devices)):
            if i!=len(self.devices)-1:
                x+=self.devices + ", "
            else:
                x+=self.devices + "])"
        return x
    
    def __repr__(self):
        x = "Outlet(["
        for i in range(len(self.devices)):
            if i!=len(self.devices)-1:
                x+=self.devices + ", "
            else:
                x+=self.devices + "])"
        return x

    def __eq__(self,other):
        if (self.devices==other.devices):
            return True
        else:
            return False
            
    def max_watts(self):	
        result=0
        for i in self.devices:
            result+=i.watts
        return result

    def watts_now(self):
        x=self.device
        return x.watts
        
    def add_device(self, device):	
        devices.append(self.device)

    def remove_device(self, name):
        for device in self.devices:
            if device.name==name:
                return self.devices.remove(device)
        return None

    def turn_off_all(self):
        for device in self.devices:
            device.turn_off()