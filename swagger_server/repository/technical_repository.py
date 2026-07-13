import os

from loguru import logger
from sqlalchemy.orm import aliased

from swagger_server.exception.custom_error_exception import CustomAPIException
from swagger_server.models.db.auditing import Auditing
from swagger_server.models.db.auditing_item import AuditingItem
from swagger_server.models.db.auditing_response import AuditingResponse
from swagger_server.models.db.auditing_sections import AuditingSections
from swagger_server.models.db.auditing_signatures_img import AuditingSignaturesImg
from swagger_server.models.db.client import Client
from swagger_server.models.db.client_projects import ClientProject
from swagger_server.models.db.level_gasoline import LevelGasoline
from swagger_server.models.db.location import ClientLocation
from swagger_server.models.db.material_technical_record import MaterialTechnicalRecord
from swagger_server.models.db.movilization_client import MovilizationClient
from swagger_server.models.db.movilization_control import MovilizationControl
from swagger_server.models.db.movilization_copilot import MovilizationCopilot
from swagger_server.models.db.movilization_images import MovilizationImages
from swagger_server.models.db.movilization_reason import MovilizationReason
from swagger_server.models.db.movilization_status import MovilizationStatus
from swagger_server.models.db.reasons_movilization import ReasonsMovilization
from swagger_server.models.db.task_location import TaskLocation
from swagger_server.models.db.task_technical import TaskTechnical
from swagger_server.models.db.tech_record_image import TechRecordImage
from swagger_server.models.db.technical_record import TechnicalRecord
from swagger_server.models.db.vehicle_copilot import VehicleCopilot
from swagger_server.models.db.vehicle_driver import VehicleDriver
from swagger_server.models.db.vehicle_license import VehicleLicense
from swagger_server.models.task_data import TaskData
from swagger_server.resources.databases.postgresql import PostgreSQLClient
from sqlalchemy import ARRAY, JSON, Text, cast, distinct, exists, func, select, text

from werkzeug.utils import secure_filename
from uuid import uuid4
import getpass


class TechnicalRepository:
    
    def __init__(self):
        self.db = PostgreSQLClient("POSTGRESQL")



    def get_all_drivers(self, internal, external):
        with self.db.session_factory() as session:
            try:
                result = session.execute(
                    select(VehicleDriver)
                )
                drivers = [
                    {
                        "id_driver": c.id_driver,
                        "name": c.name,
                        "is_active": c.is_active,
                        "created_at": c.created_at,
                        "updated_at": c.updated_at
                    }
                    for c in result.scalars().all()
                ]
                return drivers
            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al obtener en la base de datos", 500)
            

    def get_all_licenses(self, internal, external):
        with self.db.session_factory() as session:
            try:
                result = session.execute(
                    select(VehicleLicense)
                )
                drivers = [
                    {
                        "id_license": c.id_license,
                        "name": c.name,
                        "is_active": c.is_active,
                        "created_at": c.created_at,
                        "updated_at": c.updated_at
                    }
                    for c in result.scalars().all()
                ]
                return drivers
            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al obtener en la base de datos", 500)
            
    
    def get_all_reasons(self, internal, external):
        with self.db.session_factory() as session:
            try:
                result = session.execute(
                    select(ReasonsMovilization)
                )
                drivers = [
                    {
                        "id_reason": c.id_reason,
                        "name": c.name,
                        "is_active": c.is_active,
                        "created_at": c.created_at,
                        "updated_at": c.updated_at
                    }
                    for c in result.scalars().all()
                ]
                return drivers
            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al obtener en la base de datos", 500)
            
    def get_all_copilot(self, internal, external):
        with self.db.session_factory() as session:
            try:
                result = session.execute(
                    select(VehicleCopilot)
                )
                drivers = [
                    {
                        "id_copilot": c.id_copilot,
                        "name": c.name,
                        "is_active": c.is_active,
                        "created_at": c.created_at,
                        "updated_at": c.updated_at
                    }
                    for c in result.scalars().all()
                ]
                return drivers
            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al obtener en la base de datos", 500)
            
    
    def get_all_projects(self, internal, external):
        with self.db.session_factory() as session:
            try:
                result = session.execute(
                    select(ClientProject)
                )
                drivers = [
                    {
                        "id_client_projects": c.id_client_projects,
                        "name": c.name,
                        "is_active": c.is_active,
                        "created_at": c.created_at,
                        "updated_at": c.updated_at
                    }
                    for c in result.scalars().all()
                ]
                return drivers
            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al obtener en la base de datos", 500)
            

    def get_all_level_gasoline(self, internal, external):
        with self.db.session_factory() as session:
            try:
                result = session.execute(
                    select(LevelGasoline)
                )
                drivers = [
                    {
                        "id_level": c.id_level,
                        "name": c.name,
                        "is_active": c.is_active,
                        "created_at": c.created_at,
                        "updated_at": c.updated_at
                    }
                    for c in result.scalars().all()
                ]
                return drivers
            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al obtener en la base de datos", 500)
            

    def get_all_tech_control(self, internal, external):
        with self.db.session_factory() as session:
            try:
                mvc = MovilizationControl
                mcc = MovilizationClient
                mvr = MovilizationReason
                mctr = MovilizationCopilot
                mimg = MovilizationImages
                cp = ClientProject
                rs = ReasonsMovilization
                cpt = VehicleCopilot
                dvh = VehicleDriver
                lvh = VehicleLicense
                gsl = LevelGasoline
                sts = MovilizationStatus

                gsl_initial = aliased(gsl)
                gsl_final = aliased(gsl)

                def json_agg_filtered(build_obj, filter_col):
                    return func.coalesce(
                        func.json_agg(
                            func.distinct(build_obj)
                        ).filter(filter_col.isnot(None)),
                        func.cast('[]', JSON)
                    )

                clients_agg = json_agg_filtered(
                    func.jsonb_build_object("id", cp.id_client_projects, "name", cp.name),
                    cp.id_client_projects
                ).label("clients")

                reasons_agg = json_agg_filtered(
                    func.jsonb_build_object("id", rs.id_reason, "name", rs.name),
                    rs.id_reason
                ).label("reasons")

                copilots_agg = json_agg_filtered(
                    func.jsonb_build_object("id", cpt.id_copilot, "name", cpt.name),
                    cpt.id_copilot
                ).label("copilots")

                # Imágenes inline en vez de subquery separada
                images_agg = func.coalesce(
                    func.array_agg(func.distinct(mimg.image_path)).filter(mimg.image_path.isnot(None)),
                    func.cast([], ARRAY(Text))
                ).label("images")

                query = (
                    session.query(
                        mvc.id_movilization,
                        mvc.exit_date,
                        mvc.arrival_date,
                        mvc.initial_km,
                        mvc.final_km,
                        mvc.destiny,
                        mvc.exit_point,
                        mvc.observations,
                        mvc.status,
                        mvc.created_at,
                        mvc.updated_at,
                        mvc.created_by,
                        mvc.updated_by,
                        clients_agg,
                        reasons_agg,
                        copilots_agg,
                        images_agg,
                        dvh.name.label("name_driver"),
                        mvc.initial_gasoline_id,
                        gsl_initial.name.label("name_gasoline_initial"),
                        mvc.final_gasoline_id,
                        gsl_final.name.label("name_gasoline_final"),
                        mvc.license_id,
                        lvh.name.label("license"),
                        sts.name.label("name_status"),
                    )
                    .outerjoin(mcc, mcc.movilization_id == mvc.id_movilization)
                    .outerjoin(mimg, mimg.movilization_id == mvc.id_movilization)
                    .outerjoin(dvh, dvh.id_driver == mvc.driver_id)
                    .outerjoin(lvh, lvh.id_license == mvc.license_id)
                    .outerjoin(sts, sts.id_status == mvc.status)
                    .outerjoin(gsl_final, gsl_final.id_level == mvc.final_gasoline_id)
                    .outerjoin(gsl_initial, gsl_initial.id_level == mvc.initial_gasoline_id)
                    .outerjoin(mvr, mvr.movilization_id == mvc.id_movilization)
                    .outerjoin(mctr, mctr.movilization_id == mvc.id_movilization)
                    .outerjoin(cp, cp.id_client_projects == mcc.client_project_id)
                    .outerjoin(rs, rs.id_reason == mvr.reason_id)
                    .outerjoin(cpt, cpt.id_copilot == mctr.copilot_id)
                    # GROUP BY solo por la PK — PostgreSQL infiere el resto
                    .group_by(
                        mvc.id_movilization,
                        dvh.name,
                        gsl_initial.name,
                        gsl_final.name,
                        sts.name,
                        lvh.name,
                    )
                    .order_by(mvc.created_at.desc())
                )

                return query.all()  # usar .all() directamente

            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                raise CustomAPIException("Error al obtener en la base de datos", 500)


    def post_technical_control(self, data, images, internal, external) -> None:
        saved_files = []

        if images and len(images) > 10:
            raise CustomAPIException("Máximo 10 imagenes", 500)

        with self.db.session_factory() as session:
            try:

                technical_record = TechnicalRecord(
                    task_id=data.get('task_id'),
                    client_id=data.get('client_id'),
                    location_id=data.get('location_id'),
                    resume=data.get('resume'),
                    created_by=data.get('user'),
                )

                session.add(technical_record)
                session.flush()

                record_technical_id = technical_record.id_record

                for material in data.get('materials'):
                    material_tech = MaterialTechnicalRecord(
                        record_id=record_technical_id,
                        quantity=material.get('quantity'),
                        material=material.get('material')
                    )
                    session.add(material_tech)

                #Guardar imágenes (máx 10)
                for file in images[:10]:
                    result = self.save_image(file)
                    saved_files.append(result["url"])

                    image = TechRecordImage(
                        record_id=record_technical_id,
                        image_path=result["url"],
                    )

                    session.add(image)

                session.commit()

            except Exception as exception:
                session.rollback()

                #limpia archivos guardados si falla DB
                for path in saved_files:
                    full_path = os.path.join("/var/www", path.lstrip("/"))
                    if os.path.exists(full_path):
                        os.remove(full_path)

                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al insertar en la base de datos", 500)

            finally:
                session.close()



    def put_technical_control(self, data, images, internal, external) -> None:
        saved_files = []

        if images and len(images) > 10:
            raise CustomAPIException("Máximo 10 imagenes", 500)

        with self.db.session_factory() as session:
            try:
                movilization_exists = session.execute(
                    select(MovilizationControl).where(
                        MovilizationControl.id_movilization == data.get('id_movilization')
                    )
                ).scalar_one_or_none()

                if not movilization_exists:
                    raise CustomAPIException(
                        message="No existe el registro de control técnico",
                        status_code=404
                    )

                movilization = MovilizationControl(
                    final_gasoline_id=data.get("final_gasoline_id"),
                    final_km=data.get("final_km"),
                    have_incident=data.get("have_incident"),

                    status=2
                )

                session.add(movilization)

                movilization_id = movilization.id_movilization

                #Guardar imágenes (máx 10)
                for file in images[:10]:
                    result = self.save_image(file)
                    saved_files.append(result["url"])

                    image = MovilizationImages(
                        movilization_id=movilization_id,
                        image_path=result["url"],
                        type="finales"
                    )

                    session.add(image)

                session.commit()

            except Exception as exception:
                session.rollback()

                #limpia archivos guardados si falla DB
                for path in saved_files:
                    full_path = os.path.join("/var/www", path.lstrip("/"))
                    if os.path.exists(full_path):
                        os.remove(full_path)

                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al insertar en la base de datos", 500)

            finally:
                session.close()


    def save_image(self, file):
        folder = "/var/www/uploads/technical"
        ALLOWED_EXTENSIONS = {"webp"}
        MAX_FILENAME_LEN = 255
        MAX_BASENAME_LEN = 50

        if not file or file.filename == "":
            raise ValueError("Archivo inválido")

        if not os.path.exists(folder):
            raise CustomAPIException(f"La carpeta root de imágenes no existe {getpass.getuser()} - {os.getuid()} - {os.geteuid()}", 404)
        

        if not os.access(folder, os.W_OK):
            raise CustomAPIException(f"No hay permisos de escritura en la carpeta de imágenes {getpass.getuser()} - {os.getuid()} - {os.geteuid()}", 400)
        
        ext = file.filename.rsplit(".", 1)[-1].lower()

        if ext not in ALLOWED_EXTENSIONS:
            raise ValueError("Formato no permitido. Solo se acepta WEBP.")

        original_name = secure_filename(file.filename)
        base_name = os.path.splitext(original_name)[0][:MAX_BASENAME_LEN]

        filename = f"{uuid4()}_{base_name}.webp"

        if len(filename.encode("utf-8")) > MAX_FILENAME_LEN:
            filename = f"{uuid4().hex}.webp"

        path = os.path.join(folder, filename)
        file.save(path)

        return {
            "url": f"/uploads/technical/{filename}"
        }
    
    def get_clients(self, internal, external):
        with self.db.session_factory() as session:
            try:
                result = session.execute(
                    select(Client)
                )
                drivers = [
                    {
                        "id_client": c.id_client,
                        "name": c.name,
                        "created_by": c.created_by,
                        "updated_by": c.updated_by,
                        "created_at": c.created_at,
                        "updated_at": c.updated_at
                    }
                    for c in result.scalars().all()
                ]
                return drivers
            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al obtener en la base de datos", 500)
            

    def get_location(self, filters, internal, external):
        with self.db.session_factory() as session:
            try:
                query_stmt = (
                    select(ClientLocation)
                )

                if filters.get("clients"):
                    query_stmt = query_stmt.where(
                        ClientLocation.client_id.in_(filters["clients"])
                    )

                rows = session.execute(query_stmt).scalars().all()

                data = [
                    {
                        "id_location": c.id_location,
                        "client_id": c.client_id,
                        "name": c.name,
                        "address": c.address,
                        "long": c.long,
                        "lat": c.lat,
                        "created_by": c.created_by,
                        "updated_by": c.updated_by,
                        "created_at": c.created_at,
                        "updated_at": c.updated_at
                    }
                    for c in rows
                ]
                return data
            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al obtener en la base de datos", 500)
            

    def get_task(self, filters, internal, external):
        with self.db.session_factory() as session:
            try:
                query_stmt = (
                    select(
                        TaskTechnical,
                        ClientLocation,
                        Client
                    )
                    .outerjoin(
                        TaskLocation,
                        TaskLocation.task_id == TaskTechnical.id_task
                    )
                    .outerjoin(
                        ClientLocation,
                        ClientLocation.id_location == TaskLocation.location_id
                    )
                    .outerjoin(
                        Client,
                        Client.id_client == ClientLocation.client_id
                    )
                    .order_by(TaskTechnical.created_at.desc())
                )

                if filters.get("locations"):
                    query_stmt = query_stmt.where(
                        ClientLocation.id_location.in_(filters["locations"])
                    )

                if filters.get("clients"):
                    query_stmt = query_stmt.where(
                        ClientLocation.client_id.in_(filters["clients"])
                    )


                rows = session.execute(query_stmt).all()

                data = [
                    {
                        "id_task": task.id_task,
                        "name": task.name,
                        "client": client.name,
                        "description": task.description,
                        "location": location.name if location else None,
                        "code": task.code,
                        "status": task.status,
                        "created_by": task.created_by,
                        "updated_by": task.updated_by,
                        "created_at": task.created_at,
                        "updated_at": task.updated_at
                    }
                    for task, location, client in rows
                ]

                return data
            
            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al obtener en la base de datos", 500)
            

    def post_task(self, data: TaskData, internal, external) -> None:
        with self.db.session_factory() as session:
            try:
                new_task = TaskTechnical(
                    name=data.name,
                    description=data.description,
                    code=data.code,
                    status="Aprobado",
                    created_by=data.user,
                    updated_by=data.user
                )

                session.add(new_task)
                session.flush()

                new_task_location= TaskLocation(
                    location_id=data.location_id,
                    task_id=new_task.id_task,
                    created_by=data.user,
                    updated_by=data.user
                )

                session.add(new_task_location)
                session.commit()
            except Exception as exception:
                session.rollback()
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al insertar en la base de datos", 500)

            finally:
                session.close()


    def get_tech_record(self, filters, internal, external):
        with self.db.session_factory() as session:
            try:
                query_stmt = (
                    select(
                        TechnicalRecord,
                        TaskTechnical,
                        Client,
                        ClientLocation
                    )
                    .outerjoin(
                        TaskTechnical,
                        TaskTechnical.id_task == TechnicalRecord.task_id
                    )
                    .outerjoin(
                        ClientLocation,
                        ClientLocation.id_location == TechnicalRecord.location_id
                    )
                    .outerjoin(
                        Client,
                        Client.id_client == TechnicalRecord.client_id
                    )
                    .order_by(TechnicalRecord.created_at.desc())
                )

                if filters.get("locations"):
                    query_stmt = query_stmt.where(
                        ClientLocation.id_location.in_(filters["locations"])
                    )

                if filters.get("clients"):
                    query_stmt = query_stmt.where(
                        ClientLocation.client_id.in_(filters["clients"])
                    )

                if filters.get("tasks"):
                    query_stmt = query_stmt.where(
                        TaskTechnical.id_task.in_(filters["tasks"])
                    )

                rows = session.execute(query_stmt).all()

                data = [
                    {
                        "id_record": record.id_record,
                        "resume": record.resume,
                        "client_name": client.name,
                        "location_name": location.name if location else None,
                        "task_code": task.code if task else None,
                        "created_by": record.created_by,
                        "updated_by": record.updated_by,
                        "created_at": record.created_at,
                        "updated_at": record.updated_at
                    }
                    for record, task, client, location in rows
                ]

                return data
            
            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al obtener en la base de datos", 500)
            

    def get_auditing(self, filters, internal, external):
        with self.db.session_factory() as session:
            try:
                query_stmt = (
                    select(
                        Auditing,
                        AuditingResponse,
                        AuditingItem,
                        AuditingSections,
                        ClientLocation,
                        Client,
                    )
                    .outerjoin(
                        AuditingResponse,
                        AuditingResponse.auditing_id == Auditing.id_auditing
                    )
                    .outerjoin(
                        AuditingItem,
                        AuditingItem.id_item == AuditingResponse.item_id
                    )
                    .outerjoin(
                        AuditingSections,
                        AuditingSections.id_section == AuditingItem.section_id
                    )
                    .outerjoin(
                        ClientLocation,
                        ClientLocation.id_location == Auditing.location_id
                    )
                    .outerjoin(
                        Client,
                        Client.id_client == ClientLocation.client_id
                    )
                    .order_by(Auditing.created_at.desc())
                )

                if filters.get("locations"):
                    query_stmt = query_stmt.where(
                        ClientLocation.id_location.in_(filters["locations"])
                    )

                if filters.get("clients"):
                    query_stmt = query_stmt.where(
                        ClientLocation.client_id.in_(filters["clients"])
                    )

                if filters.get("tasks"):
                    query_stmt = query_stmt.where(
                        Auditing.task_id.in_(filters["tasks"])
                    )

                rows = session.execute(query_stmt).all()

                auditing_map = {}

                for auditing, response, item, section, client_location, client in rows:
                    if auditing.id_auditing not in auditing_map:
                        auditing_map[auditing.id_auditing] = {
                            "id_auditing": auditing.id_auditing,
                            "task_id": auditing.task_id,
                            "location_id": auditing.location_id,
                            "responsible": auditing.responsible,
                            "percentage_compliance": auditing.percentage_compliance,
                            "status": auditing.status,
                            "created_by": auditing.created_by,
                            "updated_by": auditing.updated_by,
                            "created_at": auditing.created_at,
                            "updated_at": auditing.updated_at,
                            "client_name": client.name,
                            "location_name": client_location.name,
                            "responses": [],
                        }

                    if response is not None:
                        auditing_map[auditing.id_auditing]["responses"].append({
                            "id_response": response.id_response,
                            "response": response.response,
                            "observation": response.observation,
                            "item": {
                                "id_item": item.id_item,
                                "name": item.name,
                                "order_number": item.order_number,
                                "section": {
                                    "id_section": section.id_section,
                                    "name": section.name,
                                    "order_number": section.order_number,
                                } if section is not None else None,
                            } if item is not None else None,
                        })

                return list(auditing_map.values())

            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception

                raise CustomAPIException("Error al obtener en la base de datos", 500)
            

    def post_auditing(self, data: TaskData, images, internal, external) -> None:
        saved_files = []

        with self.db.session_factory() as session:
            try:
                new_auditing = Auditing(
                    task_id=data.task_id,
                    location_id=data.location_id,
                    responsible=data.responsible,
                    percentage_compliance=data.percentage_compliance,
                    status=data.status,
                    created_by=data.user,
                    updated_by=data.user
                )

                session.add(new_auditing)
                session.flush()
                
                for response in data.responses:
                    new_response= AuditingResponse(
                        auditing_id=new_auditing.id_auditing,
                        item_id=response.item_id,
                        response=response.response,
                        observation=data.observation,
                        created_by=data.user,
                        updated_by=data.user
                    )
                    session.add(new_response)

                signature = AuditingSignaturesImg(
                    auditing_id=new_auditing.id_auditing
                )

                fields = {
                    "auditor_img": "auditor_path",
                    "responsible_img": "responsible_path",
                    "client_img": "client_path",
                }

                for image_key, model_attr in fields.items():
                    image = images.get(image_key)
                    if image:
                        result = self.save_image(image)
                        saved_files.append(result["url"])
                        setattr(signature, model_attr, result["url"])

                session.add(signature)

                session.commit()
            except Exception as exception:
                session.rollback()
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al insertar en la base de datos", 500)

            finally:
                session.close()