import resource
import pandas as pd
from pympler.asizeof import asizeof


def get_current_maxrss():
    """ Get the current python process maxrss(high water mark of rss)

        usage the command: man getrusage for more information
        Return:
            maxrss in unit of Mib
    """
    # In Linux, maxrss is in unit of kilobyte
    mem_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return float(mem_kb) / 1024


def size_of(obj):
    """ Estimate the size of object.

        Args:
            python objects
        Return:
            the memory usage in unit of Mib
    """
    if isinstance(obj, pd.DataFrame):
        mem_usage_b = obj.memory_usage(deep=True).sum()
    elif isinstance(obj, pd.Series):
        mem_usage_b = obj.memory_usage(deep=True)
    else:
        mem_usage_b = asizeof(obj)

    ret = round(float(mem_usage_b) / 1024**2, 1)

    return ret
