from __future__ import print_function

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from frontend import *

class CalendarHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        frontend, contentType = getCalendarFrontend(self.path.lstrip("/"))

        if not frontend:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("404: File not found.")
            return

        serverString = frontend(CalendarHandler.events).getFile()

        self.send_response(200)
        self.send_header("Content-type", contentType)
        self.end_headers()
        self.wfile.write(serverString)

def startServer(events):
    CalendarHandler.events = events
    server = HTTPServer(("", 54321), CalendarHandler)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()