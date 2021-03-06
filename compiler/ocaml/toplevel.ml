let macro_list = [];;

let rec main_loop stream ofile= 
    match Stream.peek stream with
    | Some token ->
            begin
                try match token with
                | Token.Invariant   ->  
                        let invariant = (Parser.parse_invariant stream) in  
                        Ast.print_macro invariant ofile;
                | Token.Justice   ->    
                        let justice =  (Parser.parse_justice stream) in 
                        Ast.print_macro justice ofile;
                | Token.Reaction    ->  
                        let reaction = (Parser.parse_reaction stream)in   
                        Ast.print_macro reaction ofile;
                | Token.Precedence  ->  
                        let precedence = (Parser.parse_precedence stream)in   
                        Ast.print_macro precedence ofile;
                | _ -> Printf.printf "expecting macro, get %s\n" (Token.string_of_token token) ;  
                with Stream.Error s ->
                    print_endline "Some Stream Error !!";
                    Stream.junk stream;
            end;
        main_loop stream ofile;
    | None -> ()
