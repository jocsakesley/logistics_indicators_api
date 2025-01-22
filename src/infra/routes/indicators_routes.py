

from flask import Blueprint, request

from src.controllers.indicators.get_sla_controller import GetSLAController
from src.controllers.indicators.get_productivity_controller import GetProductivityController
from src.models.customer_service_model import CustomerServiceModel
from src.infra.db import db
from src.repositories.repository import Repository
from src.usecases.indicators.get_productivity_use_case import GetProductivityUseCase
from src.usecases.indicators.get_sla_use_case import GetSLAAngelUseCase, GetSLAPoloUseCase


indicator_bp = Blueprint('indicators', __name__)

@indicator_bp.get('/indicators/productivity')
def get_indicators():
    repository = Repository(db.DbSession, CustomerServiceModel)
    use_case = GetProductivityUseCase(repository)
    return GetProductivityController(use_case).handle(request=request)

@indicator_bp.get('/indicators/sla/angel')
def get_sla_angel():
    repository = Repository(db.DbSession, CustomerServiceModel)
    use_case = GetSLAAngelUseCase(repository)
    return GetSLAController(use_case).handle(request=request)

@indicator_bp.get('/indicators/sla/polo')
def get_sla_polo():
    repository = Repository(db.DbSession, CustomerServiceModel)
    use_case = GetSLAPoloUseCase(repository)
    return GetSLAController(use_case).handle(request=request)