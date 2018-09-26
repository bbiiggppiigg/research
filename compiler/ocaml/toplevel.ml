let macro_list = [];;
let rec main_loop stream = 
    match Stream.peek stream with
    | Some token ->
            begin
                try match token with
                | Token.Invariant   ->  
                        let invariant = (Parser.parse_invariant stream) in  
                        Ast.print_macro invariant;
                        invariant; 
                | Token.Justice   ->    
                        let justice =  (Parser.parse_justice stream) in 
                        Ast.print_macro justice;
                        justice ;    
                | Token.Reaction    ->  
                        let reaction = (Parser.parse_reaction stream)in   
                        Ast.print_macro reaction;
                        reaction ;
                | Token.Precedence  ->  
                        let precedence = (Parser.parse_precedence stream)in   
                        Ast.print_macro precedence;
                        precedence; 
                | _ -> Printf.printf "expecting macro, get %s\n" (Token.string_of_token token) ;  Ast.Error
                with Stream.Error s ->
                    print_endline "Some Stream Error !!";
                    Stream.junk stream;
                    Ast.Error
            end;
        (*Stream.junk stream;*)
        main_loop stream;
    | None -> Ast.Error
