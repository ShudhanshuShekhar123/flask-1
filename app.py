from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import render_template

app = Flask(__name__)
CORS(app, origins="*")

# //first part  
@app.route('/')
def hello_world():
    return 'Welcome to Homepage'

@app.route('/greet/Shudhanshu')
def hello_world1():
    return 'Hello! , Shudhanshu'

@app.route('/farewell/Shudhanshu')
def hello_world2():
    return 'GoodBye!,  Shudhanshu'


my_dictionary= {}
# //second part

@app.route('/create', methods=["POST"])
def create_entry():

    # if request.method == "POST":
        data = request.json
      
        key = data["key"]
        value = data["value"]
        
        my_dictionary[key] = value
     
        # print(my_dictionary)
  
      
        response_message = "Entry created successfully"
        return jsonify(response_message)  # Return plain text response
    # else:
        
    #      return render_template('create.html')
   

@app.route('/read')
def read():
    print(my_dictionary)
    return render_template('read.html')

@app.route('/delete', methods=["DELETE"])
def delete():
          item_id = request.args.get("id")
          print(item_id, "here")
          if item_id in my_dictionary:
           # Perform the delete operation by removing the item from the dictionary
           del my_dictionary[item_id]
    
    
          return jsonify({"message": "Item deleted successfully"})


@app.route('/getentries')
def getentry():
    print(my_dictionary)
    return jsonify(my_dictionary)


if __name__ == '__main__':
    app.run()