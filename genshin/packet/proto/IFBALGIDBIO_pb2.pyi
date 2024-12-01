from genshin.packet.proto import KOPDCBOLIKB_pb2 as _KOPDCBOLIKB_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IFBALGIDBIO(_message.Message):
    __slots__ = ("BILMBAOJDPK", "CGCNGJNCPGH", "KKAPOFHCPIB", "ILGOCDGLHMJ", "NMGBKJNIAOC", "EAGCGDDJOLH")
    class CGCNGJNCPGHEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class KKAPOFHCPIBEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class ILGOCDGLHMJEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    BILMBAOJDPK_FIELD_NUMBER: _ClassVar[int]
    CGCNGJNCPGH_FIELD_NUMBER: _ClassVar[int]
    KKAPOFHCPIB_FIELD_NUMBER: _ClassVar[int]
    ILGOCDGLHMJ_FIELD_NUMBER: _ClassVar[int]
    NMGBKJNIAOC_FIELD_NUMBER: _ClassVar[int]
    EAGCGDDJOLH_FIELD_NUMBER: _ClassVar[int]
    BILMBAOJDPK: _KOPDCBOLIKB_pb2.KOPDCBOLIKB
    CGCNGJNCPGH: _containers.ScalarMap[int, int]
    KKAPOFHCPIB: _containers.ScalarMap[int, int]
    ILGOCDGLHMJ: _containers.ScalarMap[int, int]
    NMGBKJNIAOC: bool
    EAGCGDDJOLH: int
    def __init__(self, BILMBAOJDPK: _Optional[_Union[_KOPDCBOLIKB_pb2.KOPDCBOLIKB, _Mapping]] = ..., CGCNGJNCPGH: _Optional[_Mapping[int, int]] = ..., KKAPOFHCPIB: _Optional[_Mapping[int, int]] = ..., ILGOCDGLHMJ: _Optional[_Mapping[int, int]] = ..., NMGBKJNIAOC: bool = ..., EAGCGDDJOLH: _Optional[int] = ...) -> None: ...
