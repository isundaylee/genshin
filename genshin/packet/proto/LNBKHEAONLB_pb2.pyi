from genshin.packet.proto import HCJGIFNJPPJ_pb2 as _HCJGIFNJPPJ_pb2
from genshin.packet.proto import NKCKDBLFBMP_pb2 as _NKCKDBLFBMP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LNBKHEAONLB(_message.Message):
    __slots__ = ("AGMCINCEBPB", "KMKLFECOOIA", "HGBBGLKPLFI", "CJOKFLDEFMB", "EJNINFFFKJP", "MEILGJAAFKH")
    AGMCINCEBPB_FIELD_NUMBER: _ClassVar[int]
    KMKLFECOOIA_FIELD_NUMBER: _ClassVar[int]
    HGBBGLKPLFI_FIELD_NUMBER: _ClassVar[int]
    CJOKFLDEFMB_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    MEILGJAAFKH_FIELD_NUMBER: _ClassVar[int]
    AGMCINCEBPB: _HCJGIFNJPPJ_pb2.HCJGIFNJPPJ
    KMKLFECOOIA: _containers.RepeatedCompositeFieldContainer[_NKCKDBLFBMP_pb2.NKCKDBLFBMP]
    HGBBGLKPLFI: int
    CJOKFLDEFMB: int
    EJNINFFFKJP: int
    MEILGJAAFKH: int
    def __init__(self, AGMCINCEBPB: _Optional[_Union[_HCJGIFNJPPJ_pb2.HCJGIFNJPPJ, _Mapping]] = ..., KMKLFECOOIA: _Optional[_Iterable[_Union[_NKCKDBLFBMP_pb2.NKCKDBLFBMP, _Mapping]]] = ..., HGBBGLKPLFI: _Optional[int] = ..., CJOKFLDEFMB: _Optional[int] = ..., EJNINFFFKJP: _Optional[int] = ..., MEILGJAAFKH: _Optional[int] = ...) -> None: ...
