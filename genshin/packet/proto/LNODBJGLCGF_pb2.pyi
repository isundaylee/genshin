from genshin.packet.proto import EMEKKIANDLE_pb2 as _EMEKKIANDLE_pb2
from genshin.packet.proto import FDNFFENOFKF_pb2 as _FDNFFENOFKF_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LNODBJGLCGF(_message.Message):
    __slots__ = ("KNGBDMDCNHK", "location_info", "widget_creator_info")
    KNGBDMDCNHK_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    WIDGET_CREATOR_INFO_FIELD_NUMBER: _ClassVar[int]
    KNGBDMDCNHK: int
    location_info: _EMEKKIANDLE_pb2.EMEKKIANDLE
    widget_creator_info: _FDNFFENOFKF_pb2.FDNFFENOFKF
    def __init__(self, KNGBDMDCNHK: _Optional[int] = ..., location_info: _Optional[_Union[_EMEKKIANDLE_pb2.EMEKKIANDLE, _Mapping]] = ..., widget_creator_info: _Optional[_Union[_FDNFFENOFKF_pb2.FDNFFENOFKF, _Mapping]] = ...) -> None: ...
