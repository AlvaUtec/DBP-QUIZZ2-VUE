from flask import (
    Blueprint,
    request,
    jsonify,
    abort,
)

from .models import Partido
from .models import Lista
from config.local import config  

partido_bp = Blueprint('/partidos', __name__)


@partido_bp.route('/partidos', methods=['POST'])
def create_partido():
    error_lists = []
    returned_code = 201
    try:
        body = request.get_json()

        if 'local' not in body:
            error_lists.append('local is required')
        else:
            local = body['local']

        if 'visitante' not in body:
            error_lists.append('visitante is required')
        else:
            visitante = body['visitante']
        
        if 'estadio' not in body:
            error_lists.append('estadio is required')
        else:
            estadio = body['estadio']

        if 'lista' not in body:
            error_lists.append('lista is required')
        else:
            listaKey = Lista.query.filter_by(nombre=body['lista']).first()
            if not listaKey:
                error_lists.append('Lista no encontrada')
            else:
                listaKey = listaKey.serialize().get('id')

        if len(error_lists) > 0:
            returned_code = 400
        else:
            partido = Partido(local, visitante, estadio, listaKey)
            partido_id = partido.insert()

    except Exception as e:
        print('e: ', e)
        returned_code = 500

    
    if returned_code == 400:
        return jsonify({
            'success': False,
            'errors': error_lists,
            'message': 'Error creando nuevo partido'
        }), returned_code
    elif returned_code == 500:
        abort(returned_code)
    else:
        return jsonify({
            'success': True,
            'partido_created_id': partido_id,
        }), returned_code
    
@partido_bp.route('/partidos', methods=['GET'])
def get_partido():
    returned_code = 200
    error_message = ''
    partido_list = []

    try:
        search_query = request.args.get('search', None)

        print('CANTIDAD TOTAL DE PARTIDOS: ', Partido.query.count())    

        if search_query:
            partidos = Partido.query.filter(
                Partido.local.ilike(f'%{search_query}%') | Partido.visitante.ilike(f'%{search_query}%')
            )

            partido_list = [partido.serialize() for partido in partidos]

        elif Partido.query.count() != 0:
            partidos = Partido.query.all()
            partido_list = [partido.serialize() for partido in partidos]

        else:
            partido_list = []

    except Exception as e:
        print('e: ', e)
        returned_code = 500
        error_message = 'Error obteniendo partidos'

    if returned_code != 200:
        return jsonify({
            'success': False,
            'message': error_message
        }), returned_code
    return jsonify({
        'success': True,
        'partidos': partido_list
    }), returned_code
