# Copyright © 2020 baneon - MIT License
# See `LICENSE.md` included in the source distribution for details.


class DeviceExceptions(Exception):
    def __init__(self, *args, **kwargs):
        super(DeviceExceptions, self).__init__(*args, **kwargs)
        self.FAILED = 444

    def validate_code(self, range, code):
        if type(range) == tuple:
            return code \
                if code >= range[0] and code <= range[1] else self.FAILED
        else:
            return code \
                if code == range else self.FAILED


class DeviceNotFound(DeviceExceptions):
    """Couldn't find a device"""

    def __init__(self, code):
        super(DeviceNotFound, self).__init__()
        errors = 144
        self.code = self.validate_code(errors, code)


class WiFiNotFound(DeviceExceptions):
    """No available wifi networks detected"""

    def __init__(self, code):
        super(WiFiNotFound, self).__init__()
        errors = 145
        self.code = self.validate_code(errors, code)
