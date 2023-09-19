from flask import Flask, request, jsonify

app = Flask(__name__)

nums= [10,20,30,40,50]

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/evenodd<int:num>")  # by default get method
def evenodd(num):
    status= None
    if num%2==0:
        status = "Even"
    else:
        status = "Odd"

    return jsonify({'status':status})

# Route for data generate or data enter
@app.route("/addnum", methods=['POST'])
def addnum():
    request_data = request.get_json()
    print(request_data['num'])
    nums.append(request_data['num'])
    

@app.route("/showlist")
def showlist():
    return jsonify({'list':nums})

if __name__ == "__main__":
    app.run(debug=True)  # run app in debug mode on
    

