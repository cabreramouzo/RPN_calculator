import http.server
import socketserver
import logging


log = logging.getLogger(__file__)

# https://en.wikipedia.org/wiki/Percent-encoding
def unescape_ops(s):
    # ! 	# 	    $ 	     & 	    ' 	    ( 	    ) 	    * 	    + 	    , 	    / 	    : 	    ; 	    = 	    ? 	   @ 	    [ 	    ]
    # %21 	%23 	%24 	%26 	%27 	%28 	%29 	%2A 	%2B 	%2C 	%2F 	%3A 	%3B 	%3D 	%3F 	%40 	%5B 	%5D
    return s.replace('+', ' ').replace('%2A', '*').replace('%2B', '+')

PORT = 8000
class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        print("Requested path: {}".format(self.path))
        if self.path == '/life':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            response = bytearray('The meaning of life is 42', 'utf-8')
            self.wfile.write(response)
            return
        super().do_GET()

    def do_POST(self):
        """Begin serving a POST request. The request data is readable
        on a file-like object called self.rfile"""

        print('message class: {}'.format(self.MessageClass))
        print('keys: {}'.format('\n'.join(self.headers.keys())))
        length = int(self.headers['Content-Length'])
        print(f'length: {length}')
        print('content-type: {}'.format(self.headers['Content-Type']))
        all_bytes = self.rfile.read(length)
        payload = all_bytes.decode('ascii')
        print('all_bytes: {}'.format(all_bytes.decode('ascii')))
        tuples = payload.split('&')        
        post = dict(t.split('=') for t in tuples)        
        print(f'post: {post}')
        rpn_exp = unescape_ops(post['display'])
        print(rpn_exp)
        # print(self.rfile)
        # self.rfile

        




        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        #replico la pagina de la UI original LOL
        resp = """
        <html>
    <head>
    </head>
<body>
<p>RPN Calculator</p>
        <table>
           <tr>
              <td colspan="4">
                  <form name="RPN_Calculator" action="/calculate" method="POST">
                 <input type="text" name="display" id="display" value="" />
                 <td><input type="submit" value="="></td>
                </form>
              </td>
           </tr>
           <tr>
                <td><input type="button" name="seven" value="7" onclick="RPN_Calculator.display.value += '7'"></td>
                <td><input type="button" name="eight" value="8" onclick="RPN_Calculator.display.value += '8'"></td>
                <td><input type="button" name="nine" value="9" onclick="RPN_Calculator.display.value += '9'"></td>
                <td><input type="button" class="operator" name="plus" value="+" onclick="RPN_Calculator.display.value += '+'"></td>
          </tr>
          <tr>
                 <td><input type="button" name="four" value="4" onclick="RPN_Calculator.display.value += '4'"></td>
                 <td><input type="button" name="five" value="5" onclick="RPN_Calculator.display.value += '5'"></td>
                 <td><input type="button" name="six" value="6" onclick="RPN_Calculator.display.value += '6'"></td>
                 <td><input type="button" class="operator" name="minus" value="-" onclick="RPN_Calculator.display.value += '-'"></td>
          </tr>
          <tr>
                <td><input type="button" name="one" value="1" onclick="RPN_Calculator.display.value += '1'"></td>
                <td><input type="button" name="two" value="2" onclick="RPN_Calculator.display.value += '2'"></td>
                <td><input type="button" name="three" value="3" onclick="RPN_Calculator.display.value += '3'"></td>
                <td><input type="button" class="operator" name="times" value="x" onclick="RPN_Calculator.display.value += '*'"></td>
          </tr>
          <tr>
                 <td><input type="button" id="clear" name="clear" value="C" onclick="RPN_Calculator.display.value = '' "></td>
                 <td><input type="button" name="zero" value="0" onclick="RPN_Calculator.display.value += '0' "></td>                 
                 <td><input type="button" class="operator" name="div" value="/" onclick="RPN_Calculator.display.value += '/'"></td>
           </tr>
        </table>        
     
</body>
</html>
        """
        response = bytearray(resp, 'utf-8')
        self.wfile.write(response)
        return

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
