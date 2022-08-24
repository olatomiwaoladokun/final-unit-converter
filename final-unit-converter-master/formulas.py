

class Meter:
    def meter_meter(self, x): 
        y = x*1
        return y
    def meter_kilometer(self, x):
        y = x*0.001
        return y
    def meter_centimeter(self, x): 
        y = x*100
        return y
    def meter_milimeter(self, x): 
        y = x*1000
        return y
    def meter_yard(self, x): 
        y = x*1.0936132983
        return y
    def meter_foot(self, x):
        y = x*3.280839895
        return y  

class Kilometer:
    def kilometer_meter(self, x):
        y = x*1000
        return y
    def kilometer_kilometer(self, x):
        y = x*1
        return y
    def kilometer_centimeter(self, x): 
        y = x*100000
        return y
    def kilometer_milimeter(self, x):
        y = x*1000000
        return y
    def  kilometer_yard(self, x):
        y = x* 1093.6132983
        return y
    def kilometer_foot(self, x):
        y = x* 3280.839895
        return y


class Centimeter:
    def cetimeter_meter(self, x):
        y = x*0.01
        return y

    def centimeter_kilometer(self, x): 
        y = x*0.00001
        return y
    def centimeter_centimeter(self, x):
        y = x*1
        return y
    def centimeter_milimemter(self, x):
        y = x*10
        return y
    def centimeter_yard(self, x):
        y = x*0.010936133
        return y
    def centimeter_foot(self, x):
        y = x*0.032808399
        return y

class Milimeter:
    def milimeter_meter(self, x):
        y = x*0.001
        return y
    def milimeter_kilometer(self, x):
        y = x*0.000001
        return y
    def milimeter_centimeter(self, x):
        y = x*0.1
        return y
    def milimeter_milimeter(self, x):
        y = x*1
        return y
    def milimeter_yard(self, x):
        y = x*0.0010936133
        return y
    def milimeter_foot(self, x):
        y = 0.0032808399
        return y


class Yard:
    def yard_meter(self, x):
        y = x*0.9144
        return y 
    def yard_kilometer(self, x):
        y = x*0.0009144
        return y
    def yard_centimeter(self, x):
        y = x*91.44
        return y
    def yard_milimeter(self, x):
        y = x*914.4
        return y
    def yard_yard(self, x):
        y = x*1
        return y        
    def yard_foot(self, x):
        y = x*3
        return y


class Foot:
    def foot_meter(self, x):
        y = x*0.3048
        return y
    def foot_kilometer(self, x):
        y = x*0.0003048
        return y
    def foot_centimeter(self, x):
        y = x*30.48
        return y
    def foot_milimeter(self, x):
        y = x*304.8
        return y
    def foot_yard(self, x):
        y = x*0.3333333333
        return y
    def foot_foot(self, x):
        y = x*1
        return y



# a = meter.meter_meter(2)
# print(a)      