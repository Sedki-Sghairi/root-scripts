#!/usr/bin/env python3

import os
import shutil
import sys
import socket

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

