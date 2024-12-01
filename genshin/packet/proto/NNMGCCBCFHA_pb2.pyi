from genshin.packet.proto import HOPFEEIPGJP_pb2 as _HOPFEEIPGJP_pb2
from genshin.packet.proto import EFHIGEKEJJO_pb2 as _EFHIGEKEJJO_pb2
from genshin.packet.proto import BOGMLIEEDGC_pb2 as _BOGMLIEEDGC_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NNMGCCBCFHA(_message.Message):
    __slots__ = ("AKGOOIIBCOM", "HMFFAPHMBGC", "HHDNNMNHNCI", "chest_info", "shop_info")
    AKGOOIIBCOM_FIELD_NUMBER: _ClassVar[int]
    HMFFAPHMBGC_FIELD_NUMBER: _ClassVar[int]
    HHDNNMNHNCI_FIELD_NUMBER: _ClassVar[int]
    CHEST_INFO_FIELD_NUMBER: _ClassVar[int]
    SHOP_INFO_FIELD_NUMBER: _ClassVar[int]
    AKGOOIIBCOM: _HOPFEEIPGJP_pb2.HOPFEEIPGJP
    HMFFAPHMBGC: int
    HHDNNMNHNCI: bool
    chest_info: _EFHIGEKEJJO_pb2.EFHIGEKEJJO
    shop_info: _BOGMLIEEDGC_pb2.BOGMLIEEDGC
    def __init__(self, AKGOOIIBCOM: _Optional[_Union[_HOPFEEIPGJP_pb2.HOPFEEIPGJP, _Mapping]] = ..., HMFFAPHMBGC: _Optional[int] = ..., HHDNNMNHNCI: bool = ..., chest_info: _Optional[_Union[_EFHIGEKEJJO_pb2.EFHIGEKEJJO, _Mapping]] = ..., shop_info: _Optional[_Union[_BOGMLIEEDGC_pb2.BOGMLIEEDGC, _Mapping]] = ...) -> None: ...
