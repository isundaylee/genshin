from genshin.packet.proto import FireworksLaunchParam_pb2 as _FireworksLaunchParam_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FireworksLaunchSchemeData(_message.Message):
    __slots__ = ("launch_param_list", "scheme_id", "fireworks_id_list")
    LAUNCH_PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    SCHEME_ID_FIELD_NUMBER: _ClassVar[int]
    FIREWORKS_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    launch_param_list: _containers.RepeatedCompositeFieldContainer[_FireworksLaunchParam_pb2.FireworksLaunchParam]
    scheme_id: int
    fireworks_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, launch_param_list: _Optional[_Iterable[_Union[_FireworksLaunchParam_pb2.FireworksLaunchParam, _Mapping]]] = ..., scheme_id: _Optional[int] = ..., fireworks_id_list: _Optional[_Iterable[int]] = ...) -> None: ...
