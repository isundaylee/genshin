from genshin.packet.proto import CKDPMACGDJO_pb2 as _CKDPMACGDJO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EPHHNHEDDGL(_message.Message):
    __slots__ = ("CMBAACJKANJ", "DCMMNMAHACO", "HLKDDNGCKJN", "JIBLEDAFCEB", "JABGACILLEC", "DFDNFDDCCPB", "DNBEFLJLAMB", "PAJKKMDPFFA", "LKOFKODPMGO")
    CMBAACJKANJ_FIELD_NUMBER: _ClassVar[int]
    DCMMNMAHACO_FIELD_NUMBER: _ClassVar[int]
    HLKDDNGCKJN_FIELD_NUMBER: _ClassVar[int]
    JIBLEDAFCEB_FIELD_NUMBER: _ClassVar[int]
    JABGACILLEC_FIELD_NUMBER: _ClassVar[int]
    DFDNFDDCCPB_FIELD_NUMBER: _ClassVar[int]
    DNBEFLJLAMB_FIELD_NUMBER: _ClassVar[int]
    PAJKKMDPFFA_FIELD_NUMBER: _ClassVar[int]
    LKOFKODPMGO_FIELD_NUMBER: _ClassVar[int]
    CMBAACJKANJ: _containers.RepeatedCompositeFieldContainer[_CKDPMACGDJO_pb2.CKDPMACGDJO]
    DCMMNMAHACO: _containers.RepeatedScalarFieldContainer[int]
    HLKDDNGCKJN: int
    JIBLEDAFCEB: bool
    JABGACILLEC: int
    DFDNFDDCCPB: int
    DNBEFLJLAMB: int
    PAJKKMDPFFA: int
    LKOFKODPMGO: int
    def __init__(self, CMBAACJKANJ: _Optional[_Iterable[_Union[_CKDPMACGDJO_pb2.CKDPMACGDJO, _Mapping]]] = ..., DCMMNMAHACO: _Optional[_Iterable[int]] = ..., HLKDDNGCKJN: _Optional[int] = ..., JIBLEDAFCEB: bool = ..., JABGACILLEC: _Optional[int] = ..., DFDNFDDCCPB: _Optional[int] = ..., DNBEFLJLAMB: _Optional[int] = ..., PAJKKMDPFFA: _Optional[int] = ..., LKOFKODPMGO: _Optional[int] = ...) -> None: ...
