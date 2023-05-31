
from meritous.core import Property

import uuid
import datetime


class StrProperty(Property):

    def __init__(self, **kwargs):
        super().__init__(str, **kwargs)


class UUIDProperty(StrProperty):

    def __init__(self, required=True):
        super(StrProperty, self).__init__(str, required=required, default=str(uuid.uuid4()))


    def validate():
        if not super(Property, self).validate():
            return False
        try:
            uuid_obj = UUID(uuid_to_test, version=version)
        except ValueError:
            return False
        return True


class DateProperty(Property):

    def __init__(self, **kwargs):
        super().__init__(datetime.date, **kwargs)
