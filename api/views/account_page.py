from dataclasses import dataclass
import logging
from typing import Callable
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class AccountPageDTO:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {"id": self.id, "name": self.name}


@dataclass
class DTOBuilder:
    id: str = None
    name: str = None


class AccountPage(viewsets.ModelViewSet):
    @action(detail=False, methods=['get'], url_path='page')
    def account_page(self, request, *args, **kwargs):
        token = request.headers.get("Authorization", "")
        logger.info("account_page")

        to_dto = self.to_home_page_dto(additional_processing=lambda builder: setattr(builder, 'name', 'name') or builder)
        return Response(to_dto.to_dict())

    def to_home_page_dto(self, additional_processing: Callable[[DTOBuilder], DTOBuilder] = None):
        builder = DTOBuilder()
        if additional_processing:
            builder = additional_processing(builder)
        builder.id = "1"
        return self.to_dto(builder)

    @staticmethod
    def to_dto(dto_builder: DTOBuilder):
        return AccountPageDTO(dto_builder.id, dto_builder.name)
