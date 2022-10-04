#This program analyzes video Jpeg-sequence and calculate dynamics of border moving between light and shadow  in refractometr.

#!!!!NOTE! video should be in folder : "C:\Python27\Movies

#!!!!NOTE! files txt can be found in folder: "C:\Python27\Txtfiles
#default sr_brightness 44.416 (35/55/sr)////default border color value 39

#In my simulations the slope of plot was accurate but the second part of graph lay in approximately 0.0007 (in n-coef  scale) below real dependency!

#For its workis needed knowledge of several parametrs : name of video, name of txt-file, number of jpeg-images,
#Y&X coordinates  of cross in pixels,  values of initial  and cross N.

from PIL import Image#,  ImageDraw#,  ImageChops
#import math
#import string

way1=raw_input('print way to folder for txt files: default: C:\Python27\Txtfiles\ \n')

if  len(way1)!=0:
    type_d=1
else:
    type_d=0
way2=raw_input('print way to your video folder: default: C:\Python27\Movies\(and here folder \imya\inya_#####.jpg files should be)\n')
if  len(way2)!=0:
    type_e=1
else:
    type_e=0

#print type_d, type_e
name1=raw_input('print name of video:')

name2=raw_input('print name of txt-file:')

s3=int(input('print number of jpeg images in sequence:'))

s4=int(input('print Y coordinate:'))

x_per=int(input('print X coordinate:'))

n_init=float(input('print n initial:'))

n_per=float(input('print n cross:'))


#! the most important parametrs
def_br=round(44.4162122864,10)#no_change

#! the most important paeametrs
def_aaaa=39#can_change --- border color value

if (n_per>2)|(n_init>2)|(n_init<1)|(n_per<1)|(n_init>n_per)|(abs(n_per-n_init)>1):
    print "Mistake in parametrs!"
    print "Do you want to continue?"
    
type_a=1#brightness mode

type_b=1#monochrome camera
#!
#type_b=0
if(type_b==0):
    def_br=round(15.131314,10)
    def_aaaa=13





#! the most important parametrs
type_c=10#can_change delta Y
text=".txt"

if (type_d==0):
    text="C:\Python27\Txtfiles\.txt"# can_change --- way to your folder
else:
    text=way1+text[0:]

    
b=len(text)-4
text=text[0:b]+name2+text[b:]

ff = open(text, 'w')
factor = int(input('ready to start, press 1:'))
ff.write("im_num")  
ff.write(";")
ff.write("average_n")
ff.write("\n")
ksum1=0
sum1=0
qsum=0
qqsum=0
qqqsum=0
ti=0.165*s3*1.0000/500*10*(1+type_a)*(1+type_a)/0.04

print "all is normal, wait about " +str(ti)+"minutes..."

aaaa=def_aaaa/def_br #no_change
bsum=0
nsum=0
k=1.0000000000
x1ot=1
print aaaa #  relative border value of your video

if (type_a!=0):
    for mm in range(48,49):
        for ll in range(48,58):
            for kk in range(48,58):
                for jj in range(48,58):
                    for ii in range(48,58):
                        if (((kk-48) *100+(jj-48)*10+(ii-48)+(ll-48)*1000)>s3):    
                            break
                        if ((mm==48)&(ll==48)&(kk==48)&(jj==48)&(ii==48)):
                            bsum=0
                            ksum1=0
                            sum1=0
                        text="_.jpg"
                        if (type_e==0):
                            text="C:\Python27\Movies\_.jpg"
                        else:
                            text=way2+text[0:]
    


                       
                        #text="C:\Python27\Movies\_.jpg"#can_change --- wau to txt files folder
                        path_l=len(text)-5      
                        text=text[0:path_l]+ name1+text[path_l-1]+name1 +text[path_l]+chr(mm)+chr(ll)+chr(kk)+chr(jj)+chr(ii)+text[(path_l+1):]
                        
                        ss=Image.open(text)
                        f=0.00000001
                        w1,h1=ss.size
                        if (x_per<w1*0.5)|(x_per>(w1-200))|(s4>(0.6*h1))|(s4<0.4*h1):
                            print "Mistake in parametrs!*1"
                            break
                        t1=list(ss.getdata())
                        w1,h1=ss.size
                        ksum1=0
                        sum1=0
                        qsum=0
                        qqsum=0

                        for y in range(0,h1):
                            for x in range(0,w1):
                                if (x>w1*0.5)&(x<0.9*w1)&(y<0.8*h1)&(y>0.2*h1):                                    
                                    offse=y*w1+x
                                    r,g,b=t1[offse]         
                                    S = r+g+b
                                    if (type_b==1)&(S/3>35)&(S/3<55):#no_change!
                                        sum1=sum1+S
                                        ksum1=ksum1+1
                                    if (type_b==0)&(S/3>10)&(S/3<35):#no_change!
                                        sum1=sum1+S
                                        ksum1=ksum1+1
                                    if (S/3>10)&(S/3<225) :
                                        qsum=qsum+1
                                        qqsum=qqsum+S
                        bsum=bsum+sum1/ksum1     
                        qqqsum=qqqsum+qqsum/qsum              
  

    bsum=round(bsum/(3.00*(1+s3)), 10)
    qqqsum=round(qqqsum/(3.00*(1+s3)),10)
    aaaa=bsum*aaaa#can_change_in_manual_mode---border value for your video
    
    ndif=0.0
for mm in range(48,49):
    for ll in range(48,58):
        for kk in range(48,58):
            for jj in range(48,58):
                for ii in range(48,58):        
                    if (((kk-48) *100+(jj-48)*10+(ii-48)+(ll-48)*1000)>s3): 
                        break
                    text="_.jpg"
                    if (type_e==0):
                        text="C:\Python27\Movies\_.jpg"
                    else:
                        text=way2+text[0:]


                    path_l=len(text)-5      
                    text=text[0:path_l]+ name1+text[path_l-1]+name1 +text[path_l]+chr(mm)+chr(ll)+chr(kk)+chr(jj)+chr(ii)+text[(path_l+1):]
                  
                    ss=Image.open(text)
                    f=0.00000001
                    w1,h1=ss.size
                    if (x_per<w1*0.5)|(x_per>(w1-200))|(s4>(0.6*h1))|(s4<0.4*h1):
                        print "Mistake in parametrs!*2"
                        break
                    t1=list(ss.getdata())
                    x1min=1100
                    x1res=0.0000
                    x2res=0.00000
                    x2resnum=0.0000
                    f2=0.00001
                       
                    y11=0
                    x11=0
                    ksum1=0
                    sum1=0
                    if (ksum1!=0):
                        ksum1=ksum1-ksum1
                        print "if 0 !"
                      
                    #find brightness of every image
                    if (type_a!=0):
                        ksum1=0
                        sum1=0
                        for y in range(0,h1):
                            for x in range(0,w1):
                                offse=y*w1+x
                                r,g,b=t1[offse]         
                                S = r+g+b
                                if (type_b==1)&(x>w1*0.5)&(x<0.9*w1)&(y<0.8*h1)&(y>0.2*h1)&(S/3<50)&(S/3>25): #no_change!
                                    if (y==0)&(x==0):
                                        ksum1=0
                                        sum1=0   
                                    sum1=sum1+S                                    
                                    ksum1=ksum1+1
                                if (type_b==0)&(x>w1*0.5)&(x<0.9*w1)&(y<0.8*h1)&(y>0.2*h1)&(S/3<35)&(S/3>10): #no_change!
                                    if (y==0)&(x==0):
                                        ksum1=0
                                        sum1=0   
                                    sum1=sum1+S                                    
                                    ksum1=ksum1+1
                    else:
                        aaaa=def_aaaa #no_change!
                    #aaaa=def_aaaa # _ not to notice bright of full video
                    for y in range(0,h1):
                        for x in range(0,w1):
                            offse=y*w1+x
                            r,g,b=t1[offse]       
                            S = r+g+b       
                            if (type_a!=0):
                                if ((mm==48)&(ll==48)&(kk==48)&(jj==48)&(ii==48)):
                                    aa=aaaa#no_change
                                    
                                    aa_1=round(sum1/ksum1, 10)
                                   # bb=15
                                else:    
                                    aa=round(aaaa*ksum1*aa_1/(sum1), 10)
                                
                            else:
                                aa=aaaa
                            #color checking; height in  delta +-10 cross y
                            if(type_b==0)|(type_b==1):  #       (type_b!=0):
                                if (x>w1*0.5)&((S/3)>aa)&(x<1100)&(y<(s4+type_c))&(y>(s4-type_c)):#&(r>g)&(r>b):
                                    S2=(t1[offse-1][0]+t1[offse-1][2]+t1[offse-1][1])/3 
                                    if (S2<aa):
                                        f=f+1
                                        x11=x
                                        x2res=x2res+x11
                                        x2resnum=x2resnum+1
                                        if (x11<x1min):
                                            x1min=x11
                                            x1res=x1res+x11              
                                            f2=f2+1
                                            
                       #     else:#redefnition of aa
                             #   if (x>w1*0.5)&((S/3)>(bb))&(x<1100)&(y<(s4+type_c))&(y>(s4-type_c)):#&(r>g)&(r>b):#your conditions for multicolor camera//to enable this mode change type_b from 1 to 0
                       #             S2=(t1[offse-1][0]+t1[offse-1][2]+t1[offse-1][1])/3 
                          #          if (S2<bb):
                                #        f=f+1
                       #                 x11=x
                            #            x2res=x2res+x11
                                   #     x2resnum=x2resnum+1
                        #                if (x11<x1min):
                                  #          x1min=x11
                                   #         x1res=x1res+x11              
                             #               f2=f2+1
                                            
                                            
                                            
              
                    if ((mm==48)&(ll==48)&(kk==48)&(jj==48)&(ii==48)):
                        x1ot=x1min    
                    
                    a=2*len(name1)+path_l+2
                    k=round(1.000*(n_init-n_per)/(x_per-x1ot),10)    
      
                    ff.write(str(text[a:a+5]))   
                    ff.write(";")
                    
                    if (f2==0)|(x2resnum==0):
                        print "Mistake in X&Y or conditions!*3"
                        ff.write("mistake")
                        break
                    
                    if ((mm==48)&(ll==48)&(kk==48)&(jj==48)&(ii==48)):
                        ff.write(str(round(n_init,6)))
                        ndif=round(k*(x2res/x2resnum-x1ot),6)
                        ff.write(";")
                        ff.write("\n")
                    else:
                        ff.write(str(round(-k*(x2res/x2resnum-x1ot)+n_init+ndif,6)))   
                        ff.write(";")
                        ff.write("\n")

                    

print ("n="+str(n_init)+"+("+str(k)+"*delta_pix"+")")#n-to-delta-pix dependency for your video
                    
ff.close()

