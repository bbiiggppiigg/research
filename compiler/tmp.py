def gr1_expr(expr):
    expr = expr.strip()
    print "expr = ",expr
    ast_type = expr.split("(")[0].strip()
    args_string = expr[len(ast_type)-1:]
    print (len(args_string))
    args = parse_args(args_string)
    print "ast_type = ",ast_type," args = ",args,"\n"
    if(ast_type=="Value"):
        return parse_value(args[0]) 
    else:
        if(ast_type == 'And'):
            return And(gr1_expr(args[0]),parse_expr(args[1]))
        if(ast_type == "BImplies"):
            return (gr1_expr(args[0]) == parse_expr(args[1]))
        if(ast_type == "Or"):
            return And(gr1_expr(args[0]),parse_expr(args[1]))
        if(ast_type == "Not"):
            return Not(gr1_expr(args[0]))
        if(ast_type == "Equal"):
            if(is_ip(args[1])):
                print "do something !"
                left = gr1_expr(args[0])
                ips =  get_ip(args[1])
                return And(left <= ips[0] , left >= ips[1])
            else:
                return(gr1_expr(args[0])==parse_expr(args[1]))
 
