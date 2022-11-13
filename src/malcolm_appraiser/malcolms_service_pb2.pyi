from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

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

class Samples(_message.Message):
    __slots__ = ["coordinates", "uuid"]
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    coordinates: _containers.RepeatedScalarFieldContainer[float]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ..., coordinates: _Optional[_Iterable[float]] = ...) -> None: ...

class TrueSamples(_message.Message):
    __slots__ = ["coordinates", "posterior_values", "uuid"]
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    POSTERIOR_VALUES_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    coordinates: _containers.RepeatedScalarFieldContainer[float]
    posterior_values: _containers.RepeatedScalarFieldContainer[float]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ..., coordinates: _Optional[_Iterable[float]] = ..., posterior_values: _Optional[_Iterable[float]] = ...) -> None: ...

class UUID(_message.Message):
    __slots__ = ["uuid"]
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class WalkRequest(_message.Message):
    __slots__ = ["number_of_samples", "starting_point", "uuid"]
    NUMBER_OF_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    STARTING_POINT_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    number_of_samples: int
    starting_point: _containers.RepeatedScalarFieldContainer[float]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ..., starting_point: _Optional[_Iterable[float]] = ..., number_of_samples: _Optional[int] = ...) -> None: ...
