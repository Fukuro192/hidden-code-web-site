from flask import Flask, Response, send_from_directory

app = Flask('app', static_url_path='')

@app.route('/style.css')
def stylecss():
    return send_from_directory('.', path='style.css')

@app.route('/omaemona.jpeg')
def image():
    return send_from_directory('.', path='omaemona.jpeg')

@app.route('/')
def hello_world():
    response = Response()
    response.headers['link'] = '<style.css>; rel=stylesheet;'
    response.headers['Refresh'] = '5; url=https://www.youtube.com/watch?v=L1GeSlydcrM'
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)