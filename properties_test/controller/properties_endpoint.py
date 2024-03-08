from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qsl
from database.db_connection import db_connection, filtered_search
from models.property import Property


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        db = db_connection()
        parsed_url = urlparse(self.path)
        print(parsed_url.query)
        data = parse_qsl(parsed_url.query)
        data = dict(data)
        
        if parsed_url.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello, world')   

        elif parsed_url.path == '/properties':

            try:
                filtered_properties = filtered_search(db,year= data.get('year', None), city= data.get('city', None), status= data.get('status', None))
            except ValueError as e :
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(bytes(e.__str__(), 'utf-8'))
                return

            property_list = []
            for result in filtered_properties:
                if result['address'] != '':

                    property = Property(result['id'], result['address'], result['city'],  result['price'],
                                        result['description'], result['year'], result['name'])
                    property_list.append(property.to_dict())
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(property_list).encode())

