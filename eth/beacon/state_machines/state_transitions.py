from abc import (
    ABC,
    abstractmethod,
)

from eth.utils.datatypes import (
    Configurable,
)

from eth.beacon.types.blocks import BaseBeaconBlock
from eth.beacon.types.states import BeaconState

from eth.beacon.state_machines.configs import BeaconConfig


class BaseStateTransition(Configurable, ABC):
    config = None

    def __init__(self, config: BeaconConfig):
        self.config = config

    @abstractmethod
    def apply_state_transition(self, state: BeaconState, block: BaseBeaconBlock) -> BeaconState:
        pass

    @abstractmethod
    def per_slot_transition(self, state: BeaconState, block: BaseBeaconBlock) -> BeaconState:
        pass

    @abstractmethod
    def per_block_transition(self, state: BeaconState, block: BaseBeaconBlock) -> BeaconState:
        pass

    @abstractmethod
    def per_epoch_transition(self, state: BeaconState, block: BaseBeaconBlock) -> BeaconState:
        pass