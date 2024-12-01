from genshin.packet.proto import CACGLIBJIIE_pb2 as _CACGLIBJIIE_pb2
from genshin.packet.proto import GDMLPOEDPJO_pb2 as _GDMLPOEDPJO_pb2
from genshin.packet.proto import OAODPGJOMPF_pb2 as _OAODPGJOMPF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AFCMCKHFILO(_message.Message):
    __slots__ = ("CBAKCKLKJHJ", "CJGOFEODNAH", "PJEEOONMMDK", "CIDMBDPHCHJ")
    CBAKCKLKJHJ_FIELD_NUMBER: _ClassVar[int]
    CJGOFEODNAH_FIELD_NUMBER: _ClassVar[int]
    PJEEOONMMDK_FIELD_NUMBER: _ClassVar[int]
    CIDMBDPHCHJ_FIELD_NUMBER: _ClassVar[int]
    CBAKCKLKJHJ: _containers.RepeatedCompositeFieldContainer[_CACGLIBJIIE_pb2.CACGLIBJIIE]
    CJGOFEODNAH: _containers.RepeatedCompositeFieldContainer[_GDMLPOEDPJO_pb2.GDMLPOEDPJO]
    PJEEOONMMDK: _containers.RepeatedCompositeFieldContainer[_GDMLPOEDPJO_pb2.GDMLPOEDPJO]
    CIDMBDPHCHJ: _containers.RepeatedCompositeFieldContainer[_OAODPGJOMPF_pb2.OAODPGJOMPF]
    def __init__(self, CBAKCKLKJHJ: _Optional[_Iterable[_Union[_CACGLIBJIIE_pb2.CACGLIBJIIE, _Mapping]]] = ..., CJGOFEODNAH: _Optional[_Iterable[_Union[_GDMLPOEDPJO_pb2.GDMLPOEDPJO, _Mapping]]] = ..., PJEEOONMMDK: _Optional[_Iterable[_Union[_GDMLPOEDPJO_pb2.GDMLPOEDPJO, _Mapping]]] = ..., CIDMBDPHCHJ: _Optional[_Iterable[_Union[_OAODPGJOMPF_pb2.OAODPGJOMPF, _Mapping]]] = ...) -> None: ...
