from django.shortcuts import render

# Create your views here.

from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

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

def emp_mgr_dept(request):
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').all()
    #emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
    #emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    #emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    #emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
    #emp_mgr_dept=Emp.objects.select_related('deptno','mgr').order_by(Length('ename'))
    #emp_mgr_dept=Emp.objects.select_related('deptno','mgr').order_by(Length('ename').desc())
    #emp_mgr_dept=Emp.objects.select_related('deptno','mgr').order_by(Length('mgr'))
    #emp_mgr_dept=Emp.objects.select_related('deptno','mgr').order_by(Length('mgr').desc())
    #emp_mgr_dept=Emp.objects.select_related('deptno','mgr').all()[2:4]
    #emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(ename__endswith='E')
    #emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(ename__startswith='A')
    #emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(Q(ename='ALLEN') | Q(sal__gte=0))
    #emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(Q(ename='BLAKE') | Q(comm=0))
    #emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(Q(mgr__ename='BLAKE') | Q(sal__lte=0))
    #emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='RESEARCH') | Q(deptno=20))
    #emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(Q(ename='ALLEN') | Q(hiredate__year__gte=2000))
    d={'emp_mgr_dept':emp_mgr_dept}
    return render(request,'emp_mgr_dept.html',d)

def emp_salgrade(request):
    # EO=Emp.objects.all()
    # SO=SalGrade.objects.all()
    
    # SO=SalGrade.objects.filter(grade=3)# [grade3 sal grade objects]
    #  Retrieving the data of employess who belongs to grade 4
    # EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal))
    #   Retrieving the data of employess who belongs to grade 3,4

    SO=SalGrade.objects.filter(grade__in=(3,4))

    EO=Emp.objects.none()
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal))

    
    d={'EO':EO,'SO':SO} 
    return render(request,'emp_salgrade.html',d)



