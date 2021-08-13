from flask import Flask, request



# create the Flask app

app = Flask(__name__)



@app.route('/', methods=['GET','POST'])

def handle_request():

    #request_data = request.get_json()

    result = int(request.form['value']) * 2



    return str(result)





if __name__ == '__main__':

    # run app in debug mode on port 5000

    app.run(host = "0.0.0.0", debug = True, port = 5000)