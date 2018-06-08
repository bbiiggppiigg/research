#!/bin/bash
compiler.py flip.ss > flip.sl
slugs --explicitStrategy --jsonOutput flip.sl > flip.explicit
slugs --symbolicStrategy flip.sl flip.symbolic
