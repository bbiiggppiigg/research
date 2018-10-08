let binop_precedence:(Token.token, int) Hashtbl.t = Hashtbl.create 10
let precedence c = try Hashtbl.find binop_precedence c with Not_found -> -1


(* return expression type *)
let rec parse_primary = parser
    | [< 'Token.Number n1 ; ip_or_int=(parse_number n1) >] ->  ip_or_int
    | [< 'Token.Lparen ; expr= parse_expr ; 'Token.Rparen >] -> expr
    | [< 'Token.Not ; expr=parse_negation; >] ->  expr
    | [< 'Token.Next ; expr = parse_expr; >] ->  new Ast.unext expr
    | [< 'Token.Ident str ; expr = (parse_pred str); >] -> expr
    | [<>] -> print_endline "end parsing primary"; new Ast.gg
and parse_negation = parser
    | [<'Token.Lparen ; e = parse_expr ; 'Token.Rparen >] -> new Ast.unot e
    | [<'Token.Ident str>] -> new Ast.bmatch (new Ast.var str) (new Ast.boolean "false")
and print_endline = 
    (fun x -> () )
and parse_pred str = parser
    | [< 'Token.Match; rhs=parse_primary >]  -> new Ast.bmatch ( new Ast.var str) rhs 
    | [< 'Token.NMatch; rhs=parse_primary >] -> new Ast.bnmatch (new Ast.var str) rhs
    | [< 'Token.Gt; rhs=parse_primary >] -> new Ast.bgt (new Ast.var str) rhs
    | [< 'Token.Geq; rhs=parse_primary >] -> new Ast.bgeq (new Ast.var str) rhs
    | [< 'Token.Lt; rhs=parse_primary >] -> new Ast.blt (new Ast.var str) rhs
    | [< 'Token.Leq; rhs=parse_primary >] -> new Ast.bleq (new Ast.var str) rhs
    | [< 'Token.Assign; rhs=parse_primary >] -> new Ast.bassign (new Ast.var str) rhs
    | [<>] -> 
        let lower = String.lowercase str in
        match lower with 
        | "true" -> new Ast.boolean "true"
        | "false" -> new Ast.boolean "false"
        | _ -> new Ast.bmatch (new Ast.var str) (new Ast.boolean "true")
and parse_number n1 = parser 
    | [< 'Token.Dot ; 'Token.Number n2 ; 'Token.Dot ; 'Token.Number n3 ; 'Token.Dot; 'Token.Number n4;  ip=(parse_ip n1 n2 n3 n4) >] -> 
    ip
    | [<>] -> new Ast.integer n1
and parse_ip n1 n2 n3 n4= parser
    | [< 'Token.Div; 'Token.Number mask>] -> new Ast.ip n1 n2 n3 n4 mask
    | [<>] -> new Ast.ip n1 n2 n3 n4 32
and combine_binary op lhs rhs = match op with
    | Token.Implies -> new Ast.bimplies lhs rhs ; 
    | Token.Match -> new Ast.bmatch lhs rhs 
    | Token.NMatch -> new Ast.bnmatch lhs rhs
    | Token.Assign -> new Ast.bassign lhs rhs
    | Token.And  -> new Ast.band lhs rhs
    | Token.Or  -> new Ast.bor lhs rhs
    | Token.BImplies -> new Ast.bbimplies lhs rhs
    | _ -> new Ast.gg
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
            | Token.Implies | Token.Plus | Token.Minus | Token.Mul | Token.Div | Token.Match | Token.Assign | Token.And | Token.Or | Token.BImplies  | Token.NMatch (*as op *)
                -> (*Printf.printf "some binary token %s\n" (Token.string_of_token op);*)
                parse_bin_rhs 0 lhs stream
            | _ -> lhs
            end;
        | _ -> lhs
    end;
    | [<>] -> print_endline "failure pare_primary" ; new Ast.var "hello"


let parse_precedence = parser
| [< 'Token.Precedence; 'Token.Lparen; before = parse_expr; 'Token.Comma ; after = parse_expr; 'Token.Rparen >] 
    ->  
        new Ast.precedence before after

| [<>] -> new Ast.unsupported

let parse_reaction = parser
    | [< 'Token.Reaction; 'Token.Lparen; trigger = parse_expr; 'Token.Comma; policy =parse_expr;'Token.Comma ; deactivate = parse_expr; 'Token.Rparen >] 
        ->  new Ast.reaction trigger policy deactivate
    | [<>] ->new Ast.unsupported


let parse_invariant = parser
    [< 'Token.Invariant; 'Token.Lparen ; prop = parse_expr; 'Token.Rparen >] 
    ->  
        new Ast.invariant prop
| [<>] -> new Ast.unsupported

let parse_justice = parser
    [< 'Token.Justice; 'Token.Lparen ; prop = parse_expr; 'Token.Rparen >] 
    -> new Ast.justice prop 
| [<>] -> new Ast.unsupported





