#%%
from http.server import HTTPServer

from controller.properties_endpoint import SimpleHTTPRequestHandler


def run(server_class: HTTPServer = HTTPServer, handler_class: SimpleHTTPRequestHandler = SimpleHTTPRequestHandler, port: int = 8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
# %%
