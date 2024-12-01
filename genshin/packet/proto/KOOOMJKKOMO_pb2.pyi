from genshin.packet.proto import LNJHDKEPBFO_pb2 as _LNJHDKEPBFO_pb2
from genshin.packet.proto import FLMMAAODDGD_pb2 as _FLMMAAODDGD_pb2
from genshin.packet.proto import GDEJPLCEOKO_pb2 as _GDEJPLCEOKO_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KOOOMJKKOMO(_message.Message):
    __slots__ = ("EAIPGEMKNPO", "third_stage_info", "second_stage_info", "first_stage_info")
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    THIRD_STAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    SECOND_STAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    FIRST_STAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO: int
    third_stage_info: _LNJHDKEPBFO_pb2.LNJHDKEPBFO
    second_stage_info: _FLMMAAODDGD_pb2.FLMMAAODDGD
    first_stage_info: _GDEJPLCEOKO_pb2.GDEJPLCEOKO
    def __init__(self, EAIPGEMKNPO: _Optional[int] = ..., third_stage_info: _Optional[_Union[_LNJHDKEPBFO_pb2.LNJHDKEPBFO, _Mapping]] = ..., second_stage_info: _Optional[_Union[_FLMMAAODDGD_pb2.FLMMAAODDGD, _Mapping]] = ..., first_stage_info: _Optional[_Union[_GDEJPLCEOKO_pb2.GDEJPLCEOKO, _Mapping]] = ...) -> None: ...
