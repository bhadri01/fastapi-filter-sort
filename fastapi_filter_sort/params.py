# fastapi_querybuilder/params.py

from typing import Optional
from fastapi import Query


class QueryParams:
    def __init__(
        self,
        filters: Optional[str] = Query(
            None, description="JSON-encoded filters"),
        search: Optional[str] = Query(None),
        sort: Optional[str] = Query(
            None, description="e.g. name:asc or user__email:desc")
    ):
        self.filters = filters
        self.search = search
        self.sort = sort
