import base64

m=[]
v=open("v305.b",'w')
for i in range(300):
    if i%5==0:
        c=open(str(i)+'.raw','rb')
        q=c.read()
        c.close()
        e=base64.b64encode(q)
        g=str(e,encoding="utf8")
        v.write(g+"\n")
v.close()