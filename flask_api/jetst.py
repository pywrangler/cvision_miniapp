from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.config['SECRET_KEY'] = "my_test_key"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/get_token/', methods=['POST'])
@cross_origin()
def get_token():
    token = jwt.encode({
        'image_id' = '1',
        'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds = 60)
    },
    app.config['SECRET_KEY'])
    return jsonify({'token' : token.decode('utf-8')})


@app.route('/upload_image/', methods=['POST'])
@cross_origin()
def upload_image():
    print "request= ",request
    content = request.get_json()
    print "content=",content
    #image_file = content['redirect']
    #print 'image=',image_file
    return "Image Upload Success"

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)