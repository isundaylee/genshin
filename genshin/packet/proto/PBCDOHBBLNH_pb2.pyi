from genshin.packet.proto import KDEHCGJAGFJ_pb2 as _KDEHCGJAGFJ_pb2
from genshin.packet.proto import ALGFPDOAAFA_pb2 as _ALGFPDOAAFA_pb2
from genshin.packet.proto import CKKGDKCKLKH_pb2 as _CKKGDKCKLKH_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PBCDOHBBLNH(_message.Message):
    __slots__ = ("FGAFONOJIPA", "ABNHMHDLOKH", "FKDNDPILLJM", "velocity", "time", "JGCCKLNFEHE", "axis_speed", "rotation", "rotation_speed")
    FGAFONOJIPA_FIELD_NUMBER: _ClassVar[int]
    ABNHMHDLOKH_FIELD_NUMBER: _ClassVar[int]
    FKDNDPILLJM_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    JGCCKLNFEHE_FIELD_NUMBER: _ClassVar[int]
    AXIS_SPEED_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
    ROTATION_SPEED_FIELD_NUMBER: _ClassVar[int]
    FGAFONOJIPA: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    ABNHMHDLOKH: float
    FKDNDPILLJM: bool
    velocity: float
    time: float
    JGCCKLNFEHE: _ALGFPDOAAFA_pb2.ALGFPDOAAFA
    axis_speed: _CKKGDKCKLKH_pb2.CKKGDKCKLKH
    rotation: _KDEHCGJAGFJ_pb2.KDEHCGJAGFJ
    rotation_speed: _CKKGDKCKLKH_pb2.CKKGDKCKLKH
    def __init__(self, FGAFONOJIPA: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., ABNHMHDLOKH: _Optional[float] = ..., FKDNDPILLJM: bool = ..., velocity: _Optional[float] = ..., time: _Optional[float] = ..., JGCCKLNFEHE: _Optional[_Union[_ALGFPDOAAFA_pb2.ALGFPDOAAFA, str]] = ..., axis_speed: _Optional[_Union[_CKKGDKCKLKH_pb2.CKKGDKCKLKH, _Mapping]] = ..., rotation: _Optional[_Union[_KDEHCGJAGFJ_pb2.KDEHCGJAGFJ, _Mapping]] = ..., rotation_speed: _Optional[_Union[_CKKGDKCKLKH_pb2.CKKGDKCKLKH, _Mapping]] = ...) -> None: ...
