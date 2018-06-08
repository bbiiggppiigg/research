#!/bin/bash
compiler.py simple.ss > simple.sl
slugs --explicitStrategy --jsonOutput simple.sl > simple.explicit
slugs --symbolicStrategy simple.sl simple.symbolic
