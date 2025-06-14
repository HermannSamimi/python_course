from flask import Flask
import json


def first_names():
    with open("/Users/hermann/Documents/Python Course/data/json_file.json", "r") as file:
        data = json.load(file)

        for i in data:
            firstname = data[i]["firstname"]
            print(firstname)

    return "Done"

print(first_names())



# --------------------------------------------- Flask Web Framework  ---------------------------------------------
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, Flask is running!"


@app.route('/firsnames')
def get_first_names():
    with open("/Users/hermann/Documents/Python Course/data/json_file.json", "r") as file:
        data = json.load(file)

        firstnames = [data[i]["firstname"] for i in data]
    
    return {"firstnames": firstnames}
    



if __name__ == '__main__':
    app.run(debug=True)

# ---------------------------------------------------------------------------------------------------------------

