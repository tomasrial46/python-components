import logging
from programmingtheiot.common.ConfigUtil import ConfigUtil
import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask
from pisense import SenseHAT

class FanActuatorEmulatorTask(BaseActuatorSimTask):
    def __init__(self):
        super(FanActuatorEmulatorTask, self).__init__(
            name=ConfigConst.FAN_ACTUATOR_NAME,
            typeID=ConfigConst.FAN_ACTUATOR_TYPE,
            simpleName="Fan"
        )
        enableEmulation = ConfigUtil().getBoolean(
            ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_EMULATOR_KEY)

        self.sh = SenseHAT(emulate=enableEmulation)

    def _activateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
        if self.sh.screen:
            self.sh.screen.scroll_text("FAN ON", text_colour=(0, 0, 255))
            return 0
        else:
            logging.warning("No SenseHAT screen found.")
            return -1

    def _deactivateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
        if self.sh.screen:
            self.sh.screen.clear()
            return 0
        else:
            logging.warning("No SenseHAT screen to clear.")
            return -1
