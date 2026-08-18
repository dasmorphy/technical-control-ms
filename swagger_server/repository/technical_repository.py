from datetime import datetime
import os

from loguru import logger
from sqlalchemy.orm import aliased

from swagger_server.exception.custom_error_exception import CustomAPIException
from swagger_server.models.auditing_data import AuditingData
from swagger_server.models.db.auditing import Auditing
from swagger_server.models.db.auditing_findings import AuditingFinding
from swagger_server.models.db.auditing_findings_img import AuditingFindingsImg
from swagger_server.models.db.auditing_item import AuditingItem
from swagger_server.models.db.auditing_response import AuditingResponse
from swagger_server.models.db.auditing_sections import AuditingSections
from swagger_server.models.db.auditing_signatures_img import AuditingSignaturesImg
from swagger_server.models.db.client import Client
from swagger_server.models.db.client_projects import ClientProject
from swagger_server.models.db.history_status_project import HistoryStatusProject
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
from swagger_server.models.db.tech_staff_record import TechStaffRecord
from swagger_server.models.db.technical_equipment import TechnicalEquipment
from swagger_server.models.db.technical_record import TechnicalRecord
from swagger_server.models.db.technical_staff import TechnicalStaff
from swagger_server.models.db.users import Users
from swagger_server.models.db.vehicle_copilot import VehicleCopilot
from swagger_server.models.db.vehicle_driver import VehicleDriver
from swagger_server.models.db.vehicle_license import VehicleLicense
from swagger_server.models.task_data import TaskData
from swagger_server.resources.databases.postgresql import PostgreSQLClient
from sqlalchemy import ARRAY, JSON, String, Text, and_, case, cast, distinct, exists, func, select, text, update

from werkzeug.utils import secure_filename
from uuid import uuid4
import getpass

from swagger_server.service.notification_client import NotificationClient
from swagger_server.service.rabbitMQ import RabbitMQClient
from swagger_server.utils.utils import calculate_score_percentage


class TechnicalRepository:
    
    def __init__(self):
        self.db = PostgreSQLClient("POSTGRESQL")
        self.notification_client = NotificationClient()
        self.rabbitMQ = RabbitMQClient()



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

                has_records = session.scalar(
                    select(
                        exists().where(
                            TechnicalRecord.task_id == data.get("task_id")
                        )
                    )
                )

                # Si es el primer registro, actualizar el estado de la tarea
                if not has_records:
                    session.execute(
                        update(TaskTechnical)
                        .where(TaskTechnical.id_task == data.get("task_id"))
                        .values(
                            status="En ejecución",
                            updated_by=data.get("user")
                        )
                    )

                technical_record = TechnicalRecord(
                    status=data.get('status'),
                    task_id=data.get('task_id'),
                    client_id=data.get('client_id'),
                    location_id=data.get('location_id'),
                    resume=data.get('resume'),
                    created_by=data.get('user'),
                    vehicle=data.get('vehicle'),
                    updated_by=data.get('user'),
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

                for tech_staff_id in data.get('technical_staff'):
                    tech_staff_record = TechStaffRecord(
                        record_id=record_technical_id,
                        tech_staff_id=tech_staff_id
                    )
                    session.add(tech_staff_record)

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


    def save_image(self, file,  name_folder: str="technical"):
        folder = f"/var/www/uploads/{name_folder}"
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
            "url": f"/uploads/{name_folder}/{filename}"
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
                images_subq = (
                    select(
                        TechRecordImage.record_id.label("record_id"),
                        func.array_agg(
                            TechRecordImage.image_path
                        )
                        .filter(TechRecordImage.image_path.isnot(None))
                        .label("images")
                    )
                    .group_by(TechRecordImage.record_id)
                    .subquery()
                )
                
                tech_record_subq = (
                    select(
                        TechnicalRecord.task_id.label("task_id"),
                        func.json_agg(
                            func.json_build_object(
                                "id_record", TechnicalRecord.id_record,
                                "client_id", TechnicalRecord.client_id,
                                "location_id", TechnicalRecord.location_id,
                                "resume", TechnicalRecord.resume,
                                "created_by", TechnicalRecord.created_by,
                                "created_at", TechnicalRecord.created_at,
                                "images", func.coalesce(
                                    images_subq.c.images,
                                    []
                                )
                            )
                        ).label("record_technical")
                    )
                    .outerjoin(
                        images_subq,
                        images_subq.c.record_id == TechnicalRecord.id_record
                    )
                    .group_by(TechnicalRecord.task_id)
                    .subquery()
                )


                query_stmt = (
                    select(
                        TaskTechnical,
                        ClientLocation,
                        Client,
                        tech_record_subq.c.record_technical,
                        Users.user
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
                    .outerjoin(
                        tech_record_subq,
                        tech_record_subq.c.task_id == TaskTechnical.id_task
                    )
                    .outerjoin(
                        Users,
                        cast(Users.id_user, String) == TaskTechnical.requested_by
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

                
                if filters.get("status"):
                    query_stmt = query_stmt.where(
                        TaskTechnical.status.in_(filters["status"])
                    )

                rows = session.execute(query_stmt).all()

                data = [
                    {
                        "id_task": task.id_task,
                        "name": task.name,
                        "client": client.name,
                        "requested_by": user,
                        "client_id": client.id_client,
                        "description": task.description,
                        "location_id": location.id_location if location else None,
                        "location": location.name if location else None,
                        "code": task.code,
                        "status": task.status,
                        "record_technical": record_technical or None,
                        "created_by": task.created_by,
                        "updated_by": task.updated_by,
                        "created_at": task.created_at,
                        "updated_at": task.updated_at
                    }
                    for task, location, client, record_technical, user in rows
                ]

                return data
            
            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al obtener en la base de datos", 500)

    def generate_project_code(self, session):
        next_id = session.execute(
            text("SELECT nextval('technical.task_technical_id_seq')")
        ).scalar_one()

        code = f"TLSG-PRY-{next_id:04d}"

        return code


    def post_task(self, data: TaskData, internal, external) -> None:
        with self.db.session_factory() as session:
            try:
                code_generated = self.generate_project_code(session)
                new_task = TaskTechnical(
                    name=data.name,
                    description=data.description,
                    code=code_generated,
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
                # ============================
                # MATERIALES
                # ============================
                materials_subq = (
                    select(
                        MaterialTechnicalRecord.record_id.label("record_id"),
                        func.json_agg(
                            func.json_build_object(
                                "id_material_record", MaterialTechnicalRecord.id_material_record,
                                "material", MaterialTechnicalRecord.material,
                                "quantity", MaterialTechnicalRecord.quantity,
                            )
                        ).label("materials")
                    )
                    .group_by(MaterialTechnicalRecord.record_id)
                    .subquery()
                )

                # ============================
                # PERSONAL TÉCNICO
                # ============================
                staff_subq = (
                    select(
                        TechStaffRecord.record_id.label("record_id"),
                        func.json_agg(
                            func.json_build_object(
                                "id_technical", TechnicalStaff.id_technical,
                                "name", TechnicalStaff.name,
                            )
                        ).label("technical_staff")
                    )
                    .join(
                        TechnicalStaff,
                        TechnicalStaff.id_technical == TechStaffRecord.tech_staff_id
                    )
                    .group_by(TechStaffRecord.record_id)
                    .subquery()
                )

                # ============================
                # CONSULTA PRINCIPAL
                # ============================
                query_stmt = (
                    select(
                        TechnicalRecord,
                        TaskTechnical,
                        Client,
                        ClientLocation,
                        materials_subq.c.materials,
                        staff_subq.c.technical_staff,
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
                    .outerjoin(
                        materials_subq,
                        materials_subq.c.record_id == TechnicalRecord.id_record
                    )
                    .outerjoin(
                        staff_subq,
                        staff_subq.c.record_id == TechnicalRecord.id_record
                    )
                    .order_by(
                        TechnicalRecord.created_at.desc()
                    )
                )

                # ============================
                # FILTROS
                # ============================
                if filters.get("locations"):
                    query_stmt = query_stmt.where(
                        ClientLocation.id_location.in_(filters["locations"])
                    )

                if filters.get("clients"):
                    query_stmt = query_stmt.where(
                        ClientLocation.client_id.in_(filters["clients"])
                    )

                if filters.get("user"):
                    query_stmt = query_stmt.where(
                        TechnicalRecord.created_by == filters["user"]
                    )

                if filters.get("tasks"):
                    query_stmt = query_stmt.where(
                        TaskTechnical.id_task.in_(filters["tasks"])
                    )

                rows = session.execute(query_stmt).all()

                # ============================
                # RESPONSE
                # ============================
                data = [
                    {
                        "id_record": record.id_record,
                        "resume": record.resume,
                        "status": record.status,
                        "vehicle": record.vehicle,

                        "client_name": client.name if client else None,
                        "location_name": location.name if location else None,
                        "task_code": task.code if task else None,

                        "materials": materials or [],
                        "technical_staff": technical_staff or [],

                        "created_by": record.created_by,
                        "updated_by": record.updated_by,
                        "created_at": record.created_at,
                        "updated_at": record.updated_at,
                    }
                    for (
                        record,
                        task,
                        client,
                        location,
                        materials,
                        technical_staff
                    ) in rows
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
            

    def post_auditing(self, data, images, internal, external) -> None:
        saved_files = []

        with self.db.session_factory() as session:
            try:
                data_dict = data.get("data")
                percentage = calculate_score_percentage(data_dict.get("responses"))
                
                new_auditing = Auditing(
                    task_id=data_dict.get("task_id"),
                    location_id=data_dict.get("location_id"),
                    responsible=data_dict.get("responsible"),
                    percentage_compliance=percentage,
                    status=data_dict.get("status"),
                    created_by=data_dict.get("user"),
                    updated_by=data_dict.get("user")
                )

                session.add(new_auditing)
                session.flush()
                
                for response in data_dict.get("responses"):
                    new_response= AuditingResponse(
                        auditing_id=new_auditing.id_auditing,
                        item_id=response.get("item_id"),
                        response=response.get("response"),
                        observation=response.get("observation"),
                        created_by=data_dict.get("user"),
                        updated_by=data_dict.get("user")
                    )
                    session.add(new_response)

                for finding in data_dict.get("findings"):
                    new_finding= AuditingFinding(
                        auditing_id=new_auditing.id_auditing,
                        description=finding.get("description"),
                        criticality=finding.get("criticality"),
                        responsible=finding.get("responsible"),
                        commitment=finding.get("commitment"),
                    )
                    session.add(new_finding)
                    session.flush()

                    # Guardar imágenes del hallazgo
                    for image_name in finding.get("images"):
                        image = images.get(image_name)

                        if image:
                            result = self.save_image(image, "findings")
                            saved_files.append(result["url"])
                            new_image = AuditingFindingsImg(
                                finding_auditing_id=new_finding.id_finding,
                                img_path=result["url"],
                            )

                            session.add(new_image)

                fields = [
                    "auditor_path",
                    "responsible_path",
                    "client_path",
                ]

                signature = AuditingSignaturesImg(
                    auditing_id=new_auditing.id_auditing,
                )

                for field in fields:
                    image = images.get(field.replace("_path", "_img"))

                    if image:
                        result = self.save_image(image, "signatures")
                        saved_files.append(result["url"])
                        setattr(signature, field, result["url"])

                session.add(signature)
                session.commit()
            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                session.rollback()

                #limpia archivos guardados si falla DB
                for path in saved_files:
                    full_path = os.path.join("/var/www", path.lstrip("/"))
                    if os.path.exists(full_path):
                        os.remove(full_path)

                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al insertar en la base de datos", 500)

            finally:
                session.close()


    def get_tech_materials(self, internal, external):
            with self.db.session_factory() as session:
                try:
                    query_stmt = select(TechnicalEquipment)
                    rows = session.execute(query_stmt).scalars().all()
    
                    data = [
                        {
                            "id_equipment": record.id_equipment,
                            "code": record.code,
                            "product": record.product,
                            "unit": record.unit,
                            "model": record.model,
                            "base_price": record.base_price,
                            "profit_margin": record.profit_margin,
                            "profit_margin_dollar": record.profit_margin_dollar,
                            "price": record.price,
                            "provider": record.provider,
                            "description": record.description,
                            "stock": record.stock,
                            "created_by": record.created_by,
                            "updated_by": record.updated_by,
                            "created_at": record.created_at,
                            "updated_at": record.updated_at
                        }
                        for record in rows
                    ]
    
                    return data
                
                except Exception as exception:
                    logger.error('Error: {}', str(exception), internal=internal, external=external)
                    if isinstance(exception, CustomAPIException):
                        raise exception
                    
                    raise CustomAPIException("Error al obtener en la base de datos", 500)


    def get_auditing_sections(self, internal, external):
        with self.db.session_factory() as session:
            try:
                query_stmt = (
                    select(AuditingSections, AuditingItem)
                    .outerjoin(
                        AuditingItem,
                        AuditingItem.section_id == AuditingSections.id_section
                    )
                    .order_by(
                        AuditingSections.order_number.asc(),
                        AuditingItem.order_number.asc()
                    )
                )

                rows = session.execute(query_stmt).all()

                sections = {}

                for section, item in rows:
                    if section.id_section not in sections:
                        sections[section.id_section] = {
                            "id_section": section.id_section,
                            "name": section.name,
                            "order_number": section.order_number,
                            "items": [],
                            "created_by": section.created_by,
                            "created_at": section.created_at,
                        }

                    if item:
                        sections[section.id_section]["items"].append({
                            "id_item": item.id_item,
                            "name": item.name,
                            "order_number": item.order_number,
                            "created_by": item.created_by,
                            "created_at": item.created_at,
                        })

                return list(sections.values())

            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)

                if isinstance(exception, CustomAPIException):
                    raise exception

                raise CustomAPIException("Error al obtener en la base de datos", 500)


    def update_status_project(self, id_task: int, body, internal: str, external: str) -> None:
        with self.db.session_factory() as session:
            try:
                users_id_send = []
                notyfication_type = body.get("notification_type")

                project = session.execute(
                    select(TaskTechnical)
                    .where(TaskTechnical.id_task == id_task)
                    .with_for_update()
                ).scalar_one_or_none()

                if not project:
                    raise CustomAPIException(
                        message="No existe el proyecto",
                        status_code=404
                    )

                history_entry = HistoryStatusProject(
                    tech_task_id=id_task,
                    status=body["new_status"],
                    previous_status=project.status,
                    commentary=body.get("commentary"),
                    created_by=body["user"]
                )
                
                project.status = body["new_status"]
                project.updated_by = body["user"]
                project.updated_at = datetime.now()

                if notyfication_type == "TECHNICAL_REQUEST_APPROVAL":
                    user_id = session.scalar(
                        select(Users.id_user).where(
                            Users.user == body["user"]
                        )
                    )
                    project.requested_by = str(user_id) if user_id else None
                    users_id_send.append("bce2f555-e458-4022-9a69-968e5dddf6bd") #jefe_tecnico

                elif notyfication_type == "TECHNICAL_APPROVAL_REQUEST_REJECTED" or notyfication_type == "TECHNICAL_APPROVAL_REQUEST_APPROVED":
                    users_id_send.append(project.requested_by)

                session.add(history_entry)
                session.flush()

                session.commit()

                try:
                    data_notification = {
                        "channel": "ZENTINEL",
                        "data": {
                            "data": {
                                "history_id": history_entry.id_history
                            },
                            "notification_type": notyfication_type,
                            "user_ids": users_id_send,
                            "variables": {
                                "username": body["user"],
                                "project_name": project.name
                            }
                        },
                        "externalTransactionId": external
                    }
                    # self.notification_client.send_notification(data_notification)
                    self.rabbitMQ.send_event(
                        routing_key="technical.callbacks.notification",
                        body=data_notification
                    )
                except Exception as e:
                    logger.error("Error enviando notificación: {}", str(e), internal=internal, external=external)

            except Exception as exception:
                session.rollback()
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception

                raise CustomAPIException("Error al actualizar en la base de datos", 500)

            finally:
                session.close()

    def get_technical_staff(self, internal, external):
        with self.db.session_factory() as session:
            try:
                query_stmt = select(TechnicalStaff)
                rows = session.execute(query_stmt).scalars().all()

                data = [
                    {
                        "id_staff": record.id_technical,
                        "name": record.name,
                        "created_by": record.created_by,
                        "updated_by": record.updated_by,
                        "created_at": record.created_at,
                        "updated_at": record.updated_at
                    }
                    for record in rows
                ]

                return data
            
            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al obtener en la base de datos", 500)

    def get_history_project(self, filters, internal, external):
        with self.db.session_factory() as session:
            try:

                tech_record_subq = (
                    select(
                        TechnicalRecord.task_id.label("task_id"),
                        func.json_agg(
                            func.json_build_object(
                                "id_record", TechnicalRecord.id_record,
                                "client_id", TechnicalRecord.client_id,
                                "location_id", TechnicalRecord.location_id,
                                "resume", TechnicalRecord.resume,
                                "created_by", TechnicalRecord.created_by,
                                "created_at", TechnicalRecord.created_at,
                            )
                        ).label("record_technical")
                    )
                    .group_by(TechnicalRecord.task_id)
                    .subquery()
                )

                query_stmt = (
                    select(
                        HistoryStatusProject,
                        TaskTechnical,
                        ClientLocation,
                        Client,
                        tech_record_subq.c.record_technical
                    )
                    .join(
                        TaskTechnical,
                        TaskTechnical.id_task
                        == HistoryStatusProject.tech_task_id
                    )
                    .outerjoin(
                        TaskLocation,
                        TaskLocation.task_id
                        == TaskTechnical.id_task
                    )
                    .outerjoin(
                        ClientLocation,
                        ClientLocation.id_location
                        == TaskLocation.location_id
                    )
                    .outerjoin(
                        Client,
                        Client.id_client
                        == ClientLocation.client_id
                    )
                    .outerjoin(
                        tech_record_subq,
                        tech_record_subq.c.task_id
                        == TaskTechnical.id_task
                    )
                    .order_by(
                        HistoryStatusProject.created_at.desc()
                    )
                )

                if filters.get("id_history"):
                    query_stmt = query_stmt.where(
                        HistoryStatusProject.id_history
                        == filters["id_history"]
                    )

                if filters.get("task_id"):
                    query_stmt = query_stmt.where(
                        HistoryStatusProject.tech_task_id
                        == filters["task_id"]
                    )

                rows = session.execute(query_stmt).all()

                data = [
                    {
                        "id_history": history.id_history,
                        "tech_task_id": history.tech_task_id,
                        "commentary": history.commentary,
                        "status": history.status,
                        "previous_status": history.previous_status,
                        "created_by": history.created_by,
                        "created_at": history.created_at,

                        "task": {
                            "id_task": task.id_task,
                            "name": task.name,
                            "client": client.name if client else None,
                            "client_id": client.id_client if client else None,
                            "description": task.description,
                            "location_id": (
                                location.id_location
                                if location else None
                            ),
                            "location": (
                                location.name
                                if location else None
                            ),
                            "code": task.code,
                            "status": task.status,
                            "record_technical": (
                                record_technical
                                if record_technical
                                else None
                            ),
                            "created_by": task.created_by,
                            "updated_by": task.updated_by,
                            "created_at": task.created_at,
                            "updated_at": task.updated_at,
                        }
                    }
                    for (
                        history,
                        task,
                        location,
                        client,
                        record_technical
                    ) in rows
                ]

                return data

            except Exception as exception:
                logger.error('Error: {}',str(exception),internal=internal,external=external)

                if isinstance(exception, CustomAPIException):
                    raise exception

                raise CustomAPIException("Error al obtener en la base de datos", 500)
            

    def get_task_technical_count_by_status(self, filtersBase, internal, external):
        with self.db.session_factory() as session:
            try:
                stmt = (
                    select(
                        TaskTechnical.status.label("status"),
                        func.count(TaskTechnical.id_task).label("count")
                    )
                    .select_from(TaskTechnical)
                )

                if filtersBase.get("user"):
                    stmt = stmt.where(
                        TaskTechnical.created_by == filtersBase.get("user")
                    )

                if filtersBase.get("start_date"):
                    stmt = stmt.where(
                        TaskTechnical.created_at >= filtersBase.get("start_date")
                    )

                if filtersBase.get("end_date"):
                    stmt = stmt.where(
                        TaskTechnical.created_at <= filtersBase.get("end_date")
                    )

                stmt = (
                    stmt
                    .group_by(TaskTechnical.status)
                    .order_by(TaskTechnical.status)
                )

                result = session.execute(stmt).all()

                task_count_by_status = [
                    {
                        "status": row.status,
                        "count": row.count
                    }
                    for row in result
                ]

                return task_count_by_status

            except Exception as exception:
                logger.error('Error: {}',str(exception),internal=internal,external=external)

                if isinstance(exception, CustomAPIException):
                    raise exception

                raise CustomAPIException("Error al obtener el resumen de tareas técnicas por status en la base de datos", 500)


    def get_task_technical_audit_percentage(self, filtersBase, internal, external):
        with self.db.session_factory() as session:
            try:
                # Subconsulta: determina si la tarea tiene al menos una auditoría
                audited_exists = (
                    select(Auditing.id_auditing)
                    .where(
                        Auditing.task_id == TaskTechnical.id_task
                    )
                    .exists()
                )

                stmt = (
                    select(
                        func.count(TaskTechnical.id_task).label("total"),
                        func.count(
                            case(
                                (audited_exists, 1)
                            )
                        ).label("audited")
                    )
                    .select_from(TaskTechnical)
                )

                if filtersBase.get("user"):
                    stmt = stmt.where(
                        TaskTechnical.created_by == filtersBase.get("user")
                    )

                if filtersBase.get("start_date"):
                    stmt = stmt.where(
                        TaskTechnical.created_at >= filtersBase.get("start_date")
                    )

                if filtersBase.get("end_date"):
                    stmt = stmt.where(
                        TaskTechnical.created_at <= filtersBase.get("end_date")
                    )

                return session.execute(stmt).one()

            except Exception as exception:
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                raise CustomAPIException("Error al obtener el porcentaje de tareas técnicas auditadas", 500)