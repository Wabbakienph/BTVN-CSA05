# - Tạo class `Point2D` với các thuộc tính: `x`, `y`
#     - Viết hàm tính khoang cách giữa 2 điểm 2D
#     - Viết hàm tính `__add__`, `__sub__` cho 2 điểm 2D

# - Tạo class `Point3D` kế thừa `Point2D` với các thuộc tính: `x`, `y`, `z`
#     - Viết hàm tính khoảng cách giữa 2 điểm 3D
#     - Viết hàm tính `__add__`, `__sub__` cho 2 điểm 3D
# Class Point2D
# Supperclass of Point3D
#  x, y
import math 
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def khoangcach(self, other):
        kc = math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return kc

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point2D(x,y)

    def __sub__(self,other):
        x = other.x - self.x
        y = other.y - self.y
        return Point2D(x,y)


# Class Point3D
# Point2D subclass
# x, y, z
class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
        
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point3D(x,y,z)

    def __sub__(self,other):
        x = other.x - self.x
        y = other.y - self.y
        z = other.z - self.z
        return Point3D(x,y,z)

    def khoangcach(self, other):
        kc = math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2)
        return kc
    
p2d1 = Point2D(1, 2)
p2d2 = Point2D(0, 4)
p3d1 = Point3D(1, 2, 3)
p3d2 = Point3D(5, 6, 7)

p2dadd = p2d1 + p2d2
p2dsub = p2d1 - p2d2
p3dadd = p3d1 + p3d2
p3dsub = p3d1 + p3d2
print(p2d1,'+',p2d2,'=',p2dadd)
print(p2d1,'-',p2d2,'=',p2dsub)
print(p3d1,'+',p3d2,'=',p3dadd)
print(p3d1,'-',p3d2,'=',p3dsub)
print(Point2D.khoangcach(p2d1,p2d2))
print(Point3D.khoangcach(p3d1,p3d2))
