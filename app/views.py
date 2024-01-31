from django.shortcuts import render

# Create your views here.

from app.models import *
from django.db.models.functions import Length

def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
   # EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2023)
   # EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
   # EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=False)
   # EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
   # EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    
   # EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')

   # EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__gte=1600,sal__lt=5000) greaterthan,lessthan,and operator denotaed with camma
   # EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__gte=0,comm__lt=500)
   # EMPOBJECTS=Emp.objects.select_related('deptno').all()[2:5]
    
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)

def selfjoins(request):
    EMPMGROBJECTS=Emp.objects.select_related('mgr').all()
    #EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(sal__gte=2000)
    #EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    #EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__isnull=False)
    #EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__ename='BLAKE')
    #EMPMGROBJECTS=Emp.objects.select_related('mgr').all()[1:5]
    #EMPMGROBJECTS=Emp.objects.select_related('mgr').all().order_by(Length('ename'))   
    #EMPMGROBJECTS=Emp.objects.select_related('mgr').all().order_by(Length('ename').desc()) 
    #EMPMGROBJECTS=Emp.objects.select_related('mgr').all().order_by(Length('mgr').desc())                                                 
    


    d={'EMPMGROBJECTS':EMPMGROBJECTS}
    return render(request,'selfjoins.html',d)