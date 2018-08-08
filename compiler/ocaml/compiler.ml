let main() = 
    Hashtbl.add Parser.binop_precedence Token.And 50;
    Hashtbl.add Parser.binop_precedence Token.Or 40;
    Hashtbl.add Parser.binop_precedence Token.Implies 30;
    Hashtbl.add Parser.binop_precedence Token.BImplies 20;
     
    let filename = Array.get Sys.argv 1 in
    let infile = open_in filename in
    let stream = Stream.of_channel infile in
    Toplevel.main_loop (Lexer.lex stream);
;;
main()
