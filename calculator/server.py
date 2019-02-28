import http.server
import socketserver
import logging
import re

#importo les funcions del rpn
from calculator.rpn import calculate_response 

def calculate_response_server(rpn_exp=None):
    if not is_valid_rpn_input(rpn_exp):
        result_rpn = "INVALID EXPRESSION"
    elif rpn_exp is not None:
        result_rpn = calculate_response(rpn_exp)
    else:
        result_rpn = ''
    return str(result_rpn)


def search_for_invalid_operator(str_input):

    ocurrences_plus = str_input.count("+")
    ocurrences_minus = str_input.count("-")
    ocurrences_mult = str_input.count("*")
    ocurrences_div = str_input.count("/")

    #usamos expresiones regulares del package re
    #r abans d'un str vol dir raw string, es perque no l'interpeti com a unicode: 
    #https://stackoverflow.com/questions/50504500/deprecationwarning-invalid-escape-sequence-what-to-use-instead-of-d

    #search for NumberOperator pattern  for example "5+", "6/" 
    finded_plus = re.findall(r"\d\++", str_input)
    finded_minus = re.findall(r"\d-+", str_input)
    finded_mult = re.findall(r"\d\*+", str_input)
    finded_div = re.findall(r"\d/+", str_input)

    print(finded_plus)
    print(finded_minus)
    print(finded_mult)
    print(finded_div)

    #not lista es como decir lista.empty()
    pattern1 = not finded_plus and not finded_minus and not finded_mult and not finded_div
    
    #search for OperatorNumber pattern  for example "+5", "/6" 
    finded_plus = re.findall(r"\+\d+", str_input)
    finded_minus = re.findall(r"-\d+", str_input)
    finded_mult = re.findall(r"\*\d+", str_input)
    finded_div = re.findall(r"/\d+", str_input)

    pattern2 = not finded_plus and not finded_minus and not finded_mult and not finded_div

    
    b = pattern1 and pattern2
    return not b



#Com que es una part de servidor (en realitat frontend) ho he implementat aqui, no a rpn.py
def is_valid_rpn_input(str_input):
    return not search_for_invalid_operator(str_input)

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
