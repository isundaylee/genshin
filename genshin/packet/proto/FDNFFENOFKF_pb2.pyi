from genshin.packet.proto import EMEKKIANDLE_pb2 as _EMEKKIANDLE_pb2
from genshin.packet.proto import INOOIEHHKLI_pb2 as _INOOIEHHKLI_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FDNFFENOFKF(_message.Message):
    __slots__ = ("ALDIPFFJEOI", "KGCONLDGJPG", "AGIDBEEINDE")
    ALDIPFFJEOI_FIELD_NUMBER: _ClassVar[int]
    KGCONLDGJPG_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    ALDIPFFJEOI: _EMEKKIANDLE_pb2.EMEKKIANDLE
    KGCONLDGJPG: _INOOIEHHKLI_pb2.INOOIEHHKLI
    AGIDBEEINDE: int
    def __init__(self, ALDIPFFJEOI: _Optional[_Union[_EMEKKIANDLE_pb2.EMEKKIANDLE, _Mapping]] = ..., KGCONLDGJPG: _Optional[_Union[_INOOIEHHKLI_pb2.INOOIEHHKLI, str]] = ..., AGIDBEEINDE: _Optional[int] = ...) -> None: ...
