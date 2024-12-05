class ComputedProperty(property):
    def __init__(self, fget, fset=None, fdel=None, doc=None):
        super().__init__(fget, fset, fdel, doc)
        self._doc = doc

    @property
    def __doc__(self):
        return self._doc


def computed_property(*dependencies):
    def decorator(func):
        property_name = func.__name__
        cache_name = f"_{property_name}_cache"
        dependencies_states = f"_{property_name}_dependencies_states"

        def getter(instance):
            if not hasattr(instance, cache_name):
                setattr(instance, cache_name, None)
                setattr(instance, dependencies_states, {})

            current_states = getattr(instance, dependencies_states)

            cached_invalidated = False
            for dependency in dependencies:
                try:
                    value = getattr(instance, dependency)
                except AttributeError:
                    continue
                if (
                    dependency not in current_states
                    or current_states[dependency] != value
                ):
                    cached_invalidated = True
                    current_states[dependency] = value

            if cached_invalidated:
                cached_value = func(instance)
                setattr(instance, cache_name, cached_value)

            return getattr(instance, cache_name)

        return ComputedProperty(getter, doc=func.__doc__)

    return decorator
