#!/bin/bash
compiler.py email.ss > email.sl
slugs --explicitStrategy --jsonOutput email.sl > email.explicit
slugs --symbolicStrategy email.sl email.symbolic
