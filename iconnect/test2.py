# class DeviceExceptions(Exception):
#     def __init__(self, *args):
#         super(DeviceExceptions, self).__init__(*args)
#         print(*args)
#
#
# class WiFiNotFound(DeviceExceptions):
#     """No available wifi networks detected"""
#
#     def __init__(self, code):
#         if code > 139 and code < 150:
#             self.code = code
#         else:
#             self.code = None
#
# try:
#     raise WiFiNotFound(145)
# except WiFiNotFound as err:
#     code = err.code
#     print(code)

# class MyParentClass():
#     def __init__(self):
#         pass
#
#     def imprimir(self, msg):
#         print(msg)
#
# class SubClass(MyParentClass):
#     def __init__(self, msg):
#         self.imprimir(msg)
#
#     def imprimir(self, msg):
#         super(SubClass, self).imprimir(msg)
#
#
# a = SubClass('hola')


class DeviceExceptions(Exception):
    def __init__(self, code):
        self.code = code
        # super(DeviceExceptions, self).__init__(*args, **kwargs)

    def validate_code(self, range, code):
        return code if code >= range[0] and code <= range[1] else 444


class WiFiNotFound(DeviceExceptions):
    """No available wifi networks detected"""

    def __init__(self, code):
        super(WiFiNotFound, self).__init__(code)
        range = (140, 145)
        self.response = self.validate_code(range, code)


try:
    raise WiFiNotFound(200)
except WiFiNotFound as err:
    print(err.response)
