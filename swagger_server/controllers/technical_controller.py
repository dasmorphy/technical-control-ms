from timeit import default_timer

import connexion

from swagger_server.exception.custom_error_exception import CustomAPIException
from swagger_server.models.generic_response import GenericResponse  # noqa: E501
from swagger_server.models.response_error import ResponseError  # noqa: E501
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
        self.technical_use_case = TechnicalUseCase(technical_control_repository)

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
        function_name = "post_technical"
        response = {}
        status_code = 500
        try:
            if request.content_type.startswith("multipart/form-data"):
                start_time = default_timer()
                internal_transaction_id = str(generate_internal_transaction_id())
                technical_data = request.files.get("technical_data")

                if not technical_data:
                    raise CustomAPIException("Campo technical_data no enviado", 400)

                technical_raw = technical_data.read().decode("utf-8")
                technical_dict = json.loads(technical_raw)

                external_transaction_id = technical_dict['external_transaction_id']
                internal_process = (internal_transaction_id, external_transaction_id)
                response["internal_transaction_id"] = internal_transaction_id
                response["external_transaction_id"] = external_transaction_id
                message = f"start request: {function_name}, channel: {technical_dict['channel']}"
                logger.info(message, internal=internal_transaction_id, external=external_transaction_id)
                files = request.files.getlist("images")
                self.technical_use_case.post_technical_control(technical_dict, internal_transaction_id, external_transaction_id)
                response["error_code"] = 0
                response["message"] = "Control técnico creado correctamente"
                end_time = default_timer()
                logger.info(f"Fin de la transacción, procesada en : {end_time - start_time} milisegundos",
                            internal=internal_transaction_id, external=technical_dict['external_transaction_id'])
                status_code = 200
        except Exception as ex:
            response, status_code = CustomAPIException.check_exception(ex, function_name, internal_process)
            
        return response, status_code


    def get_all_drivers(self):
        internal_process = (None, None)
        function_name = "get_all_drivers"
        response = {}
        status_code = 500
        try:
            if connexion.request.headers:
                start_time = default_timer()
                internal_transaction_id = str(generate_internal_transaction_id())
                external_transaction_id = request.headers.get('externalTransactionId')
                internal_process = (internal_transaction_id, external_transaction_id)
                response["internal_transaction_id"] = internal_transaction_id
                response["external_transaction_id"] = external_transaction_id
                message = f"start request: {function_name}, channel: {request.headers.get('channel')}"
                logger.info(message, internal=internal_transaction_id, external=external_transaction_id)
                results = self.technical_use_case.get_all_drivers(internal_transaction_id, external_transaction_id)
                response["error_code"] = 0
                response["message"] = "Registros obtenidos correctamente"
                response["data"] = results
                end_time = default_timer()
                logger.info(f"Fin de la transacción, procesada en : {end_time - start_time} milisegundos",
                            internal=internal_transaction_id, external=external_transaction_id)
                status_code = 200
        except Exception as ex:
            response, status_code = CustomAPIException.check_exception(ex, function_name, internal_process)
            
        return response, status_code

    def get_all_licenses(self):
        internal_process = (None, None)
        function_name = "get_all_licenses"
        response = {}
        status_code = 500
        try:
            if connexion.request.headers:
                start_time = default_timer()
                internal_transaction_id = str(generate_internal_transaction_id())
                external_transaction_id = request.headers.get('externalTransactionId')
                internal_process = (internal_transaction_id, external_transaction_id)
                response["internal_transaction_id"] = internal_transaction_id
                response["external_transaction_id"] = external_transaction_id
                message = f"start request: {function_name}, channel: {request.headers.get('channel')}"
                logger.info(message, internal=internal_transaction_id, external=external_transaction_id)
                results = self.technical_use_case.get_all_licenses(internal_transaction_id, external_transaction_id)
                response["error_code"] = 0
                response["message"] = "Registros obtenidos correctamente"
                response["data"] = results
                end_time = default_timer()
                logger.info(f"Fin de la transacción, procesada en : {end_time - start_time} milisegundos",
                            internal=internal_transaction_id, external=external_transaction_id)
                status_code = 200
        except Exception as ex:
            response, status_code = CustomAPIException.check_exception(ex, function_name, internal_process)
            
        return response, status_code


    def get_all_reasons(self):
        internal_process = (None, None)
        function_name = "get_all_reasons"
        response = {}
        status_code = 500
        try:
            if connexion.request.headers:
                start_time = default_timer()
                internal_transaction_id = str(generate_internal_transaction_id())
                external_transaction_id = request.headers.get('externalTransactionId')
                internal_process = (internal_transaction_id, external_transaction_id)
                response["internal_transaction_id"] = internal_transaction_id
                response["external_transaction_id"] = external_transaction_id
                message = f"start request: {function_name}, channel: {request.headers.get('channel')}"
                logger.info(message, internal=internal_transaction_id, external=external_transaction_id)
                results = self.technical_use_case.get_all_reasons(internal_transaction_id, external_transaction_id)
                response["error_code"] = 0
                response["message"] = "Registros obtenidos correctamente"
                response["data"] = results
                end_time = default_timer()
                logger.info(f"Fin de la transacción, procesada en : {end_time - start_time} milisegundos",
                            internal=internal_transaction_id, external=external_transaction_id)
                status_code = 200
        except Exception as ex:
            response, status_code = CustomAPIException.check_exception(ex, function_name, internal_process)
            
        return response, status_code
    
    def get_all_copilot(self):
        internal_process = (None, None)
        function_name = "get_all_copilot"
        response = {}
        status_code = 500
        try:
            if connexion.request.headers:
                start_time = default_timer()
                internal_transaction_id = str(generate_internal_transaction_id())
                external_transaction_id = request.headers.get('externalTransactionId')
                internal_process = (internal_transaction_id, external_transaction_id)
                response["internal_transaction_id"] = internal_transaction_id
                response["external_transaction_id"] = external_transaction_id
                message = f"start request: {function_name}, channel: {request.headers.get('channel')}"
                logger.info(message, internal=internal_transaction_id, external=external_transaction_id)
                results = self.technical_use_case.get_all_copilot(internal_transaction_id, external_transaction_id)
                response["error_code"] = 0
                response["message"] = "Registros obtenidos correctamente"
                response["data"] = results
                end_time = default_timer()
                logger.info(f"Fin de la transacción, procesada en : {end_time - start_time} milisegundos",
                            internal=internal_transaction_id, external=external_transaction_id)
                status_code = 200
        except Exception as ex:
            response, status_code = CustomAPIException.check_exception(ex, function_name, internal_process)
            
        return response, status_code
    
    def get_all_projects(self):
        internal_process = (None, None)
        function_name = "get_all_projects"
        response = {}
        status_code = 500
        try:
            if connexion.request.headers:
                start_time = default_timer()
                internal_transaction_id = str(generate_internal_transaction_id())
                external_transaction_id = request.headers.get('externalTransactionId')
                internal_process = (internal_transaction_id, external_transaction_id)
                response["internal_transaction_id"] = internal_transaction_id
                response["external_transaction_id"] = external_transaction_id
                message = f"start request: {function_name}, channel: {request.headers.get('channel')}"
                logger.info(message, internal=internal_transaction_id, external=external_transaction_id)
                results = self.technical_use_case.get_all_projects(internal_transaction_id, external_transaction_id)
                response["error_code"] = 0
                response["message"] = "Registros obtenidos correctamente"
                response["data"] = results
                end_time = default_timer()
                logger.info(f"Fin de la transacción, procesada en : {end_time - start_time} milisegundos",
                            internal=internal_transaction_id, external=external_transaction_id)
                status_code = 200
        except Exception as ex:
            response, status_code = CustomAPIException.check_exception(ex, function_name, internal_process)
            
        return response, status_code
    
    def get_all_level_gasoline(self):
        internal_process = (None, None)
        function_name = "get_all_level_gasoline"
        response = {}
        status_code = 500
        try:
            if connexion.request.headers:
                start_time = default_timer()
                internal_transaction_id = str(generate_internal_transaction_id())
                external_transaction_id = request.headers.get('externalTransactionId')
                internal_process = (internal_transaction_id, external_transaction_id)
                response["internal_transaction_id"] = internal_transaction_id
                response["external_transaction_id"] = external_transaction_id
                message = f"start request: {function_name}, channel: {request.headers.get('channel')}"
                logger.info(message, internal=internal_transaction_id, external=external_transaction_id)
                results = self.technical_use_case.get_all_level_gasoline(internal_transaction_id, external_transaction_id)
                response["error_code"] = 0
                response["message"] = "Registros obtenidos correctamente"
                response["data"] = results
                end_time = default_timer()
                logger.info(f"Fin de la transacción, procesada en : {end_time - start_time} milisegundos",
                            internal=internal_transaction_id, external=external_transaction_id)
                status_code = 200
        except Exception as ex:
            response, status_code = CustomAPIException.check_exception(ex, function_name, internal_process)
            
        return response, status_code
