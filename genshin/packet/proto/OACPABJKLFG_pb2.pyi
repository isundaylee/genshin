from genshin.packet.proto import CJGPOAMEDNG_pb2 as _CJGPOAMEDNG_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OACPABJKLFG(_message.Message):
    __slots__ = ("BAGJBBKNADL", "MEAILAOFHPB", "EAIPGEMKNPO")
    BAGJBBKNADL_FIELD_NUMBER: _ClassVar[int]
    MEAILAOFHPB_FIELD_NUMBER: _ClassVar[int]
    EAIPGEMKNPO_FIELD_NUMBER: _ClassVar[int]
    BAGJBBKNADL: _containers.RepeatedCompositeFieldContainer[_CJGPOAMEDNG_pb2.CJGPOAMEDNG]
    MEAILAOFHPB: bool
    EAIPGEMKNPO: int
    def __init__(self, BAGJBBKNADL: _Optional[_Iterable[_Union[_CJGPOAMEDNG_pb2.CJGPOAMEDNG, _Mapping]]] = ..., MEAILAOFHPB: bool = ..., EAIPGEMKNPO: _Optional[int] = ...) -> None: ...
