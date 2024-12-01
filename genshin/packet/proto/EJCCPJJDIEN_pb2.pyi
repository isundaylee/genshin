from genshin.packet.proto import EEJAGBCFPNA_pb2 as _EEJAGBCFPNA_pb2
from genshin.packet.proto import NIAJPBBJMJB_pb2 as _NIAJPBBJMJB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EJCCPJJDIEN(_message.Message):
    __slots__ = ("PNDPNMBDOKF", "HGAIBENIOCI")
    PNDPNMBDOKF_FIELD_NUMBER: _ClassVar[int]
    HGAIBENIOCI_FIELD_NUMBER: _ClassVar[int]
    PNDPNMBDOKF: _containers.RepeatedCompositeFieldContainer[_EEJAGBCFPNA_pb2.EEJAGBCFPNA]
    HGAIBENIOCI: _containers.RepeatedCompositeFieldContainer[_NIAJPBBJMJB_pb2.NIAJPBBJMJB]
    def __init__(self, PNDPNMBDOKF: _Optional[_Iterable[_Union[_EEJAGBCFPNA_pb2.EEJAGBCFPNA, _Mapping]]] = ..., HGAIBENIOCI: _Optional[_Iterable[_Union[_NIAJPBBJMJB_pb2.NIAJPBBJMJB, _Mapping]]] = ...) -> None: ...
