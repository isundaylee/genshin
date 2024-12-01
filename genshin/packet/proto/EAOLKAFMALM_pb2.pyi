from genshin.packet.proto import CLPBKEMPLNM_pb2 as _CLPBKEMPLNM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EAOLKAFMALM(_message.Message):
    __slots__ = ("PNDPNMBDOKF",)
    PNDPNMBDOKF_FIELD_NUMBER: _ClassVar[int]
    PNDPNMBDOKF: _containers.RepeatedCompositeFieldContainer[_CLPBKEMPLNM_pb2.CLPBKEMPLNM]
    def __init__(self, PNDPNMBDOKF: _Optional[_Iterable[_Union[_CLPBKEMPLNM_pb2.CLPBKEMPLNM, _Mapping]]] = ...) -> None: ...
