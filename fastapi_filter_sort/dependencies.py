# fastapi_querybuilder/dependencies.py

from fastapi import Depends, Request
from sqlalchemy.orm import Session
from .params import QueryParams
from .builder import build_query
from typing import Type, Callable


def QueryBuilder(model: Type, get_db: Callable[[], Session]):
    def wrapper(
        request: Request,
        db: Session = Depends(get_db),
        params: QueryParams = Depends()
    ):
        return build_query(model, db, params)
    return Depends(wrapper)
