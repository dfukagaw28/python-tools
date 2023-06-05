"""
Show system information
"""

import datetime
import os
import platform
import psutil
import sys


def bytes2gib(x):
    return f'{x/(1<<30):.1f}GiB'


def print_system_info():
    print('Local Time:', datetime.datetime.now())
    print('Platform:', platform.platform())
    try:
        info = platform.freedesktop_os_release()
        print('Linux distro:', info['PRETTY_NAME'])
    except:
        pass
    print('Host:', platform.uname().node)
    print('Python Version:', sys.version)
    print('Python Executable:', sys.executable)
    print('Current Working Directory:', os.getcwd())

    cpufreq = psutil.cpu_freq()
    print(
        f'CPU: Phys:{psutil.cpu_count(logical=False)} Log:{psutil.cpu_count(logical=True)}'
        f' Freq:{cpufreq.current/1000:.2f}Ghz'
    )

    svmem = psutil.virtual_memory()
    print(f'Memory: Total:{bytes2gib(svmem.total)} (Available:{bytes2gib(svmem.available)})')
    swap = psutil.swap_memory()
    print(f'  Swap: Total:{bytes2gib(swap.total)} (Free:{bytes2gib(swap.free)})')

    sdu = psutil.disk_usage('.')
    print(f'Disk: Total:{bytes2gib(sdu.total)} (Free:{bytes2gib(sdu.free)})')

    ipv4s = []
    for interface_name, interface_addresses in psutil.net_if_addrs().items():
        ipv4s += [addr.address for addr in interface_addresses if str(addr.family) == 'AddressFamily.AF_INET']
    print('Network:', *ipv4s)


if __name__ == '__main__':
    print_system_info()
