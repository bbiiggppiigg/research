#!/bin/bash
compiler.py gardenwall.ss > gardenwall.sl
slugs --explicitStrategy gardenwall.sl > gardenwall.explicit
slugs --symbolicStrategy gardenwall.sl gardenwall.symbolic
