# app/filters/operators.py

from sqlalchemy import and_, or_
from sqlalchemy.sql import operators
from .utils import _adjust_date_range

LOGICAL_OPERATORS = {
    "$and": and_,
    "$or": or_
}

COMPARISON_OPERATORS = {
    "$eq": lambda column, value: (
        column.is_(None) if value == ""
        else (
            adjusted_value if is_range else column == adjusted_value
        )
        if (adjusted_value := _adjust_date_range(column, value, "$eq")[0]) is not None and (is_range := _adjust_date_range(column, value, "$eq")[1]) is not None
        else column == value
    ),
    "$ne": lambda column, value: (
        column.is_not(None) if value == ""
        else (
            adjusted_value if is_range else column != adjusted_value
        )
        if (adjusted_value := _adjust_date_range(column, value, "$ne")[0]) is not None and (is_range := _adjust_date_range(column, value, "$ne")[1]) is not None
        else column != value
    ),
    "$gt": lambda column, value: operators.gt(column, _adjust_date_range(column, value, "$gt")[0]),
    "$gte": lambda column, value: operators.ge(column, _adjust_date_range(column, value, "$gte")[0]),
    "$lt": lambda column, value: operators.lt(column, _adjust_date_range(column, value, "$lt")[0]),
    "$lte": lambda column, value: operators.le(column, _adjust_date_range(column, value, "$lte")[0]),
    "$in": lambda column, value: (
        or_(*[
            _adjust_date_range(column, v, "$eq")[
                0] if isinstance(v, str) else column == v
            for v in value
        ])
    ),
    "$contains": lambda column, value: column.ilike(f"%{value}%"),
    "$ncontains": lambda column, value: ~column.ilike(f"%{value}%"),
    "$startswith": lambda column, value: column.ilike(f"{value}%"),
    "$endswith": lambda column, value: column.ilike(f"%{value}"),
    "$isnotempty": lambda column: column.is_not(None),
    "$isempty": lambda column: column.is_(None),
    "$isanyof": lambda column, value: (
        or_(*[
            _adjust_date_range(column, v, "$eq")[
                0] if isinstance(v, str) else column == v
            for v in value
        ])
    )
}
