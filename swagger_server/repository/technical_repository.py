import os

from loguru import logger
from sqlalchemy.orm import aliased

from swagger_server.exception.custom_error_exception import CustomAPIException
from swagger_server.models.db.client_projects import ClientProject
from swagger_server.models.db.level_gasoline import LevelGasoline
from swagger_server.models.db.movilization_client import MovilizationClient
from swagger_server.models.db.movilization_control import MovilizationControl
from swagger_server.models.db.movilization_copilot import MovilizationCopilot
from swagger_server.models.db.movilization_images import MovilizationImages
from swagger_server.models.db.movilization_reason import MovilizationReason
from swagger_server.models.db.movilization_status import MovilizationStatus
from swagger_server.models.db.reasons_movilization import ReasonsMovilization
from swagger_server.models.db.vehicle_copilot import VehicleCopilot
from swagger_server.models.db.vehicle_driver import VehicleDriver
from swagger_server.models.db.vehicle_license import VehicleLicense
from swagger_server.resources.databases.postgresql import PostgreSQLClient
from sqlalchemy import JSON, cast, distinct, exists, func, select, text

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
                cpt= VehicleCopilot
                dvh = VehicleDriver
                lvh = VehicleLicense
                gsl = LevelGasoline
                sts = MovilizationStatus
                
                gsl_initial = aliased(gsl)
                gsl_final = aliased(gsl)

                clients_agg = func.coalesce(
                    func.json_agg(
                        func.distinct(
                            func.jsonb_build_object(
                                "id", cp.id_client_projects,
                                "name", cp.name
                            )
                        )
                    ).filter(cp.id_client_projects != None),
                    func.cast('[]', JSON)
                ).label("clients")

                reasons_agg = func.coalesce(
                    func.json_agg(
                        func.distinct(
                            func.jsonb_build_object(
                                "id", rs.id_reason,
                                "name", rs.name
                            )
                        )
                    ).filter(rs.id_reason != None),
                    func.cast('[]', JSON)
                ).label("reasons")

                copilots_agg = func.coalesce(
                    func.json_agg(
                        func.distinct(
                            func.jsonb_build_object(
                                "id", cpt.id_copilot,
                                "name", cpt.name
                            )
                        )
                    ).filter(cpt.id_copilot != None),
                    func.cast('[]', JSON)
                ).label("copilots")

                query = (
                    session.query(
                        mvc,
                        clients_agg,
                        reasons_agg,
                        copilots_agg,
                        dvh.name.label("name_driver"),
                        gsl_initial.name.label("name_gasoline_initial"),
                        gsl_final.name.label("name_gasoline_final"),
                        lvh.name.label("license"),
                        sts.name.label("name_status"),
                        func.coalesce(
                            func.array_agg(mimg.image_path)
                                .filter(mimg.image_path.isnot(None)),
                            []
                        ).label("images")
                    )
                    .outerjoin(mcc, mcc.movilization_id == mvc.id_movilization)
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
                    .outerjoin(
                        mimg,
                        mimg.movilization_id == mvc.id_movilization
                    )
                    .group_by(
                        mvc.id_movilization,
                        dvh.name,
                        gsl_initial.name,
                        gsl_final.name,
                        sts.name,
                        lvh.name,
                        mvc.created_at,
                    )
                    .order_by(mvc.created_at.desc())
                )
                result = session.execute(query).all()

                return result

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

                movilization = MovilizationControl(
                    driver_id=data.get('id_driver'),
                    destiny=data.get('destiny'),
                    initial_km=data.get('initial_km'),
                    exit_point=data.get('route_point'),
                    observations=data.get('observations'),
                    license_id=data.get('id_truck_license'),
                    initial_gasoline_id=data.get('initial_gasoline_id'),
                    status=1
                )

                session.add(movilization)
                session.flush()

                movilization_id = movilization.id_movilization

                for id_project in data.get('project'):
                    client = MovilizationClient(
                        movilization_id=movilization_id,
                        client_project_id=id_project
                    )
                    session.add(client)

                for id_reason in data.get('reasons'):
                    reason = MovilizationReason(
                        movilization_id=movilization_id,
                        reason_id=id_reason
                    )
                    session.add(reason)
                
                for id_copilot in data.get('driver_companion'):
                    copilot = MovilizationCopilot(
                        movilization_id=movilization_id,
                        copilot_id=id_copilot
                    )
                    session.add(copilot)

                #Guardar imágenes (máx 10)
                for file in images[:10]:
                    result = self.save_image(file)
                    saved_files.append(result["url"])

                    image = MovilizationImages(
                        movilization_id=movilization_id,
                        image_path=result["url"],
                        type="iniciales"
                    )

                    session.add(image)

                session.commit()
                # category_exists = session.execute(
                #     select(
                #         exists().where(
                #             Category.id_category == logbook_entry_body.category_id
                #         )
                #     )
                # ).scalar()

                # unity_weight_exists = session.execute(
                #     select(
                #         exists().where(
                #             UnityWeight.id_unity == logbook_entry_body.unity_id
                #         )
                #     )
                # ).scalar()

                # group_business_exists = session.execute(
                #     select(GroupBusiness).where(
                #         GroupBusiness.id_group_business == logbook_entry_body.group_business_id
                #     )
                # ).scalar_one_or_none()

                # category = session.execute(
                #     select(Category).where(
                #         Category.id_category == logbook_entry_body.category_id
                #     )
                # ).scalar_one_or_none()

                # if not category_exists:
                #     raise CustomAPIException(
                #         message="No existe la categoría",
                #         status_code=404
                #     )
                
                # if not unity_weight_exists:
                #     raise CustomAPIException(
                #         message="No existe la unidad de peso",
                #         status_code=404
                #     )
                
                # if not group_business_exists:
                #     raise CustomAPIException(
                #         message="No existe el grupo de negocio",
                #         status_code=404
                #     )
                
                # session.add(logbook_entry_body)
                # session.flush()
                
                # logbook_entry_id = logbook_entry_body.id_logbook_entry

                # #Guardar imágenes (máx 10)
                # for file in images[:10]:
                #     if logbook_entry_body.shipping_guide == 'test daniel':
                #         result = self.save_image(file)
                #     else:
                #         result = self.save_image_as_webp(file)
                #     saved_files.append(result["url"])

                #     image = LogbookImages(
                #         logbook_id_entry=logbook_entry_id,
                #         image_path=result["url"]
                #     )

                #     session.add(image)

                # session.commit()

                # logbook_entry_dict = logbook_entry_body.to_dict()
                # logbook_entry_dict["name_category"] = category.name_category
                # logbook_entry_dict["group_name"] = group_business_exists.name

                # self.redis_client.client.publish(
                #     "logbook_channel",
                #     json.dumps({
                #         "type": "logbook_saved",
                #         "logbook": logbook_entry_dict
                #     })
                # )

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