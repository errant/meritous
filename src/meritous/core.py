
from .exceptions import PropertyException, SchemaException, ModelException


class Property:
    _value = None
    _type = None
    _default = None
    _required = None

    def __init__(self, type, default=None, required=True, validate_on_set=True):

        self._type = type
        self.validate_on_set = validate_on_set
        self._required = required

        if default:
            self._default = default
            self.value = default

    def validate(self):
        return type(self._value) == self._type

    @property
    def is_required(self):
        return self._required

    def _format_value(self, value):
        return value

    @property
    def value(self):
        return self._format_value(self._value)

    @value.setter
    def value(self, value):
        if self.validate_on_set and not(type(value) == self._type):
            raise PropertyException("{0} attempted to set value {1} which doesn't match property type {2}".format(self.__class__.__name__, value, self._type))
        self._value = value


class Schema(dict):

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def marshall(self, store):
        return map(lambda name, property: store.marshall(property.value), self.items())

    def validate(self):
        for property_name, property in self.items():
            if not isinstance(property, Property):
                raise SchemaException('Property {0} is not an instance of Property class'.format(property_name))
            if not property.validate():
                raise PropertyException("{0} has value {1} which doesn't match property type {2}".format(property.__class__.__name__, property._value, property._type))


class Model:
    _schema = None
    _data = None

    def marshall(self, store):
        return self._schema._storage_representation(store)

    def validate(self):
        self._schema.validate()

    def __getattr__(self, name):
        if name in self._schema:
            return self._schema[name].value

    def __setattr__(self, name, value):
        if name in self._schema:
            self._schema[name].value = value
        else:
            self.__dict__[name] = value


class Store:

    def save(self, **kwargs):
        pass

    def marshall(self, value):
        return str(value)

    @staticmethod
    def load(self, **kwargs):
        pass
