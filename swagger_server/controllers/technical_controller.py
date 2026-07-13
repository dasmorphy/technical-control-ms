from timeit import default_timer

import connexion

from swagger_server.exception.custom_error_exception import CustomAPIException
from swagger_server.models.generic_response import GenericResponse  # noqa: E501
from swagger_server.models.request_post_auditing import RequestPostAuditing
from swagger_server.models.request_post_task import RequestPostTask
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

    def put_technical(self, technical_data=None, channel=None, external_transaction_id=None):  # noqa: E501
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
                files = request.files.getlist("final_images")
                self.technical_use_case.put_technical_control(technical_dict, files, internal_transaction_id, external_transaction_id)
                response["error_code"] = 0
                response["message"] = "Control técnico actualizado correctamente"
                end_time = default_timer()
                logger.info(f"Fin de la transacción, procesada en : {end_time - start_time} milisegundos",
                            internal=internal_transaction_id, external=technical_dict['external_transaction_id'])
                status_code = 200
        except Exception as ex:
            response, status_code = CustomAPIException.check_exception(ex, function_name, internal_process)
            
        return response, status_code
    

    def get_all_tech_control(self):
        internal_process = (None, None)
        function_name = "get_all_tech_control"
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
                results = self.technical_use_case.get_all_tech_control(internal_transaction_id, external_transaction_id)
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

    def get_clients(self):
        internal_process = (None, None)
        function_name = "get_clients"
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
                results = self.technical_use_case.get_clients(internal_transaction_id, external_transaction_id)
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


    def get_location(self):
        internal_process = (None, None)
        function_name = "get_location"
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
                results = self.technical_use_case.get_location(request.args ,internal_transaction_id, external_transaction_id)
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
    

    def get_task(self):
        internal_process = (None, None)
        function_name = "get_task"
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
                results = self.technical_use_case.get_task(request.args ,internal_transaction_id, external_transaction_id)
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
    
    
    def post_task(self):
        internal_process = (None, None)
        function_name = "post_task"
        response = {}
        status_code = 500
        try:
            if connexion.request.is_json:
                body = RequestPostTask.from_dict(connexion.request.get_json())  # noqa: E501
                start_time = default_timer()
                internal_transaction_id = str(generate_internal_transaction_id())
                external_transaction_id = body.external_transaction_id
                internal_process = (internal_transaction_id, external_transaction_id)
                response["internal_transaction_id"] = internal_transaction_id
                response["external_transaction_id"] = external_transaction_id
                message = f"start request: {function_name}, channel: {body.channel}"
                logger.info(message, internal=internal_transaction_id, external=external_transaction_id)
                self.technical_use_case.post_task(body.technical_data, internal_transaction_id, external_transaction_id)
                response["error_code"] = 0
                response["message"] = "Registro guardado correctamente"
                end_time = default_timer()
                logger.info(f"Fin de la transacción, procesada en : {end_time - start_time} milisegundos",
                            internal=internal_transaction_id, external=body.external_transaction_id)
                status_code = 200
        except Exception as ex:
            response, status_code = CustomAPIException.check_exception(ex, function_name, internal_process)
            
        return response, status_code
    

    def get_tech_record(self):
        internal_process = (None, None)
        function_name = "get_tech_record"
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
                results = self.technical_use_case.get_tech_record(request.args ,internal_transaction_id, external_transaction_id)
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
    
    def post_tech_record(self):
        internal_process = (None, None)
        function_name = "post_tech_record"
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
                self.technical_use_case.post_technical_control(technical_dict, files, internal_transaction_id, external_transaction_id)
                response["error_code"] = 0
                response["message"] = "Registro guardado correctamente"
                end_time = default_timer()
                logger.info(f"Fin de la transacción, procesada en : {end_time - start_time} milisegundos",
                            internal=internal_transaction_id, external=technical_dict['external_transaction_id'])
                status_code = 200
        except Exception as ex:
            response, status_code = CustomAPIException.check_exception(ex, function_name, internal_process)
            
        return response, status_code
    

    def get_auditing(self):
        internal_process = (None, None)
        function_name = "get_auditing"
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
                results = self.technical_use_case.get_auditing(request.args ,internal_transaction_id, external_transaction_id)
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
    
    def post_auditing(self):
        internal_process = (None, None)
        function_name = "post_auditing"
        response = {}
        status_code = 500
        try:
            if request.content_type.startswith("multipart/form-data"):
                start_time = default_timer()
                internal_transaction_id = str(generate_internal_transaction_id())
                auditing_data = request.files.get("data")

                if not auditing_data:
                    raise CustomAPIException("Campo data no enviado", 400)

                auditing_raw = auditing_data.read().decode("utf-8")
                auditing_dict = json.loads(auditing_raw)

                external_transaction_id = auditing_dict['external_transaction_id']
                internal_process = (internal_transaction_id, external_transaction_id)
                response["internal_transaction_id"] = internal_transaction_id
                response["external_transaction_id"] = external_transaction_id
                message = f"start request: {function_name}, channel: {auditing_dict['channel']}"
                logger.info(message, internal=internal_transaction_id, external=external_transaction_id)
                auditor_img = request.files.get("auditor_img")
                responsible_img = request.files.get("responsible_img")
                client_img = request.files.get("client_img")
                self.technical_use_case.post_auditing(
                    auditing_dict,
                    {
                        "auditor_img": auditor_img,
                        "responsible_img": responsible_img,
                        "client_img": client_img,
                    },
                    internal_transaction_id,
                    external_transaction_id
                )
                response["error_code"] = 0
                response["message"] = "Control técnico actualizado correctamente"
                end_time = default_timer()
                logger.info(f"Fin de la transacción, procesada en : {end_time - start_time} milisegundos",
                            internal=internal_transaction_id, external=auditing_dict['external_transaction_id'])
                status_code = 200
        except Exception as ex:
            response, status_code = CustomAPIException.check_exception(ex, function_name, internal_process)
            
        return response, status_code