class Point:
    color = 'red'  # атребут класса или свойство
    circle =2

    def set_coords(self,t,y):
        self.u = t;
        self.z = y;


pt = Point()
pt.set_coords(4,6)
print(pt.__dict__)





