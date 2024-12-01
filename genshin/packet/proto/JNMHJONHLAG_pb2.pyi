from genshin.packet.proto import GDHBFFBPIIJ_pb2 as _GDHBFFBPIIJ_pb2
from genshin.packet.proto import KNMPNCPBMMP_pb2 as _KNMPNCPBMMP_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JNMHJONHLAG(_message.Message):
    __slots__ = ("GGPKAKOCHAI", "affix_map", "HMLFALPADMC", "guid", "level", "JAFJMOBLENI", "item_id", "AGIDBEEINDE", "OCKIBANLDMK", "promote_level")
    class AffixMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    GGPKAKOCHAI_FIELD_NUMBER: _ClassVar[int]
    AFFIX_MAP_FIELD_NUMBER: _ClassVar[int]
    HMLFALPADMC_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    JAFJMOBLENI_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    AGIDBEEINDE_FIELD_NUMBER: _ClassVar[int]
    OCKIBANLDMK_FIELD_NUMBER: _ClassVar[int]
    PROMOTE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    GGPKAKOCHAI: _GDHBFFBPIIJ_pb2.GDHBFFBPIIJ
    affix_map: _containers.ScalarMap[int, int]
    HMLFALPADMC: _KNMPNCPBMMP_pb2.KNMPNCPBMMP
    guid: int
    level: int
    JAFJMOBLENI: bool
    item_id: int
    AGIDBEEINDE: int
    OCKIBANLDMK: int
    promote_level: int
    def __init__(self, GGPKAKOCHAI: _Optional[_Union[_GDHBFFBPIIJ_pb2.GDHBFFBPIIJ, _Mapping]] = ..., affix_map: _Optional[_Mapping[int, int]] = ..., HMLFALPADMC: _Optional[_Union[_KNMPNCPBMMP_pb2.KNMPNCPBMMP, _Mapping]] = ..., guid: _Optional[int] = ..., level: _Optional[int] = ..., JAFJMOBLENI: bool = ..., item_id: _Optional[int] = ..., AGIDBEEINDE: _Optional[int] = ..., OCKIBANLDMK: _Optional[int] = ..., promote_level: _Optional[int] = ...) -> None: ...
