from datetime import date, datetime, timedelta
from typing import List
from pytz import timezone
import re

from swagger_server.models.response_auditing_data import ResponseAuditingData

# Funciones de utilidad para el sistema completo.

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def format_uri_connection(connection):
    return connection["DRIVER"] \
        + "+" \
        + connection["LIBRARY"] \
        + "://" \
        + connection["USER"] \
        + ":" \
        + connection["PASSWORD"] \
        + "@" \
        + connection["HOST"] \
        + ":" \
        + connection["PORT"] \
        + "/" \
        + connection["DB"]


def filter_dict(dict, fields):
    # Filtra el diccionario entrante, retornando nuevo diccionario
    # sólo con los campos definidos y descartando los demás.

    filtered_dict = {}

    for key in dict:

        if key in fields:
            filtered_dict[key] = dict[key]

    return filtered_dict


def format_date(datetime):
    # Retorna una representación en String de una fecha/hora dada.

    return datetime.strftime(DATE_FORMAT)


def get_current_datetime():
    # Retorna la fecha actual en su correspondiente timezone

    return datetime.now(timezone('America/Guayaquil'))


def check_email(email):
    """
    Valida el email

    Args:
        email (String): correo electronico

    Returns:
        True or False si mail es valido o invalido
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False
    
def get_date_range(fecha_inicio=None, fecha_fin=None):
    if fecha_inicio and fecha_fin:
        return fecha_inicio, fecha_fin

    today = date.today()
    start = datetime.combine(today, datetime.min.time())
    end = start + timedelta(days=1)

    return start, end

def calculate_score_percentage(items: List[ResponseAuditingData]):
    """
    Calcula el porcentaje de cumplimiento.

    Reglas:
    - "si"  = 100%
    - "no"  = 0%
    - "n/a" = no se considera

    Parámetro:
        items: lista de diccionarios con la propiedad 'response'

    Retorna:
        float: porcentaje entre 0 y 100.
    """

    valid_answers = [
        item.response.strip().lower()
        for item in items
        if item.response and item.response.strip().lower() != "n/a"
    ]

    if not valid_answers:
        return 0.0

    positive_answers = sum(answer == "si" for answer in valid_answers)

    return round((positive_answers / len(valid_answers)) * 100, 2)
