from genshin.packet.proto import Vector_pb2 as _Vector_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ToTheMoonQueryPathReq(_message.Message):
    __slots__ = ("filter_type", "query_type", "PMELMGPKENE", "destination_pos", "scene_id", "fuzzy_range", "EAHHCMBPGDJ", "CCHHHAJICHB", "astar_method", "source_pos", "query_id")
    class OptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPTION_NONE: _ClassVar[ToTheMoonQueryPathReq.OptionType]
        OPTION_NORMAL: _ClassVar[ToTheMoonQueryPathReq.OptionType]
    OPTION_NONE: ToTheMoonQueryPathReq.OptionType
    OPTION_NORMAL: ToTheMoonQueryPathReq.OptionType
    class AStarMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AStarMethod_CLASSIC: _ClassVar[ToTheMoonQueryPathReq.AStarMethod]
        AStarMethod_TENDENCY: _ClassVar[ToTheMoonQueryPathReq.AStarMethod]
        AStarMethod_ADAPTIVE: _ClassVar[ToTheMoonQueryPathReq.AStarMethod]
        AStarMethod_INFLECTION: _ClassVar[ToTheMoonQueryPathReq.AStarMethod]
    AStarMethod_CLASSIC: ToTheMoonQueryPathReq.AStarMethod
    AStarMethod_TENDENCY: ToTheMoonQueryPathReq.AStarMethod
    AStarMethod_ADAPTIVE: ToTheMoonQueryPathReq.AStarMethod
    AStarMethod_INFLECTION: ToTheMoonQueryPathReq.AStarMethod
    class FilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FilterType_ALL: _ClassVar[ToTheMoonQueryPathReq.FilterType]
        FilterType_AIR: _ClassVar[ToTheMoonQueryPathReq.FilterType]
        FilterType_WATER: _ClassVar[ToTheMoonQueryPathReq.FilterType]
    FilterType_ALL: ToTheMoonQueryPathReq.FilterType
    FilterType_AIR: ToTheMoonQueryPathReq.FilterType
    FilterType_WATER: ToTheMoonQueryPathReq.FilterType
    FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PMELMGPKENE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_POS_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    FUZZY_RANGE_FIELD_NUMBER: _ClassVar[int]
    EAHHCMBPGDJ_FIELD_NUMBER: _ClassVar[int]
    CCHHHAJICHB_FIELD_NUMBER: _ClassVar[int]
    ASTAR_METHOD_FIELD_NUMBER: _ClassVar[int]
    SOURCE_POS_FIELD_NUMBER: _ClassVar[int]
    QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    filter_type: ToTheMoonQueryPathReq.FilterType
    query_type: ToTheMoonQueryPathReq.OptionType
    PMELMGPKENE: bool
    destination_pos: _Vector_pb2.Vector
    scene_id: int
    fuzzy_range: int
    EAHHCMBPGDJ: bool
    CCHHHAJICHB: _containers.RepeatedScalarFieldContainer[int]
    astar_method: ToTheMoonQueryPathReq.AStarMethod
    source_pos: _Vector_pb2.Vector
    query_id: int
    def __init__(self, filter_type: _Optional[_Union[ToTheMoonQueryPathReq.FilterType, str]] = ..., query_type: _Optional[_Union[ToTheMoonQueryPathReq.OptionType, str]] = ..., PMELMGPKENE: bool = ..., destination_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., scene_id: _Optional[int] = ..., fuzzy_range: _Optional[int] = ..., EAHHCMBPGDJ: bool = ..., CCHHHAJICHB: _Optional[_Iterable[int]] = ..., astar_method: _Optional[_Union[ToTheMoonQueryPathReq.AStarMethod, str]] = ..., source_pos: _Optional[_Union[_Vector_pb2.Vector, _Mapping]] = ..., query_id: _Optional[int] = ...) -> None: ...
