from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersForm
from django.shortcuts import render
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
# for admin save
from contactenquiry.models import contactEnquiry
def homePage(request):
    # for news 
    newsData=News.objects.all()
    servicesData=Service.objects.all()#.order_by('-Service_title')  #[2:5] 
    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:servicesData=Service.objects.filter(Service_title__icontains=st)
            
    data={
       'servicesData':servicesData,
    #    for news 
       'newsData' :newsData
    }
    return render(request,"index.html",data)



# for save data in model
def saveEnquiry(request):
    n=''
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        website=request.POST.get('website')
        message=request.POST.get('message')
        
        savetoadmin=contactEnquiry(name=name,email=email,phone=phone,websitelink=website,message=message)
        savetoadmin.save()
        n="Data Inserted"
    
        return render(request,"index.html",{n:n})






# for news details
def newsDetails(request,slug):#newsid or slug
    newsDetails=News.objects.get(news_slug=slug)# or (news_slug=slug)
    data={
        'newsDetails':newsDetails
    }
    return render(request,"newsdetails.html",data)










# bcz i have only one html page no reqired for url for all
def about(request):
    return render(request,"index.html",)
def services(request):
    return render(request,"index.html",)
def portfolio(request):
    return render(request,"index.html",)
def contact(request):
    return render(request,"index.html",)


# from get method
# def userForm(request):
#     finalans=0
#     try:
#         if request.method=="GET":
#         # method1
#         # n1=int(request.GET['num1'])
#         # n2=int(request.GET['num2'])
#         # print(n1+n2)
#         # method 2
#             n1=int(request.GET.get('num1')) # type: ignore
#             n2=int(request.GET.get('num2')) # type: ignore
#             finalans=n1+n2
        
#     except:
#         pass
#     return render(request,"userform.html",{'output':finalans})
# get method closed

# POST method start
def userForm(request):
    finalans=0
    fn=usersForm()
    data={'form':fn}
    try:
        if request.method=="POST":
        # method1
        # n1=int(request.POST['num1'])
        # n2=int(request.POST['num2'])
        # print(n1+n2)
        # method 2
            n1=int(request.POST.get('num1')) # type: ignore
            n2=int(request.POST.get('num2')) # type: ignore
            finalans=n1+n2
            data={
                'form':fn,
                'output':finalans
            }
            # redirect from here
            url="formoutput/?output={}".format(finalans)
            # its first HttpResponseRedirect Method
            # return HttpResponseRedirect(url)  
            # its 2nd Redirect method
            return redirect(url)
    except:
        pass
    return render(request,"userform.html",data)

# POST method closed



# redirect page
def formOutput(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"formoutput.html",{'output':output})
# redirect page end

def aboutUs(request):
    return HttpResponse("Welcome to Pratik about-us Page")

def course(request):
    return HttpResponse("course page")

def courseDetails(request,courseid):
    return HttpResponse(courseid)



# for marksheet
def marksheet(request):
    data={}
    if request.method=="POST":
        S1=eval(request.POST.get('subject1'))
        S2=eval(request.POST.get('subject2'))
        S3=eval(request.POST.get('subject3'))
        S4=eval(request.POST.get('subject4'))
        S5=eval(request.POST.get('subject5'))
        t=S1+S2+S3+S4+S5
        p=t*100/500
        if p>=90 and p<=100:
            d="A Grade"
        elif p>=80 and p<90:
            d="B Grade"
        elif p>=70 and p<80:
            d="C Grade"
        elif p>=60 and p<70:
            d="D Grade"
        elif p<60 and p>=35:
            d="E Grade"
        elif p<35 and p>=0:
            d="Fail"
        else:
            d="Invalid Input"
        data={
            'total':t,
            'per':p,
            'div':d,
            's1':S1,
            's2':S2,
            's3':S3,
            's4':S4,
            's5':S5,
        }
        return render(request,"marksheet.html",data)
    return render(request,"marksheet.html")




# using action submit form
def submitform(request):
    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1')) # type: ignore
            n2=int(request.POST.get('num2')) # type: ignore
            finalans=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans
            }
            
            return HttpResponseRedirect(finalans)
    except:
        pass
    
    
    
    
    
#for evenodd form
# manual form validation
def saveevenodd(request):
    c=''
    n=''
    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render(request,"evenodd.html",{'error':True})
        n=eval(request.POST.get('num1'))
        if n%2==0:
          c="Even Number"
        else:
           c="Odd Number"
    data={
        'n1':n,
        'c':c
    }
    return render(request,"evenodd.html",data)



# for pagination
def homePage(request):
    serviceData=Service.objects.all()
    paginator=Paginator(serviceData,2)
    Page_number=request.GET.get('page')
    ServiceDataFinal=paginator.get_page(Page_number)
    totalpage=ServiceDataFinal.paginator.num_pages
        
    data={
        'serviceData':ServiceDataFinal,
        'lastpage':totalpage,
        'totalPagelist':[n+1 for n in range(totalpage)]
    }
    
            
    
    return render(request,"index.html",data)
