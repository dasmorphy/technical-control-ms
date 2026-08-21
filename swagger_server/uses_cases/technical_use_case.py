from swagger_server.models.db.movilization_control import MovilizationControl
from swagger_server.models.db.task_technical import TaskTechnical
from swagger_server.models.task_data import TaskData
from swagger_server.repository.technical_repository import TechnicalRepository


class TechnicalUseCase:

    def __init__(self, technical_control_repository: TechnicalRepository):
        self.technical_control_repository = technical_control_repository

    def post_technical_control(self, body, images, internal, external) -> None:
        self.technical_control_repository.post_technical_control(body, images, internal, external)

    def put_technical_control(self, body, images, internal, external) -> None:
        self.technical_control_repository.put_technical_control(body, images, internal, external)

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
                "id_movilization": row[0],
                "exit_date": row[1],
                "arrival_date": row[2],
                "initial_km": row[3],
                "final_km": row[4],
                "destiny": row[5],
                "exit_point": row[6],
                "observations": row[7],
                "status_id": row[8],
                "created_at": row[9],
                "updated_at": row[10],
                "created_by": row[11],
                "updated_by": row[12],
                "clients": row[13],
                "reasons": row[14],
                "copilots": row[15],
                "images": row[16],
                "name_driver": row[17],
                "initial_gasoline_id": row[18],
                "name_gasoline_initial": row[19],
                "final_gasoline_id": row[20],
                "name_gasoline_final": row[21],
                "license_id": row[22],
                "license": row[23],
                "name_status": row[24],
            }
            for row in rows  # desempaquetar tupla
        ]
        
        return results
    
    def get_clients(self, internal, external):
        return self.technical_control_repository.get_clients(internal, external)
    
    def get_location(self, params, internal, external):
        clients = params.get("client_id")

        filters = {
            "clients": [int(x) for x in clients.split(",")] if clients else [],
        }

        return self.technical_control_repository.get_location(filters, internal, external)

    
    def get_task(self, params, internal, external):
        locations = params.get("locations")
        clients = params.get("clients")
        clients = params.get("clients")
        status = params.get("status")

        filters = {
            "locations": [int(x) for x in locations.split(",")] if locations else [],
            "clients": [int(x) for x in clients.split(",")] if clients else [],
            "status": [x for x in status.split(",")] if status else [],
            "support": params.get("support")
        }

        return self.technical_control_repository.get_task(filters, internal, external)
    
    def post_task(self, data: TaskData, internal, external):
        self.technical_control_repository.post_task(data, internal, external)

    
    def post_auditing(self, data, images, internal, external):
        self.technical_control_repository.post_auditing(data, images, internal, external)

    
    def get_tech_record(self, params, internal, external):
        locations = params.get("locations")
        clients = params.get("clients")
        tasks = params.get("tasks")
        
        filters = {
            "locations": [int(x) for x in locations.split(",")] if locations else [],
            "clients": [int(x) for x in clients.split(",")] if clients else [],
            "tasks": [int(x) for x in tasks.split(",")] if tasks else [],
            "user": params.get("user"),
            "id_tech_record": [int(params.get("id-record"))] if params.get("id-record") else []
        }

        return self.technical_control_repository.get_tech_record(filters, internal, external)
    
    def get_auditing(self, params, internal, external):
        locations = params.get("locations")
        clients = params.get("clients")
        tasks = params.get("tasks")
        
        filters = {
            "locations": [int(x) for x in locations.split(",")] if locations else [],
            "clients": [int(x) for x in clients.split(",")] if clients else [],
            "tasks": [int(x) for x in tasks.split(",")] if tasks else [],
        }

        return self.technical_control_repository.get_auditing(filters, internal, external)


    def get_tech_materials(self, internal, external):
        return self.technical_control_repository.get_tech_materials(internal, external)

    def get_auditing_sections(self, internal, external):
        return self.technical_control_repository.get_auditing_sections(internal, external)

    def update_status_project(self, id_task: int, body, internal: str, external: str) -> None:
        self.technical_control_repository.update_status_project(id_task, body, internal, external)

    def get_technical_staff(self, internal, external):
        return self.technical_control_repository.get_technical_staff(internal, external)

    def get_history_project(self, params, internal, external):        
        filters = {
            "id_history": params.get("id_history"),
            "task_id": params.get("task_id")
        }

        return self.technical_control_repository.get_history_project(filters, internal, external)

    def resume_graphs(self, params, internal, external):
        filters = {
            "start_date": params.get("start_date"),
            "end_date": params.get("end_date"),
            "user": params.get("user")
        }

        count_status = self.technical_control_repository.get_task_technical_count_by_status(filters, external, internal)
        auditing_percentaje = self.get_auditing_percentaje(filters, internal, external)

        return {
            "count_status": count_status,
            "auditing_percentaje": auditing_percentaje
        }

    def get_auditing_percentaje(self, filters, internal, external):
        result = self.technical_control_repository.get_task_technical_audit_percentage(filters, internal, external)
        total = result.total
        audited = result.audited
        not_audited = total - audited

        audited_percentage = (
            (audited / total) * 100
            if total > 0
            else 0
        )

        not_audited_percentage = (
            (not_audited / total) * 100
            if total > 0
            else 0
        )

        return {
            "total": total,
            "audited": audited,
            "not_audited": not_audited,
            "audited_percentage": round(audited_percentage, 2),
            "not_audited_percentage": round(not_audited_percentage, 2)
        }
