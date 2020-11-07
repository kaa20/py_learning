import os
import csv

"""Parse a csv file and create list of Car-objects"""

#Base class for all cars
class CarBase:

    def __init__(self, car_type, photo_file_name, brand, carrying):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)


#Passenger car class
class Car(CarBase):

    def __init__(self, car_type, photo_file_name, brand, carrying, passenger_seats_count):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.passenger_seats_count = passenger_seats_count


#Truck car class
class Truck(CarBase):

    def __init__(self, car_type, photo_file_name, brand, carrying, body_whl):
        super().__init__(car_type, photo_file_name, brand, carrying)
        list_whl = self._parser_whl(body_whl)
        self.body_width = list_whl[0]
        self.body_height = list_whl[1]
        self.body_length = list_whl[2]

    def _parser_whl(self, body_whl):
        list_whl = []
        zero_whl = [0, 0, 0]
        tmp_list = body_whl.split('x')
        if len(tmp_list) != 3:
            return zero_whl
        try:
            for item in tmp_list:
                f_item = float(item)
                if f_item < 0:
                    return zero_whl
                list_whl.append(float(item))
        except ValueError:
            return zero_whl
        return list_whl

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length



#Special car class
class SpecMachine(CarBase):

    def __init__(self, car_type, photo_file_name, brand, carrying, extra):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.extra = extra

#getter cars list
def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        list_title = next(reader) # skipping the title
        for row in reader:
            car_attr = {}
            for i in range(len(list_title)):
                car_attr[list_title[i]] = row[i]
            print(car_attr)
            print('{}'.format())
            #if not isinstance(body_whl, str):
            #car_list.append(row)
            #print(row)
    return car_list