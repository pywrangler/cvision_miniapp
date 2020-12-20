from flask import Flask, request, jsonify,flash,redirect,url_for
from flask_cors import CORS, cross_origin
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import datetime
from functools import wraps
import jwt,os
UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}
SECRET_KEY = 'myjwtsecret'
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

uid = 0
limiter = Limiter(
    app,
    key_func=get_remote_address,
)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = data['public_id']
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    return jsonify({'Authentication' : 'Success'})

def generateUserId():
    global uid
    uid += 1
    return str(uid)
@app.route('/get_new_token')
def get_new_token():
    auth = request.authorization
    token = jwt.encode({'public_id' : generateUserId(), 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
    return jsonify({'token' : token.decode('UTF-8')})

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route('/upload_image', methods=['GET', 'POST'])
@cross_origin()
@token_required
@limiter.limit("5 per minute")
def upload_image(current_user):
    print ('current_user=',current_user)
    if request.method == 'POST':
        #print (request.files['file'])
        # # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return "no file received"
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            #flash('No selected file')
            return "no filename"
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'error'

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)