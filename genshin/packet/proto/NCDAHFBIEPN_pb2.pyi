from genshin.packet.proto import EIKAMCKBFDF_pb2 as _EIKAMCKBFDF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NCDAHFBIEPN(_message.Message):
    __slots__ = ("HJOMKFNMLCH", "PDHEKMEMBLG", "EDOJGAFAKDA", "MPNJAOCKMAH", "JIMELGDJMLF", "NEKECFNAHOM")
    HJOMKFNMLCH_FIELD_NUMBER: _ClassVar[int]
    PDHEKMEMBLG_FIELD_NUMBER: _ClassVar[int]
    EDOJGAFAKDA_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    JIMELGDJMLF_FIELD_NUMBER: _ClassVar[int]
    NEKECFNAHOM_FIELD_NUMBER: _ClassVar[int]
    HJOMKFNMLCH: _containers.RepeatedCompositeFieldContainer[_EIKAMCKBFDF_pb2.EIKAMCKBFDF]
    PDHEKMEMBLG: _containers.RepeatedScalarFieldContainer[int]
    EDOJGAFAKDA: bool
    MPNJAOCKMAH: int
    JIMELGDJMLF: int
    NEKECFNAHOM: int
    def __init__(self, HJOMKFNMLCH: _Optional[_Iterable[_Union[_EIKAMCKBFDF_pb2.EIKAMCKBFDF, _Mapping]]] = ..., PDHEKMEMBLG: _Optional[_Iterable[int]] = ..., EDOJGAFAKDA: bool = ..., MPNJAOCKMAH: _Optional[int] = ..., JIMELGDJMLF: _Optional[int] = ..., NEKECFNAHOM: _Optional[int] = ...) -> None: ...
