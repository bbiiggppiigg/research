#!/usr/bin/python
from subprocess import check_output , STDOUT
import shlex
import generate_slug
import gen_frenetic

def parse_spec(path):
    cmd = "./compiler %s.txt  %s.ast" % (path,path)
    print cmd
    out = check_output(shlex.split(cmd),stderr=STDOUT)
    if ("Success" in out):
        return True
    print "Something Wrong parsing the spec",out
    exit(-1)
    return False
    
def execute_slugs(path):
    cmd = "/home/frenetic/slugs/src/slugs --symbolicStrategy %s.slugs %s.symbolic" % (path,path)
    print cmd
    out = check_output(shlex.split(cmd),stderr=STDOUT)
    if( "is realizable" in out ):
        return True
    print "Something Wrong with the spec",out
    exit(-1)

def execute_minterm(path):
    decl = path+".decl"
    ast = path+".ast"
    slugs = path+".structured_slugs"
    db = path + ".db"
    ret = generate_slug.generate_slugs(decl,ast,slugs,db)
    if (not ret):
        print "Someting Wrong with generating slugs"
        exit(-1)
    return ret

def gen_final(path):
    db = path + ".db"
    strategy = path + ".symbolic"
    code = path +".py"
    ret = gen_frenetic.gen_frenetic(db,strategy,code)
    if (not ret):
        print "Someting Wrong with generating code",ret
        exit(-1)
    return ret


def main():
    example="liveness"
    #example="block"
    path="example/%s/%s"%(example,example)
    parse_spec(path)
    execute_minterm(path)
    execute_slugs(path)
    gen_final(path)

main()
