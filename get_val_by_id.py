#get object value when the variable is lost
import ctypes
object_id = int(input('object\'s id: '))
print(ctypes.cast(object_id, ctypes.py_object).value)
