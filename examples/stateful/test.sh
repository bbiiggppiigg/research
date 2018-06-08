#!/bin/bash
compiler.py ids.ss > ids.sl
slugs --explicitStrategy ids.sl > ids.explicit
slugs --symbolicStrategy ids.sl ids.symbolic
