from genshin.packet.proto import JOEJJOFMCIB_pb2 as _JOEJJOFMCIB_pb2
from genshin.packet.proto import HCHCCIHILMH_pb2 as _HCHCCIHILMH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IPILFEALJCL(_message.Message):
    __slots__ = ("BAGJBBKNADL", "HGAIBENIOCI")
    BAGJBBKNADL_FIELD_NUMBER: _ClassVar[int]
    HGAIBENIOCI_FIELD_NUMBER: _ClassVar[int]
    BAGJBBKNADL: _containers.RepeatedCompositeFieldContainer[_JOEJJOFMCIB_pb2.JOEJJOFMCIB]
    HGAIBENIOCI: _containers.RepeatedCompositeFieldContainer[_HCHCCIHILMH_pb2.HCHCCIHILMH]
    def __init__(self, BAGJBBKNADL: _Optional[_Iterable[_Union[_JOEJJOFMCIB_pb2.JOEJJOFMCIB, _Mapping]]] = ..., HGAIBENIOCI: _Optional[_Iterable[_Union[_HCHCCIHILMH_pb2.HCHCCIHILMH, _Mapping]]] = ...) -> None: ...
