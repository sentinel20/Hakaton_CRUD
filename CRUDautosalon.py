# import json

# class Cars():
#     FILE = 'jsoncarsdb/carsdata.json'
#     id = 0

#     def __init__(self, make, model, year, engin_volume, color, body, miles, price, likes, comments):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.engin_volume = engin_volume
#         self.color = color
#         self.body = body
#         self.miles = miles
#         self.price = price
#         self.likes = likes
#         self.comments = comments
#         self.create_data()
#     @classmethod
#     def get_id(cls):
#         cls.id += 1
#         return cls.id
#     @classmethod
#     def get_data(cls):
#         with open(cls.FILE) as file:
#             return json.load(file)
    
#     @staticmethod
#     def get_one_car(data, id):
#         vehicle = list(filter(lambda x: x['id'] == id, data))
#         if not vehicle:
#             return 'No such car!'
#         return vehicle[0]
#     @classmethod
#     def send_data_to_json(cls, data):
#         with open(cls.FILE, 'w') as file:
#             json.dump(data, file)

#     def create_data(self):
#         data = Cars.get_data()
#         vehicle = {
#             'id': Cars.get_id(),
#             'make': self.make,
#             'model': self.model,
#             'year': self.year,
#             'engine': self.engin_volume,
#             'color': self.color,
#             'body': self.body,
#             'miles': self.miles,
#             'price': self.price,
#             'likes': self.likes,
#             'Comments': self.comments
#         }
#         data.append(vehicle)

#         with open(Cars.FILE, 'w') as file:
#             json.dump(data, file)

#         return {'Status': '201', 'msg': vehicle}

#     @classmethod
#     def retrieve_data(cls, id):
#         data = cls.get_data()
#         vehicle = cls.get_one_car(data, id)
#         return vehicle
#     @classmethod
#     def update_data(cls, id, **kwargs):
#         data = cls.get_data()
#         vehicle = cls.get_one_car(data, id)
#         if type(vehicle) != dict:
#             return vehicle
#         index = data.index(vehicle)
#         data[index].update(**kwargs)
#         cls.send_data_to_json(data)
#         return {'Status': '200', 'msg': 'Updated'}
#     @classmethod
#     def delete_data(cls, id):
#         data = cls.get_data()
#         vehicle = cls.get_one_car(data, id)
#         if type(vehicle) != dict:
#             return vehicle
#         index = data.index(vehicle)
#         data.pop(index)    
#         cls.send_data_to_json(data)
#         return {'Status': '204', 'msg': 'Deleted'}

# with open(Cars.FILE, 'w') as file:
#     json.dump([], file)

# car1 = Cars('BMW', '5-series', 2022, 5.5, 'black', 'sedan', 0, 50000.00, 5, 'Very good car!!')
# car2 = Cars('AUDI', 'E-Tron', 2022, 5.0, 'silver', 'SUV', 10, 95000.00, 30, 'Beautifull car!!')
# car3 = Cars('Mercedes-Benz', 'CLS-500', 2021, 6.3, 'white', 'cupe', 100, 71000.00, 11, 'Very fast car!!!')

# print('All vehicles:\n', Cars.get_data())
# print('\n', Cars.retrieve_data(3))
# print(Cars.update_data(1, model = '3-series'))
# print(Cars.retrieve_data(3))
# print(Cars.delete_data(3))
# print('All vehicles:\n', Cars.get_data())
