#!/usr/bin/env python -W all

from __future__ import print_function

from schema import *
from util import *
from backend import *
from frontend import *

import server

import os
import sys

def main():
    events = []

    for root, dirs, files in os.walk("data"):
        for fileName in [os.path.join(root, f) for f in files]:
            fileExtension = os.path.splitext(os.path.basename(fileName))[1].lower()
            backend = getCalendarBackend(fileExtension.strip("."))

            if backend:
                cal = backend(fileName)
                events.extend(cal.events)

    server.startServer(iCalendarFrontend(events).getFile())

if __name__ == "__main__":
    main()
