from flask import Response, Flask, request
import requests
import json
from config import get_url, get_argument
from werkzeug.exceptions import abort
# reference - https://medium.com/customorchestrator/simple-reverse-proxy-server-using-flask-936087ce0afb

app = Flask(__name__)

wrong_route = False;
no_input = False


@app.route('/', defaults={'path': ''}, methods=["GET"])
@app.route('/<path:path>', methods=["GET"])
def proxy(path):
    # path will be whole way up to x
    if not request.args.get('x'):
        global no_input
        global wrong_route
        no_input = True
        wrong_route = False
        abort(404)

    elif request.method == 'GET':
        p = path.split('/')
        function = p[0]
        url = get_url(function)
        if url == "error":
            wrong_route = True
            no_input = False
            abort(404)
        else:
            user_input = request.args.get('x')
            arg = get_argument(function)

            if arg == "":  # need this as average_word_length does not use ?x= it appends the arg after the /
                new_path = url + "/" + user_input
            else:
                new_path = url + "/?" + arg + "=" + user_input
            r = requests.get(new_path)
            excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
            headers = [(name, value) for (name, value) in r.raw.headers.items() if name.lower() not in excluded_headers]
            response = Response(r.content, r.status_code, headers)
            response.headers['Content-Type'] = 'application/json'
            response.headers['Access-Control-Allow-Origin'] = '*'
            return response


@app.errorhandler(404)
def route_error_handling(error):
    if no_input:
        error_text = "No Input Parameters Provided"
    elif wrong_route:
        error_text = "The specified route is not a re-directable function"
    r = {
        "String": error_text,
        "answer": 0,
        "Status Code": "404",
        "Errors": "true"
    }
    status = 404
    reply = json.dumps(r)
    response = Response(response=reply, status=status, mimetype="application/json")
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
