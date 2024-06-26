import json
from collections.abc import Callable, Sequence
from datetime import date, time, timedelta
from datetime import datetime as real_datetime
from decimal import Decimal
from typing import Any

from django.core.management.color import Style
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.utils import CursorWrapper
from django.db.models.base import Model
from django.db.models.constants import OnConflict
from django.db.models.expressions import Case, Col, Expression
from django.db.models.fields import Field
from django.db.models.sql.compiler import SQLCompiler
from typing_extensions import TypeAlias

_Converter: TypeAlias = Callable[[Any, Expression, BaseDatabaseWrapper], Any]

class BaseDatabaseOperations:
    compiler_module: str
    integer_field_ranges: dict[str, tuple[int, int]]
    set_operators: dict[str, str]
    cast_data_types: dict[Any, Any]
    cast_char_field_without_max_length: str | None
    PRECEDING: str
    FOLLOWING: str
    UNBOUNDED_PRECEDING: str
    UNBOUNDED_FOLLOWING: str
    CURRENT_ROW: str
    explain_prefix: str | None
    connection: BaseDatabaseWrapper
    def __init__(self, connection: BaseDatabaseWrapper) -> None: ...
    def autoinc_sql(self, table: str, column: str) -> str | None: ...
    def bulk_batch_size(self, fields: Any, objs: Any) -> int: ...
    def cache_key_culling_sql(self) -> str: ...
    def unification_cast_sql(self, output_field: Field) -> str: ...
    def date_extract_sql(self, lookup_type: str, sql: Any, params: Any) -> tuple[str, Any]: ...
    # def date_interval_sql(self, timedelta: None) -> Any: ...
    def date_trunc_sql(self, lookup_type: str, sql: str, params: Any, tzname: str | None = ...) -> tuple[str, Any]: ...
    def datetime_cast_date_sql(self, sql: str, params: Any, tzname: str | None) -> tuple[str, Any]: ...
    def datetime_cast_time_sql(self, sql: str, params: Any, tzname: str | None) -> tuple[str, Any]: ...
    def datetime_extract_sql(self, lookup_type: str, sql: str, params: Any, tzname: str | None) -> tuple[str, Any]: ...
    def datetime_trunc_sql(self, lookup_type: str, sql: str, params: Any, tzname: str | None) -> str: ...
    def time_trunc_sql(self, lookup_type: str, sql: str, params: Any, tzname: str | None = ...) -> str: ...
    def time_extract_sql(self, lookup_type: str, sql: str, params: Any) -> str: ...
    def deferrable_sql(self) -> str: ...
    def distinct_sql(self, fields: list[str], params: list[Any] | None) -> tuple[list[str], list[str]]: ...
    def fetch_returned_insert_columns(self, cursor: Any, returning_params: Any) -> Any: ...
    def field_cast_sql(self, db_type: str | None, internal_type: str) -> str: ...
    def force_no_ordering(self) -> list[Any]: ...
    def for_update_sql(self, nowait: bool = ..., skip_locked: bool = ..., of: Any = ..., no_key: bool = ...) -> str: ...
    def limit_offset_sql(self, low_mark: int, high_mark: int | None) -> str: ...
    def last_executed_query(self, cursor: Any, sql: Any, params: Any) -> str: ...
    def last_insert_id(self, cursor: CursorWrapper, table_name: str, pk_name: str) -> int: ...
    def lookup_cast(self, lookup_type: str, internal_type: str | None = ...) -> str: ...
    def max_in_list_size(self) -> int | None: ...
    def max_name_length(self) -> int | None: ...
    def no_limit_value(self) -> str | None: ...
    def pk_default_value(self) -> str: ...
    def prepare_sql_script(self, sql: Any) -> list[str]: ...
    def process_clob(self, value: str) -> str: ...
    def return_insert_columns(self, fields: list[Field[Any, Any]]) -> tuple[str, list[Any]]: ...
    def compiler(self, compiler_name: str) -> type[SQLCompiler]: ...
    def quote_name(self, name: str) -> str: ...
    def regex_lookup(self, lookup_type: str) -> str: ...
    def savepoint_create_sql(self, sid: str) -> str: ...
    def savepoint_commit_sql(self, sid: str) -> str: ...
    def savepoint_rollback_sql(self, sid: str) -> str: ...
    def set_time_zone_sql(self) -> str: ...
    def sql_flush(
        self, style: Style, tables: Sequence[str], *, reset_sequences: bool = ..., allow_cascade: bool = ...
    ) -> list[str]: ...
    def execute_sql_flush(self, sql_list: list[str]) -> None: ...
    def sequence_reset_by_name_sql(self, style: Style, sequences: list[dict[str, str | None]]) -> list[str]: ...
    def sequence_reset_sql(self, style: Style, model_list: list[type[Model]]) -> list[str]: ...
    def start_transaction_sql(self) -> str: ...
    def end_transaction_sql(self, success: bool = ...) -> str: ...
    def tablespace_sql(self, tablespace: str, inline: bool = ...) -> str: ...
    def prep_for_like_query(self, x: object) -> str: ...
    def prep_for_iexact_query(self, x: object) -> str: ...
    def validate_autopk_value(self, value: int) -> int: ...
    def adapt_unknown_value(self, value: Any) -> Any: ...
    def adapt_datefield_value(self, value: date | None) -> str | None: ...
    def adapt_datetimefield_value(self, value: real_datetime | None) -> str | None: ...
    def adapt_timefield_value(self, value: real_datetime | time | None) -> str | None: ...
    def adapt_decimalfield_value(
        self, value: Decimal | None, max_digits: int | None = ..., decimal_places: int | None = ...
    ) -> str | None: ...
    def adapt_ipaddressfield_value(self, value: str | None) -> str | None: ...
    def adapt_json_value(self, value: Any, encoder: type[json.JSONEncoder] | None) -> str: ...
    def adapt_integerfield_value(self, value: Any, internal_type: Any) -> Any: ...
    def year_lookup_bounds_for_date_field(self, value: int, iso_year: bool = ...) -> list[str]: ...
    def year_lookup_bounds_for_datetime_field(self, value: int, iso_year: bool = ...) -> list[str]: ...
    def get_db_converters(self, expression: Expression) -> list[_Converter]: ...
    def convert_durationfield_value(
        self, value: float | None, expression: Expression, connection: BaseDatabaseWrapper
    ) -> timedelta | None: ...
    def check_expression_support(self, expression: Expression) -> None: ...
    def conditional_expression_supported_in_where_clause(self, expression: Expression) -> bool: ...
    def combine_expression(self, connector: str, sub_expressions: list[str]) -> str: ...
    def combine_duration_expression(self, connector: str, sub_expressions: list[str]) -> str: ...
    def binary_placeholder_sql(self, value: Case | None) -> str: ...
    def modify_insert_params(self, placeholder: str, params: Any) -> Any: ...
    def integer_field_range(self, internal_type: Any) -> tuple[int, int]: ...
    def subtract_temporals(self, internal_type: Any, lhs: Any, rhs: Any) -> tuple[str, tuple[Any, ...]]: ...
    def window_frame_start(self, start: Any) -> str: ...
    def window_frame_end(self, end: Any) -> str: ...
    def window_frame_rows_start_end(self, start: int | None = ..., end: int | None = ...) -> tuple[str, str]: ...
    def window_frame_range_start_end(self, start: int | None = ..., end: int | None = ...) -> tuple[str, str]: ...
    def explain_query_prefix(self, format: str | None = ..., **options: Any) -> str: ...
    def insert_statement(self, on_conflict: OnConflict | None = ...) -> str: ...
    def on_conflict_suffix_sql(
        self, fields: Any, on_conflict: Any, update_fields: Any, unique_fields: Any
    ) -> str | Any: ...
    def format_for_duration_arithmetic(self, sql: str) -> str: ...
    def prepare_join_on_clause(
        self, lhs_table: str, lhs_field: Field, rhs_table: str, rhs_field: Field
    ) -> tuple[Col, Col]: ...
