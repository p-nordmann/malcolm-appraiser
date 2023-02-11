from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Boundaries(_message.Message):
    __slots__ = ["dimension", "infima", "suprema"]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    INFIMA_FIELD_NUMBER: _ClassVar[int]
    SUPREMA_FIELD_NUMBER: _ClassVar[int]
    dimension: int
    infima: _containers.RepeatedScalarFieldContainer[float]
    suprema: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, dimension: _Optional[int] = ..., infima: _Optional[_Iterable[float]] = ..., suprema: _Optional[_Iterable[float]] = ...) -> None: ...

class BoundariesUUID(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class MakeSamplesRequest(_message.Message):
    __slots__ = ["amount", "origin", "uuid"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    amount: int
    origin: _containers.RepeatedScalarFieldContainer[float]
    uuid: PosteriorUUID
    def __init__(self, uuid: _Optional[_Union[PosteriorUUID, _Mapping]] = ..., origin: _Optional[_Iterable[float]] = ..., amount: _Optional[int] = ...) -> None: ...

class PosteriorUUID(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class PosteriorValuesBatch(_message.Message):
    __slots__ = ["coordinates", "posterior_values", "uuid"]
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    POSTERIOR_VALUES_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    coordinates: _containers.RepeatedScalarFieldContainer[float]
    posterior_values: _containers.RepeatedScalarFieldContainer[float]
    uuid: BoundariesUUID
    def __init__(self, uuid: _Optional[_Union[BoundariesUUID, _Mapping]] = ..., coordinates: _Optional[_Iterable[float]] = ..., posterior_values: _Optional[_Iterable[float]] = ...) -> None: ...

class SamplesBatch(_message.Message):
    __slots__ = ["coordinates"]
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    coordinates: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, coordinates: _Optional[_Iterable[float]] = ...) -> None: ...
