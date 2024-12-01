from genshin.packet.proto import OMBEIFNNEDF_pb2 as _OMBEIFNNEDF_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DNJMJFMEBML(_message.Message):
    __slots__ = ("ILKGEFDHPFI", "EMEDJDNNGJI", "OJHCPPEHHKG", "PGDONCKDOMB", "KCOIMECCODP", "BBPGIJFJHEN", "avatar_id")
    ILKGEFDHPFI_FIELD_NUMBER: _ClassVar[int]
    EMEDJDNNGJI_FIELD_NUMBER: _ClassVar[int]
    OJHCPPEHHKG_FIELD_NUMBER: _ClassVar[int]
    PGDONCKDOMB_FIELD_NUMBER: _ClassVar[int]
    KCOIMECCODP_FIELD_NUMBER: _ClassVar[int]
    BBPGIJFJHEN_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    ILKGEFDHPFI: _containers.RepeatedScalarFieldContainer[int]
    EMEDJDNNGJI: _containers.RepeatedScalarFieldContainer[int]
    OJHCPPEHHKG: _containers.RepeatedScalarFieldContainer[int]
    PGDONCKDOMB: _containers.RepeatedCompositeFieldContainer[_OMBEIFNNEDF_pb2.OMBEIFNNEDF]
    KCOIMECCODP: bool
    BBPGIJFJHEN: int
    avatar_id: int
    def __init__(self, ILKGEFDHPFI: _Optional[_Iterable[int]] = ..., EMEDJDNNGJI: _Optional[_Iterable[int]] = ..., OJHCPPEHHKG: _Optional[_Iterable[int]] = ..., PGDONCKDOMB: _Optional[_Iterable[_Union[_OMBEIFNNEDF_pb2.OMBEIFNNEDF, _Mapping]]] = ..., KCOIMECCODP: bool = ..., BBPGIJFJHEN: _Optional[int] = ..., avatar_id: _Optional[int] = ...) -> None: ...
