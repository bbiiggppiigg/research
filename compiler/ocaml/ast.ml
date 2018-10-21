class virtual expr = object
    method virtual __repr__: string
end;;

class virtual const = object
    inherit expr
    method virtual __repr__: string
end;;

class integer  initial= object
    inherit const
    val mutable value = initial;
    method __repr__ = Printf.sprintf "(int (%d))" value
end;;

class boolean initial  = object
    inherit const
    val mutable value = 
        let lower = String.lowercase initial in 
        match lower with
        | "true" -> "true"
        | _ -> "false"
    method __repr__ = Printf.sprintf "(bool (%s))" value
end;;

class ip   i1 i2 i3 i4 mask= object
    inherit const
    val mutable tuple = [| i1 ; i2 ; i3 ;  i4 |]
    val mutable mask = mask
    method __repr__ = Printf.sprintf "(ip (%d.%d.%d.%d/%d))" (Array.get tuple 0) (Array.get tuple 1) (Array.get tuple 2) (Array.get tuple 3) mask
end;;

class var name= object
    inherit expr
    val name:string = name
    method __repr__ = Printf.sprintf "(var (%s))" name
end


class predicate ast_type variable const_value = object
    inherit expr
    val mutable ast_type:string = ast_type
    val mutable var:var = variable
    val mutable value:const =  const_value
    
    method __repr__ = 
        Printf.sprintf "( %s %s %s )" ast_type var#__repr__ const_value#__repr__
end;;

class bgt  variable const_value  = object
    inherit predicate "gt" variable const_value
end;;
class bgeq  variable const_value  = object
    inherit predicate "geq" variable const_value
end;;
class blt  variable const_value  = object
    inherit predicate "lt" variable const_value
end;;
class bleq variable const_value  = object
    inherit predicate "leq" variable const_value
end;;
class bassign  variable const_value  = object
    inherit predicate "assign" variable const_value
end;;
class bnassign  variable const_value  = object
    inherit predicate "nassign" variable const_value
end;;

class bmatch  variable const_value  = object
    inherit predicate "match" variable const_value
end;;

class bnmatch  variable const_value  = object
    inherit predicate "nmatch" variable const_value
end;;

class uop ast_type e1= object
    inherit expr
    val e1 = e1
    val ast_type = ast_type
    method __repr__ = Printf.sprintf "(%s %s)" ast_type e1#__repr__
end;;


class unot e1 = object
    inherit uop "not" e1
end;;

class unext e1 = object
    inherit uop "next" e1
end;;

class bool_expr e1 = object
    inherit expr
    val e1:string = e1
    
    method __repr__ =  Printf.sprintf "( bool_expr (%s))" e1
end;;


class bop ast_type e1 e2= object
    inherit expr
    val e1:expr = e1
    val e2:expr = e2
    val ast_type = ast_type
    method __repr__ = Printf.sprintf "(%s %s %s)" ast_type e1#__repr__ e2#__repr__
end;;
class band  e1 e2= object
    inherit bop "and" e1 e2
end
class bor e1 e2= object
    inherit bop "or" e1 e2
end
class bimplies e1 e2= object
    inherit bop "implies" e1 e2
end
class bbimplies e1 e2= object
    inherit bop "bimplies" e1 e2
end

class gg = object
    inherit expr
    method __repr__ = "GG"
end


class virtual macro ast_type= object
    method virtual __repr__:string
    val ast_type:string = ast_type
end

class invariant inv= object
    inherit macro "invariant"
    val inv:expr = inv
    method __repr__ = Printf.sprintf "%s %s" ast_type inv#__repr__ 
end

class justice inv= object
    inherit macro "justice"
    val inv:expr = inv
    method __repr__ = Printf.sprintf "%s %s" ast_type inv#__repr__ 
end


class reaction trigger policy ending= object
    inherit macro "reaction"
    val trigger:expr = trigger
    val policy:expr  = policy
    val ending:expr  = ending 
    method __repr__ = Printf.sprintf "%s %s %s %s" ast_type trigger#__repr__ policy#__repr__ ending#__repr__ 
end

class precedence before after= object
    inherit macro "precedence"
    val bofore:expr = before
    val after:expr  = after
    method __repr__ = Printf.sprintf "%s %s %s" ast_type before#__repr__ after#__repr__ 
end

class unsupported = object
    inherit macro "error"
    method __repr__ = Printf.sprintf "(%s)" ast_type
end

let rec print_expr expr depth=
    print_string  expr#__repr__

let print_macro macro = 
    Printf.printf "%s\n" macro#__repr__

