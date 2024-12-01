from genshin.packet.proto import JGBLKFDNIHF_pb2 as _JGBLKFDNIHF_pb2
from genshin.packet.proto import HPPANKBCFGI_pb2 as _HPPANKBCFGI_pb2
from genshin.packet.proto import EBPONABNLJE_pb2 as _EBPONABNLJE_pb2
from genshin.packet.proto import KDPBGPNNCLD_pb2 as _KDPBGPNNCLD_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JHJILIAANKO(_message.Message):
    __slots__ = ("avatar_available_count_result", "avatar_result", "card_result", "coin_result", "JBBKFMAPHOE", "INNKMKKBBPK", "LFNOBKNIAJH")
    AVATAR_AVAILABLE_COUNT_RESULT_FIELD_NUMBER: _ClassVar[int]
    AVATAR_RESULT_FIELD_NUMBER: _ClassVar[int]
    CARD_RESULT_FIELD_NUMBER: _ClassVar[int]
    COIN_RESULT_FIELD_NUMBER: _ClassVar[int]
    JBBKFMAPHOE_FIELD_NUMBER: _ClassVar[int]
    INNKMKKBBPK_FIELD_NUMBER: _ClassVar[int]
    LFNOBKNIAJH_FIELD_NUMBER: _ClassVar[int]
    avatar_available_count_result: _JGBLKFDNIHF_pb2.JGBLKFDNIHF
    avatar_result: _HPPANKBCFGI_pb2.HPPANKBCFGI
    card_result: _EBPONABNLJE_pb2.EBPONABNLJE
    coin_result: _KDPBGPNNCLD_pb2.KDPBGPNNCLD
    JBBKFMAPHOE: bool
    INNKMKKBBPK: int
    LFNOBKNIAJH: int
    def __init__(self, avatar_available_count_result: _Optional[_Union[_JGBLKFDNIHF_pb2.JGBLKFDNIHF, _Mapping]] = ..., avatar_result: _Optional[_Union[_HPPANKBCFGI_pb2.HPPANKBCFGI, _Mapping]] = ..., card_result: _Optional[_Union[_EBPONABNLJE_pb2.EBPONABNLJE, _Mapping]] = ..., coin_result: _Optional[_Union[_KDPBGPNNCLD_pb2.KDPBGPNNCLD, _Mapping]] = ..., JBBKFMAPHOE: bool = ..., INNKMKKBBPK: _Optional[int] = ..., LFNOBKNIAJH: _Optional[int] = ...) -> None: ...
