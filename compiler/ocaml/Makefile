CC=ocamlc
CC_OPT=-pp camlp4o


all: compiler
	$(CC) $(CC_OPT)  -o ../compiler token.cmo lexer.cmo ast.cmo parser.cmo toplevel.cmo compiler.cmo

token:
	$(CC) $(CC_OPT) -c token.ml
lexer: token
	$(CC) $(CC_OPT) -c lexer.ml

ast: lexer
	$(CC) $(CC_OPT) -c ast.ml

parser: ast
	$(CC) $(CC_OPT) -c parser.ml

toplevel: parser
	$(CC) $(CC_OPT) -c toplevel.ml

compiler: toplevel
	$(CC) $(CC_OPT) -c compiler.ml

clean:
	-rm ../compiler *.cmi *.cmo

