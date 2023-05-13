import pickle
import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/prophetv3', methods=['POST'])
def prophet3():

    m2 = pickle.load(open('Prophet.pckl', 'rb'))
    mes = int(request.json['mes'])

    future2 = m2.make_future_dataframe(periods=mes, freq='MS')
    forecast2 = m2.predict(future2)

    data = forecast2[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-1:]

    response = data.to_json(orient='records', date_format='iso')
    parsed = json.loads(response)
    return parsed


if __name__ == '__main__':
    app.run(debug=False, port=4100)
