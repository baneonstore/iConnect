# Copyright © 2020 baneon - MIT License
# See`LICENSE.md` included in the source distribution for details


import shlex
import subprocess

from exceptions import DeviceNotFound, WiFiNotFound
from .Code import code


class Detect(object):
    """docstring for ."""


    def __init__(self):
        pass


    def run_command(self, rule):
        """Execute a command.

        Helps format command-line for nmcli and provides support for detecting
        possible execution errors

        Args:
            rule (str): command-line nmcli

        Returns:
            tuple: It contains a list and the return value

        """

        command = shlex.split(rule)
        sp = subprocess.run(command,
                            universal_newlines=True,
                            capture_output=True)
        if not sp.stderr:
            stdout = (sp.stdout.split(), sp.returncode)
            return stdout


    def show_devices(self):
        """Show available network devices.

        Returns a tuple containing a list of available network devices and a
        return value of the command "nmcli -t -f DEVICE device status"

        Returns:
            tuple: It contains a list and the return value

        Raises:
            DeviceNotFound: It is launched when it does not detect an available
                            device.

        """

        try:
            response = self.run_command('nmcli -t -f DEVICE device status')
            if response[0]:
                return response
            else:
                raise DeviceNotFound(144)
        except DeviceNotFound as err:
            print(code[err.code])


    def show_wifi(self):
        """Shows available Wi-Fi networks.

        Returns a tuple containing a list of network SSID and the return value
        of the command "nmcli -t -f SSID dev wifi"

        Returns:
            tuple: It contains a list and the return value

        Raises:
        WiFiNotFound: It is launched when it does not detect available Wi-Fi
                      networks

        """

        try:
            response = self.run_command('nmcli -t -f SSID dev wifi')
            if response[0]:
                return response
            else:
                raise WiFiNotFound(145)
        except WiFiNotFound as err:
            return code[err.code]


    def show_connection_active(self):
        try:
            response = self.run_command(
                'nmcli -t -f NAME connection show --active')
            if response[0]:
                return response
        except:
            pass


    def enable_device(self):
        pass


    def disable_device(self):
        pass
