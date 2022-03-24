import json

from flask import request

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    # return 'hello'
    return render_template(
        'View.html'
    )


@app.route('/popup')
def popup():
    # return 'hello'
    return render_template(
        'popup.html'
    )


@app.route('/add_flower', methods=["POST"])
def test():
    output = request.form
    print(output)  # This is the output that was stored in the JSON within the browser
    print(type(output))
    # result = json.loads(output)  # this converts the json output to a python dictionary
    # print(result)  # Printing the new dictionary
    # print(type(result))  # this shows the json converted as a python dictionary
    # return result

    return output


if __name__== "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')