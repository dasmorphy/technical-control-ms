from swagger_server.models.db.movilization_control import MovilizationControl
from swagger_server.repository.technical_repository import TechnicalRepository


class TechnicalUseCase:

    def __init__(self, technical_control_repository: TechnicalRepository):
        self.technical_control_repository = technical_control_repository

    def post_technical_control(self, body, images, internal, external) -> None:
        

        self.technical_control_repository.post_technical_control(body, images, internal, external)

    def get_all_drivers(self, internal, external):
        return self.technical_control_repository.get_all_drivers(internal, external)
    
    def get_all_licenses(self, internal, external):
        return self.technical_control_repository.get_all_licenses(internal, external)
    
    def get_all_reasons(self, internal, external):
        return self.technical_control_repository.get_all_reasons(internal, external)
    
    def get_all_copilot(self, internal, external):
        return self.technical_control_repository.get_all_copilot(internal, external)
    
    def get_all_projects(self, internal, external):
        return self.technical_control_repository.get_all_projects(internal, external)
    
    def get_all_level_gasoline(self, internal, external):
        return self.technical_control_repository.get_all_level_gasoline(internal, external)
    
    def get_all_tech_control(self, internal, external):
        rows = self.technical_control_repository.get_all_tech_control(internal, external)

        results = [
            {
                "exit_date": mvc.exit_date,
                "arrival_date": mvc.arrival_date,
                "license_id": mvc.license_id,
                "initial_km": mvc.initial_km,
                "final_km": mvc.final_km,
                "final_gasoline_id": mvc.final_gasoline_id,
                "initial_gasoline_id": mvc.initial_gasoline_id,
                "destiny": mvc.destiny,
                "exit_point": mvc.exit_point,
                "clients": clients,
                "reasons": reasons,
                "copilots": copilots,
                "created_at": mvc.created_at,
                "updated_at": mvc.updated_at,
                "created_by": mvc.created_by,
                "updated_by": mvc.updated_by,
                "images": images,
                "name_driver": name_driver,
                "name_gasoline_final": name_gasoline_final,
                "name_gasoline_initial": name_gasoline_initial,
                "license": license
            }
            for mvc, clients, reasons, copilots, name_driver, name_gasoline_initial, name_gasoline_final, license, images in rows  # desempaquetar tupla
        ]
        
        return results

