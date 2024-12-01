from genshin.packet.proto import BIFEDDINLOD_pb2 as _BIFEDDINLOD_pb2
from genshin.packet.proto import OMBEIFNNEDF_pb2 as _OMBEIFNNEDF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IOAHICPMIEB(_message.Message):
    __slots__ = ("DOBEBMLDBIO", "OBHPOELIAPM", "MJMIFKJBKBN", "HJIKNNIEELI", "EPFCIDIKLKG", "OJLMDPLJIFI")
    DOBEBMLDBIO_FIELD_NUMBER: _ClassVar[int]
    OBHPOELIAPM_FIELD_NUMBER: _ClassVar[int]
    MJMIFKJBKBN_FIELD_NUMBER: _ClassVar[int]
    HJIKNNIEELI_FIELD_NUMBER: _ClassVar[int]
    EPFCIDIKLKG_FIELD_NUMBER: _ClassVar[int]
    OJLMDPLJIFI_FIELD_NUMBER: _ClassVar[int]
    DOBEBMLDBIO: _containers.RepeatedScalarFieldContainer[int]
    OBHPOELIAPM: _containers.RepeatedCompositeFieldContainer[_BIFEDDINLOD_pb2.BIFEDDINLOD]
    MJMIFKJBKBN: _containers.RepeatedScalarFieldContainer[int]
    HJIKNNIEELI: _containers.RepeatedCompositeFieldContainer[_OMBEIFNNEDF_pb2.OMBEIFNNEDF]
    EPFCIDIKLKG: int
    OJLMDPLJIFI: int
    def __init__(self, DOBEBMLDBIO: _Optional[_Iterable[int]] = ..., OBHPOELIAPM: _Optional[_Iterable[_Union[_BIFEDDINLOD_pb2.BIFEDDINLOD, _Mapping]]] = ..., MJMIFKJBKBN: _Optional[_Iterable[int]] = ..., HJIKNNIEELI: _Optional[_Iterable[_Union[_OMBEIFNNEDF_pb2.OMBEIFNNEDF, _Mapping]]] = ..., EPFCIDIKLKG: _Optional[int] = ..., OJLMDPLJIFI: _Optional[int] = ...) -> None: ...
