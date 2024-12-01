from genshin.packet.proto import KBDGJPCLCHJ_pb2 as _KBDGJPCLCHJ_pb2
from genshin.packet.proto import ICIEAHBEMCJ_pb2 as _ICIEAHBEMCJ_pb2
from genshin.packet.proto import NPAGLLEIBJM_pb2 as _NPAGLLEIBJM_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ELDJEDMBNBG(_message.Message):
    __slots__ = ("GHIHAIDBACF", "HPDGOGMDLJF", "DODFAJFPAKB", "NFLAKFJLCME", "ENOEKKLHBNH", "EJNINFFFKJP")
    class DODFAJFPAKBEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    GHIHAIDBACF_FIELD_NUMBER: _ClassVar[int]
    HPDGOGMDLJF_FIELD_NUMBER: _ClassVar[int]
    DODFAJFPAKB_FIELD_NUMBER: _ClassVar[int]
    NFLAKFJLCME_FIELD_NUMBER: _ClassVar[int]
    ENOEKKLHBNH_FIELD_NUMBER: _ClassVar[int]
    EJNINFFFKJP_FIELD_NUMBER: _ClassVar[int]
    GHIHAIDBACF: _KBDGJPCLCHJ_pb2.KBDGJPCLCHJ
    HPDGOGMDLJF: _ICIEAHBEMCJ_pb2.ICIEAHBEMCJ
    DODFAJFPAKB: _containers.ScalarMap[int, int]
    NFLAKFJLCME: int
    ENOEKKLHBNH: _NPAGLLEIBJM_pb2.NPAGLLEIBJM
    EJNINFFFKJP: int
    def __init__(self, GHIHAIDBACF: _Optional[_Union[_KBDGJPCLCHJ_pb2.KBDGJPCLCHJ, _Mapping]] = ..., HPDGOGMDLJF: _Optional[_Union[_ICIEAHBEMCJ_pb2.ICIEAHBEMCJ, _Mapping]] = ..., DODFAJFPAKB: _Optional[_Mapping[int, int]] = ..., NFLAKFJLCME: _Optional[int] = ..., ENOEKKLHBNH: _Optional[_Union[_NPAGLLEIBJM_pb2.NPAGLLEIBJM, str]] = ..., EJNINFFFKJP: _Optional[int] = ...) -> None: ...
