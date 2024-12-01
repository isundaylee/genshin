from genshin.packet.proto import BKFKEIHHBCC_pb2 as _BKFKEIHHBCC_pb2
from genshin.packet.proto import KOHNLAFGBMO_pb2 as _KOHNLAFGBMO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ACOJIJOEFPM(_message.Message):
    __slots__ = ("BLACDJFDAHF", "GIKAOEGNLHL", "KNGJHMLLCNP", "GGAGMENIJDB", "CGMEBDLBKMH", "MPNJAOCKMAH", "LOJBHHKEFJO", "HCJFDJHILAM")
    BLACDJFDAHF_FIELD_NUMBER: _ClassVar[int]
    GIKAOEGNLHL_FIELD_NUMBER: _ClassVar[int]
    KNGJHMLLCNP_FIELD_NUMBER: _ClassVar[int]
    GGAGMENIJDB_FIELD_NUMBER: _ClassVar[int]
    CGMEBDLBKMH_FIELD_NUMBER: _ClassVar[int]
    MPNJAOCKMAH_FIELD_NUMBER: _ClassVar[int]
    LOJBHHKEFJO_FIELD_NUMBER: _ClassVar[int]
    HCJFDJHILAM_FIELD_NUMBER: _ClassVar[int]
    BLACDJFDAHF: _containers.RepeatedCompositeFieldContainer[_BKFKEIHHBCC_pb2.BKFKEIHHBCC]
    GIKAOEGNLHL: _containers.RepeatedCompositeFieldContainer[_KOHNLAFGBMO_pb2.KOHNLAFGBMO]
    KNGJHMLLCNP: int
    GGAGMENIJDB: int
    CGMEBDLBKMH: int
    MPNJAOCKMAH: int
    LOJBHHKEFJO: int
    HCJFDJHILAM: bool
    def __init__(self, BLACDJFDAHF: _Optional[_Iterable[_Union[_BKFKEIHHBCC_pb2.BKFKEIHHBCC, _Mapping]]] = ..., GIKAOEGNLHL: _Optional[_Iterable[_Union[_KOHNLAFGBMO_pb2.KOHNLAFGBMO, _Mapping]]] = ..., KNGJHMLLCNP: _Optional[int] = ..., GGAGMENIJDB: _Optional[int] = ..., CGMEBDLBKMH: _Optional[int] = ..., MPNJAOCKMAH: _Optional[int] = ..., LOJBHHKEFJO: _Optional[int] = ..., HCJFDJHILAM: bool = ...) -> None: ...
