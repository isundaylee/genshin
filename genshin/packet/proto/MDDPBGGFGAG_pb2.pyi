from genshin.packet.proto import ELLDEPILOFC_pb2 as _ELLDEPILOFC_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MDDPBGGFGAG(_message.Message):
    __slots__ = ("MBOGPBBOIEH", "HHOGHBECPNP")
    MBOGPBBOIEH_FIELD_NUMBER: _ClassVar[int]
    HHOGHBECPNP_FIELD_NUMBER: _ClassVar[int]
    MBOGPBBOIEH: _ELLDEPILOFC_pb2.ELLDEPILOFC
    HHOGHBECPNP: int
    def __init__(self, MBOGPBBOIEH: _Optional[_Union[_ELLDEPILOFC_pb2.ELLDEPILOFC, str]] = ..., HHOGHBECPNP: _Optional[int] = ...) -> None: ...
