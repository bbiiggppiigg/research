type ip = 
    | Masked of int * int * int * int * int
    | Normal of int * int * int * int


type value = 
    | IP of ip
    | Number of int
    | Bool of string


type expr = 
    | And of expr * expr
    | Or of expr * expr
    | Implies of expr * expr
    | Not of expr
    | Next of expr 
    | BImplies of expr * expr
    | Plus of expr * expr
    | Minus of expr * expr
    | Assign of expr * expr
    | Value of value
    | Match of expr * expr
    | NMatch of expr * expr

type macro =
  | Invariant of expr 
  | Justice of expr
  | Precedence of expr * expr
  | Reaction of expr * expr * expr
  | Error 
;;
     
(*type prog=
  | Macro of macro 
  | And of macro * macro;;
*)


let rec print_expr expr depth=
    match expr with 
    | BImplies (e1,e2) -> print_string "( BImplies " ; print_expr e1 (depth+1) ; print_string " " ;print_expr e2 (depth+1); print_string ")"
    | Assign (e1,e2) -> print_string "( Assign " ; print_expr e1 (depth+1) ; print_string " " ;print_expr e2 (depth+1); print_string ")"
    | NMatch (e1,e2) -> print_string "( NMatch " ; print_expr e1 (depth+1) ;  print_string " " ;print_expr e2 (depth+1); print_string ")"
    | Match (e1,e2) -> print_string "( Match " ; print_expr e1 (depth+1) ;  print_string " " ;print_expr e2 (depth+1); print_string ")"
    | Implies (e1,e2) ->  print_string "( Implies " ; print_expr e1 (depth+1) ; print_string " " ; print_expr e2 (depth+1); print_string ")"
    | And (e1,e2) -> print_string "( And " ; print_expr e1 (depth+1)  ; print_string " " ;print_expr e2 (depth+1); print_string ")"
    | Or (e1,e2) -> print_string "( Or " ; print_expr e1 (depth+1) ;  print_string " " ;print_expr e2 (depth+1); print_string ")"
    | Next(e) ->  print_string "( Next" ; print_expr e (depth+1); print_string ")"
    | Not(e) -> print_string "( Not" ; print_expr e (depth+1); print_string ")"
    | Value(v) -> print_string "( Value " ;  print_value v;  print_string ")"
    | _ -> print_endline "something else"; ()
and print_value v=
    match v with
    | IP(ip) -> begin 
        match ip with 
        | Masked(n1,n2,n3,n4,mask) -> Printf.printf "( IP ( Masked %d.%d.%d.%d/%d))" n1 n2 n3 n4 mask
        | Normal (n1,n2,n3,n4)  -> Printf.printf "( IP ( Normal %d.%d.%d.%d))" n1 n2 n3 n4
        end

    | Number(n) -> print_string "( Number " ; print_int n ; print_string ")"
    | Bool str -> print_string "( Bool " ; print_string str; print_string ")"

and print_space offset = 
    print_string (String.make offset ' ' )
;;
let print_macro macro = 
    match macro with
    | Invariant(exp) -> print_string "Invariant " ;print_expr exp 1; print_endline ""
    | Justice(exp) -> print_string "Justice " ;print_expr exp 1 ; print_endline ""
    | Precedence(e1,e2) -> print_string  "Precedence "; print_expr e1 1 ; print_string " " ;print_expr e2 1 ; print_endline ""
    | Reaction(e1,e2,e3) -> print_string "Reaction "; print_expr e1 1 ; print_string " " ; print_expr e2 1 ; print_string " " ; print_expr e3 1 ; print_endline ""


