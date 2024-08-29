from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16.enums import ChargePointStatus, Action

class EVCharger(cp):
    def __init__(self, id, connection):
        super().__init__(id, connection)
        self.status = ChargePointStatus.available

    async def send_status_notification(self):
        """ Send a status notification to the Central System. """
        response = await self.call(
            action="StatusNotification",
            status=self.status
        )
        print(f"Status notification sent: {response}")

    @on(Action.StartTransaction)
    async def on_start_transaction(self, **kwargs):
        print("Charging started.")
        self.status = ChargePointStatus.charging
        await self.send_status_notification()
        return {
            "idTagInfo": {
                "status": "Accepted",
            },
            "transactionId": 1,
        }

    @on(Action.StopTransaction)
    async def on_stop_transaction(self, **kwargs):
        print("Charging stopped.")
        self.status = ChargePointStatus.available
        await self.send_status_notification()
        return {
            "idTagInfo": {
                "status": "Accepted",
            }
        }
