from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from genshin.packet.proto import Vector3Int_pb2 as _Vector3Int_pb2
from genshin.packet.proto import QueryFilter_pb2 as _QueryFilter_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryPathReq(_message.Message):
    __slots__ = ("destination_pos", "query_type", "scene_id", "source_pos", "ANCGPGGGOAJ", "IFMLKJBFKDK", "query_id", "filter")
    class OptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPTION_NONE: _ClassVar[QueryPathReq.OptionType]
        OPTION_NORMAL: _ClassVar[QueryPathReq.OptionType]
        OPTION_FIRST_CAN_GO: _ClassVar[QueryPathReq.OptionType]
    OPTION_NONE: QueryPathReq.OptionType
    OPTION_NORMAL: QueryPathReq.OptionType
    OPTION_FIRST_CAN_GO: QueryPathReq.OptionType
    DESTINATION_POS_FIELD_NUMBER: _ClassVar[int]
    QUERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_POS_FIELD_NUMBER: _ClassVar[int]
    ANCGPGGGOAJ_FIELD_NUMBER: _ClassVar[int]
    IFMLKJBFKDK_FIELD_NUMBER: _ClassVar[int]
    QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    destination_pos: _containers.RepeatedCompositeFieldContainer[_Vector_pb2.Vector]
    query_type: QueryPathReq.OptionType
    scene_id: int
    source_pos: _Vector_pb2.Vector
    ANCGPGGGOAJ: _Vector3Int_pb2.Vector3Int
    IFMLKJBFKDK: _Vector3Int_pb2.Vector3Int
    query_id: int
    filter: _QueryFilter_pb2.QueryFilter
    def __init__(self, destination_pos: _Optional[_Iterable[_Union[_Vector_pb2.Vector, _Mapping]]] = ..., query_type: _Optional[_Union[QueryPathReq.OptionType, str]] = ..., scene_id: _Optional[int] = ..., source_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., ANCGPGGGOAJ: _Optional[_Union[_Vector3Int_pb2.Vector3Int, _Mapping]] = ..., IFMLKJBFKDK: _Optional[_Union[_Vector3Int_pb2.Vector3Int, _Mapping]] = ..., query_id: _Optional[int] = ..., filter: _Optional[_Union[_QueryFilter_pb2.QueryFilter, _Mapping]] = ...) -> None: ...
