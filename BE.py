import math
def parallel():
	r1=list(map(float,input("Enter first impedance:").strip().split()))[:]
	r2=list(map(float,input("Enter second impedance:").strip().split()))[:]
	a=(r1[0]*r2[0])-(r1[1]*r2[1])
	b=(r1[0]*r2[1])+(r1[1]*r2[0])
	
	conjugate=[r1[0]+r2[0],-1*(r2[1]+r1[1])]


	result=[(a*conjugate[0]-b*conjugate[1]),(a*conjugate[1]+b*conjugate[0])]
	mod=((r1[0]+r2[0])**2+(r1[1]+r2[1])**2)
	
	result[0]/=mod
	result[1]/=mod
	print(result)



def toPhasor():
	q=list(map(float, input("Enter quantity:").strip().split()))[:]
	amp=(q[0]**2+q[1]**2)**0.5
	phase=math.degrees(math.atan(q[1]/q[0]))
	print(amp, phase)


def divide():
	q1=list(map(float, input("Enter quantity 1:").strip().split()))[:]
	q2=list(map(float, input("Enter quantity 2:").strip().split()))[:]
	result=[q1[0]*q2[0]+q1[1]*q2[1],q1[1]*q2[0]-q1[0]*q2[1]]
	mod=((q2[0])**2+(q2[1])**2)
	

	result[0]/=mod;
	result[1]/=mod;

	print(result)

def addPhasors():
	q1=list(map(float, input("Enter quantity 1:").strip().split()))[:]
	q2=list(map(float, input("Enter quantity 2:").strip().split()))[:]

	z1=[q1[0]*math.cos(math.radians(q1[1])),q1[0]*math.sin(math.radians(q1[1]))]
	z2=[q2[0]*math.cos(math.radians(q2[1])),q2[0]*math.sin(math.radians(q2[1]))]
	z=[z1[0]+z2[0],z1[1]+z2[1]]
	print(z)


print("1.Convert to phasor\n2.Parallel addition\n3.Divide\n4.Add phasors")
choice=int(input("Enter choice:"))
if(choice==1):
	toPhasor()

elif(choice==2):
	parallel()
elif(choice==3):
	divide()
else:
	addPhasors()
