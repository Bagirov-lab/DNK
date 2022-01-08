import os
from flask import Flask, jsonify, request, render_template
from DNK import GEN, compare_gens
import pandas as pd

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return render_template('home.html')


@app.route('/compare', methods=['GET'])
def compare():

    try:
        test_json = request.get_json()
        test = pd.read_json(test_json, orient='records')

    except Exception as e:
        raise e

    query_params = request.args

    # Check that data is full
    if test.empty:
        return(jsonify({'error': 'No input data supplied'}))
    else:

        # Store Gen info
        Gens_list = []

        for i, row in test.iterrows():
            Gens_list.append(
                GEN(
                    os=None,
                    ox=None,
                    gn=row['gn'],
                    pe=None,
                    sv=None,
                    fasta=row['fasta']
                )
            )

        # Compare gens
        results = compare_gens(Gens_list)

        responses = jsonify(results)
        responses.status_code = 200

        return responses
