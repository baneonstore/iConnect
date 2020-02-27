# Copyright © 2020 baneon - MIT License
# See`LICENSE` included in the source distribution for details


import shlex
import subprocess

from exceptions import DeviceNotFound, WiFiNotFound
from .Code import code


class Detect(object):
    """docstring for ."""

    # TODO: You need to take arguments
    # <BANEON 2020-02-04 d:2w p:1>
    def __init__(self):
        pass


    def run_command(self, rule):
        """Execute a command.

        Helps format command-line for nmcli and provides support for detecting
        possible execution errors

        Args:
            rule (str): command-line for nmcli

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
        """Shows the active connection.

        Returns:
            tuple: It contains a list and the return value

        # DOCDO: Incorrect documentation
        # <BANEON 2020-02-04 d:1w p:1>
        Raises:
            WiFiNotFound: It is launched when it does not detect available Wi-Fi
                          networks

        """

        try:
            response = self.run_command(
                'nmcli -t -f NAME connection show --active')
            if response[0]:
                return response
            else:
                # TODO: You need your own exception
                # <BANEON 2020-02-04 d:1w p:2>
                raise WiFiNotFound(146)
        except WiFiNotFound as err:
            return code[err.code]

    # TODOC: Add documentation
    # <BANEON 2020-02-04 d:1w p:2>
    def enable_device(self, device):
        try:
            response = self.run_command(
                'nmcli dev set {} managed on'.format(device))
            if response[0]:
                return response
            else:
                raise DeviceNotFound(143)
        except DeviceNotFound as err:
            return code[err.code]

    # TODOC: Add documentation
    # <BANEON 2020-02-04 d:1w p:2>
    def disable_device(self, device):
        try:
            response = self.run_command(
                'nmcli dev set {} managed off'.format(device))
            if response[0]:
                return response
            else:
                raise DeviceNotFound(143)
        except DeviceNotFound as err:
            return code[err.code]

    # TODO: Implement
    # <BANEON 2020-02-04 d:1w p:2>
    def connect(self):
        pass
