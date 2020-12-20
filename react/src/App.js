
import React, { Component } from 'react';
import './App.css';
 
class App extends Component {
  constructor(props) {
    super(props);
      this.state = {
        imgToUpload: null,
        token: null
      }
  };
  componentDidMount() {
    fetch('http://0.0.0.0:5000/get_new_token', { 
  method: 'GET'
})
.then(function(response) { return response.json(); })
.then(function(json) {
  console.log(json.token);
  return json.token;
})
.then((jtoken) =>
  this.setState({
    token:jtoken
  }))}

render() {
  
  return (

    <div className="center">
        <form method="post" id ="iPick-Form" action="#" encType="multipart/form-data">
              <div className="iPick-div-one">
                <label>Browse Image </label>
                <input type="file" name="img-file" className="iPick-finput" onChange={this.iPickOnChange} accept="image/*"/>
              </div>
              <div className="iPick-upld-btn-div">
              <button width="100%" type="button" className="iPick-btn" onClick={this.uploadImage.bind(this)}>Upload Image</button>
              </div>
          </form>
</div>
  );
}

iPickOnChange=event=>{
  var picked_img = event.target.files[0];
  var formData = new FormData();
  formData.append('file', event.target.files[0]);
  console.log(picked_img);
   this.setState({
    imgToUpload: formData,
    });
}


async postData(url = '', _data = FormData) {

  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'omit', // include, *same-origin, omit
    headers: {
      'x-access-token':this.state.token
      //'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    body:_data,
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
  });
  return response.json(); // parses JSON response into native JavaScript objects
}

 uploadImage() {
   console.log('the image file', this.state.imgToUpload);
   
  this.postData('http://0.0.0.0:5000/upload_image', this.state.imgToUpload )
  .then(data => {
    console.log(data); // JSON data parsed by `data.json()` call
  });
}

  
};
export default App;