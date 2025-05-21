import logging
import unittest
from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.cda.connection.MqttClientConnector import MqttClientConnector
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.DataUtil import DataUtil

class MqttClientControlPacketTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Iniciando pruebas de paquetes de control MQTT...")
        cls.cfg = ConfigUtil()
        cls.mcc = MqttClientConnector()

    def test_connect_and_disconnect(self):
        self.mcc.connectClient()
        sleep(2)
        self.mcc.disconnectClient()
        sleep(2)

    def test_publish_qos_levels(self):
        self.mcc.connectClient()
        sleep(2)
        for qos in [0, 1, 2]:
            sensor_data = SensorData()
            sensor_data.setValue(25.0 + qos)
            payload = DataUtil().sensorDataToJson(sensor_data)
            self.mcc.publishMessage(resource=ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, msg=payload, qos=qos)
            sleep(2)
        self.mcc.disconnectClient()
        sleep(2)

    def test_subscribe_and_unsubscribe(self):
        self.mcc.connectClient()
        sleep(2)
        self.mcc.subscribeToTopic(resource=ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE, qos=1)
        sleep(2)
        self.mcc.unsubscribeFromTopic(resource=ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE)
        sleep(2)
        self.mcc.disconnectClient()
        sleep(2)

    def test_ping(self):
        self.mcc.connectClient()
        sleep(self.cfg.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.KEEP_ALIVE_KEY, ConfigConst.DEFAULT_KEEP_ALIVE) + 5)
        self.mcc.disconnectClient()
        sleep(2)

if __name__ == "__main__":
	unittest.main()