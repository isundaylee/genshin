from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SceneAreaWeatherNotify(_message.Message):
    __slots__ = ("trans_duration", "weather_value_map", "weather_area_id", "climate_type", "weather_gadget_id")
    class WeatherValueMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    TRANS_DURATION_FIELD_NUMBER: _ClassVar[int]
    WEATHER_VALUE_MAP_FIELD_NUMBER: _ClassVar[int]
    WEATHER_AREA_ID_FIELD_NUMBER: _ClassVar[int]
    CLIMATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    WEATHER_GADGET_ID_FIELD_NUMBER: _ClassVar[int]
    trans_duration: float
    weather_value_map: _containers.ScalarMap[int, str]
    weather_area_id: int
    climate_type: int
    weather_gadget_id: int
    def __init__(self, trans_duration: _Optional[float] = ..., weather_value_map: _Optional[_Mapping[int, str]] = ..., weather_area_id: _Optional[int] = ..., climate_type: _Optional[int] = ..., weather_gadget_id: _Optional[int] = ...) -> None: ...
