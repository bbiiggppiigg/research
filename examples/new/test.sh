#!/bin/bash
compiler.py new.ss > new.sl
slugs --explicitStrategy --jsonOutput new.sl > new.explicit
slugs --symbolicStrategy new.sl new.symbolic
