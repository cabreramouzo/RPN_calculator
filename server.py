import http.server
import socketserver
import logging

#importo les funcions del rpn
from rpn import calculate_response

def calculate_response_server(rpn_exp=None):
    if rpn_exp is not None:
        result_rpn = calculate_response(rpn_exp)
    else:
        result_rpn = ''
    return str(result_rpn)


log = logging.getLogger(__file__)

# https://en.wikipedia.org/wiki/Percent-encoding
def unescape_ops(s):
    # ! 	# 	    $ 	     & 	    ' 	    ( 	    ) 	    * 	    + 	    , 	    / 	    : 	    ; 	    = 	    ? 	   @ 	    [ 	    ]
    # %21 	%23 	%24 	%26 	%27 	%28 	%29 	%2A 	%2B 	%2C 	%2F 	%3A 	%3B 	%3D 	%3F 	%40 	%5B 	%5D
    return s.replace('+', ' ').replace('%2A', '*').replace('%2B', '+')
    #TODO: entendre la linea de dalt


def render_calc(calc_result=''):    
    response_text = f"""
            <html>
        <head>
            <link rel="stylesheet" href="style.css">
        </head>
    <body>
    <p>RPN Calculator</p>
            <table>
            <tr>
                <td colspan="4">
                    <form name="RPN_Calculator" action="/calculate" method="POST">
                    <input type="text" name="display" id="display" value="" />
                    <h3 style="color:white;">{calc_result}</h3>
                </td>
            </tr>
            <tr>
                    <td><input type="button" name="seven" value="7" onclick="RPN_Calculator.display.value += '7 '"></td>
                    <td><input type="button" name="eight" value="8" onclick="RPN_Calculator.display.value += '8 '"></td>
                    <td><input type="button" name="nine" value="9" onclick="RPN_Calculator.display.value += '9 '"></td>
                    <td><input type="button" class="operator" name="plus" value="+" onclick="RPN_Calculator.display.value += '+ '"></td>
            </tr>
            <tr>
                    <td><input type="button" name="four" value="4" onclick="RPN_Calculator.display.value += '4 '"></td>
                    <td><input type="button" name="five" value="5" onclick="RPN_Calculator.display.value += '5 '"></td>
                    <td><input type="button" name="six" value="6" onclick="RPN_Calculator.display.value += '6 '"></td>
                    <td><input type="button" class="operator" name="minus" value="-" onclick="RPN_Calculator.display.value += '- '"></td>
            </tr>
            <tr>
                    <td><input type="button" name="one" value="1" onclick="RPN_Calculator.display.value += '1 '"></td>
                    <td><input type="button" name="two" value="2" onclick="RPN_Calculator.display.value += '2 '"></td>
                    <td><input type="button" name="three" value="3" onclick="RPN_Calculator.display.value += '3 '"></td>
                    <td><input type="button" class="operator" name="times" value="x" onclick="RPN_Calculator.display.value += '* '"></td>
            </tr>
            <tr>
                    <td><input type="button" id="clear" name="clear" value="C" onclick="RPN_Calculator.display.value = '' "></td>
                    <td><input type="button" name="zero" value="0" onclick="RPN_Calculator.display.value += '0 ' "></td>                 
                    <td><input type="button" class="operator" name="div" value="/" onclick="RPN_Calculator.display.value += '/ '"></td>
                    <td><input type="submit" value="="></td>
                    </form>
            </tr>
            </table>        
        
    </body>
    </html>
            """
    return response_text



PORT = 8080
class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        print("Requested path: {}".format(self.path))
        if self.path == '/':
            response_text = render_calc()
            self._send_text_response(response_text)
            return            
        super().do_GET()

    def do_POST(self):
        """Begin serving a POST request. The request data is readable
        on a file-like object called self.rfile"""                
        rpn_exp = self._parse_rpn_input()
        calc_result = calculate_response_server(rpn_exp)
        response_text = render_calc(calc_result)
        self._send_text_response(response_text)

    def _send_text_response(self, text):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        response = bytearray(text, 'utf-8')
        self.wfile.write(response)

    def _parse_rpn_input(self):
        length = int(self.headers['Content-Length'])               
        all_bytes = self.rfile.read(length)
        payload = all_bytes.decode('ascii')        
        tuples = payload.split('&')        
        post = dict(t.split('=') for t in tuples)        
        rpn_exp = unescape_ops(post['display'])
        return rpn_exp

def main():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

if __name__ == '__main__':
    main()