"""

Meritous Example: Event Model


"""
from meritous import Model, Schema
from meritous.properties import UUIDProperty, StrProperty, DateProperty

from datetime import date

class EventModel(Model):

    _schema = Schema(**{
        "id"          : UUIDProperty(),
        "title"       : StrProperty(),
        "date"        : DateProperty(),
        "description" : StrProperty(),
    })


event = EventModel()
print(event.id)
event.title = 'Sample Event'
event.date = date.fromisoformat('2023-01-10')
print(event.title)
print(event._schema['date'].value)
