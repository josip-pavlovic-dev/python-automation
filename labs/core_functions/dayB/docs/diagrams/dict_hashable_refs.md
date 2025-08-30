# 🔑 Hashable vs Unhashable (dict keys)

             +----------------+
             |   HASHABLE     |
             +----------------+
             | int            |
             | float (finite) |
             | str            |
             | bool           |
             | tuple(*)       |
             | frozenset      |
             +----------------+
                  ✅ može biti ključ
                  (stabilan __hash__)

             +----------------+
             | UNHASHABLE     |
             +----------------+
             | list           |
             | dict           |
             | set            |
             | tuple sa list  |
             | bytearray      |
             +----------------+
                  ❌ ne može biti ključ
                  (menja se u mestu → hash se kvari)

`(*)` tuple je hashable SAMO ako su svi njegovi elementi hashable.
