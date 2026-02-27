from swagger_server.models.db.movilization_control import MovilizationControl
from swagger_server.repository.technical_repository import TechnicalRepository


class TechnicalUseCase:

    def __init__(self, technical_control_repository: TechnicalRepository):
        self.technical_control_repository = technical_control_repository

    def post_technical_control(self, body, internal, external) -> None:
        

        self.technical_control_repository.post_technical_control(body, internal, external)

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