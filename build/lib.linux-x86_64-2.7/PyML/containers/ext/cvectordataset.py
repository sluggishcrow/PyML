# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info

if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp

        fp = None
        try:
            fp, pathname, description = imp.find_module('_cvectordataset', [dirname(__file__)])
        except ImportError:
            import _cvectordataset

            return _cvectordataset
        if fp is not None:
            try:
                _mod = imp.load_module('_cvectordataset', fp, pathname, description)
            finally:
                fp.close()
            return _mod

    _cvectordataset = swig_import_helper()
    del swig_import_helper
else:
    import _cvectordataset
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method: return method(self, value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method: return method(self)
    raise AttributeError(name)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass

    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")

    __repr__ = _swig_repr
    __swig_destroy__ = _cvectordataset.delete_SwigPyIterator
    __del__ = lambda self: None;

    def value(self): return _cvectordataset.SwigPyIterator_value(self)

    def incr(self, n=1): return _cvectordataset.SwigPyIterator_incr(self, n)

    def decr(self, n=1): return _cvectordataset.SwigPyIterator_decr(self, n)

    def distance(self, *args): return _cvectordataset.SwigPyIterator_distance(self, *args)

    def equal(self, *args): return _cvectordataset.SwigPyIterator_equal(self, *args)

    def copy(self): return _cvectordataset.SwigPyIterator_copy(self)

    def next(self): return _cvectordataset.SwigPyIterator_next(self)

    def __next__(self): return _cvectordataset.SwigPyIterator___next__(self)

    def previous(self): return _cvectordataset.SwigPyIterator_previous(self)

    def advance(self, *args): return _cvectordataset.SwigPyIterator_advance(self, *args)

    def __eq__(self, *args): return _cvectordataset.SwigPyIterator___eq__(self, *args)

    def __ne__(self, *args): return _cvectordataset.SwigPyIterator___ne__(self, *args)

    def __iadd__(self, *args): return _cvectordataset.SwigPyIterator___iadd__(self, *args)

    def __isub__(self, *args): return _cvectordataset.SwigPyIterator___isub__(self, *args)

    def __add__(self, *args): return _cvectordataset.SwigPyIterator___add__(self, *args)

    def __sub__(self, *args): return _cvectordataset.SwigPyIterator___sub__(self, *args)

    def __iter__(self): return self


SwigPyIterator_swigregister = _cvectordataset.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _cvectordataset.IntVector_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cvectordataset.IntVector___nonzero__(self)

    def __bool__(self):
        return _cvectordataset.IntVector___bool__(self)

    def __len__(self):
        return _cvectordataset.IntVector___len__(self)

    def pop(self):
        return _cvectordataset.IntVector_pop(self)

    def __getslice__(self, *args):
        return _cvectordataset.IntVector___getslice__(self, *args)

    def __setslice__(self, *args):
        return _cvectordataset.IntVector___setslice__(self, *args)

    def __delslice__(self, *args):
        return _cvectordataset.IntVector___delslice__(self, *args)

    def __delitem__(self, *args):
        return _cvectordataset.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cvectordataset.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cvectordataset.IntVector___setitem__(self, *args)

    def append(self, *args):
        return _cvectordataset.IntVector_append(self, *args)

    def empty(self):
        return _cvectordataset.IntVector_empty(self)

    def size(self):
        return _cvectordataset.IntVector_size(self)

    def clear(self):
        return _cvectordataset.IntVector_clear(self)

    def swap(self, *args):
        return _cvectordataset.IntVector_swap(self, *args)

    def get_allocator(self):
        return _cvectordataset.IntVector_get_allocator(self)

    def begin(self):
        return _cvectordataset.IntVector_begin(self)

    def end(self):
        return _cvectordataset.IntVector_end(self)

    def rbegin(self):
        return _cvectordataset.IntVector_rbegin(self)

    def rend(self):
        return _cvectordataset.IntVector_rend(self)

    def pop_back(self):
        return _cvectordataset.IntVector_pop_back(self)

    def erase(self, *args):
        return _cvectordataset.IntVector_erase(self, *args)

    def __init__(self, *args):
        this = _cvectordataset.new_IntVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, *args):
        return _cvectordataset.IntVector_push_back(self, *args)

    def front(self):
        return _cvectordataset.IntVector_front(self)

    def back(self):
        return _cvectordataset.IntVector_back(self)

    def assign(self, *args):
        return _cvectordataset.IntVector_assign(self, *args)

    def resize(self, *args):
        return _cvectordataset.IntVector_resize(self, *args)

    def insert(self, *args):
        return _cvectordataset.IntVector_insert(self, *args)

    def reserve(self, *args):
        return _cvectordataset.IntVector_reserve(self, *args)

    def capacity(self):
        return _cvectordataset.IntVector_capacity(self)

    __swig_destroy__ = _cvectordataset.delete_IntVector
    __del__ = lambda self: None;


IntVector_swigregister = _cvectordataset.IntVector_swigregister
IntVector_swigregister(IntVector)


class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _cvectordataset.DoubleVector_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cvectordataset.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _cvectordataset.DoubleVector___bool__(self)

    def __len__(self):
        return _cvectordataset.DoubleVector___len__(self)

    def pop(self):
        return _cvectordataset.DoubleVector_pop(self)

    def __getslice__(self, *args):
        return _cvectordataset.DoubleVector___getslice__(self, *args)

    def __setslice__(self, *args):
        return _cvectordataset.DoubleVector___setslice__(self, *args)

    def __delslice__(self, *args):
        return _cvectordataset.DoubleVector___delslice__(self, *args)

    def __delitem__(self, *args):
        return _cvectordataset.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cvectordataset.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cvectordataset.DoubleVector___setitem__(self, *args)

    def append(self, *args):
        return _cvectordataset.DoubleVector_append(self, *args)

    def empty(self):
        return _cvectordataset.DoubleVector_empty(self)

    def size(self):
        return _cvectordataset.DoubleVector_size(self)

    def clear(self):
        return _cvectordataset.DoubleVector_clear(self)

    def swap(self, *args):
        return _cvectordataset.DoubleVector_swap(self, *args)

    def get_allocator(self):
        return _cvectordataset.DoubleVector_get_allocator(self)

    def begin(self):
        return _cvectordataset.DoubleVector_begin(self)

    def end(self):
        return _cvectordataset.DoubleVector_end(self)

    def rbegin(self):
        return _cvectordataset.DoubleVector_rbegin(self)

    def rend(self):
        return _cvectordataset.DoubleVector_rend(self)

    def pop_back(self):
        return _cvectordataset.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _cvectordataset.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        this = _cvectordataset.new_DoubleVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, *args):
        return _cvectordataset.DoubleVector_push_back(self, *args)

    def front(self):
        return _cvectordataset.DoubleVector_front(self)

    def back(self):
        return _cvectordataset.DoubleVector_back(self)

    def assign(self, *args):
        return _cvectordataset.DoubleVector_assign(self, *args)

    def resize(self, *args):
        return _cvectordataset.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _cvectordataset.DoubleVector_insert(self, *args)

    def reserve(self, *args):
        return _cvectordataset.DoubleVector_reserve(self, *args)

    def capacity(self):
        return _cvectordataset.DoubleVector_capacity(self)

    __swig_destroy__ = _cvectordataset.delete_DoubleVector
    __del__ = lambda self: None;


DoubleVector_swigregister = _cvectordataset.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)


class StringVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _cvectordataset.StringVector_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cvectordataset.StringVector___nonzero__(self)

    def __bool__(self):
        return _cvectordataset.StringVector___bool__(self)

    def __len__(self):
        return _cvectordataset.StringVector___len__(self)

    def pop(self):
        return _cvectordataset.StringVector_pop(self)

    def __getslice__(self, *args):
        return _cvectordataset.StringVector___getslice__(self, *args)

    def __setslice__(self, *args):
        return _cvectordataset.StringVector___setslice__(self, *args)

    def __delslice__(self, *args):
        return _cvectordataset.StringVector___delslice__(self, *args)

    def __delitem__(self, *args):
        return _cvectordataset.StringVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cvectordataset.StringVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cvectordataset.StringVector___setitem__(self, *args)

    def append(self, *args):
        return _cvectordataset.StringVector_append(self, *args)

    def empty(self):
        return _cvectordataset.StringVector_empty(self)

    def size(self):
        return _cvectordataset.StringVector_size(self)

    def clear(self):
        return _cvectordataset.StringVector_clear(self)

    def swap(self, *args):
        return _cvectordataset.StringVector_swap(self, *args)

    def get_allocator(self):
        return _cvectordataset.StringVector_get_allocator(self)

    def begin(self):
        return _cvectordataset.StringVector_begin(self)

    def end(self):
        return _cvectordataset.StringVector_end(self)

    def rbegin(self):
        return _cvectordataset.StringVector_rbegin(self)

    def rend(self):
        return _cvectordataset.StringVector_rend(self)

    def pop_back(self):
        return _cvectordataset.StringVector_pop_back(self)

    def erase(self, *args):
        return _cvectordataset.StringVector_erase(self, *args)

    def __init__(self, *args):
        this = _cvectordataset.new_StringVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, *args):
        return _cvectordataset.StringVector_push_back(self, *args)

    def front(self):
        return _cvectordataset.StringVector_front(self)

    def back(self):
        return _cvectordataset.StringVector_back(self)

    def assign(self, *args):
        return _cvectordataset.StringVector_assign(self, *args)

    def resize(self, *args):
        return _cvectordataset.StringVector_resize(self, *args)

    def insert(self, *args):
        return _cvectordataset.StringVector_insert(self, *args)

    def reserve(self, *args):
        return _cvectordataset.StringVector_reserve(self, *args)

    def capacity(self):
        return _cvectordataset.StringVector_capacity(self)

    __swig_destroy__ = _cvectordataset.delete_StringVector
    __del__ = lambda self: None;


StringVector_swigregister = _cvectordataset.StringVector_swigregister
StringVector_swigregister(StringVector)


class LongVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LongVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LongVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _cvectordataset.LongVector_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cvectordataset.LongVector___nonzero__(self)

    def __bool__(self):
        return _cvectordataset.LongVector___bool__(self)

    def __len__(self):
        return _cvectordataset.LongVector___len__(self)

    def pop(self):
        return _cvectordataset.LongVector_pop(self)

    def __getslice__(self, *args):
        return _cvectordataset.LongVector___getslice__(self, *args)

    def __setslice__(self, *args):
        return _cvectordataset.LongVector___setslice__(self, *args)

    def __delslice__(self, *args):
        return _cvectordataset.LongVector___delslice__(self, *args)

    def __delitem__(self, *args):
        return _cvectordataset.LongVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cvectordataset.LongVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cvectordataset.LongVector___setitem__(self, *args)

    def append(self, *args):
        return _cvectordataset.LongVector_append(self, *args)

    def empty(self):
        return _cvectordataset.LongVector_empty(self)

    def size(self):
        return _cvectordataset.LongVector_size(self)

    def clear(self):
        return _cvectordataset.LongVector_clear(self)

    def swap(self, *args):
        return _cvectordataset.LongVector_swap(self, *args)

    def get_allocator(self):
        return _cvectordataset.LongVector_get_allocator(self)

    def begin(self):
        return _cvectordataset.LongVector_begin(self)

    def end(self):
        return _cvectordataset.LongVector_end(self)

    def rbegin(self):
        return _cvectordataset.LongVector_rbegin(self)

    def rend(self):
        return _cvectordataset.LongVector_rend(self)

    def pop_back(self):
        return _cvectordataset.LongVector_pop_back(self)

    def erase(self, *args):
        return _cvectordataset.LongVector_erase(self, *args)

    def __init__(self, *args):
        this = _cvectordataset.new_LongVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, *args):
        return _cvectordataset.LongVector_push_back(self, *args)

    def front(self):
        return _cvectordataset.LongVector_front(self)

    def back(self):
        return _cvectordataset.LongVector_back(self)

    def assign(self, *args):
        return _cvectordataset.LongVector_assign(self, *args)

    def resize(self, *args):
        return _cvectordataset.LongVector_resize(self, *args)

    def insert(self, *args):
        return _cvectordataset.LongVector_insert(self, *args)

    def reserve(self, *args):
        return _cvectordataset.LongVector_reserve(self, *args)

    def capacity(self):
        return _cvectordataset.LongVector_capacity(self)

    __swig_destroy__ = _cvectordataset.delete_LongVector
    __del__ = lambda self: None;


LongVector_swigregister = _cvectordataset.LongVector_swigregister
LongVector_swigregister(LongVector)


class DataSet(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DataSet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DataSet, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")

    __repr__ = _swig_repr
    __swig_setmethods__["Y"] = _cvectordataset.DataSet_Y_set
    __swig_getmethods__["Y"] = _cvectordataset.DataSet_Y_get
    if _newclass: Y = _swig_property(_cvectordataset.DataSet_Y_get, _cvectordataset.DataSet_Y_set)
    __swig_setmethods__["norms"] = _cvectordataset.DataSet_norms_set
    __swig_getmethods__["norms"] = _cvectordataset.DataSet_norms_get
    if _newclass: norms = _swig_property(_cvectordataset.DataSet_norms_get, _cvectordataset.DataSet_norms_set)
    __swig_setmethods__["kernel"] = _cvectordataset.DataSet_kernel_set
    __swig_getmethods__["kernel"] = _cvectordataset.DataSet_kernel_get
    if _newclass: kernel = _swig_property(_cvectordataset.DataSet_kernel_get, _cvectordataset.DataSet_kernel_set)

    def setY(self, *args):
        return _cvectordataset.DataSet_setY(self, *args)

    def computeNorms(self):
        return _cvectordataset.DataSet_computeNorms(self)

    def setKernel(self, *args):
        return _cvectordataset.DataSet_setKernel(self, *args)

    def attachKernel(self, *args):
        return _cvectordataset.DataSet_attachKernel(self, *args)

    def getKernelMatrixAsVector(self):
        return _cvectordataset.DataSet_getKernelMatrixAsVector(self)

    def size(self):
        return _cvectordataset.DataSet_size(self)

    def dotProduct(self, *args):
        return _cvectordataset.DataSet_dotProduct(self, *args)

    def duplicate(self, *args):
        return _cvectordataset.DataSet_duplicate(self, *args)

    def castToBase(self):
        return _cvectordataset.DataSet_castToBase(self)

    def show(self):
        return _cvectordataset.DataSet_show(self)

    __swig_destroy__ = _cvectordataset.delete_DataSet
    __del__ = lambda self: None;


DataSet_swigregister = _cvectordataset.DataSet_swigregister
DataSet_swigregister(DataSet)


class VectorDataSet(DataSet):
    __swig_setmethods__ = {}
    for _s in [DataSet]: __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorDataSet, name, value)
    __swig_getmethods__ = {}
    for _s in [DataSet]: __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, VectorDataSet, name)
    __repr__ = _swig_repr
    __swig_setmethods__["n"] = _cvectordataset.VectorDataSet_n_set
    __swig_getmethods__["n"] = _cvectordataset.VectorDataSet_n_get
    if _newclass: n = _swig_property(_cvectordataset.VectorDataSet_n_get, _cvectordataset.VectorDataSet_n_set)
    __swig_setmethods__["numFeatures"] = _cvectordataset.VectorDataSet_numFeatures_set
    __swig_getmethods__["numFeatures"] = _cvectordataset.VectorDataSet_numFeatures_get
    if _newclass: numFeatures = _swig_property(_cvectordataset.VectorDataSet_numFeatures_get,
                                               _cvectordataset.VectorDataSet_numFeatures_set)
    __swig_setmethods__["prob"] = _cvectordataset.VectorDataSet_prob_set
    __swig_getmethods__["prob"] = _cvectordataset.VectorDataSet_prob_get
    if _newclass: prob = _swig_property(_cvectordataset.VectorDataSet_prob_get, _cvectordataset.VectorDataSet_prob_set)
    __swig_setmethods__["X"] = _cvectordataset.VectorDataSet_X_set
    __swig_getmethods__["X"] = _cvectordataset.VectorDataSet_X_get
    if _newclass: X = _swig_property(_cvectordataset.VectorDataSet_X_get, _cvectordataset.VectorDataSet_X_set)
    __swig_setmethods__["featureName"] = _cvectordataset.VectorDataSet_featureName_set
    __swig_getmethods__["featureName"] = _cvectordataset.VectorDataSet_featureName_get
    if _newclass: featureName = _swig_property(_cvectordataset.VectorDataSet_featureName_get,
                                               _cvectordataset.VectorDataSet_featureName_set)

    def __init__(self, *args):
        this = _cvectordataset.new_VectorDataSet(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    __swig_destroy__ = _cvectordataset.delete_VectorDataSet
    __del__ = lambda self: None;

    def size(self):
        return _cvectordataset.VectorDataSet_size(self)

    def castToBase(self):
        return _cvectordataset.VectorDataSet_castToBase(self)

    def getPattern(self, *args):
        return _cvectordataset.VectorDataSet_getPattern(self, *args)

    def getFeature(self, *args):
        return _cvectordataset.VectorDataSet_getFeature(self, *args)

    def show(self):
        return _cvectordataset.VectorDataSet_show(self)

    def duplicate(self, *args):
        return _cvectordataset.VectorDataSet_duplicate(self, *args)

    def addPattern(self, *args):
        return _cvectordataset.VectorDataSet_addPattern(self, *args)

    def addFeature(self, *args):
        return _cvectordataset.VectorDataSet_addFeature(self, *args)

    def addFeatures(self, *args):
        return _cvectordataset.VectorDataSet_addFeatures(self, *args)

    def featureIDcompute(self):
        return _cvectordataset.VectorDataSet_featureIDcompute(self)

    def setFeatureName(self, *args):
        return _cvectordataset.VectorDataSet_setFeatureName(self, *args)

    def eliminateFeatures(self, *args):
        return _cvectordataset.VectorDataSet_eliminateFeatures(self, *args)

    def normalize(self, *args):
        return _cvectordataset.VectorDataSet_normalize(self, *args)

    def scale(self, *args):
        return _cvectordataset.VectorDataSet_scale(self, *args)

    def translate(self, *args):
        return _cvectordataset.VectorDataSet_translate(self, *args)

    def mean(self, *args):
        return _cvectordataset.VectorDataSet_mean(self, *args)

    def standardDeviation(self, *args):
        return _cvectordataset.VectorDataSet_standardDeviation(self, *args)

    def weightedSum(self, *args):
        return _cvectordataset.VectorDataSet_weightedSum(self, *args)

    def featureCount(self, *args):
        return _cvectordataset.VectorDataSet_featureCount(self, *args)

    def featureCounts(self, *args):
        return _cvectordataset.VectorDataSet_featureCounts(self, *args)

    def nonzero(self, *args):
        return _cvectordataset.VectorDataSet_nonzero(self, *args)

    def dotProduct(self, *args):
        return _cvectordataset.VectorDataSet_dotProduct(self, *args)

    def libsvm_construct(self, *args):
        return _cvectordataset.VectorDataSet_libsvm_construct(self, *args)


VectorDataSet_swigregister = _cvectordataset.VectorDataSet_swigregister
VectorDataSet_swigregister(VectorDataSet)

# This file is compatible with both classic and new-style classes.


