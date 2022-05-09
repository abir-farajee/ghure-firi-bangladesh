from django.shortcuts import render


import pyrebase
import json
import ast
from json import dumps,loads
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from datetime import datetime,timezone
import pytz
from django.core.mail import send_mail
import requests 
import random 
from random import randint
from django.urls import reverse
import urllib.request
import urllib.parse
import pdfkit
from django.utils.crypto import get_random_string



config = {

  'apiKey': "AIzaSyAPBXBYOuClJop3F3aDEOhfF1kZjhUxGFA",
  'authDomain': "ghurefiribangladesh-e7ef2.firebaseapp.com",
  'databaseURL': "https://ghurefiribangladesh-e7ef2.firebaseio.com",
  'projectId': "ghurefiribangladesh-e7ef2",
  'storageBucket': "ghurefiribangladesh-e7ef2.appspot.com",
  'messagingSenderId': "198487718440",
  'appId': "1:198487718440:web:ab16558cabb12902c7931d",
  'measurementId': "G-B8PY09CQDG"
  }


firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database=firebase.database()

#---------------------------EXPLORE POST UPLOAD------------------------------

def allpackage(request):
    
    uid = request.session.get('localid')

    if uid is None:
        return redirect('login')
    else:

        
        postID = database.child('Package').shallow().get().val()
        if postID is not None:
            postData=[]
            for i in postID:

                postData.append(i)

            

            package_district=[]
            package_district1=[]
            package_district2=[]
            package_district3=[]


            package_name = []
            package_image = []
            package_desc=[]
            package_price=[]
            package_hotel=[]
            package_restaursnt=[]
            package_transportation=[]
            package_spot=[]
            pack_id=[]
            recomand=[]
            checkrecom=[]
            startdate=[]
            enddate=[]


            for i in postData:

                check=database.child('Stars').child(i).shallow().get().val()
                if check is None:
                    count="0"
                else:
                 count=len(database.child('Stars').child(i).shallow().get().val())

                pack_img = database.child('Package').child(i).child('pack_img').get().val()
                pack_dis = database.child('Package').child(i).child('district').get().val()
                pack_name = database.child('Package').child(i).child('packname').get().val()
                pack_desc = database.child('Package').child(i).child('packdesc').get().val()
                pack_price = database.child('Package').child(i).child('packprice').get().val()
                pack_hotel = database.child('Package').child(i).child('hotel').get().val()
                pack_res = database.child('Package').child(i).child('res').get().val()
                pack_trans = database.child('Package').child(i).child('trans').get().val()
                pack_spot = database.child('Package').child(i).child('spot').get().val()
                s_date = database.child('Package').child(i).child('startdate').get().val()
                e_date = database.child('Package').child(i).child('enddate').get().val()

                recomcheck = database.child('Stars').child(i).child(uid).get().val()
                if recomcheck is not None:
                    like = "true"
                else:
                    like = "false"


                id = i
                package_district.append(pack_dis)
                package_district1.append('')
                package_district2.append('')
                package_district3.append('')

                package_name.append(pack_name)
                package_image.append(pack_img)
                package_desc.append(pack_desc)
                package_price.append(pack_price)
                package_hotel.append(pack_hotel)
                package_restaursnt.append(pack_res)
                package_transportation.append(pack_trans)
                package_spot.append(pack_spot)
                recomand.append(count)
                checkrecom.append(like)
                startdate.append(s_date)
                enddate.append(e_date)
                
                pack_id.append(id)
            print(package_name)


     

     
            dist = zip(package_district,package_district1,package_district2,package_district3)
            comb_lis = zip(startdate,enddate,package_district,package_name,package_image,package_desc,package_price,package_hotel,package_restaursnt,package_transportation,package_spot, pack_id,checkrecom,recomand)
        
            uid = request.session.get('localid')
            user_photo= database.child("users").child(uid).child("Image Url").get().val()
            user_email= database.child("users").child(uid).child("email").get().val()
            user_phone= database.child("users").child(uid).child("phone").get().val()
            user_name= database.child("users").child(uid).child("username").get().val()

        
    

        
            return render(request,'package.html',{'comb_lis':comb_lis,'dist':dist,"name":user_name,"photo":user_photo,"email":user_email,"phone":user_phone})
        else:
            package_name = []
            package_image = []
            package_desc=[]
            package_price=[]
            package_hotel=[]
            package_restaursnt=[]
            package_transportation=[]
            package_spot=[]
            startdate=[]
            enddate=[]
            

            package_name.append('n')
            package_image.append('n')
            package_desc.append('n')
            package_price.append('n')
            package_hotel.append('n')
            package_restaursnt.append('n')
            package_transportation.append('n')
            package_spot.append('n')
            startdate.append('n')
            enddate.append('n')
            comb_lis = zip(startdate,enddate,package_district,package_name,package_image,package_desc,package_price,package_hotel,package_restaursnt,package_transportation,package_spot, pack_id,recomand)

            user_photo= database.child("users").child(uid).child("Image Url").get().val()
            user_email= database.child("users").child(uid).child("email").get().val()
            user_phone= database.child("users").child(uid).child("phone").get().val()
            user_name= database.child("users").child(uid).child("username").get().val()
            return render(request,'package.html',{'comb_lis':comb_lis,"name":user_name,"photo":user_photo,"email":user_email,"phone":user_phone})

def searchbylocation(request):
    
  uid = request.session.get('uid')

  if uid is None:
        return redirect('login')
  else:
    if request.method=='POST':
        location = request.POST['location']

        
        postID = database.child('Package').order_by_child('district').equal_to(location).get().val()
        if postID is not None:
            postData=[]
            for i in postID:

                postData.append(i)

            postData.sort(reverse=True)

            package_district=[]
            package_district1=[]
            package_district2=[]
            package_district3=[]
            package_name = []
            package_image = []
            package_desc=[]
            package_price=[]
            package_hotel=[]
            package_restaursnt=[]
            package_transportation=[]
            package_spot=[]
            recomand=[]
            pack_id=[]
            startdate=[]
            checkrecom=[]
            enddate=[]


            for i in postData:

                check=database.child('Stars').child(i).shallow().get().val()
                if check is None:
                    count="0"
                else:
                 count=len(database.child('Stars').child(i).shallow().get().val())

                pack_img = database.child('Package').child(i).child('pack_img').get().val()
                pack_dis = database.child('Package').child(i).child('district').get().val()
                pack_name = database.child('Package').child(i).child('packname').get().val()
                pack_desc = database.child('Package').child(i).child('packdesc').get().val()
                pack_price = database.child('Package').child(i).child('packprice').get().val()
                pack_hotel = database.child('Package').child(i).child('hotel').get().val()
                pack_res = database.child('Package').child(i).child('res').get().val()
                pack_trans = database.child('Package').child(i).child('trans').get().val()
                pack_spot = database.child('Package').child(i).child('spot').get().val()
                s_date = database.child('Package').child(i).child('startdate').get().val()
                e_date = database.child('Package').child(i).child('enddate').get().val()

                recomcheck = database.child('Stars').child(i).child(uid).get().val()
                if recomcheck is not None:
                    like = "true"
                else:
                    like = "false"
                id = i
                package_district.append(pack_dis)
                package_district1.append('')
                package_district2.append('')
                package_district3.append('')

                package_name.append(pack_name)
                package_image.append(pack_img)
                package_desc.append(pack_desc)
                package_price.append(pack_price)
                package_hotel.append(pack_hotel)
                package_restaursnt.append(pack_res)
                package_transportation.append(pack_trans)
                package_spot.append(pack_spot)
                startdate.append(s_date)
                enddate.append(e_date)
                recomand.append(count)
                checkrecom.append(like)

                pack_id.append(id)
            print(package_name)


     

     
            
            comb_lis = zip(startdate,enddate,package_district,package_name,package_image,package_desc,package_price,package_hotel,package_restaursnt,package_transportation,package_spot, pack_id,checkrecom,recomand)
        
            postID = database.child('Package').shallow().get().val()
        
            postData=[]
            for i in postID:

                postData.append(i)
            

            package_district=[]
            package_district1=[]
            package_district2=[]
            package_district3=[]

            for i in postData:
                pack_dis = database.child('Package').child(i).child('district').get().val()
                
                package_district.append(pack_dis)
                package_district1.append('')
                package_district2.append('')
                package_district3.append('')

            dist = zip(package_district,package_district1,package_district2,package_district3)



            uid = request.session.get('localid')
            user_photo= database.child("users").child(uid).child("Image Url").get().val()
            user_email= database.child("users").child(uid).child("email").get().val()
            user_phone= database.child("users").child(uid).child("phone").get().val()
            user_name= database.child("users").child(uid).child("username").get().val()

        
    

        
            return render(request,'package.html',{'comb_lis':comb_lis,'dist':dist,"name":user_name,"photo":user_photo,"email":user_email,"phone":user_phone})
        else:
            package_name = []
            package_image = []
            package_desc=[]
            package_price=[]
            package_hotel=[]
            package_restaursnt=[]
            package_transportation=[]
            package_spot=[]
            startdate=[]
            enddate=[]
            

            package_name.append('n')
            package_image.append('n')
            package_desc.append('n')
            package_price.append('n')
            package_hotel.append('n')
            package_restaursnt.append('n')
            package_transportation.append('n')
            package_spot.append('n')
            
            startdate.append('n')
            enddate.append('n')
            comb_lis = zip(startdate,enddate,package_district,package_name,package_image,package_desc,package_price,package_hotel,package_restaursnt,package_transportation,package_spot, pack_id,recomand)

            user_photo= database.child("users").child(uid).child("Image Url").get().val()
            user_email= database.child("users").child(uid).child("email").get().val()
            user_phone= database.child("users").child(uid).child("phone").get().val()
            user_name= database.child("users").child(uid).child("username").get().val()
            return render(request,'package.html',{'comb_lis':comb_lis,"name":user_name,"photo":user_photo,"email":user_email,"phone":user_phone})

def searchbyprice(request):
    
  uid = request.session.get('uid')

  if uid is None:
        return redirect('login')
  else:
    if request.method=='POST':
        minimumprice = request.POST['minprice']
        maximumprice = request.POST['maxprice']
   

        
        postID = database.child('Package').order_by_child('packprice').start_at(minimumprice).end_at(maximumprice).get().val()
        if postID is not None:
            postData=[]
            for i in postID:

                postData.append(i)

            postData.sort(reverse=True)

            package_district=[]
            package_district1=[]
            package_district2=[]
            package_district3=[]
            package_name = []
            package_image = []
            package_desc=[]
            package_price=[]
            package_hotel=[]
            package_restaursnt=[]
            package_transportation=[]
            package_spot=[]
            pack_id=[]
            startdate=[]
            enddate=[]


            for i in postData:

                pack_img = database.child('Package').child(i).child('pack_img').get().val()
                pack_dis = database.child('Package').child(i).child('district').get().val()
                pack_name = database.child('Package').child(i).child('packname').get().val()
                pack_desc = database.child('Package').child(i).child('packdesc').get().val()
                pack_price = database.child('Package').child(i).child('packprice').get().val()
                pack_hotel = database.child('Package').child(i).child('hotel').get().val()
                pack_res = database.child('Package').child(i).child('res').get().val()
                pack_trans = database.child('Package').child(i).child('trans').get().val()
                pack_spot = database.child('Package').child(i).child('spot').get().val()
                s_date = database.child('Package').child(i).child('startdate').get().val()
                e_date = database.child('Package').child(i).child('enddate').get().val()

                id = i
                package_district.append(pack_dis)
                package_district1.append('')
                package_district2.append('')
                package_district3.append('')

                package_name.append(pack_name)
                package_image.append(pack_img)
                package_desc.append(pack_desc)
                package_price.append(pack_price)
                package_hotel.append(pack_hotel)
                package_restaursnt.append(pack_res)
                package_transportation.append(pack_trans)
                package_spot.append(pack_spot)
                startdate.append(s_date)
                enddate.append(e_date)

                pack_id.append(id)
            print(package_name)


     

     
            dist = zip(package_district,package_district1,package_district2,package_district3)
            comb_lis = zip(startdate,enddate,package_district,package_name,package_image,package_desc,package_price,package_hotel,package_restaursnt,package_transportation,package_spot, pack_id,checkrecom,recomand)
        
            uid = request.session.get('localid')
            user_photo= database.child("users").child(uid).child("Image Url").get().val()
            user_email= database.child("users").child(uid).child("email").get().val()
            user_phone= database.child("users").child(uid).child("phone").get().val()
            user_name= database.child("users").child(uid).child("username").get().val()

        
    

        
            return render(request,'package.html',{'comb_lis':comb_lis,'dist':dist,"name":user_name,"photo":user_photo,"email":user_email,"phone":user_phone})
        else:
            package_name = []
            package_image = []
            package_desc=[]
            package_price=[]
            package_hotel=[]
            package_restaursnt=[]
            package_transportation=[]
            package_spot=[]
            startdate=[]
            enddate=[]
            

            package_name.append('n')
            package_image.append('n')
            package_desc.append('n')
            package_price.append('n')
            package_hotel.append('n')
            package_restaursnt.append('n')
            package_transportation.append('n')
            package_spot.append('n')
            startdate.append('n')
            enddate.append('n')
            comb_lis = zip(startdate,enddate,package_district,package_name,package_image,package_desc,package_price,package_hotel,package_restaursnt,package_transportation,package_spot, pack_id,recomand)
            user_email= database.child("users").child(uid).child("email").get().val()
            user_phone= database.child("users").child(uid).child("phone").get().val()
            user_name= database.child("users").child(uid).child("username").get().val()
            return render(request,'package.html',{'comb_lis':comb_lis,"name":user_name,"photo":user_photo,"email":user_email,"phone":user_phone})


#---------------------------POST LIKE ------------------------------

def addstar(request):

    if request.method=='POST':
        
        pack_id = request.POST['pack_id']

        a = request.session['localid']

        data = {a:"true"
                 }


        check = database.child('Stars').child(pack_id).update(data)

       

        if check is not None:

            return redirect("allpackage")

        else:
            return redirect("allpackage")


#---------------------------POST UNLIKE ------------------------------

def removestar(request):

    if request.method=='POST':
        
        pack_id = request.POST['pack_id']

        a = request.session['localid']

       
        database.child('Stars').child(pack_id).child(a).remove()


        return redirect("allpackage")





def booking(request):
    
  uid = request.session.get('uid')

  if uid is None:
        return redirect('login')
  else:
    if request.method=='POST':

        
        journeydate = request.POST['journeydate']
        pack_id = request.POST['pack_id']


        
        pack_name = database.child('Package').child(pack_id).child('packname').get().val()
        pack_desc = database.child('Package').child(pack_id).child('packdesc').get().val()
        pack_price = database.child('Package').child(pack_id).child('packprice').get().val()
        pack_hotel = database.child('Package').child(pack_id).child('hotel').get().val()
        pack_res = database.child('Package').child(pack_id).child('res').get().val()
        pack_trans = database.child('Package').child(pack_id).child('trans').get().val()
        pack_spot = database.child('Package').child(pack_id).child('spot').get().val()

        booking_data={
            'Covering_Spots': pack_spot,
            'Dining':pack_res,
            'Hotel_name': pack_hotel,
            'Journey_Date': journeydate,
            'Package_Description':pack_desc ,
            'Package_Name':pack_name,
            'Payment': "Unpaid",
            'Total_Amount': pack_price,
            'Transportation': pack_trans,
            'uid':uid

        }


        set_booking = database.child('PackageOrders').push(booking_data)

        if set_booking is not None:


            bookedID=set_booking['name']
            message = "Booking successfully done. Now complete your payment."
            

            

            return render(request,'pack_payment.html',{'success_msg':message,'bookedID':bookedID,'Covering_Spots': pack_spot,'Dining':pack_res,'Hotel_name': pack_hotel,'Journey_Date': journeydate,'Package_Description': pack_desc,'Package_Name':pack_name,'Total_Amount': pack_price,'Transportation': pack_trans,'uid':uid})


        

def sendmsgpack(request):

    uid = request.session.get('uid')

    if uid is None:
            return redirect('login')
    else:
        if request.method=='POST':
            phonenumber = request.POST['phone']
            bookingid = request.POST['bookedID']


            r1 = randint(100000,999999)
            transaction = get_random_string(8).upper()
            request.session['verification_code']=r1

            print(r1)

            api = "http://api.greenweb.com.bd/api.php"

            token = "3fa8287141f334db97c7bb32c9de68d3"

            to = '+8801622124013'

            data = {'token':token, 
                    'to':to, 
                    'message':'Your verification code for GhureFiri Bangladesh is - '+ str(r1)} 
            
            responses = requests.post(url = api, data = data) 

            response = responses.text 
            print(response)
            packname = database.child('PackageOrders').child(bookingid).child('Package_Name').get().val()
            amount = database.child('PackageOrders').child(bookingid).child('Total_Amount').get().val()

            data={
                'Order_ID':bookingid,
                'uid':uid,
                'Amount':amount,
                'Pack_Name':packname,
                'TransactionID':transaction
            }

            database.child("Transaction").child(bookingid).update(data)

            print(transaction)



            return render(request,"pay_verify.html",{'phone':phonenumber,'bookingid':bookingid})
        else:
            return redirect('allpackage')


def packpaymentverify(request):

    uid = request.session.get('uid')

    if uid is None:
            return redirect('login')
    else:

            code = int(request.POST['code'])
            bookingid = request.POST['bookedID']
            transactionid = request.POST['transactionid']
            systemcode=int(request.session.get('verification_code'))
            

            if code==systemcode:
                message = "Payment verification Successfull"
                request.session['message']=message
                del request.session['verification_code']
                data={
                    'Payment':"Processing",
                    'TransactionID':transactionid
                }

                database.child('PackageOrders').child(bookingid).update(data)


                return render(request,"pay_verify.html",{'messg':message,'type':"success"})

                

            else:
                message = "Not Match"
                print(systemcode)
                print(code)


                return render(request,"pay_verify.html",{'messg':message,'type':"error"})
                
