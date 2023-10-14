from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   return render(request,'index.html')

def signUp(request):
   return render(request,'signUp.html')


def fun2(request):
    return render(request,'2.html')

#def removepunc(request):
 #  myText=request.GET.get('text','default')
  # return HttpResponse('remove puchuation from given text')

def analyze(request):

   mytext=request.GET.get('text','off')
   mycheckbox=request.GET.get('mycheckbox','off')
   upbox=request.GET.get('upbox','off')
   lowbox=request.GET.get('lowbox','off')
   charbox=request.GET.get('charbox','off')

   punchuation='''!@$%^&*()_+<>:"?'''
   analyzed=""
   print(mycheckbox)
   print(mytext)
   if mycheckbox == "on":
      for char in mytext:
         if char not in punchuation:
            analyzed = analyzed+char

      params ={'purpose':"remove puncutation",'analyzed_text':analyzed}
      return render(request, 'analyzePage.html', params)
   elif upbox=="on":
      # for char in mytext:
        analyzed=mytext.upper()
        params={'purpose':"Converted To Uppercase",'analyzed_text':analyzed}
        return render(request,'analyzePage.html',params)

   elif lowbox=="on":
      # for char in mytext:
         analyzed=mytext.lower()
         params={'purpose':"Captalized Text",'analyzed_text':analyzed}
         return render(request,'analyzePage.html',params)
      
   elif charbox=="on":
      for char in mytext:
         analyzed=analyzed+char
         totalcount=len(analyzed)

      
      params={'purpose':"total number of characters",'analyzed_text':totalcount}
      return render(request,'analyzePage.html',params)
   else:
      return HttpResponse("Error no check box selected")
      
      

   
      


   

# def lwecase(request):
#    mytext=request.GET.get('text','default')
#    mycheckbox2=request.GET.get('mycheckbox2','off')
#    str=""
    
#    print(mycheckbox2)
#    if mycheckbox2=="on":
#       str=mytext.lower()
#       var={'lowerCase':str}
#       print(mytext)
#       return render(request,'lowerCase.html',var)
#    else:
#        return HttpResponse('check box not selected')
   
      
            

        
        


def uprcase(request):
   return HttpResponse('upcase <a href="/">back to home</a><br>')
def charcount(request):
   return HttpResponse('charcount <a href="/">back to home</a><br>')





