CC=ocamlc
CC_OPT=-pp camlp4o


all: compiler.cmi
	$(CC) $(CC_OPT)  -o ../compiler token.cmo lexer.cmo ast.cmo parser.cmo toplevel.cmo compiler.cmo

token.cmi: token.ml
	$(CC) $(CC_OPT) -c token.ml
lexer.cmi: token.cmi lexer.ml
	$(CC) $(CC_OPT) -c lexer.ml

ast.cmi: lexer.cmi ast.ml
	$(CC) $(CC_OPT) -c ast.ml

parser.cmi: ast.cmi parser.ml
	$(CC) $(CC_OPT) -c parser.ml

toplevel.cmi: parser.cmi toplevel.ml
	$(CC) $(CC_OPT) -c toplevel.ml

compiler.cmi: toplevel.cmi compiler.ml
	$(CC) $(CC_OPT) -c compiler.ml

clean:
	-rm ../compiler *.cmi *.cmo

