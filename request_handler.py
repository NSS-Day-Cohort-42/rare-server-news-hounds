from categories.request import create_category
from http.server import BaseHTTPRequestHandler, HTTPServer
from categories import get_all_categories, get_single_category
from users import get_all_users, get_single_user, create_user
import json


class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        if "?" in resource:

            param = resource.split("?")[1]  
            resource = resource.split("?")[0]  
            pair = param.split("=")  
            key = pair[0]  
            value = pair[1] 

            return (resource,key,value )

        else:
            id = None
            try:
                id = int(path_params[2])
            except IndexError:
                pass 
            except ValueError:
                pass  

            return (resource, id)

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)
        response = {}  

        parsed = self.parse_url(self.path)
        if len(parsed) == 2:
            (resource, id) = self.parse_url(self.path)

            if resource == "categories":
                if id is not None:
                    response = f"{get_single_category(id)}"
                else:
                    response = f"{get_all_categories()}"
            # elif resource == "otherResource":
            # ...
            elif resource == "users":
                if id is not None:
                    response = f"{get_single_user(id)}"
                else:
                    response = f"{get_all_users()}"

        elif len(parsed) == 3:
             (resource,key,value ) = parsed
            # if key == "yourKey" and resource == "yourResource":
            #     response = get_yourResource_by_yourKey(value)
            # ...

        self.wfile.write(response.encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        new_item = None

        # POST resource method logic 
        if resource == "categories":
          new_item = create_category(post_body)
        # elif resource == " ":
        #   new_item = yourCreate_handler(post_body)
        #...
        elif resource == "users":
          new_item = create_user(post_body)

        self.wfile.write(f"{new_item}".encode())

    def do_PUT(self):

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        success = False

        # if resource == "yourResource":
        #     success = update_yourResource(id, post_body)    
        #  ...

        if not success:
            self._set_headers(404)
        else:
            self._set_headers(204)

        self.wfile.write("".encode())

    def do_DELETE(self):
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        # if resource == " ":
        #   delete_yourResource(id)
        # elif resource == " ":
        #   delete_yourResource(id)
        # ...
     

        self.wfile.write("".encode())

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()