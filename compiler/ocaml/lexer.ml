(*===----------------------------------------------------------------------===
 * Lexer
 *===----------------------------------------------------------------------===*)

(*look at first character until end*)

let rec lex = parser
  (* Skip any whitespace. *)
  | [< ' (' ' | '\n' | '\r' | '\t'); stream >] -> lex stream

  (* identifier: [a-zA-Z][a-zA-Z0-9] *)
  | [< ' ( '_'  | 'A' .. 'Z' | 'a' .. 'z' as c); stream >] ->
      let buffer = Buffer.create 1 in
      Buffer.add_char buffer c;
      lex_ident buffer stream

  (* number: [0-9.]+ *)
  | [< ' ('0' .. '9' as c); stream >] ->
      let buffer = Buffer.create 1 in
      Buffer.add_char buffer c;
      lex_number buffer stream

  (* Comment until end of line. *)
  | [< ' ('#'); stream >] ->
      lex_comment stream
  | [<' (',') ; stream >]->
    [< ' Token.Comma; lex stream >]
   | [<' ('.') ; stream >]->
    [< ' Token.Dot; lex stream >]
  
   | [<' ('!') ; stream >]->
    [< ' Token.Not; lex stream >]

  | [<' ('(') ; stream >]->
    [< ' Token.Lparen; lex stream >]
   | [<' (')') ; stream >]->
    [< ' Token.Rparen; lex stream >]
        
  | [<' ('=' | '-' | '+' | '*' | '/' | '<' | '>' | '&' | '|'  as c ) ; stream >] ->
    let buffer = Buffer.create 1 in
    Buffer.add_char buffer c;
    lex_operator buffer stream


  (* Otherwise, just return the character as its ascii value. *)
  | [< 'c; stream >] ->
      [< 'Token.Kwd c; lex stream >]

  (* end of stream. *)
  | [< >] -> [< >]
and lex_operator buffer = parser
    | [<' ('=' | '-' | '+' | '*' | '/' | '<' | '>' | '&' | '|'  as c ) ; stream >] ->
        Buffer.add_char buffer c;
        lex_operator buffer stream
    | [< stream=lex >] ->
        match Buffer.contents buffer with
        | "==" -> [< 'Token.Equal; stream >]
        | "=" -> [< 'Token.Assign; stream >]
        | "+" -> [< 'Token.Plus; stream >]
        | "-" -> [< 'Token.Minus; stream >]
        | "*" -> [< 'Token.Mul; stream >]
        | "/" -> [< 'Token.Div; stream >]
        | "->" -> [< 'Token.Implies; stream >]
        | "&" | "&&" -> [< 'Token.And; stream >]
        | "|" | "||" -> [< 'Token.Or; stream >]
        | "<->" -> [< 'Token.BImplies; stream >]
        | id -> [<'Token.Ident id; stream >]
and lex_number buffer = parser
  | [< ' ('0' .. '9' as c); stream >] ->
      Buffer.add_char buffer c;
      lex_number buffer stream
  | [< stream=lex >] ->
      [< 'Token.Number (int_of_string (Buffer.contents buffer)); stream >]

and lex_ident buffer = parser (*lex identifier start with a-zA-z , followed by 0-9 *)
  | [< ' ( '_' | 'A' .. 'Z' | 'a' .. 'z' | '0' .. '9' as c); stream >] ->
      Buffer.add_char buffer c;
      lex_ident buffer stream
  | [< stream=lex >] ->
      match Buffer.contents buffer with
      | "Invariant" -> [< 'Token.Invariant; stream >]
      | "Reaction" -> [< 'Token.Reaction; stream >]
      | "Precedence" -> [< 'Token.Precedence; stream >]
      | "X" -> [< 'Token.Next; stream >]
      | id -> [< 'Token.Ident id; stream >]

and lex_comment = parser
  | [< ' ('\n'); stream=lex >] -> stream
  | [< 'c; e=lex_comment >] -> e
  | [< >] -> [< >]
