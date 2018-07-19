# The MIT License (MIT)
#
# Copyright (c) 2018 ladyada for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_mcp3xxx.single_ended`
====================================================

Single-ended driver for MCP3xxx ADCs.

* Author(s): Brent Rubell
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_MCP3xxx.git"

from .adafruit_mcp3xxx import MCP3xxx

class MCP3xxx_SingleEnded(MCP3xxx):
    """Base functionality for MCP3xxx analog to digital converters operating
    in single ended mode."""

    def read_adc(self, pin):
        return self._read(pin)

    def read_volts(self, pin, voltage=3.3):
        """Read a single ADC channel and return the voltage as a floating point
        result. Channel must be a value within 0-3.
        """
        assert 0 <= pin <= 7, 'Channel must be a value within 0-7!'
        raw_read = self._read(pin)
        return (raw_read * voltage) / 1023

class MCP3008(MCP3xxx_SingleEnded):
    """MCP3008 10-bit single ended analog to digital converter instance"""

    def __init__(self, *args, **kwargs):
        super(MCP3008, self).__init__(*args, **kwargs)

    def _read_pin(self, pin):
        return self._read(pin)

    def _read_pin_volts(self, pin):
        return self.read_volts(pin)