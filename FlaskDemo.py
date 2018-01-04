from _init_ import app

@app.route('/')
def hello_world():
    return 'Hello Flask!'


if __name__ == '__main__':
    app.debug = app.config['DEBUG']
    app.run(host='0.0.0.0')
