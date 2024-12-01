from genshin.packet.proto import GKFGINKLNCH_pb2 as _GKFGINKLNCH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IHFFHFGOKPG(_message.Message):
    __slots__ = ("INDFGANKPPO", "AGIDBEEINDE")
    INDFGANKPPO_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    INDFGANKPPO: _containers.RepeatedScalarFieldContainer[_GKFGINKLNCH_pb2.GKFGINKLNCH]
    AGIDBEEINDE: int
    def __init__(self, INDFGANKPPO: _Optional[_Iterable[_Union[_GKFGINKLNCH_pb2.GKFGINKLNCH, str]]] = ..., AGIDBEEINDE: _Optional[int] = ...) -> None: ...
