from genshin.packet.proto import HGMLODJCJNO_pb2 as _HGMLODJCJNO_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LFLJDEIHLDM(_message.Message):
    __slots__ = ("JNOFEOHIMOB", "ONPGICEBPFJ", "FKJPHKIHBMD", "LEMCPFECPMB", "MBBKAENBCKD", "OPOOBJEOOKM", "ALKGNKPNKIJ")
    class JNOFEOHIMOBEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class FKJPHKIHBMDEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class LEMCPFECPMBEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    JNOFEOHIMOB_FIELD_NUMBER: _ClassVar[int]
    ONPGICEBPFJ_FIELD_NUMBER: _ClassVar[int]
    FKJPHKIHBMD_FIELD_NUMBER: _ClassVar[int]
    LEMCPFECPMB_FIELD_NUMBER: _ClassVar[int]
    MBBKAENBCKD_FIELD_NUMBER: _ClassVar[int]
    OPOOBJEOOKM_FIELD_NUMBER: _ClassVar[int]
    ALKGNKPNKIJ_FIELD_NUMBER: _ClassVar[int]
    JNOFEOHIMOB: _containers.ScalarMap[int, int]
    ONPGICEBPFJ: _containers.RepeatedScalarFieldContainer[int]
    FKJPHKIHBMD: _containers.ScalarMap[int, int]
    LEMCPFECPMB: _containers.ScalarMap[int, int]
    MBBKAENBCKD: int
    OPOOBJEOOKM: _HGMLODJCJNO_pb2.HGMLODJCJNO
    ALKGNKPNKIJ: int
    def __init__(self, JNOFEOHIMOB: _Optional[_Mapping[int, int]] = ..., ONPGICEBPFJ: _Optional[_Iterable[int]] = ..., FKJPHKIHBMD: _Optional[_Mapping[int, int]] = ..., LEMCPFECPMB: _Optional[_Mapping[int, int]] = ..., MBBKAENBCKD: _Optional[int] = ..., OPOOBJEOOKM: _Optional[_Union[_HGMLODJCJNO_pb2.HGMLODJCJNO, str]] = ..., ALKGNKPNKIJ: _Optional[int] = ...) -> None: ...
