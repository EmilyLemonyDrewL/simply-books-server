import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from views import get_books, get_single_book, get_authors, get_single_author, create_author, create_book, update_author, update_book, delete_author, delete_book

class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split("/")
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    # Here's a class function
    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handles GET requests to the server
        """
        # Set the response code to 'Ok'
        self._set_headers(200)
        response = {}
        parsed = self.parse_url(self.path)

        if '?' not in self.path:
            ( resource, id ) = parsed

            if resource == "books":
                if id is not None:
                    response = get_single_book(id)

                else:
                    response = get_books()

            if resource == "authors":
                if id is not None:
                    response = get_single_author(id)

                else:
                    response = get_authors()

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server
        """
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        (resource, id) = self.parse_url(self.path)

        new_book = None
        new_author = None

        if resource == "books":
            new_book = create_book(post_body)

        if resource == "authors":
            new_author = create_author(post_body)

        if new_book is not None:
            self.wfile.write(json.dumps(new_book).encode())
        if new_author is not None:
            self.wfile.write(json.dumps(new_author).encode())

    def do_PUT(self):
        """Handles PUT requests to the server
        """
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)
        success = False

        if resource == "books":
            update_book(id, post_body)

        if resource == "authors":
            update_author(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

    def do_DELETE(self):
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        if resource == "books":
            delete_book(id)

        if resource == "authors":
            delete_author(id)

        self.wfile.write("".encode())

def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
