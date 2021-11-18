from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def index():
   return "Hello World"

@app.route('/login', methods=['POST', 'GET'])
def login():
    default = {
        'username': 'admin',
        'password': 'admin'
    }
    if request.method == 'GET':
        print(request.args.get)
        if request.args.get('username') == default['username'] and request.args.get('password') == default['password']:
            return 'Login success'
        else :
            return 'Login failed'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return "Invalid username/password"

if __name__ == '__main__':
  app.run(debug=True)