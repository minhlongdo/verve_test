import logging


LOGGER = logging.getLogger(__name__)


class RewardsEngine(object):

    # Store this here for now till I think of how we should get this data in to the Engine.
    REWARDS = {"rewards": [
        {"name": "General Ticket", "points": 100, "max_per_user": 5},
        {"name": "VIP Ticket", "points": 1000, "max_per_user": 1},
        {"name": "Weekend Ticket", "points": 250, "max_per_user": 2},
        {"name": "Free Drink Voucher", "points": 50, "max_per_user": 10},
        {"name": "Free Limo to event", "points": 5000, "max_per_user": 1}
    ]
    }

    # to be consistent "queueService" should be "queue_service"
    def __init__(self, queue_service):
        self._queue_service = queue_service

    def points_from_purchase(self, price):
        return price * 10

    def on_message(self, body):
        LOGGER.info('REWARDS ENGINE message %s', body)
