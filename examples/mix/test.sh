#!/bin/bash
compiler.py auth.ss > auth.sl
slugs --explicitStrategy auth.sl > auth.explicit
slugs --symbolicStrategy auth.sl auth.symbolic
