






from loguru import logger

from swagger_server.exception.custom_error_exception import CustomAPIException
from swagger_server.resources.databases.postgresql import PostgreSQLClient
from sqlalchemy import cast, exists, func, select


class TechnicalRepository:
    
    def __init__(self):
        self.db = PostgreSQLClient("POSTGRESQL")


    def post_logbook_entry(self, logbook_entry_body, images, internal, external) -> None:
        saved_files = []

        if len(images) > 10:
            raise CustomAPIException("Máximo 10 imagenes", 500)

        with self.db.session_factory() as session:
            try:
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
                logger.error('Error: {}', str(exception), internal=internal, external=external)
                if isinstance(exception, CustomAPIException):
                    raise exception
                
                raise CustomAPIException("Error al insertar en la base de datos", 500)

            finally:
                session.close()