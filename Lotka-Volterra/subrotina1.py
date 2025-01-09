def der(t,u,args):
    N,P = u
    r,c,b,m = args
    return [r*N - c*N*P,  b*N*P - m*P ]

def der_2(t,u,args):
  N, P = u
  r, c, b, m, h = args
  return [ (r-h)*N - c*N*P,  b*N*P - (m+h)*P ]

def der_3(t,u,args):
  N, P = u
  r, c, b, m, K = args
  return [ r*N*(1 - N/K) - c*N*P, b*N*P - m*P ]

def der_adm(t,u,args):
    x,y = u
    alfa,beta = args
    return [x*(1-x-y),beta*(x-alfa)*y]

def der_lim(t,u,args):
    r,theta = u
    beta, a, omega, b = args
    return [r*(beta + a*r*r), omega + b*r*r ]

