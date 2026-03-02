from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from swagger_server.models.db.level_gasoline import LevelGasoline
from swagger_server.models.db.client_projects import ClientProject
from swagger_server.models.db.movilization_control import MovilizationControl
from swagger_server.models.db.movilization_status import MovilizationStatus
from swagger_server.models.db.movilization_client import MovilizationClient
from swagger_server.models.db.movilization_reason import MovilizationReason
from swagger_server.models.db.movilization_copilot import MovilizationCopilot
