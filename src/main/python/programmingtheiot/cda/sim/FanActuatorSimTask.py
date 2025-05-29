import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask

class FanActuatorSimTask(BaseActuatorSimTask):
    def __init__(self):
        super(FanActuatorSimTask, self).__init__(
            name=ConfigConst.FAN_ACTUATOR_NAME,
            typeID=ConfigConst.FAN_ACTUATOR_TYPE
        )
