from flask import Flask, request
import json


app = Flask(__name__)

@app.route('/api/', methods=['GET', 'POST'])
def reverse():
    if request.method == 'GET':
        return '8-)'
    else:
        parsed = json.loads(request.data)
        print(json.dumps(parsed, indent=4))
        return request.data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
