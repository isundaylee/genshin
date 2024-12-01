from genshin.packet.proto import IKAAKKLBGMB_pb2 as _IKAAKKLBGMB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AGAGGELMLFC(_message.Message):
    __slots__ = ("CEOFALLNIIM", "KFCMCNLNDFC", "BODIEJCLGMB", "AKCLJOALODI", "MPNJAOCKMAH", "APAAPHBHHMK")
    CEOFALLNIIM_FIELD_NUMBER: _ClassVar[int]
    KFCMCNLNDFC_FIELD_NUMBER: _ClassVar[int]
    BODIEJCLGMB_FIELD_NUMBER: _ClassVar[int]
    AKCLJOALODI_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    APAAPHBHHMK_FIELD_NUMBER: _ClassVar[int]
    CEOFALLNIIM: _containers.RepeatedScalarFieldContainer[int]
    KFCMCNLNDFC: _containers.RepeatedCompositeFieldContainer[_IKAAKKLBGMB_pb2.IKAAKKLBGMB]
    BODIEJCLGMB: int
    AKCLJOALODI: bool
    MPNJAOCKMAH: int
    APAAPHBHHMK: int
    def __init__(self, CEOFALLNIIM: _Optional[_Iterable[int]] = ..., KFCMCNLNDFC: _Optional[_Iterable[_Union[_IKAAKKLBGMB_pb2.IKAAKKLBGMB, _Mapping]]] = ..., BODIEJCLGMB: _Optional[int] = ..., AKCLJOALODI: bool = ..., MPNJAOCKMAH: _Optional[int] = ..., APAAPHBHHMK: _Optional[int] = ...) -> None: ...
