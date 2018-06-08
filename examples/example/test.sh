#!/bin/bash
compiler.py example.ss > example.sl
slugs --explicitStrategy --jsonOutput example.sl > example.explicit
slugs --symbolicStrategy example.sl example.symbolic
