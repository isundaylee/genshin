from genshin.packet.proto import NEDLFHJJONK_pb2 as _NEDLFHJJONK_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AJGJLIKCJPF(_message.Message):
    __slots__ = ("ONINIIHMHCP", "CKIECFILLBC", "item_id")
    ONINIIHMHCP_FIELD_NUMBER: _ClassVar[int]
    CKIECFILLBC_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ONINIIHMHCP: _containers.RepeatedCompositeFieldContainer[_NEDLFHJJONK_pb2.NEDLFHJJONK]
    CKIECFILLBC: str
    item_id: int
    def __init__(self, ONINIIHMHCP: _Optional[_Iterable[_Union[_NEDLFHJJONK_pb2.NEDLFHJJONK, _Mapping]]] = ..., CKIECFILLBC: _Optional[str] = ..., item_id: _Optional[int] = ...) -> None: ...
