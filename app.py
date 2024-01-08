from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Merhaba, Docker ile Flask Uygulamasina Hoş Geldiniz!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')