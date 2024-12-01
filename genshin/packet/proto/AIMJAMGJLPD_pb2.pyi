from genshin.packet.proto import LPKLDJKFMDA_pb2 as _LPKLDJKFMDA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AIMJAMGJLPD(_message.Message):
    __slots__ = ("AGGJLMMAPKN", "EJNINFFFKJP", "DNBEFLJLAMB")
    AGGJLMMAPKN_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    AGGJLMMAPKN: _containers.RepeatedCompositeFieldContainer[_LPKLDJKFMDA_pb2.LPKLDJKFMDA]
    EJNINFFFKJP: int
    DNBEFLJLAMB: int
    def __init__(self, AGGJLMMAPKN: _Optional[_Iterable[_Union[_LPKLDJKFMDA_pb2.LPKLDJKFMDA, _Mapping]]] = ..., EJNINFFFKJP: _Optional[int] = ..., DNBEFLJLAMB: _Optional[int] = ...) -> None: ...
