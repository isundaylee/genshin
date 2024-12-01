from genshin.packet.proto import CMOPDDPMIAO_pb2 as _CMOPDDPMIAO_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FBDEKCPNBPF(_message.Message):
    __slots__ = ("MGLFBICADEC", "JBBNJEHICAF", "JIPEIMNPJLA")
    MGLFBICADEC_FIELD_NUMBER: _ClassVar[int]
    JBBNJEHICAF_FIELD_NUMBER: _ClassVar[int]
    JIPEIMNPJLA_FIELD_NUMBER: _ClassVar[int]
    MGLFBICADEC: _CMOPDDPMIAO_pb2.CMOPDDPMIAO
    JBBNJEHICAF: int
    JIPEIMNPJLA: int
    def __init__(self, MGLFBICADEC: _Optional[_Union[_CMOPDDPMIAO_pb2.CMOPDDPMIAO, _Mapping]] = ..., JBBNJEHICAF: _Optional[int] = ..., JIPEIMNPJLA: _Optional[int] = ...) -> None: ...
