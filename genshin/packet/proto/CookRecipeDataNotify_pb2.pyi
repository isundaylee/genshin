from genshin.packet.proto import CookRecipeData_pb2 as _CookRecipeData_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CookRecipeDataNotify(_message.Message):
    __slots__ = ("recipe_data",)
    RECIPE_DATA_FIELD_NUMBER: _ClassVar[int]
    recipe_data: _CookRecipeData_pb2.CookRecipeData
    def __init__(self, recipe_data: _Optional[_Union[_CookRecipeData_pb2.CookRecipeData, _Mapping]] = ...) -> None: ...
