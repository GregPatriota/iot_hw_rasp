"""
Log printer module
"""

from json import dumps
from datetime import datetime
from env_config import DEBUG_MODE


class FormatLog:
    """
    Centralized class to print logs on terminal
    The variable DEBUG_MODE in env_config module should be set to True
    """

    __DEFAULT_DATE_TEMPLATE = "%d-%m-%Y %H:%M:%S"

    def format_log(self, content=None):
        """
        Method to format the message with timestamp register
        :param content: content in dict format
        :return: no return
        """
        if DEBUG_MODE:
            now_time = datetime.now()
            formatted_now_time = now_time.strftime(self.__DEFAULT_DATE_TEMPLATE)
            print(dumps({
                "timestamp": formatted_now_time,
                **content
            }))
