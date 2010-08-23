#!/usr/bin/env python -W all

from __future__ import print_function

from schema import *
from util import *
from backend import *

import server

import os
import sys

# TODO: better logging...

def main(dataPath="data"):
    events = []

    for root, dirs, files in os.walk(dataPath):
        for fileName in [os.path.join(root, f) for f in files]:
            fileExtension = os.path.splitext(os.path.basename(fileName))[1].lower()
            backend = getCalendarBackend(fileExtension.strip("."))

            if backend:
                cal = backend(fileName, dataPath)
                if cal.events:
                    events.extend(cal.events)

    print("Loaded {0} events.".format(len(events)))

    server.startServer(events)

if __name__ == "__main__":
    main()
