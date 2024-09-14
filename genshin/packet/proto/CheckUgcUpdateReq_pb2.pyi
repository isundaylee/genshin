from genshin.packet.proto import UgcType_pb2 as _UgcType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CheckUgcUpdateReq(_message.Message):
    __slots__ = ("ugc_type",)
    UGC_TYPE_FIELD_NUMBER: _ClassVar[int]
    ugc_type: _UgcType_pb2.UgcType
    def __init__(self, ugc_type: _Optional[_Union[_UgcType_pb2.UgcType, str]] = ...) -> None: ...
