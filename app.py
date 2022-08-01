from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    # return 'Hello World!!!'
    return render_template('index.html')


@app.route('/rand_string', methods = [ 'GET', 'POST'])
def rand_string():
    # return 'Hello World!!!'
    if request.method == 'POST':
        s = request.get_json(force = True)['random_string']
        return jsonify({'random_string':s, 'random number': random.randint(0, 100)})
    elif request.method == 'GET':
        s = request.args.get('random_string')
        return jsonify({'random_string':s, 'random number': random.randint(0, 100)})
        

if __name__ == '__main__':
    app.run(debug = True)