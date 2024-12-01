from genshin.packet.proto import BGNINGGDPAA_pb2 as _BGNINGGDPAA_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IJAJHJECJFK(_message.Message):
    __slots__ = ("FAGJDJIGLON", "EAEKNFBGKPA", "OGDCENFLHJN", "ODCMKOFFKKL", "KKPPJFKDDEP", "MPNJAOCKMAH", "JIMELGDJMLF", "EDOJGAFAKDA", "JLAIAAEKGGM")
    FAGJDJIGLON_FIELD_NUMBER: _ClassVar[int]
    EAEKNFBGKPA_FIELD_NUMBER: _ClassVar[int]
    OGDCENFLHJN_FIELD_NUMBER: _ClassVar[int]
    ODCMKOFFKKL_FIELD_NUMBER: _ClassVar[int]
    KKPPJFKDDEP_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    JIMELGDJMLF_FIELD_NUMBER: _ClassVar[int]
    EDOJGAFAKDA_FIELD_NUMBER: _ClassVar[int]
    JLAIAAEKGGM_FIELD_NUMBER: _ClassVar[int]
    FAGJDJIGLON: _containers.RepeatedCompositeFieldContainer[_BGNINGGDPAA_pb2.BGNINGGDPAA]
    EAEKNFBGKPA: int
    OGDCENFLHJN: int
    ODCMKOFFKKL: int
    KKPPJFKDDEP: int
    MPNJAOCKMAH: int
    JIMELGDJMLF: int
    EDOJGAFAKDA: bool
    JLAIAAEKGGM: bool
    def __init__(self, FAGJDJIGLON: _Optional[_Iterable[_Union[_BGNINGGDPAA_pb2.BGNINGGDPAA, _Mapping]]] = ..., EAEKNFBGKPA: _Optional[int] = ..., OGDCENFLHJN: _Optional[int] = ..., ODCMKOFFKKL: _Optional[int] = ..., KKPPJFKDDEP: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ..., JIMELGDJMLF: _Optional[int] = ..., EDOJGAFAKDA: bool = ..., JLAIAAEKGGM: bool = ...) -> None: ...
