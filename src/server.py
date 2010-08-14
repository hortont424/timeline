from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class CalendarHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/calendar")
        self.end_headers()
        self.wfile.write(CalendarHandler.serverString)

def startServer(srv):
    try:
        CalendarHandler.serverString = srv
        server = HTTPServer(("", 54321), CalendarHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()