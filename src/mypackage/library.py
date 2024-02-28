import logging


class custom:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def keyword_from_package(self):
        message = "modified keyword from custom package"
        self.logger.info(message)
        return message
