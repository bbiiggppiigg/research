(*===----------------------------------------------------------------------===
 * Lexer Tokens
 *===----------------------------------------------------------------------===*)

(* The lexer returns these 'Kwd' if it is an unknown character, otherwise one of
 * these others for known things. *)
type token =
  (* commands *)
  | Invariant | Precedence | Reaction | Justice
  
  | Next | Not
  | Comma | Dot
  | Implies | Plus | Minus | Mul | Div | Equal | Assign | And | Or | BImplies 
  | Lparen | Rparen
  (* primary *)
  | Ident of string | Number of int

  (* unknown *)
  | Kwd of char
  

let string_of_token tok = 
    match tok with
    | Not -> "not"
    | Invariant -> "invariant"
    | Precedence -> "precedence"
    | Reaction -> "reaction"
    | Justice -> "justice"
    | Next -> "next"
    | Comma -> "comma"
    | Dot -> "dot"
    | Implies -> "implies"
    | BImplies -> "bimplication"
    | Plus -> "plus"
    | Minus -> "minus"
    | Equal -> "equal"
    | Assign -> "assign"
    | And -> "and"
    | Or -> "or"
    | Lparen -> "lparen"
    | Rparen -> "rparen"
    | Ident str -> Printf.sprintf "ident:%s" str
    | Number n -> Printf.sprintf "number:%d" n
    | Kwd c -> Printf.sprintf "kwd:%c" c


