from flask import Flask, request
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

json_data = {
    "authorizeUrl":"API_ENDPOINT_URL_HERE",
    "response_type":"ecobeePin",
    "scope":"smartWrite"
}

url = json_data['authorizeUrl']
request_params = "?response_type=" + json_data["response_type"] + "&scope="+ json_data["scope"] + "&client_id="
@app.route('/getData', methods=['GET', 'POST'])
def getData():
    # get content from the request
    content = request.json
    appKey = content['appKey']

    response = requests.get(url + request_params + appKey, verify=False)
    data = response.json()
    return json.dumps(data)



if __name__ == "__main__":
    app.run(debug=True)