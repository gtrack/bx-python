"""
Utility functions for interval operations
"""

from bx.bitset import *

def warn( msg ):
    print >> sys.stderr, msg

def fail( msg ):
    print >> sys.stderr, msg
    sys.exit(1)

BED_DEFAULT_COLS = 0, 1, 2, 5
MAX_END = 512*1024*1024

def bits_set_in_range( bits, range_start, range_end ):
    """
    Yield start,end tuples for each span of set bits in [range_start,range_end)
    """
    end = range_start
    while 1:
        start = bits.next_set( end )
        end = min( bits.next_clear( start ), range_end )
        if start >= end: break
        yield start, end
        
def bits_clear_in_range( bits, range_start, range_end ):
    """
    Yield start,end tuples for each span of clear bits in [range_start,range_end)
    """
    end = range_start
    while 1:
        start = bits.next_clear( end )
        if start >= range_end: break
        end = min( bits.next_set( start ), range_end )
        yield start, end
     
