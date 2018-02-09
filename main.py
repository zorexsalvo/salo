from flask import Flask, request
app = Flask(__name__)


@app.route('/api/', methods=['GET', 'POST'])
def reverse():
    if request.method == 'GET':
        return '8-)'
    else:
        return request.data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
