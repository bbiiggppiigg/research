#!/bin/bash
compiler.py atom.ss > atom.sl
slugs --explicitStrategy --jsonOutput atom.sl > atom.explicit
slugs --symbolicStrategy atom.sl atom.symbolic
