# import http.server, socketserver, threading, ctypes

# PORT = 8000

# class QuietHandler(http.server.SimpleHTTPRequestHandler):
#     def log_message(self, format, *args):
#         pass
#     def stop_threads():
#         assert 1==0
# def webserver():
#   with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
#       httpd.serve_forever()

# kool = threading.Thread(target=webserver,daemon=True)
# kool.start()