from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class CalendarHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", CalendarHandler.contentType)
        self.end_headers()
        self.wfile.write(CalendarHandler.serverString)

    def log_message(self, format, *others):
        pass

def startServer(srv, mimetype):
    try:
        CalendarHandler.serverString = srv
        CalendarHandler.contentType = mimetype
        server = HTTPServer(("", 54321), CalendarHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()