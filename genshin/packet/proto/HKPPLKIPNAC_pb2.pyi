from genshin.packet.proto import FHPEAIOOGCI_pb2 as _FHPEAIOOGCI_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HKPPLKIPNAC(_message.Message):
    __slots__ = ("LDCJEFLLJJK",)
    class LDCJEFLLJJKEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _FHPEAIOOGCI_pb2.FHPEAIOOGCI
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_FHPEAIOOGCI_pb2.FHPEAIOOGCI, _Mapping]] = ...) -> None: ...
    LDCJEFLLJJK_FIELD_NUMBER: _ClassVar[int]
    LDCJEFLLJJK: _containers.MessageMap[int, _FHPEAIOOGCI_pb2.FHPEAIOOGCI]
    def __init__(self, LDCJEFLLJJK: _Optional[_Mapping[int, _FHPEAIOOGCI_pb2.FHPEAIOOGCI]] = ...) -> None: ...
