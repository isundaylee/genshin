from genshin.packet.proto import CookRecipeData_pb2 as _CookRecipeData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CookDataNotify(_message.Message):
    __slots__ = ("recipe_data_list", "grade")
    RECIPE_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    recipe_data_list: _containers.RepeatedCompositeFieldContainer[_CookRecipeData_pb2.CookRecipeData]
    grade: int
    def __init__(self, recipe_data_list: _Optional[_Iterable[_Union[_CookRecipeData_pb2.CookRecipeData, _Mapping]]] = ..., grade: _Optional[int] = ...) -> None: ...
