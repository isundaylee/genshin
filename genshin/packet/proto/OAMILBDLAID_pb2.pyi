from genshin.packet.proto import LKKFHDFBAHJ_pb2 as _LKKFHDFBAHJ_pb2
from genshin.packet.proto import FIDFLFBFHHH_pb2 as _FIDFLFBFHHH_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OAMILBDLAID(_message.Message):
    __slots__ = ("LILDONIELDM", "ADMKPEPMOAH")
    LILDONIELDM_FIELD_NUMBER: _ClassVar[int]
    ADMKPEPMOAH_FIELD_NUMBER: _ClassVar[int]
    LILDONIELDM: _containers.RepeatedCompositeFieldContainer[_LKKFHDFBAHJ_pb2.LKKFHDFBAHJ]
    ADMKPEPMOAH: _containers.RepeatedCompositeFieldContainer[_FIDFLFBFHHH_pb2.FIDFLFBFHHH]
    def __init__(self, LILDONIELDM: _Optional[_Iterable[_Union[_LKKFHDFBAHJ_pb2.LKKFHDFBAHJ, _Mapping]]] = ..., ADMKPEPMOAH: _Optional[_Iterable[_Union[_FIDFLFBFHHH_pb2.FIDFLFBFHHH, _Mapping]]] = ...) -> None: ...
