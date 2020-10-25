from postTags import get_postTag_by_post_id, create_postTag, delete_postTag
from tags import get_single_tag, get_all_tags, create_tag
from login import handleLogin
from categories.request import create_category
from http.server import BaseHTTPRequestHandler, HTTPServer
from categories import get_all_categories, get_single_category
from users import get_all_users, get_single_user, create_user
from posts import get_posts_by_user_id, create_post, get_all_posts, get_single_post, delete_post, get_posts_by_category_id
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
        response = {}  
        parsed = self.parse_url(self.path)
        if len(parsed) == 2:
            (resource, id) = self.parse_url(self.path)

            if resource == "categories":
                if id is not None:
                    response = get_single_category(id)
                else:
                    response = get_all_categories()

            elif resource == "users":
                if id is not None:
                    response = get_single_user(id)
                else:
                    response = get_all_users()
            
            elif resource == "tags":
                if id is not None:
                    response = get_single_tag(id)
                else:
                    response = get_all_tags()  
            elif resource == "posts":
                if id is not None:
                    response = get_single_post(id)
                else:
                    response = get_all_posts()            
            # elif resource == "otherResource":
            # ...
            

        elif len(parsed) == 3:
            (resource,key,value ) = parsed
            
            if resource == "posts" and key == "user_id":
                response = get_posts_by_user_id(value)
            
            if resource == "post_tags" and key == "post_id":
                response = get_postTag_by_post_id(value)
            
            if resource == "posts" and key == "category_id":
                response = get_posts_by_category_id(value)
            # if key == "yourKey" and resource == "yourResource":
            #     response = get_yourResource_by_yourKey(value)
            # ...


        if response == False:
            self._set_headers(404)
        else:
            self._set_headers(200)

        self.wfile.write(f"{response}".encode())

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
        elif resource == "tags":
          new_item = create_tag(post_body)        
        elif resource == "post_tags":
          new_item = create_postTag(post_body)        
        elif resource == "login":
          new_item = handleLogin(post_body)
        elif resource == "users":
          new_item = create_user(post_body)
        elif resource == "posts":
            new_item = create_post(post_body)
        # elif resource == " ":
        #   new_item = yourCreate_handler(post_body)
        #...
        
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
        (resource, id) = self.parse_url(self.path)
        success = False

        if resource == "posts":
            success = delete_post(id)
        elif resource == "post_tags":
            success = delete_postTag(id)
        # elif resource == " ":
        #   success = delete_yourResource(id)
        # ...
     
        # successfully deleted the given resource with the given id
        if(success):
            self._set_headers(204) # 204 - No Content

        # the delete query affected zero rows in the database 
        # or the requested resource to delete doesn't exist / doesn't have a DELETE handler
        else:
            self._set_headers(404) # 404 - File Not Found

        self.wfile.write("".encode())

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()