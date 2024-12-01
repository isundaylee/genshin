from genshin.packet.proto import PropValue_pb2 as _PropValue_pb2
from genshin.packet.proto import KBGFFPMOLNP_pb2 as _KBGFFPMOLNP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AFGCPBKLHMB(_message.Message):
    __slots__ = ("prop_map", "EFBHADIMHNF")
    class PropMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _PropValue_pb2.PropValue
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_PropValue_pb2.PropValue, _Mapping]] = ...) -> None: ...
    PROP_MAP_FIELD_NUMBER: _ClassVar[int]
    EFBHADIMHNF_FIELD_NUMBER: _ClassVar[int]
    prop_map: _containers.MessageMap[int, _PropValue_pb2.PropValue]
    EFBHADIMHNF: _KBGFFPMOLNP_pb2.KBGFFPMOLNP
    def __init__(self, prop_map: _Optional[_Mapping[int, _PropValue_pb2.PropValue]] = ..., EFBHADIMHNF: _Optional[_Union[_KBGFFPMOLNP_pb2.KBGFFPMOLNP, _Mapping]] = ...) -> None: ...
