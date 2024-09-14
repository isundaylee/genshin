from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WeatherInfo(_message.Message):
    __slots__ = ("weather_area_id",)
    WEATHER_AREA_ID_FIELD_NUMBER: _ClassVar[int]
    weather_area_id: int
    def __init__(self, weather_area_id: _Optional[int] = ...) -> None: ...
