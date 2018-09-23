#!/bin/bash
compiler.py even.ss > even.sl
slugs --explicitStrategy --jsonOutput even.sl > even.explicit
slugs --symbolicStrategy even.sl even.symbolic
