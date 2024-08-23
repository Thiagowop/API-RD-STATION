from flask import Blueprint, render_template, jsonify
from app.database import extract_data_from_database
from app.rd_station import transform_data_for_rd_station, integrate_data_into_rd_station

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', message="")

@main.route('/integrate', methods=['POST'])
def integrate_data():
    data = extract_data_from_database()
    if data:
        transformed_data = transform_data_for_rd_station(data)
        integrate_data_into_rd_station(transformed_data)
        message = 'Dados integrados com sucesso no RD Station Marketing'
    else:
        message = 'Falha ao integrar dados no RD Station Marketing'
    
    return render_template('index.html', message=message)
