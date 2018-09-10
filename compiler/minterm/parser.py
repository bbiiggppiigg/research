def ip_to_range(n1,n2,n3,n4,mask=32):
    ip_value = (n1 * (256**3) + n2 * (256**2)  + n3 * (256**1) + n4 ) & 0xffffffff
    #print "mask = ",mask
    rest_mask = ((1<<(32-mask)) - 1) & 0xffffffff
    front_mask = (0xffffffff - rest_mask & 0xffffffff)

    #print '{0:b}'.format(rest_mask),len( '{0:b}'.format(rest_mask)),rest_mask
    #print '{0:b}'.format(front_mask),len( '{0:b}'.format(front_mask)),front_mask


    minimum =  ip_value & front_mask
    maximum = ip_value | rest_mask
    return [minimum,maximum]


def is_ip(expr):
    if(expr.strip().split()[0]!="Value"):
        return False
    args = parse_args(expr)
    return ("IP"==args[0].strip().split()[0])

def get_ip(expr):
    args = parse_args(expr)
    ip_str = parse_args(args[0])
    return parse_ip(ip_str[0])



def find_rparen(expr):
    level =0 
    for i in range(len(expr)):
        c = expr[i]
        if(c=='(') :
            level += 1
        if(c==')') :
            level -= 1
            if(level==0):
                return i
    return -1

def find_lparen(expr):
    return expr.find("(")

def parse_ip(ip_str):
    ip_str = ip_str.strip()
    ip_type,ip = ip_str.split()
    n1,n2,n3,last = ip.split(".")
    if(len(last.split("/"))>1):
        n4,mask = last.split("/")
    else:
        n4 = last
        mask = 32
    return ip_to_range(int(n1),int(n2),int(n3),int(n4),int(mask))


def get_info(expr):
    expr = expr.strip()
    ast_type = expr.split("(")[0].strip()
    args_string = expr[len(ast_type)-1:]
    args = parse_args(args_string)
    return ast_type,args


def parse_args(expr):
    nexpr = expr
    ret = []
    while(find_lparen(nexpr) != -1):
        lpar = find_lparen(nexpr)
        rpar = find_rparen(nexpr)
        arg = nexpr[lpar+1:rpar]
        ret.append(arg)
        nexpr = nexpr[rpar+1:]
    #print len(ret),ret;
    return ret


