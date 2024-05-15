from collections.abc import Callable, Container
from datetime import datetime

from . import _ViewFuncT

def conditional_page(view_func: _ViewFuncT, /) -> _ViewFuncT: ...
def require_http_methods(request_method_list: Container[str]) -> Callable[[_ViewFuncT], _ViewFuncT]: ...
def require_GET(func: _ViewFuncT, /) -> _ViewFuncT: ...
def require_POST(func: _ViewFuncT, /) -> _ViewFuncT: ...
def require_safe(func: _ViewFuncT, /) -> _ViewFuncT: ...
def condition(
    etag_func: Callable[..., str | None] | None = ..., last_modified_func: Callable[..., datetime | None] | None = ...
) -> Callable[[_ViewFuncT], _ViewFuncT]: ...
def etag(etag_func: Callable[..., str | None]) -> Callable[[_ViewFuncT], _ViewFuncT]: ...
def last_modified(last_modified_func: Callable[..., datetime | None]) -> Callable[[_ViewFuncT], _ViewFuncT]: ...
