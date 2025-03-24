# fastapi_querybuilder/params.py

from typing import Optional
from fastapi import Query


class QueryParams:
    def __init__(
        self,
        filters: Optional[str] = Query(None,description="A JSON string representing filter conditions."),
        sort: Optional[str] = Query(None,description="e.g. name:asc or user__email:desc"),
        search: Optional[str] = Query(None,description="A string for global search across string fields.")
    ):
        self.filters = filters
        self.search = search
        self.sort = sort
