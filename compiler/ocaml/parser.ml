let binop_precedence:(Token.token, int) Hashtbl.t = Hashtbl.create 10
let precedence c = try Hashtbl.find binop_precedence c with Not_found -> -1

let rec parse_primary = parser
    | [< 'Token.Number n1 ; x=(parse_number n1) >] ->  Ast.Value(x);
    | [< 'Token.Lparen ; e = parse_expr ; 'Token.Rparen >] -> e
    | [< 'Token.Not ; e=parse_negation; >] ->  e
    | [< 'Token.Next ; e = parse_expr; >] ->  Ast.Next(e)
    | [< 'Token.Ident str ; e = (parse_pred str); >] -> print_endline "find a string, checking assignment" ; e 
    | [<>] -> print_endline "end parsing primary"; Ast.Value(Ast.Number(1))
and parse_negation = parser
    | [<'Token.Lparen ; e = parse_expr ; 'Token.Rparen >] -> Ast.Not(e)
    | [<'Token.Ident str>] -> Ast.Not(Ast.Value(Ast.Bool(str)))
and print_endline = 
    (fun x -> () )
and parse_pred lhs = parser
    | [< 'Token.Match; rhs=parse_primary >] -> print_endline "parsed_assignment"; Ast.Match(Ast.Value(Ast.Bool(lhs)),rhs)
    | [< 'Token.NMatch; rhs=parse_primary >] -> print_endline "parsed_assignment"; Ast.NMatch(Ast.Value(Ast.Bool(lhs)),rhs)
    | [<>] -> Ast.Value(Ast.Bool(lhs))
and parse_number n1 = parser 
    | [< 'Token.Dot ; 'Token.Number n2 ; 'Token.Dot ; 'Token.Number n3 ; 'Token.Dot; 'Token.Number n4;  ip=(parse_ip n1 n2 n3 n4) >] -> 
Ast.IP(ip)
    | [<>] -> Ast.Number(n1)
and parse_ip n1 n2 n3 n4= parser
    | [< 'Token.Div; 'Token.Number mask>] -> Ast.Masked(n1,n2,n3,n4,mask)
    | [<>] -> Ast.Normal(n1,n2,n3,n4)
and combine_binary op lhs rhs = match op with
    | Token.Implies -> Ast.Implies(lhs,rhs); 
    | Token.Plus -> Ast.Plus(lhs,rhs); 
    | Token.Minus -> Ast.Minus(lhs,rhs);
    | Token.Match -> Ast.Match(lhs,rhs) 
    | Token.NMatch -> Ast.NMatch(lhs,rhs) 
    | Token.Assign -> Ast.Assign(lhs,rhs)
    | Token.And  -> Ast.And(lhs,rhs)
    | Token.Or  -> Ast.Or(lhs,rhs)
    | Token.BImplies -> Ast.BImplies(lhs,rhs)
and parse_bin_rhs expr_prec lhs stream =
    match Stream.peek stream with
    (* If this is a binop, find its precedence. *)
    | Some (c) when Hashtbl.mem binop_precedence c ->
        let token_prec = precedence c in

        (* If this is a binop that binds at least as tightly as the current binop,
        * consume it, otherwise we are done. *)
        if token_prec < expr_prec then lhs else begin
        (* Eat the binop. *)
        Stream.junk stream;

        (* Parse the primary expression after the binary operator. *)
        let tmprhs = parse_primary stream in

        (* Okay, we know this is a binop. *)
        let rhs =
        match Stream.peek stream with
        | Some (c2) when Hashtbl.mem binop_precedence c2 ->

        (* If BinOp binds less tightly with rhs than the operator after
        * rhs, let the pending operator take rhs as its lhs. *)

            let next_prec = precedence c2 in
            if token_prec < next_prec
            then parse_bin_rhs (token_prec + 1) tmprhs stream
            else tmprhs
        
        
        | _ -> tmprhs
        in

        (* Merge lhs/rhs. *)
        let lhs = combine_binary c lhs rhs in
        parse_bin_rhs expr_prec lhs stream
        end
    | _ -> lhs

(* expression
*   ::= primary binoprhs *) 
and parse_expr = parser
    | [< lhs=parse_primary; stream  >] ->
    print_endline "try parsing rhs";
    begin
        match (Stream.peek stream) with
        | Some(token) -> 
            begin
            match token with
            | Token.Implies | Token.Plus | Token.Minus | Token.Mul | Token.Div | Token.Match | Token.Assign | Token.And | Token.Or | Token.BImplies  | Token.NMatch as op 
                -> (*Printf.printf "some binary token %s\n" (Token.string_of_token op);*)
                parse_bin_rhs 0 lhs stream
            | _ -> lhs
            end;
        | _ -> lhs
    end;
    | [<>] -> print_endline "failure pare_primary" ; Ast.Value(Ast.Bool("hello"))


let parse_precedence = parser
| [< 'Token.Precedence; 'Token.Lparen; before = parse_expr; 'Token.Comma ; after = parse_expr; 'Token.Rparen >] 
    ->  
        (*begin
        print_endline "parsed_precedence" ; 
        Ast.print_macro (Ast.Precedence(before,after)) ;  
        end;*)
        Ast.Precedence(before,after)

| [<>] -> print_endline "failure parse precedence" ; exit 0;Ast.Error 

let parse_reaction = parser
    | [< 'Token.Reaction; 'Token.Lparen; trigger = parse_expr; 'Token.Comma; policy =parse_expr;'Token.Comma ; deactivate = parse_expr; 'Token.Rparen >] 
        ->  
            (*begin
            print_endline "parsed_invariant" ; 
            Ast.print_macro (Ast.Reaction(trigger,policy,deactivate)) ;  
            end;*)
        Ast.Reaction(trigger,policy,deactivate)
    | [<>] -> print_endline "failure parse invariant" ; Ast.Error


let parse_invariant = parser
    [< 'Token.Invariant; 'Token.Lparen ; prop = parse_expr; 'Token.Rparen >] 
    ->  
        (*begin
        print_endline "parsed_invariant" ; 
        Ast.print_macro (Ast.Invariant(prop)) ;  
        end;*)
        Ast.Invariant(prop)
| [<>] -> print_endline "failure parse invariant" ; Ast.Error

let parse_justice = parser
    [< 'Token.Justice; 'Token.Lparen ; prop = parse_expr; 'Token.Rparen >] 
    ->  
        (*begin
        print_endline "parsed_justice" ; 
        Ast.print_macro (Ast.Justice(prop)) ;  
        end;*)
        Ast.Invariant(prop)
| [<>] -> print_endline "failure parse invariant" ; Ast.Error





