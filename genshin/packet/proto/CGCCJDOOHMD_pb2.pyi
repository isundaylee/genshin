from genshin.packet.proto import ICHHFONJDKJ_pb2 as _ICHHFONJDKJ_pb2
from genshin.packet.proto import MOEHMLAHHKD_pb2 as _MOEHMLAHHKD_pb2
from genshin.packet.proto import JBNAGIBEAIA_pb2 as _JBNAGIBEAIA_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CGCCJDOOHMD(_message.Message):
    __slots__ = ("catch_seed", "refresh_seed", "add_signal")
    CATCH_SEED_FIELD_NUMBER: _ClassVar[int]
    REFRESH_SEED_FIELD_NUMBER: _ClassVar[int]
    ADD_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    catch_seed: _ICHHFONJDKJ_pb2.ICHHFONJDKJ
    refresh_seed: _MOEHMLAHHKD_pb2.MOEHMLAHHKD
    add_signal: _JBNAGIBEAIA_pb2.JBNAGIBEAIA
    def __init__(self, catch_seed: _Optional[_Union[_ICHHFONJDKJ_pb2.ICHHFONJDKJ, _Mapping]] = ..., refresh_seed: _Optional[_Union[_MOEHMLAHHKD_pb2.MOEHMLAHHKD, _Mapping]] = ..., add_signal: _Optional[_Union[_JBNAGIBEAIA_pb2.JBNAGIBEAIA, _Mapping]] = ...) -> None: ...
