from abc import ABC, abstractmethod

class Calculation(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Robot(Calculation):  
    def area(self, height, width):  
        return height * width  
    def perimeter(self, height, width):  
        return (height + width) * 2  


# correct solution 
class Calculation(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area_triangle(self):
        pass
    
class Robot:  
    def area(self, height, width):  
        return height * width  
    def perimeter(self, height, width):  
        return (height + width) * 2   
    def area_triangle(self, side, height):  
        return (side * height) * 0.5


# wrong decision
class Calculation(ABC):
    @abstractmethod
    def area_triangle(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area_triangle(self):
        pass
    
class Robot:    
    def perimeter(self, height, width):  
        return (height + width) * 2   
    def area_triangle(self, side, height):  
        return (side * height) * 0.5
