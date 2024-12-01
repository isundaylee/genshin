from genshin.packet.proto import NAHMOAOLMPL_pb2 as _NAHMOAOLMPL_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AJMIMBMCABE(_message.Message):
    __slots__ = ("EFCDELGMMKG", "MFHKFMFACIN")
    EFCDELGMMKG_FIELD_NUMBER: _ClassVar[int]
    MFHKFMFACIN_FIELD_NUMBER: _ClassVar[int]
    EFCDELGMMKG: _containers.RepeatedCompositeFieldContainer[_NAHMOAOLMPL_pb2.NAHMOAOLMPL]
    MFHKFMFACIN: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, EFCDELGMMKG: _Optional[_Iterable[_Union[_NAHMOAOLMPL_pb2.NAHMOAOLMPL, _Mapping]]] = ..., MFHKFMFACIN: _Optional[_Iterable[int]] = ...) -> None: ...
