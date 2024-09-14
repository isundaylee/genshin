from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class VehicleInteractType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VEHICLE_INTERACT_TYPE_NONE: _ClassVar[VehicleInteractType]
    VEHICLE_INTERACT_TYPE_IN: _ClassVar[VehicleInteractType]
    VEHICLE_INTERACT_TYPE_OUT: _ClassVar[VehicleInteractType]
VEHICLE_INTERACT_TYPE_NONE: VehicleInteractType
VEHICLE_INTERACT_TYPE_IN: VehicleInteractType
VEHICLE_INTERACT_TYPE_OUT: VehicleInteractType
