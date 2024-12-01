from genshin.packet.proto import DAAELFAMFEA_pb2 as _DAAELFAMFEA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OFIFGOOPCDO(_message.Message):
    __slots__ = ("DHPCLKCHDIM", "EFCDELGMMKG")
    DHPCLKCHDIM_FIELD_NUMBER: _ClassVar[int]
    EFCDELGMMKG_FIELD_NUMBER: _ClassVar[int]
    DHPCLKCHDIM: _containers.RepeatedScalarFieldContainer[int]
    EFCDELGMMKG: _containers.RepeatedCompositeFieldContainer[_DAAELFAMFEA_pb2.DAAELFAMFEA]
    def __init__(self, DHPCLKCHDIM: _Optional[_Iterable[int]] = ..., EFCDELGMMKG: _Optional[_Iterable[_Union[_DAAELFAMFEA_pb2.DAAELFAMFEA, _Mapping]]] = ...) -> None: ...
