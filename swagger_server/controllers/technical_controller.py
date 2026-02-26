from timeit import default_timer

import connexion

from swagger_server.exception.custom_error_exception import CustomAPIException
from swagger_server.models.generic_response import GenericResponse  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
from swagger_server.models.tehnical_data import TehnicalData  # noqa: E501
from swagger_server import util
from flask import jsonify, request, send_file
from flask.views import MethodView

from loguru import logger
import json

from swagger_server.repository.technical_repository import TechnicalRepository
from swagger_server.uses_cases.technical_use_case import TechnicalUseCase
from swagger_server.utils.transactions.transaction import generate_internal_transaction_id

class TechnicalView(MethodView):
    def __init__(self):
        self.logger = logger
        technical_control_repository = TechnicalRepository()
        self.logbook_use_case = TechnicalUseCase(technical_control_repository)

    def post_technical(self, technical_data=None, channel=None, external_transaction_id=None):  # noqa: E501
        """Guarda el control tecnico en la base de datos.

        Guardado de control tecnico de ingreso # noqa: E501

        :param technical_data: 
        :type technical_data: dict | bytes
        :param channel: 
        :type channel: str
        :param external_transaction_id: 
        :type external_transaction_id: str

        :rtype: GenericResponse
        """
        internal_process = (None, None)
        function_name = "post_logbook_entry"
        response = {}
        status_code = 500
        try:
            if request.content_type.startswith("multipart/form-data"):
                start_time = default_timer()
                internal_transaction_id = str(generate_internal_transaction_id())

                logbook_file = request.files.get("logbook_entry")
                if not logbook_file:
                    raise CustomAPIException("Campo logbook_entry no enviado", 400)

                logbook_raw = logbook_file.read().decode("utf-8")
                logbook_dict = json.loads(logbook_raw)

                external_transaction_id = logbook_dict['external_transaction_id']
                internal_process = (internal_transaction_id, external_transaction_id)
                response["internal_transaction_id"] = internal_transaction_id
                response["external_transaction_id"] = external_transaction_id
                message = f"start request: {function_name}, channel: {logbook_dict['channel']}"
                logger.info(message, internal=internal_transaction_id, external=external_transaction_id)
                files = request.files.getlist("images")
                self.logbook_use_case.post_logbook_entry(logbook_dict, files, internal_transaction_id, external_transaction_id)
                response["error_code"] = 0
                response["message"] = "Bitácora de ingreso creada correctamente"
                end_time = default_timer()
                logger.info(f"Fin de la transacción, procesada en : {end_time - start_time} milisegundos",
                            internal=internal_transaction_id, external=logbook_dict['external_transaction_id'])
                status_code = 200
        except Exception as ex:
            response, status_code = CustomAPIException.check_exception(ex, function_name, internal_process)
            
        return response, status_code
