import os,json,urllib.request as w
o=16,-16,1,-1,15,17,-15,-17
n=14,18,31,33,-14,-18,-31,-33
J=(n,o[4:],o[:4],o,o)
Q=[i for i in range(128)if not i&136]
V=0,100,320,330,500,900,0
R={0:2,4:3,7:1,112:8,116:12,119:4}
Y=2654435761
def Z(p,s):return((p+7)*131+s)*Y
def A(i,s):
 for w in n:
  j=i+w
  if not j&136 and B[j]==2*s:return 1
 for w in o:
  j=i+w
  while not j&136:
   p=B[j]*s
   if p:
    if p==5 or p==3+(abs(w)in(1,16)) or j==i+w and(p==6 or p==1 and abs(w+16*s)==1):return 1
    break
   j+=w
 return 0
def E():
 v=g=f=w=0;b=[0,0,0]
 for i in Q:
  p=B[i]
  if p:
   t=abs(p);s=1-2*(p<0);r=i>>4;x=14-abs(2*(i&7)-7)-abs(2*r-7)
   if t==6:g+=s*x;f+=s*(12*(r==7*(s<0))-x)
   else:v+=s*(V[t]+5*(r if s>0 else 7-r)*(t==1)+x*(1,4,3,1,1)[t-1]);w+=(0,1,1,2,4)[t-1];b[s]+=t==3
 w=min(w,24)
 return v+25*((b[1]>1)-(b[-1]>1))+(g*(24-w)+f*w)//24
def G(s,c,e,t):
 for i in Q:
  p=B[i]*s
  if p==1:
   j=i+16*s
   if not B[j]:
    yield i,j
    if i>>4==1+5*(s<0) and not B[j+16*s]:yield i,j+16*s
   for j in(j-1,j+1):
    if not j&136 and(B[j]*s<0 or j==e):yield i,j
  elif p>1:
   for w in J[p-2]:
    j=i+w
    while not j&136 and B[j]*s<=0:
     yield i,j
     if B[j] or p in(2,6):break
     j+=w
 if not t:
  i=4+112*(s<0)
  for w,b in((1,1),(-1,2)):
   if c&b<<(2*(s<0)) and not(B[i+w] or B[i+2*w] or w<0 and B[i-3]) and not A(i+w,-s):yield i,i+2*w
def M(i,j,s,e):
 global H
 p=B[i];k=K[s];u=j;v=w=i
 if p==s and j==e:u=j-16*s
 if p==6*s:
  K[s]=j
  if j-i==2:v=i+1;w=i+3
  if j-i==-2:v=i-1;w=i-4
 a=B[u];h=H
 q=5*s if p==s and j>>4 in(0,7) else p
 H^=Z(p,i)^Z(q,j)
 if a:H^=Z(a,u)
 if v!=i:H^=Z(B[w],w)^Z(B[w],v)
 H^=Y
 B[u]=B[i]=0;B[v]=B[w];B[w]=0;B[j]=q
 return p,k,u,a,v,w,h
def U(i,j,s,z):
 global H
 p,k,u,a,v,w,h=z;B[w]=B[v];B[v]=B[j]=0;B[i]=p;B[u]=a;K[s]=k;H=h
def X(c,i,j,p):return c&~(R.get(i,0)|R.get(j,0)),(i+j)//2 if abs(p)==1 and abs(i-j)==32 else -1
def S(s,c,e,d,a,b,h):
 global N
 N-=1;d=max(d,0)
 if N<0:return 0
 if h>60:return s*E()
 key=(H,c,e)
 if h and D.get(key,0)+W.count(key)>2:return 0
 k=A(K[s],-s);q=d<1 and not k;l=a;p=m=0
 r,vv,f,p=T.get(key,(-1,0,0,0))
 if r>=d:
  vv=vv+h*((vv<-29000)-(vv>29000))
  if not f or f>0 and vv>=b or f<0 and vv<=a:return vv
 z=h-30000
 if q:z=s*E();a=max(a,z)
 def F(mm):
  i,j=mm;t=abs(B[i]);vv=V[abs(B[j])]+(900*(j>>4 in(0,7))+100*(j==e))*(t==1)
  return 30000*(mm==p and not q)+(16*vv-t if vv else 8*(not q and mm==L.get(h)))
 for i,j in G(s,c,e,k) if q and z>=b else sorted(G(s,c,e,k),key=F,reverse=True):
  t=B[j] or B[i]==s and(j==e or j>>4 in(0,7));x=M(i,j,s,e)
  if A(K[s],-s):U(i,j,s,x);continue
  if q and(z>=b or not t):U(i,j,s,x);m=(i,j);break
  cc,ee=X(c,i,j,x[0]);W.append((H,cc,ee))
  v=-S(-s,cc,ee,d-1,-a-1 if m else-b,-a,h+1)
  if m and a<v<b:v=-S(-s,cc,ee,d-1,-b,-a,h+1)
  W.pop();U(i,j,s,x)
  if N<0:return 0
  if not m or v>z:m=(i,j);z=max(z,v)
  a=max(a,z)
  if a>=b:
   if not t:L[h]=(i,j)
   break
 if not m and not k:z=0
 T[key]=(d,z+h*((z>29000)-(z<-29000)),(z>=b)-(z<=l),m)
 return z
E0=os.environ['MAKEFUN_ENV_URL'].rstrip('/')
def P(p,d):return json.load(w.urlopen(E0+p,json.dumps(d).encode()))
def I(x):return ord(x[0])-97+16*(int(x[1])-1)
def O(i):return chr(97+(i&7))+str(1+(i>>4))
while 1:
 g=P('/game',{})
 if g['status']=='done':break
 D={};a=g['game']
 while g.get('legal_moves'):
  f,s,c,e,*_=g['fen'].split()
  s=1-2*(s=='b');c=sum(1<<i for i,x in enumerate('KQkq') if x in c);e=-1 if e=='-' else I(e)
  B=[0]*128;K=[0]*3;i=112
  for x in f:
   if x=='/':i-=24
   elif x.isdigit():i+=int(x)
   else:
    p=' pnbrqk'.index(x.lower())*(1-2*x.islower());B[i]=p
    if abs(p)==6:K[p//6]=i
    i+=1
  H=0
  for i in Q:H^=B[i]and Z(B[i],i)
  H^=Y*(s<0)
  key=(H,c,e);D[key]=D.get(key,0)+1;W=[];T={};L={};N=100000;m=g['legal_moves'][0]
  for d in range(1,99):
   v=S(s,c,e,d,-30000,30000,0)
   if N<0:break
   r=T[key][3]
   if not r:break
   i,j=r;m=O(i)+O(j)+'q'*(B[i]==s and j>>4 in(0,7))
   if abs(v)>29000:break
  if m not in g['legal_moves']:m=g['legal_moves'][0]
  i=I(m);j=I(m[2:]);p=B[i];M(i,j,s,e);cc,ee=X(c,i,j,p);k2=(H,cc,ee);D[k2]=D.get(k2,0)+1
  g=P('/move',{'game':a,'move':m})
