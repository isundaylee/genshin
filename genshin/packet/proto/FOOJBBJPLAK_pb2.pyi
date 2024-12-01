from genshin.packet.proto import HBFBKIMOOGD_pb2 as _HBFBKIMOOGD_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FOOJBBJPLAK(_message.Message):
    __slots__ = ("HGNKFIJPJAA", "PGEJGJMGGOG", "DIKJLILLNCC", "HDBFKNJHBOO")
    class HGNKFIJPJAAEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    HGNKFIJPJAA_FIELD_NUMBER: _ClassVar[int]
    PGEJGJMGGOG_FIELD_NUMBER: _ClassVar[int]
    DIKJLILLNCC_FIELD_NUMBER: _ClassVar[int]
    HDBFKNJHBOO_FIELD_NUMBER: _ClassVar[int]
    HGNKFIJPJAA: _containers.ScalarMap[int, int]
    PGEJGJMGGOG: _containers.RepeatedCompositeFieldContainer[_HBFBKIMOOGD_pb2.HBFBKIMOOGD]
    DIKJLILLNCC: bool
    HDBFKNJHBOO: int
    def __init__(self, HGNKFIJPJAA: _Optional[_Mapping[int, int]] = ..., PGEJGJMGGOG: _Optional[_Iterable[_Union[_HBFBKIMOOGD_pb2.HBFBKIMOOGD, _Mapping]]] = ..., DIKJLILLNCC: bool = ..., HDBFKNJHBOO: _Optional[int] = ...) -> None: ...
