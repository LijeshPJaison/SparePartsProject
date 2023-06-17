from django.shortcuts import render,redirect,HttpResponse
from .models import*


# Create your views here.
def IndexFunction(request):
    if 'signup' in request.session:
        current_user = request.session['signup']
        param = {'current_user': current_user}
        return render(request, 'index.html', param)
    else:
        return redirect('login')


def AddQuestionsFunction(request):
    obj = Questions.objects.all()
    if request.method == 'POST':
        questions = request.POST['questions']       
        question = Questions(questions = questions)
        question.save()
    return render(request, 'add_questions.html',{'questions':obj})

def InspectionFunction(request):
    obj = Questions.objects.all()
    if  request.method == 'POST':
        images = request.FILES['input_upload_image']
        registration_number = request.POST['input_registration_number']
        description = request.POST['textarea_description']
        selected_value = request.POST.get('dropdown_value')
        inspection_person = request.POST['input_inspection_person']
        car_brand = request.POST['input_car_brand']
        car_model = request.POST['input_car_model']
        year = request.POST['input_year']
        variant = request.POST['input_variant']
        meter_reading = request.POST['input_meter_reading']
        inspect = Inspection(images=images,registration_number=registration_number,description=description,values=selected_value,inspection_person=inspection_person,car_brand=car_brand,car_model=car_model,year=year,variant=variant,meter_reading=meter_reading)
        inspect.save()
        checked_questions = request.POST.getlist("checkbox")
        for check in checked_questions:
            quest = Questions.objects.get(questions = check)
            checked = Checkbox(questions_id = quest,inspection_id = inspect)
            checked.save()
    return render(request,'inspection.html',{'questions':obj})


def ListInspectionFunction(request):
    obj = Inspection.objects.all()
    return render(request,'list_inspection.html',{'inspect':obj})

def HomeFunction(request):
    return render(request,'home.html')

def SignupFunction(request):
    message=""
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        sign = signup(name=name,username=username,email=email,mobile_number=mobile_number,password=password,confirm_password=confirm_password)
        query = signup.objects.filter(username=username)
        if not query :
            sign.save()
            return redirect('login')
        else:
            message = 'username already exist'      
    return render(request,'signup.html',{'message':message})


def LoginFunction(request):
    message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        check_user = signup.objects.filter(username=username, password=password)
        if check_user:
            request.session['signup'] = username
            return redirect('index')
        else:
            message = "Please Enter Valid Username"
    return render(request, 'login.html',{'message':message})

def ServiceFunction(request):
    if request.method == 'POST':
        search = request.POST["search_id"]
        obj = Inspection.objects.filter(id = search)
        return render(request,'service.html',{'obj':obj})
    return render(request,'service.html')

def PurchaseListFunction(request):
    obj = Inspection.objects.all()
    objects = Purchase.objects.all()
    return render(request,'purchase_list.html',{'obj':obj,'objects':objects})

def PurchaseFunction(request):
    if request.method == 'GET':
        search = request.GET.get("search")
        obj = Inspection.objects.filter(id = search).first()
        return render(request,'purchase.html',{'obj':obj})
    if request.method == 'POST':
        obj_id =request.POST['obj']
        date = request.POST['date'] 
        amount = request.POST['amount']
        obj = Inspection.objects.get(id = obj_id)
        purchase = Purchase(inspection_id = obj,date=date,amount=amount)
        purchase.save()
        return render(request,'purchase.html',{'obj':obj})
    return render(request,'purchase.html')

 
def DeleteFunction(request,id):
    delete = Inspection.objects.get(id=id)
    delete.delete()
    return redirect('list_inspection')

def DeleteQuestionsFunction(request,id):
    delete_questions = Questions.objects.get(id=id)
    delete_questions.delete()
    return redirect('add_questions')

def LogoutFunction(request):
    try:
        del request.session['signup']
    except:
        return redirect('login')
    return redirect('login')