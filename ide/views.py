from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
import os
import subprocess
from subprocess import PIPE, STDOUT
@login_required(login_url='LogIn/')
def Index(r):
    if r.method=="POST":
        
        if r.POST.get("action")=="getfile":
            fn=r.POST.get("fn")
            e=r.session['e']
            fcontent=open(e+"/"+fn).read()
            print(fcontent)
            return JsonResponse({"fc":fcontent})
        if r.POST.get("action")=="savefile":
            fn=r.POST.get("fn")
            fc=r.POST.get("fc")
            e=r.session['e']
            fw=open(e+"/"+fn,"w")
            fw.write(fc)
            fw.close()
            print("overwrote")
            return HttpResponse("success")
        if r.POST.get("action")=="compile":
            fn=r.POST.get("fn")
            e=r.session['e']
            fcontent=open(e+"/"+fn).read()
            print(fcontent)
            #fw=open(e+"/"+"op.txt","a")
            
            
            resp1=os.system("javac "+e+"/"+fn+" > "+e+"/op.txt 2>&1")
            #proc = subprocess.Popen(['javac', e+"/"+fn],stdout=PIPE, stderr=STDOUT,bufsize=1, universal_newlines=True)
            #for line in iter(proc.stdout.readline,''):
            #    fw.write(line)
            #fw.close()
            #print(resp1)
            return JsonResponse({"compileresult":"done"})
        
        if r.POST.get("action")=="run":
            fn=r.POST.get("fn")
            fs=fn.split(".")
            print("after split")
            print(fs[0])
            e=r.session['e']
            #fw=open(e+"/"+"op.txt","a")            
            #proc = subprocess.Popen(['java', e+"/"+fs[0]],stdout=PIPE, stderr=STDOUT,bufsize=1, universal_newlines=True)
            #for line in iter(proc.stdout.readline,''):
             #   fw.write(line)
            #fw.close()
            #tst=os.system("cd "+e)
            #print(tst)
            stm="java -classpath "+e+" "+fs[0]+" > "+e+"/op.txt 2>&1"
            #stm="java "+fs[0]+" >> "+e+"/op.txt 2>&1"
            resp1=os.system(stm)
            print(stm)
            #os.system("cd ..")
            return JsonResponse({"runresult":"done"})
            
        
    e=r.session['e']
    fp="dir "+e+" /b"
    fp="ls ./"+e+"/ | grep '.java'"
    #ls ./t@t.c/ | grep ".java"
    print(fp)
    #t=str(os.system(fp))
    t=os.popen(fp).read()
    tt=t.split()
    print(tt)
    #p=t.split()
    #print(p)
    return render(r,'index.html',{'t':tt,'e':r.session['e']})

def SignUp(r):
    return render(r,'signup.html')
    #return HttpResponse("gcgudgcudgvh")
    
def SignUpSave(r):
    fn=r.POST.get("fn")
    sn=r.POST.get("sn")
    e=r.POST.get("e")
    pwd=r.POST.get("pwd")
    u=r.POST.get("e")
    #create_user(username, email=None, password=None, **extra_fields)
    t=User.objects.create_user(u,e,pwd)
    t.first_name=fn
    t.last_name=sn
    t.save()
    st="mkdir "
    st+=e
    os.system(st)
    os.system("touch /"+st+"/op.txt")
    return HttpResponseRedirect("/LogIn/")

def LogIn(r):
    if r.method=="POST":
        e=r.POST.get("e")
        pwd=r.POST.get("pwd")
        u=authenticate(username=e,password=pwd)
        if u is not None:
            auth_login(r,u)
            r.session['e']=e
            print("logged in")
            return JsonResponse({"l":"valid"})
        else:
            print("failed login")
            return JsonResponse({"l":"invalid"})
            
    return render(r,'login.html')

def console(r):
    e=r.session['e']
    return render(r,e+'/op.txt')

def logout(r):
    del r.session['e']
    auth_logout(r)
    return render(r,'login.html')
