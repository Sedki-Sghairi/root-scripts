#!/usr/bin/env python3

import os
import shutil
import sys
import socket

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return True
    return False    

def check_root_full():
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_no_network():
    try:
        socket.gethostbyname("www.sedkisghairi.com")
        return False
    except:
        return True
            
