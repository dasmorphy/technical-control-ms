






import os

from loguru import logger

from swagger_server.exception.custom_error_exception import CustomAPIException
from swagger_server.models.db.movilization_client import MovilizationClient
from swagger_server.models.db.movilization_control import MovilizationControl
from swagger_server.models.db.movilization_images import MovilizationImages
from swagger_server.models.db.movilization_reason import MovilizationReason
from swagger_server.models.db.vehicle_driver import VehicleDriver
from swagger_server.resources.databases.postgresql import PostgreSQLClient
from sqlalchemy import cast, exists, func, select, text

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


    def post_technical_control(self, data, internal, external) -> None:
        saved_files = []

        if data.get('initial_images') and len(data.get('initial_images')) > 10:
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
                    initial_gasoline=data.get('initial_gasoline'),
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

                #Guardar imágenes (máx 10)
                for file in data.get('initial_images')[:10]:
                    result = self.save_image(file)
                    saved_files.append(result["url"])

                    image = MovilizationImages(
                        movilization_id=movilization_id,
                        image_path=result["url"],
                        type="iniciales"
                    )

                    session.add(image)

                return
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