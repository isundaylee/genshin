from genshin.packet.proto import BPFBCCNHLFN_pb2 as _BPFBCCNHLFN_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EJMPGPPFPJG(_message.Message):
    __slots__ = ("GAIBIDBIBLK", "PPOEDCOJFAB", "AHHFCLEFKNE", "KFPHEMBCEFN", "JPLLDOBLMGD")
    class PPOEDCOJFABEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _BPFBCCNHLFN_pb2.BPFBCCNHLFN
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_BPFBCCNHLFN_pb2.BPFBCCNHLFN, _Mapping]] = ...) -> None: ...
    GAIBIDBIBLK_FIELD_NUMBER: _ClassVar[int]
    PPOEDCOJFAB_FIELD_NUMBER: _ClassVar[int]
    AHHFCLEFKNE_FIELD_NUMBER: _ClassVar[int]
    KFPHEMBCEFN_FIELD_NUMBER: _ClassVar[int]
    JPLLDOBLMGD_FIELD_NUMBER: _ClassVar[int]
    GAIBIDBIBLK: _containers.RepeatedScalarFieldContainer[int]
    PPOEDCOJFAB: _containers.MessageMap[int, _BPFBCCNHLFN_pb2.BPFBCCNHLFN]
    AHHFCLEFKNE: _containers.RepeatedScalarFieldContainer[int]
    KFPHEMBCEFN: int
    JPLLDOBLMGD: int
    def __init__(self, GAIBIDBIBLK: _Optional[_Iterable[int]] = ..., PPOEDCOJFAB: _Optional[_Mapping[int, _BPFBCCNHLFN_pb2.BPFBCCNHLFN]] = ..., AHHFCLEFKNE: _Optional[_Iterable[int]] = ..., KFPHEMBCEFN: _Optional[int] = ..., JPLLDOBLMGD: _Optional[int] = ...) -> None: ...
