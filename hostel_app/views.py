from django.shortcuts import render , HttpResponse , HttpResponseRedirect
from .models import Admin_pass , Student_data ,Student_pass , Guard_data ,Guard_pass, Admin_data,Gatepass
import json
from django.core.mail import send_mail
from datetime import datetime , date
import random
import array
from django.contrib import messages
import qrcode
import cv2
import os
# Create your views here.

def password_gen():
    MAX_LEN = 8
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']
    
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']
    
    SYMBOLS = ['@', '#', '$', '%', '=',  '?','*']
    
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
    
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
    
    password = ""
    for x in temp_pass_list:
            password = password + x
            
    return password

def check_pass(username,password,data_file):
    chaeck = False
    for i in data_file:
        if i.username == username and i.password ==password:
                chaeck = True
                break
    return chaeck
        

def username_genretar(student_name,data_file):
            username = ""
            for i in student_name.lower():
                if i != " ":
                    username += i
            username_data = data_file
            uname_check = True
            count = 0
            temp = username
            while True:
                for uname in username_data:
                    if username in str(uname):
                        uname_check = False
                        break
                if uname_check:
                    username += "@lcithostel"
                    break
                else:
                    count+=1
                    if count ==1:
                        username += str(count)
                    else:
                        username = username[0:len(username)-1] + str(count)
                    uname_check = True
            return username
    
def email_send(email,name,username,password,txt):
    send_mail(
            txt,
            f'Dear {name}, Your Username in \'{username}\' and password is \'{password}\' .',
            'gouravpatel16111.com',
            [email,'gouravpatel16111@gmail.com'],
            fail_silently=False,
                )


def update_password(n_password,data_file):
    data_file.password = n_password
    data_file.save()
    

def encode(data):
    str_data = ""
    for k in str(data):
        if k!= ' ':
            str_data += k
    value_data = ''
    for k in str_data:
        if len(str(ord(k))) == 2:
            num = f'0{ord(k)}'
        else:
            num = str(ord(k))
        value_data += num
    h = hex(int(value_data))


    return h
        
def make_qr(id,data):
    img = qrcode.make(data)
    name = "hostel_app\static\qr_code\\"+str(id)+".png"
    img.save(name)




def index(request):
    return render(request, 'index.html')


def student_login(request):
    return render(request, 'student_login.html')


def guard_login(request):
    return render(request, 'guard_login.html')

def admin_login(request):
    
    login_fail = {'login':False}
    return render(request, 'admin_login.html',login_fail)
    

def check_admin_pass(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
        chaeck= check_pass(username, password, Admin_pass.objects.all())
        if chaeck:
            admin_data = {'admin': username}
            return render(request, "admin.html",admin_data)
        else:
            login_fail = {'login':True}
            return render(request,"admin_login.html",login_fail)
    
    else:
        login_fail = {'login':False}
        return render(request, 'admin_login.html',login_fail)
 

def check_student_pass(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
        chaeck= check_pass(username, password, Student_pass.objects.all())
        if chaeck:
            return render(request, "student.html",{'user':username})
        else:
            
            login_fail = {'login':True}
            return render(request,"student_login.html",login_fail)
    
    else:
        login_fail = {'login':False}
        return render(request, 'student_login.html',login_fail)
  
 
def check_guard_pass(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
        chaeck= check_pass(username, password, Guard_pass.objects.all())
        if chaeck:
            return render(request, "guard.html",{'guard_username':username})
            
        else:
            login_fail = {'login':True}
            return render(request,"guard_login.html",login_fail)
    
    else:
        login_fail = {'login':False}
        return render(request, 'guard_login.html',login_fail)
     
    
def newstudent(request):
    if request.method == 'POST':
        admin_name = request.POST['admin_name']
        all_data = Student_data.objects.all()
        chk_no = 0
        for i in all_data:
            chk_no += 1
        params = {'admin':admin_name,'chk_data':chk_no}
        return render(request, "newstudent.html",params)
    else:
        return render(request, "index.html")

def addstudent(request):
    if request.method == 'POST':
        admin_name = request.POST['admin_name']
        post_chk_no = request.POST['chk_no']
        all_data = Student_data.objects.all()
        chk_no = 0
        for i in all_data:
            chk_no += 1
        if str(post_chk_no)  != str(chk_no):
            admin_data = {'admin': admin_name}
            return render(request, "admin.html",admin_data)
        student_name = request.POST['studentName']
        student_number = request.POST['phone']
        student_email = request.POST['email']
        father_name = request.POST['fatherName']
        parents_phone = request.POST['parents_phone']
        address = request.POST['address']
        course = request.POST['course']
        room_no = request.POST['room_no']
        data_fill = True
        data = [student_name,student_number,student_email,father_name,parents_phone,address,course]

        for i in data:
            if i =="":
                data_fill = False
                break
            
            
        if data_fill:
            username = username_genretar(student_name,Student_pass.objects.all())
            std_password = password_gen()
            std_data = Student_data(student_name= student_name,
                                    username=username,
                                    student_number= student_number, 
                                    student_email=student_email,
                                    father_name=father_name,
                                    parents_number=parents_phone,
                                    address=address,
                                    course=course,
                                    room_no=room_no,
                                    join_date= datetime.now(),
                                    join_by= admin_name,
                                    )
            std_data.save()
            std_pass = Student_pass(username=username,
                                    password=std_password)
            std_pass.save()
            try:
                email_send(student_email, student_name, username, std_password,'Lcit Hostel Ragistation Sucsessfull')
            except:
                pass
            
            std = Student_pass.objects.all()
            id_no = 1
            for i in std:
                id_no+=1
            params = {'id':id_no,
                      'name': student_name,
                      'number': student_number,
                      'email': student_email,
                      'date': date.isoformat(date.today()),
                      'admin': admin_name,
                      'username': username,
                      'password': std_password,
                    
                    }
            return render(request, "rgs.html",params)
        else:
            messages.warning(request, 'Fill all datials proparly')
            return render(request, "newstudent.html")
                
    else:
        return HttpResponse("Add Student")
    
    
def newguard(request):
    if request.method == 'POST':
        admin_name = request.POST['admin_name']
        all_data = Guard_data.objects.all()
        chk_no = 0
        for i in all_data:
            chk_no += 1
        params = {'admin':admin_name,'chk_no':chk_no}
        return render(request, "newguard.html",params)
    else:
        return render(request, "index.html")


def addguard(request):
    if request.method == 'POST':
        admin_name = request.POST['admin_name']
        post_chk_no = request.POST['chk_no']
        all_data = Guard_data.objects.all()
        chk_no = 0
        for i in all_data:
            chk_no += 1
        print( str(post_chk_no)  , str(chk_no))  
        if str(post_chk_no)  != str(chk_no):
            admin_data = {'admin': admin_name}
            return render(request, "admin.html",admin_data)
      
        guard_name = request.POST['guardname']
        guard_number = request.POST['phone']
        guard_email = request.POST['email']
        address = request.POST['address']

        data_fill = True
        data = [guard_name,guard_number,guard_email,address]
        print(data)
        for i in data:
            if i =="":
                data_fill = False
                break
            
        if data_fill:
            username = username_genretar(guard_name, Guard_pass.objects.all())
            guard_password = password_gen()
            guard_data = Guard_data(guard_name= guard_name,
                                    username=username,
                                    guard_number= guard_number,
                                    guard_email= guard_email,
                                    address=address,
                                    join_date= datetime.now(),
                                    join_by= admin_name,
                                    )
            guard_data.save()
            guard_pass = Guard_pass(username=username,
                                    password=guard_password)
            guard_pass.save()
            try:
                email_send(guard_email, guard_name, username ,guard_password,'Lcit Hostel Ragistation Sucsessfull')
            except:
                pass

            guard = Guard_data.objects.all()
            id_no = 1
            for i in guard:
                id_no+=1
            params = {'id':id_no,
                      'name': guard_name,
                      'number': guard_number,
                      'email': guard_email,
                      'date': date.isoformat(date.today()),
                      'admin': admin_name,
                      'username': username,
                      'password': guard_password,
                    
                    }
            return render(request, "rgs_guard.html",params)
        else:
            messages.warning(request, 'Fill all datials proparly')
            return render(request, "newguard.html")
                
    else:
        return render(request, "admin_login.html")
    
    
    
def newadmin(request):
    if request.method == 'POST':
        admin_name = request.POST['admin_name']
        all_data = Admin_data.objects.all()
        chk_no = 0
        for i in all_data:
            chk_no += 1
        params = {'admin':admin_name,'chk_no':chk_no}
        return render(request, "newadmin.html",params)
    else:
        return render(request, "admin_login.html")



def addadmin(request):
    if request.method == 'POST':
        admin_name = request.POST['admin_name']
        post_chk_no = request.POST['chk_no']
        all_data = Admin_data.objects.all()
        chk_no = 0
        for i in all_data:
            chk_no += 1
        print("------------------", str(post_chk_no)  , str(chk_no))  
        if str(post_chk_no)  != str(chk_no):
            admin_data = {'admin': admin_name}
            return render(request, "admin.html",admin_data)
      
        name = request.POST['adminname']
        admin_number = request.POST['phone']
        admin_email = request.POST['email']
        admin_post = request.POST['post']

        data_fill = True
        data = [name,admin_number,admin_email,admin_post]
        for i in data:
            if i =="":
                data_fill = False
                break
            
        if data_fill:
            username = username_genretar(name, Admin_pass.objects.all())
            admin_password = password_gen()
            admin_data = Admin_data(admin_name= name,
                                    username=username,
                                    admin_number= admin_number,
                                    admin_email= admin_email,
                                    post=admin_post,
                                    join_date= datetime.now(),
                                    join_by= admin_name,
                                    )
            admin_data.save()
            admin_pass = Admin_pass(username=username,
                                    password=admin_password)
            admin_pass.save()
            try:
                email_send(admin_email, name, username ,admin_password,'Lcit Hostel Ragistation Sucsessfull')
            except:
                pass

            admin = Admin_data.objects.all()
            id_no = 1
            for i in admin:
                id_no+=1
            params = {'id':id_no,
                      'name': name,
                      'number': admin_number,
                      'email': admin_email,
                      'date': date.isoformat(date.today()),
                      'admin': admin_name,
                      'username': username,
                      'password': admin_password,
                    
                    }
            return render(request, "rgs_admin.html",params)
            return HttpResponse( data_fill)
        else:
            messages.warning(request, 'Fill all datials proparly')
            return render(request, "newadmin.html")
                
    else:
        return render(request, "admin_login.html")
    
    
    
def admin_profile(request):
    if request.method == 'POST':
        admin_username = request.POST['admin_name']
        data =  Admin_data.objects.get(username=admin_username)
        return render(request, "admin_profile.html",{'data':data})
    else:
        return render(request, "admin_profile.html")
   
def student_profile(request):
    if request.method == 'POST':
        student_username = request.POST['student_username']
        data = Student_data.objects.get(username=student_username)
        return render(request, "student_profile.html",{'data':data})
    else:
        return render(request, "student_profile.html")
    
def guard_profile(request):
    if request.method == 'POST':
        guard_username = request.POST['guard_username']
        data = Guard_data.objects.get(username=guard_username)
        return render(request, "guard_profile.html",{'data':data})
    else:
        return render(request, "gurad_login.html")
    
   
    
def change_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        post = request.POST['post']
        
        data = {'username':username,'post':post}
        return render(request, "change_password.html",{'data':data})
    else:
        return render(request, "index.html")
    
def changed(request):
    if request.method == 'POST':
        username = request.POST['username']
        post = request.POST['post']
        c_password = request.POST['c_password']
        n_password = request.POST['n_password']
        v_password = request.POST['v_password']
        
        
        
        if n_password != v_password:
            messages.success(request, 'New password and verify password are not match')        
            data = {'username':username,'post':post}
            return render(request, "change_password.html",{'data':data})
        else:
            if post == "admin":
                data_file = Admin_pass.objects
                full_data_file = Admin_data.objects
            elif post == "student":
                data_file = Student_pass.objects
                full_data_file = Student_data.objects
            elif post == "guard":
                data_file = Guard_pass.objects
                full_data_file = Guard_data.objects
           
                
            check = check_pass(username, c_password, data_file.all())
            if check:
                update_password( n_password, data_file.get(username=username))
                
                
                messages.success(request, 'Password Changed Sucsessfully !')        
                data =  full_data_file.get(username=username)
                print(username,data,post)
                return render(request, f'{post}_profile.html',{'data':data})
            else:
                messages.success(request, 'Current Password is wrong!')        
                data = {'username':username,'post':post}
                return render(request, "change_password.html",{'data':data})
 
                
    else:
        return render(request, "index.html")
    
    
    
    

def uname_gatepass(request):
    if request.method == 'POST':
        admin_name = request.POST['admin_name']
        params = {'admin':admin_name}
        return render(request, "uname_gatepass.html",params)
    else:
        return render(request, "admin_login.html")
    

def gatepass(request):
    print(request.method,"--------------")
    if request.method == 'POST':
        admin_name = request.POST['admin_name']
        username = request.POST['username']
        try:
            data = Student_data.objects.get(username=username)
            all_data = Gatepass.objects.all()
            chk_no = 0
            for i in all_data:
                chk_no += 1
            params = {'admin':admin_name,'data':data , 'date': datetime.now().strftime("%d-%m-%Y , %I:%M-%p"),'chk_no':chk_no}
            return render(request, "gatepass.html",params)
        except:
            messages.success(request, 'Username Not Found.')
            params = {'admin':admin_name}
            return render(request, "uname_gatepass.html",params)
            
    else:
        return render(request, "admin_login.html")
    
def gatepass_issue(request):
    if request.method == 'POST':
        post_chk_no = request.POST['chk_no']
        issue_by = request.POST['admin_name']
        all_data = Gatepass.objects.all()
        chk_no = 0
        for i in all_data:
            chk_no += 1
        if str(post_chk_no)  != str(chk_no):
            admin_data = {'admin': issue_by}
            return render(request, "admin.html",admin_data)
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        course = request.POST['course']
        input_date = request.POST['input_date']
        region = request.POST['region']
        issue_date = datetime.now()
        
        gatepass_data = Gatepass(
            issue_by= issue_by,
            username= username,
            name= name,
            email=email,
            phone=phone,
            course=course,
            input_date=input_date,
            region= region,
            issue_date=issue_date,
            # out_time= datetime.now().strftime("%I:%M-%p"),
        )
        gatepass_data.save()
        
        std_data = Student_data.objects.get(username=username)
        std_data.status = "OUT"
        std_data.gate_pass_no = str(gatepass_data.id)
        std_data.save()

        qr_data = {
            'id': gatepass_data.id,
            'username': gatepass_data.username,
            'name': gatepass_data.name,
            'email': gatepass_data.email,
            'phone': gatepass_data.phone,
            'course': gatepass_data.course,
            'input_date': gatepass_data.input_date,
            'region': gatepass_data.region,
            }
        hex_code = encode(qr_data)
        gatepass_data.hex_code = hex_code
        make_qr(gatepass_data.id,hex_code)
        img = str(gatepass_data.id)
        gatepass_data.save()
        return render(request, "pass.html", {'data':qr_data,'img':img})
    else:
        return render(request, "index.html")
    
    
    
    
def gatepass_view(request):
    if request.method == 'POST':
        username = request.POST['student_username']
        try:
            std_data = Student_data.objects.get(username=username)
            if std_data.status == "OUT":
                pass_no = std_data.gate_pass_no
                data = Gatepass.objects.get(id=int(pass_no))
                if data.status == "OUT":
                    title = "Out OF Hostel"
                else:
                    title = "Gatepass View"
                return render(request, "pass_view.html", {'data':data,'img':data.id,'title':title})
            else:
                content = {'title':"Gatepass View",'text':"Currently Gatepass Not Availavle",'img':"no_pass.png"}
                return render(request, "error.html" ,{'data':content})
        except:
            content = {'title':"Gatepass View",'text':"Currently Gatepass Not Availavle",'img':"no_pass.png"}
            return render(request, "error.html" ,{'data':content})
    else:
        return render(request, "index.html")
    
    
def forget_pass(request):
    if request.method == 'POST':
        data = request.POST['data']
        return render(request, 'forget.html',{'data':data})
    else:
        return render(request, "index.html")
   
    
def forgeted(request):
    if request.method == 'POST':
        data = request.POST['data']
        username = request.POST['username']

        try:
            if data == 'admin':
                lg = "admin_login"
                database = Admin_pass.objects.get(username=username)
                full_data = Admin_data.objects.get(username=username)
                email = full_data.admin_email
                name = full_data.admin_name
            elif data == 'student':
                lg = "student_login"
                database = Student_pass.objects.get(username=username)
                full_data = Student_data.objects.get(username=username)
                email = full_data.student_email
                name = full_data.student_name
                
            elif data == 'guard':
                lg = "guard_login"
                database = Guard_pass.objects.get(username=username)
                full_data = Guard_data.objects.get(username=username)
                email = full_data.guard_email
                name = full_data.guard_name

            email_send(email, name, database.username, database.password, "LCIT Hostel forget paassword sucsessfully !!")
            return render(request, "forgeted.html",{'login':lg})
        except:
            messages.warning(request, 'Username !! not found')
            return render(request, "forget.html")
                    
    else:
        return render(request, "index.html")
   
    
    
def scan_for_outing(request):
    if request.method == 'POST':
        username = request.POST['guard_username']
        data = {'username': username, 'status':'OUT','title':'Scan For Outing'}
        return render(request, "scaner.html",{'data':data})
    else:
        return render(request, "index.html")
    
    
   
    
    
def scan_for_entry(request):
    if request.method == 'POST':
        username = request.POST['guard_username']
        data = {'username': username, 'status':'IN','title':'Scan For Entry'}
        return render(request, "scaner.html",{'data':data})
    else:
        return render(request, "index.html")
    
    
def check_qr(request):
    if request.method == 'POST':
        username = request.POST['username']
        status = request.POST['status']
        qr_code = request.POST['qr_code']
        
        if status == "IN":
            txt = "Entry"
        else :
            txt = "Outing"
        try: 
            data = Gatepass.objects.get(hex_code=qr_code)
            if data.status == status :
                context = {'title':"Error on Scaning",'text':"Go to another Scan"}
                return render(request, "error.html",{'data':context})
            else:
                return  render(request, "guard_gatepaass.html",{'data':data,'title':f'Submit Data for {txt}',"submit":True})
        except:
            context = {'title':"QR Code Scan",'text':"Error! QR Code Not Match"}
            return render(request, "error.html",{'data':context})
       
            
    else:
        return render(request, "index.html")
    
    
    
def guard_gatepass(request):
    if request.method == 'POST':
        username = request.POST['username']
        status = request.POST['status']
        qr_code = request.POST['hex_code']
        
        data = Gatepass.objects.get(hex_code=qr_code)
        student_data = Student_data.objects.get(gate_pass_no=str(data.id))
        if status == "IN":
            title = "Outing Sucsessfull !"
            
            data.out_date = datetime.now().strftime("%d-%m-%Y")
            data.out_time = datetime.now().strftime("%I:%M-%p")
            data.status = "OUT"
            student_data.status = "OUT"
            
        elif status == "OUT":
            title = "Entry Sucsessfull !"
            
            data.in_date = datetime.now().strftime("%d-%m-%Y")
            data.in_time = datetime.now().strftime("%I:%M-%p")
            data.hex_code = f'{data.hex_code}-done'
            data.status = "IN"
            student_data.status = "IN"
            student_data.gate_pass_no = "NO"
        student_data.save()
        data.save()
        return render(request, "guard_gatepaass.html",{'data':data,'title':title,"submit":False})
    else:
        return render(request, "index.html")