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
        self.devices=[]
        if self.devices!=None:
            self.devices=devices[:]
            

    def __str__(self):
        flag=False
        x = "Outlet(["
        for i in range(len(self.devices)):
            if i!=len(self.devices)-1:
                x+=str(self.devices[i]) + ", "
            else:
                x+=str(self.devices[i]) + "])"
                flag=True
        if flag==False:
             x+="])"
        return x

    
    def __repr__(self):
        flag=False
        x = "Outlet(["
        for i in range(len(self.devices)):
            if i!=len(self.devices)-1:
                x+=str(self.devices[i]) + ", "
            else:
                x+=str(self.devices[i]) + "])"
                flag=True

        if flag==False:
             x+="])"
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
        x=0
        if self.devices==True:
            x+=self.devices
        return x
        
    def add_device(self, device):	
        return self.devices.append(device)

    def remove_device(self, name):
        flag=False
        for i in self.devices:
            if i.name==name:
                flag=True
                x = self.devices
                self.devices.remove(i)
                return x
        
        if flag==False:
            return None

    def turn_off_all(self):
        for i in self.devices:
            i.turn_off()

class Circuit:
    def __init__(self, outlets=None):
        self.outlets=[]
        if self.outlets!=None:
            self.outlets=outlets[:]

    def __str__(self):	
        x = "Circuit(["
        for i in range(len(self.outlets)):
            if i!=len(self.outlets)-1:
                x+=str(self.outlets[i]) + ", "
            else:
                x+=str(self.outlets[i]) + "])"
        return x

    def __repr__(self):
        x = "Circuit(["
        for i in range(len(self.outlets)):
            if i!=len(self.outlets)-1:
                x+=str(self.outlets[i]) + ", "
            else:
                x+=str(self.outlets[i]) + "])"
        return x

    def __eq__(self,other):
        if self.outlets==other.outlets:
            return True
        else:
            return False
    
    def add_outlet(self, outlet):
        return self.outlets.append(outlet)

    def max_watts(self):	
        result=0
        for i in self.outlets:
            result+=i.watts
        return result

    def watts_now(self):
        x=0
        if self.outlets==True:
            x+=self.outlets
        return x

    def turn_off_all(self):	
        for i in self.outlets:
            i.turn_off()
    