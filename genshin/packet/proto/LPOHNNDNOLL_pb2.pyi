from genshin.packet.proto import GJDJPCPPHIC_pb2 as _GJDJPCPPHIC_pb2
from genshin.packet.proto import EFEGIIMAOMI_pb2 as _EFEGIIMAOMI_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LPOHNNDNOLL(_message.Message):
    __slots__ = ("EPNDBDPKLEP", "KPCPNEHCMEJ", "FBFDAKLPEFB", "HMOGLLBDGJM", "MNDHNPJNNGP", "PIEAPGEPMLF")
    EPNDBDPKLEP_FIELD_NUMBER: _ClassVar[int]
    KPCPNEHCMEJ_FIELD_NUMBER: _ClassVar[int]
    FBFDAKLPEFB_FIELD_NUMBER: _ClassVar[int]
    HMOGLLBDGJM_FIELD_NUMBER: _ClassVar[int]
    MNDHNPJNNGP_FIELD_NUMBER: _ClassVar[int]
    PIEAPGEPMLF_FIELD_NUMBER: _ClassVar[int]
    EPNDBDPKLEP: _GJDJPCPPHIC_pb2.GJDJPCPPHIC
    KPCPNEHCMEJ: _EFEGIIMAOMI_pb2.EFEGIIMAOMI
    FBFDAKLPEFB: int
    HMOGLLBDGJM: int
    MNDHNPJNNGP: int
    PIEAPGEPMLF: int
    def __init__(self, EPNDBDPKLEP: _Optional[_Union[_GJDJPCPPHIC_pb2.GJDJPCPPHIC, _Mapping]] = ..., KPCPNEHCMEJ: _Optional[_Union[_EFEGIIMAOMI_pb2.EFEGIIMAOMI, _Mapping]] = ..., FBFDAKLPEFB: _Optional[int] = ..., HMOGLLBDGJM: _Optional[int] = ..., MNDHNPJNNGP: _Optional[int] = ..., PIEAPGEPMLF: _Optional[int] = ...) -> None: ...
