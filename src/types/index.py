# src/types/index.py

from typing import Any, Dict, List, Optional, Union

# Custom types for the application
QueryResult = Dict[str, Any]
QueryResults = List[QueryResult]
DatabaseConnection = Dict[str, Union[str, int, float]]
ResponseModel = Dict[str, Any]
OptionalResponse = Optional[ResponseModel]