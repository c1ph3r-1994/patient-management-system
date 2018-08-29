from django.shortcuts import render,redirect
from django.http import HttpResponse
#from . import urls
import painfo.urls
from django.contrib.auth import update_session_auth_hash

# Create your views here.
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import user_passes_test
from painfo.forms import (
    RegistrationForm,
    EditProfileForm,
    painfof,
    docfile,
    sepainfo,
    ipn,
    editipno,
    edit_info,
    seipno,
    ipno_edit,
    dephoto,
    )
from django.contrib.auth.decorators import login_required
from .models import Painf,docs,ipnos
#from django.template import loader
from django.contrib import messages
#from django.views.generic.edit import FormView,CreateView
#from django.forms.models import modelformset_factory
#class FileFieldView(FormView):
#    form_class = painfof
#    template_name = 'painfo/paform.html'  # Replace with your template.
#    success_url = '/patient_info/new_form/' # Replace with your URL or reverse().
  #  print("dqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
#    def form_valid(self, form):
#        name = form.cleaned_data['name']
#        uhid = form.cleaned_data['uhid']
#        ipno = form.cleaned_data['ipno']
#        types = form.cleaned_data['types']
#        dep = form.cleaned_data['dep']
#        doc = form.cleaned_data['doc']
      #  files = [serialize(self.object)]
     #   data = {'files': files}
#        print(str(doc)+"==12333333333333333333333333333333333333333333333333333333333333333333333")
#        qw = Painf(name=name, ipno=ipno, uhid=uhid, types=types, dep=dep,doc=doc)
#        qw.save()
    #    self.object = form.save()

#        return super(FileFieldView, self).form_valid(form)




#class FileFieldView(CreateView):
#    model = Painf
#    fields = "__all__"
#    template_name = 'painfo/paform.html'
#    def form_valid(self, form):
#        self.object = form.save()
#        return HttpResponse("done")

#    def form_invalid(self, form):

#        return HttpResponse("error")

@login_required
def typesearch(request):
    if request.method == 'POST':

        typea = request.POST.get('typea', '')
        typeq = ipnos.objects.filter(types = typea)
        return render(request,'painfo/typeresult.html',{'dae':typeq})
    return render(request,'painfo/typesearch.html')




@login_required
def datesearch(request):
    if request.method == 'POST':

        date1 = request.POST.get('date1', '')
        date2 = request.POST.get('date2', '')
        # print("1234123=============================================================="+ date1)
        # print("1234123=============================================================="+ date2)
        dateq = Painf.objects.filter(date__range=[str(date1), (date2)])
        # print("1234123=============================================================="+ str(dateq))

        return render(request,'painfo/dateresult.html',{'dae':dateq})
    return render(request,'painfo/datesearch.html')

@login_required
def patient_photo(request):
    print (str(request)+"==========adskjahfkjbaksjbdjashbfhajsbdkbqjhbqjhqbjqhbqjhw")
    print (str(request)[47:-2]+"===========adskjahfkjbaksjbdjashbfhajsbdkbqjhbqjhqbjqhbqjhw")
    name=str(request)[47:-2]
    #daad = docs.objects.filter(post__uhid=name)
    daad = docs.objects.filter(ipno=name)
    ipn = ipnos.objects.get(ipno=name)
    print(str(ipn.uhid)+"=========================anskjdabsfkjbaskjbdkjqbdkjqw")
    na = Painf.objects.get(uhid=str(ipn.uhid))
    qw=[]
    for a in daad:
        print(str(a.doc)[6:] + "=================================================asbdhkjasfbkajsdbkjasbdkjasdbkjasbfkjasbebqwkjdbqwdbqw")
        qw.append(str(a.doc)[6:])
        #print(str(a)[7:]+"====asbdhkjasfbkajsdbkjasbdkjasdbkjasbfkjasbebqwkjdbqwdbqw")
    return render(request,'painfo/uhid_profile.html',{'da':qw,'ip':ipn,'name':na})




@login_required
def showp(request):
    allpa=Painf.objects.all()
#    template=loader.get_template('painfo/home.html')
    context={
        'painfo':allpa,
        'form': sepainfo(),
        'doc':docs.objects.all(),
        'pa':ipnos.objects.all(),
    }
#     return HttpResponse(template.render(context,request))
    if request.method == 'POST':
        form = sepainfo(request.POST)
      #  print("asasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda" )
        if form.is_valid():
        #    print("==========asasdqwda1244123sdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
            name = request.POST.get('Search', '')

         #   print("=asasasddqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
            try:
                print("124====ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
                uhida = Painf.objects.get(uhid=name)
                print("=23===ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
                da = docs.objects.filter(post__uhid=name)
                print("==235==ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
                ua = ipnos.objects.filter(post__uhid=name)
                print("98439sasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")

                return render(request, 'painfo/user_profile.html',{'data': uhida,'da':da,'ua': ua})
            except:
                messages.error(request, "Entered Uhid not found in datadase")




        else:
         #   print("popoposasasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
            messages.error(request, "Error")



    return render(request, 'painfo/showp.html',context)

@login_required
def user_information(request):
    print(str(request)[53:-2]+"============daskjdbaksbfkjasbdkjasbdkjasbdasd")
    print(str(request)+"=new===========daskjdbaksbfkjasbdkjasbdkjasbdasd")
    
    name=str(request)[53:-2]
    uhida = Painf.objects.get(uhid=name)
    print("=23===ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
    da = docs.objects.filter(post__uhid=name)
    print("==235==ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
    ua = ipnos.objects.filter(post__uhid=name)
    print("98439sasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")

    return render(request, 'painfo/user_profile.html', {'data': uhida, 'da': da, 'ua': ua})






@login_required
def home(request):
    return render(request,'painfo/home.html',{'no': '0' })

@login_required
def searchpa(request):
    allpa = Painf.objects.all()
    #    template=loader.get_template('painfo/home.html')
    context = {
        'painfo': allpa,
        'form': sepainfo(),
        'doc': docs.objects.all(),
        'pa': ipnos.objects.all(),
    }
    if request.method == 'POST':
        form = sepainfo(request.POST)
        if form.is_valid():
            #    print("==========asasdqwda1244123sdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
            name = request.POST.get('Search', '')

            #   print("=asasasddqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
            try:
                print("124====ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
                uhida = Painf.objects.get(uhid=name)
                print("=23===ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
                da = docs.objects.filter(post__uhid=name)
                print("==235==ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
                ua = ipnos.objects.filter(post__uhid=name)
                print("ua==98439sasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
                return render(request, 'painfo/user_profile.html', {'data': uhida, 'da': da, 'ua': ua})
            except:
                messages.error(request, "Entered Uhid not found in datadase")

        else:
            messages.error(request, "Error")
    return render(request, 'painfo/paform.html',context)


@login_required
def add_ipno(request):
    print(str(request)+"====dhsakjhdkjashfkasjhdkasjdhkasjhdkjashfkjasbdkjasd")
    print(str(request)[42:-2] + "====dhsakjhdkjashfkasjhdkasjdhkasjhdkjashfkjasbdkjasd")
    name = str(request)[42:-2]
    if request.method == 'POST':

        name=str(request)[43:-2]
        formx = editipno(request.POST,request.FILES)
        form2 = docfile(request.POST, request.FILES)

        print("START====dhsakjhdkjashfkasjhdkasjdhkasjhdkjashfkjasbdkjasd")
        if formx.is_valid() and form2.is_valid():

             #   print("try==98439sasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
               # print(str(name)+"=============my mane")
            last = Painf.objects.get(uhid=str(name))
            ipno = request.POST.get('ipno', '')
            try:
                print("last=1==98439sasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
                ua = ipnos.objects.filter(ipno=ipno,post__uhid=name)
                print(str(ua.ipno)+"===dsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafasd")
                messages.error(request, "IP/NO already Exist")
            except:
                print("last===98439sasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
                date = request.POST.get('date', '')
                print("date==98439sasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")

                print("ipno===98439sasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
                w = ipnos(ipno=ipno, uhid=name, date=date, post=last)
                print("w===98439sasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
                w.save()
                print("w.save===98439sasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
                docx = request.FILES.getlist('doc')
                print("docx===98439sasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
                for a_file in docx:
                    qw = docs(doc=a_file, uhid=name, ipno=ipno, date=date, post=last)
                    qw.save()
            messages.success(request, 'Patient details updated.')
            print("for__end==98439sasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")


        else:
            messages.error(request, "Error")
    return render(request,'painfo/fromx.html',{'formx': editipno(),'docs':docfile(),'name':name})




@login_required
def paform(request):
  #  ImageFormSet = modelformset_factory(docs,
   #                                     form=docfile, extra=3)

 #   print("asasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda"+str(qw))
    if request.method == 'POST':
        form = painfof(request.POST,request.FILES)
        form2 = docfile(request.POST,request.FILES)

   #                            queryset=docs.objects.none())
        if form.is_valid() and form2.is_valid():

            add_uhid = request.POST.get('uhid', '')
            try:
                last=Painf.objects.get(uhid = str(add_uhid))
                print(last)
                messages.error(request, "Entered UHID no is already exist")
            except:
                types=request.POST.get('types','')
                name = request.POST.get('name', '')
                ipno = request.POST.get('ipno', '')
                dep=request.POST.get('dep','')
                date = request.POST.get('date', '')
                fils = request.FILES.getlist('doc')
  #              for a_file in fils:
 #                   qw = Painf(name=name, ipno=ipno, uhid=add_uhid, types=types, dep=dep,doc=a_file)
                q = Painf(name=name,uhid=add_uhid,date=date)
                q.save()
                w = ipnos(ipno=ipno,types=types,dep=dep,uhid=add_uhid,date=date,post=q)
                w.save()
                for a_file in fils:

                    qw=docs(doc=a_file,uhid=add_uhid,ipno=ipno,date=date,post=q)
                    qw.save()


               # print(str(formset.cleaned_data)+"====asasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
          #      for forw in formset.cleaned_data:
         #           image = forw['doc']
          #          photo = docs(post=qw, image=image)
         #           photo.save()
               # doc=Painf(doc=request.FILES['doc'])
              #  print(str(doc.doc)+"===andlknqkjndkjasndkjasndakjsndkjasdnkjasndkjasndkjasdasd")
              #  doc.save()



                messages.success(request, 'Patient details updated.')
        else:
            messages.error(request, "Please Fill all The Fields")

    return render(request, 'painfo/paform.html', {'form': painfof(),'form2': docfile(),'form3': ipn()})
     #       return render(request, 'painfo/home.html', {'no':'1','last':"You have Added last UHID no in character Plss delete last UHID"})

@login_required
def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/patient_info/home')
        else :
            return render(request, 'painfo/reg_form.html',
                          {'form': form})

    else :
        form=RegistrationForm()
        args={'form':form}
        return render(request,'painfo/reg_form.html',args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form= EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/patient_info/profile')
    else:
        form=EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request,'painfo/edit_profile.html',args)
@login_required
def view_profile(request):
    args={'user':request.user}
    return render(request,'painfo/profile.html',args)
@login_required
def change_password(request):
    if request.method == 'POST':
        form= PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/patient_info/profile')
        else:
            return redirect('/account/change-password')
    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'painfo/change_password.html',args)

@login_required
def patient_photo_edit(request):

    print(str(request)[43:-2] + "====dhsakjhdkjashfkasjhdkasjdhkasjhdkjashfkjasbdkjasd")
    namex = str(request)[43:-2]
    print(namex+"================aslkdqnlkdnqw")

    if request.method == 'POST':
        form = ipno_edit(request.POST, request.FILES)
        print("form not valid =================akdnalksndlasknfkfnalskdasd")
        if form.is_valid():
            print("form valid =================akdnalksndlasknfkfnalskdasd")
            namex = str(request)[44:-2]
            print(namex + "=====111===========aslkdqnlkdnqw")
            last = ipnos.objects.get(ipno=str(namex))
            types=request.POST.get('types','')
            date=request.POST.get('date','')
            dep = request.POST.get('dep', '')
           # uhid=request.POST.get('uhid','')
            #types=request.POST.get('types','')

          #  dep=request.POST.get('dep','')
           # doc=request.POST.get('doc','')

          #  doc = Painf(doc=request.FILES['doc'])
          #  doc.save()
           # qw=last(name=name,date=date,types=types,dep=dep)
            last.types=types
            last.dep=dep
            last.date = date
            #last.types=types
            #last.dep=dep
            last.save()
          #  qw.save()
            messages.success(request, 'Patient details updated.')
        else:
            messages.error(request, "Please Fill all the Fields")


    return render(request, 'painfo/ipno_edit.html',{'form':ipno_edit(),'name':namex})

 #   return render(request, 'painfo/home.html')


@login_required
def patient_photo_add(request):
    print(str(request)[42:-2] + "====dhsakjhdkjashfkasjhdkasjdhkasjhdkjashfkjasbdkjasd")
    namex = str(request)[42:-2]
    print(namex + "================aslkdqnlkdnqw")
    if request.method == 'POST':
        form = docfile(request.POST, request.FILES)
        print("form not valid =================akdnalksndlasknfkfnalskdasd")
        if form.is_valid():
            print("form valid =================akdnalksndlasknfkfnalskdasd")
            namex = str(request)[43:-2]
            print(namex + "=====111===========aslkdqnlkdnqw")


            last = ipnos.objects.get(ipno=str(namex))
            q=Painf.objects.get(uhid=str(last.uhid))

            fils = request.FILES.getlist('doc')
            for a_file in fils:
                qw = docs(doc=a_file, uhid=last.uhid, ipno=last.ipno, date=last.date,post=q)
                qw.save()
            messages.success(request, 'Patient details updated.')
        else:
            messages.error(request, "Please Fill all the Fields")
    return render(request, 'painfo/ipno_add.html',{'form':docfile(),'name':namex})


@login_required
def edit_details(request):
    print(str(request)[50:-2] + "====dhsakjhdkjashfkasjhdkasjdhkasjhdkjashfkjasbdkjasd")
    namex = str(request)[50:-2]
    if request.method == 'POST':
        form = edit_info(request.POST, request.FILES)
        if form.is_valid():
            namex = str(request)[51:-2]
            last = Painf.objects.get(uhid=str(namex))
            name=request.POST.get('name','')
            date=request.POST.get('date','')

           # uhid=request.POST.get('uhid','')
            #types=request.POST.get('types','')

          #  dep=request.POST.get('dep','')
           # doc=request.POST.get('doc','')

          #  doc = Painf(doc=request.FILES['doc'])
          #  doc.save()
           # qw=last(name=name,date=date,types=types,dep=dep)
            last.name=name
            last.date=date
            #last.types=types
            #last.dep=dep
            last.save()
          #  qw.save()
            messages.success(request, 'Patient details updated.')
        else:
            messages.error(request, "Please Fill all the Fields")


    return render(request, 'painfo/edit_details.html', {'form': edit_info(),'name':namex})
@user_passes_test(lambda u: u.is_superuser)
def deletepa(request):
    if request.method == 'POST':
        form = sepainfo(request.POST)
        if form.is_valid():
            name = request.POST.get('Search', '')

            try:
                uhida = Painf.objects.get(uhid=name)
                uhida.delete()
                messages.success(request, "Entered UHID Sucessfully Deleted")
            except:
                messages.error(request, "Entered Uhid not found in datadase")

        else:
            messages.error(request, "Error")
    return render(request, 'painfo/deletepa.html', {'form': sepainfo()})
@user_passes_test(lambda u: u.is_superuser)
def delete_pa(request):
    qw = str(request)[65:-2]
    ua = ipnos.objects.filter(post__uhid=qw)
    print(str(request)[65:-2] + "=======assssssssssssssssssssss")

    if request.method == 'POST':
        form = seipno(request.POST)
        if form.is_valid():
            try:
                name = request.POST.get('Enter_Ipno_to_Delete', '')
                qw = str(request)[66:-2]
                ua = ipnos.objects.filter(ipno=name,post__uhid=qw)
                ua.delete()
                #messages.success(request, "Entered UHID Sucessfully Deleted")
                return render(request, 'painfo/delete_ipno.html', {'id': ua, 'name': qw, 'form': seipno()})
            except:
                messages.error(request, "Entered Uhid not found in datadase")
    return render(request, 'painfo/delete_ipno.html',{'id':ua,'name':qw,'form':seipno()})

@user_passes_test(lambda u: u.is_superuser)
def patient_photo_delete(request):
    print(str(request)[45:-2]+"==========asdddddddddasgfqeeqweqw")
    x=0
    if x==0:
        name=str(request)[45:-2]
    else:
        name = str(request)[46:-2]

    ua = docs.objects.filter(ipno=name)
    if request.method == 'POST':
        form = dephoto(request.POST)
        if form.is_valid():
            try:
                name = request.POST.get('Enter_Document_Name_to_Delete', '')
                qw = str(request)[46:-2]
                print(qw + "====123======asdddddddddasgfqeeqweqw")
                #last = ipnos.objects.get(ipno=str(qw))
                ua = docs.objects.get(ipno=qw,doc=name)
                print(qw + "====1234======asdddddddddasgfqeeqweqw")
                ua.delete()
                print(qw + "====1235======asdddddddddasgfqeeqweqw")
                ua=docs.objects.filter(ipno=qw)
                return render(request, 'painfo/ipno_delete.html', {'form': dephoto(), 'doc': ua, 'name': qw})
              #  messages.success(request, "Entered Document Sucessfully Deleted")

            except:
                messages.error(request, "Entered Uhid not found in datadase")


    return render(request, 'painfo/ipno_delete.html',{'form':dephoto(),'doc':ua,'name':name})

@login_required
def patient_ipno(request):

    allpa = ipnos.objects.all()

    #    template=loader.get_template('painfo/home.html')
    context = {
        'painfo': allpa,

        'form': sepainfo(),
        'doc': docs.objects.all(),
        'pa': ipnos.objects.all(),
    }
    #     return HttpResponse(template.render(context,request))
    if request.method == 'POST':
        form = sepainfo(request.POST)
        #  print("asasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda" )
        if form.is_valid():
            #    print("==========asasdqwda1244123sdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
            name = request.POST.get('Search', '')

            #   print("=asasasddqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
            try:
                daad = docs.objects.filter(ipno=name)
                ipn = ipnos.objects.get(ipno=name)
                print(str(ipn.uhid) + "=========================anskjdabsfkjbaskjbdkjqbdkjqw")
                na = Painf.objects.get(uhid=str(ipn.uhid))
                qw = []
                for a in daad:
                    print(str(a.doc)[
                          7:] + "=================================================asbdhkjasfbkajsdbkjasbdkjasdbkjasbfkjasbebqwkjdbqwdbqw")
                    qw.append(str(a.doc)[6:])
                    # print(str(a)[7:]+"====asbdhkjasfbkajsdbkjasbdkjasdbkjasbfkjasbebqwkjdbqwdbqw")
                return render(request, 'painfo/uhid_profile.html', {'da': qw, 'ip': ipn, 'name': na})
            except:
                messages.error(request, "Entered Uhid not found in datadase")




        else:
            #   print("popoposasasdqwdasdqddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda")
            messages.error(request, "Error")

    return render(request, 'painfo/showp_ipno.html', context)