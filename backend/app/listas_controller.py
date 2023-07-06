from flask import (
    Blueprint,
    request,
    jsonify,
    abort,
)

from .models import Lista
from config.local import config  

lista_bp = Blueprint('/listas', __name__)


@lista_bp.route('/listas', methods=['POST'])
def create_lista():
    error_lists = []
    returned_code = 201
    try:
        body = request.get_json()

        if 'name' not in body:
            error_lists.append('name is required')
        else:
            name = body['name']

        if len(error_lists) > 0:
            returned_code = 400
        else:
            lista = Lista(name)
            lista.insert()

    except Exception as e:
        print('e: ', e)
        returned_code = 500

    
    if returned_code == 400:
        return jsonify({
            'success': False,
            'errors': error_lists,
            'message': 'Error creando nuevo lista'
        }), returned_code
    elif returned_code == 500:
        abort(returned_code)
    else:
        return jsonify({
            'success': True,
            'lista_created_id': lista.id
        }), returned_code
    
@lista_bp.route('/listas', methods=['GET'])
def get_lista():
    returned_code = 200
    error_message = ''
    lista_list = []

    try:
        search_query = request.args.get('search', None)

        print("CANTIDAD TOTAL DE LISTAS", Lista.query.count())

        if (Lista.query.count() != 0):
            if search_query:
                listas = Lista.query.filter(
                    Lista.name.ilike(f'%{search_query}%')
                )
            else:
                listas = Lista.query.all()
            lista_list = [lista.serialize() for lista in listas]
        else:
            lista_list = []

    except Exception as e:
        print('e: ', e)
        returned_code = 500
        error_message = 'Error obteniendo listas'

    if returned_code != 200:
        return jsonify({
            'success': False,
            'message': error_message
        }), returned_code
    return jsonify({
        'success': True,
        'listas': lista_list
    }), returned_code
