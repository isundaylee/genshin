from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ForwardType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FORWARD_TYPE_LOCAL: _ClassVar[ForwardType]
    FORWARD_TYPE_TO_ALL: _ClassVar[ForwardType]
    FORWARD_TYPE_TO_ALL_EXCEPT_CUR: _ClassVar[ForwardType]
    FORWARD_TYPE_TO_HOST: _ClassVar[ForwardType]
    FORWARD_TYPE_TO_ALL_GUEST: _ClassVar[ForwardType]
    FORWARD_TYPE_TO_PEER: _ClassVar[ForwardType]
    FORWARD_TYPE_TO_PEERS: _ClassVar[ForwardType]
    FORWARD_TYPE_ONLY_SERVER: _ClassVar[ForwardType]
    FORWARD_TYPE_TO_ALL_EXIST_EXCEPT_CUR: _ClassVar[ForwardType]
FORWARD_TYPE_LOCAL: ForwardType
FORWARD_TYPE_TO_ALL: ForwardType
FORWARD_TYPE_TO_ALL_EXCEPT_CUR: ForwardType
FORWARD_TYPE_TO_HOST: ForwardType
FORWARD_TYPE_TO_ALL_GUEST: ForwardType
FORWARD_TYPE_TO_PEER: ForwardType
FORWARD_TYPE_TO_PEERS: ForwardType
FORWARD_TYPE_ONLY_SERVER: ForwardType
FORWARD_TYPE_TO_ALL_EXIST_EXCEPT_CUR: ForwardType
