

class Meta(type):
    def __new__(mcs, name, bases, classdict):
        """ new operator """

        def makeProperty(self, name, value, readOnly=False):
            """ add property :name: to class
              this also creates a private :_name: attribute
              if you want to make read only property, set :readOnly: flag to True
              :warn: could raise AttributeError if :name: of :_name: is already defined as an attribute
            """
            fget = lambda self: self._getProperty(name)
            fset = None if readOnly else lambda self, value: self._setProperty(name, value)
            if hasattr(self, "_" + name) or hasattr(self, name):
                raise AttributeError("_%s or %s is already defined as a member" % (name, name))
            setattr(self, '_' + name, value)
            setattr(self.__class__, name, property(fget=fget, fset=fset))

        def _setProperty(self, name, value):
            """ property setter """
            setattr(self, '_' + name, value)

        def _getProperty(self, name):
            """ property getter """
            return getattr(self, '_' + name)

        classdict["makeProperty"] = makeProperty
        classdict["_setProperty"] = _setProperty
        classdict["_getProperty"] = _getProperty
        return type.__new__(mcs, name, bases, classdict)

# example
class DynamicProps(type):
    """
    .. class:: DynamicProps

    dynamic creation of properties
    """

    def __new__(mcs, name, bases, classdict):
        """ new operator """

        def makeProperty(self, name, value, readOnly=False):
            """ add property :name: to class
      this also creates a private :_name: attribute
      if you want to make read only property, set :readOnly: flag to True
      :warn: could raise AttributeError if :name: of :_name: is already defined as an attribute
      """
            fget = lambda self: self._getProperty(name)
            fset = None if readOnly else lambda self, value: self._setProperty(name, value)
            if hasattr(self, "_" + name) or hasattr(self, name):
                raise AttributeError("_%s or %s is already defined as a member" % (name, name))
            setattr(self, '_' + name, value)
            setattr(self.__class__, name, property(fget=fget, fset=fset))

        def _setProperty(self, name, value):
            """ property setter """
            setattr(self, '_' + name, value)

        def _getProperty(self, name):
            """ property getter """
            return getattr(self, '_' + name)

        classdict["makeProperty"] = makeProperty
        classdict["_setProperty"] = _setProperty
        classdict["_getProperty"] = _getProperty
        return type.__new__(mcs, name, bases, classdict)