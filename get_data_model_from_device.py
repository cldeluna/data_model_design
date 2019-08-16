#!/usr/bin/python -tt
# Project: data_model_design
# Filename: get_data_model_from_device.py
# claudia
# PyCharm

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "2019-08-16"
__copyright__ = "Copyright (c) 2018 Claudia"
__license__ = "Python"

import argparse

import requests
import os


def save_to_file(yang_output_file, host, response):
    """
    Save the response text ino the provided output file in the local directory

    :param yang_output_file:
    :param response:
    :return:
    """
    cwd = os.getcwd()
    with open(yang_output_file, "w") as text_file:
        text_file.write(response.text)

    file_fp = os.path.join(cwd, yang_output_file)

    print(f"=== Saving YANG Model output from device {host} to file: \n\t{file_fp}\n")


def main():


    host = arguments.device
    port = arguments.port
    uname = arguments.username
    pwd = arguments.password

    url = f"https://{host}:{port}/restconf/data/Cisco-IOS-XE-native:native/"



    headers = {
        'Content-Type': "application/yang-data+json",
        'Accept': "application/yang-data+json",
        'Cache-Control': "no-cache",
        'Host': f"{host}:{port}",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
    }

    response = requests.get(url, auth=(uname, pwd), headers=headers, verify=False)

    print(response.text)

    yang_output_file = f"{host}_Read_IOSXE_All.json"

    save_to_file(yang_output_file, host, response)


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python get_data_model_from_device.py' ")

    parser.add_argument('-d', '--device', help='Device to query', action='store',
                        default="10.1.10.34")
    parser.add_argument('-p', '--port', help='Port', action='store',
                        default="443")
    parser.add_argument('-u', '--username', help='Username for device', action='store',
                        default="admin")
    parser.add_argument('-w', '--password', help='Password for device', action='store',
                        default="cisco123")
    arguments = parser.parse_args()

    main()







