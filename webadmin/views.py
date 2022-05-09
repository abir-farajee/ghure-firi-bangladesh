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

#---------------------------ADMIN LOGIN ------------------------------

def adminlog(request):
  adminid = request.session.get('adminid')
  if adminid is not None:
        return redirect('adminhome')
  else:

    if request.method=='POST':
        
       password = request.POST['password']

       if password == '1234':
               request.session['adminid']='1234'      
               return redirect('adminhome')
       else:
              
              return redirect('adminlog')
    else:

       return render(request,'adminlogin.html')

#---------------------------ADMIN DASHBOARD ------------------------------

def adminhome(request):

  adminid = request.session.get('adminid')
  if adminid is None:
        return redirect('adminlog')
  else:

      packcount=len(database.child('Package').shallow().get().val())
      tourcount=len(database.child('Tour').child('Place').shallow().get().val())
      packbookingcount=len(database.child('PackageOrders').shallow().get().val())
      tourbookingcount=len(database.child('Orders').shallow().get().val())
      if packcount is None:
         packcount='0'
      if tourcount is None:
         tourcount='0'
      if packbookingcount is None:
         packbookingcount='0'
      if tourbookingcount is None:
         tourbookingcount='0'

      return render(request,'admin_home.html',{'packcount':packcount,'tourcount':tourcount,'packbookingcount':packbookingcount,'tourbookingcount':tourbookingcount})



 #---------------------------NEW PACKAGE ADD ------------------------------ 

def addpackage(request):
  adminid = request.session.get('adminid')
  if adminid is None:
        return redirect('adminlog')
  else:


    if request.method=='POST':
         packname = request.POST['pack_name']
         packdesc = request.POST['pack_desc']
         startdate = request.POST['start_date']
         enddate = request.POST['end_date']
         packprice = request.POST['pack_price']
         pack_img = request.POST['pack_img']
         district_name = request.POST['district_name']

         hotel = request.POST['hotel']
         res = request.POST['res']
         trans = request.POST['trans']
         spot = request.POST['spots']
               
        
       
         
         details = {
                 'packname':packname,
                 'packdesc':packdesc,
                 'packprice':packprice,
                 'pack_img':pack_img,
                 'startdate':startdate,
                 'enddate':enddate,
                 'hotel':hotel,
                 'res':res,
                 'trans':trans,
                 'spot':spot,
                 'district':district_name
                 }





         check = database.child('Package').push(details)

         if check is not None:

                return redirect("addpackage")
         else:
                messages.info(request,'invalid credentials')
                return redirect('/img')
    else:
        return render(request,'add_package.html')


#--------------------------- MANAGE PACKAGE LIST ------------------------------

def packagelist(request):

  adminid = request.session.get('adminid')
  if adminid is None:
        return redirect('adminlog')
  else:

        postID = database.child('Package').shallow().get().val()
        if postID is not None:
            postData=[]
            for i in postID:

                postData.append(i)

            

            package_district=[]
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


                id = i
                package_district.append(pack_dis)
                package_name.append(pack_name)
                package_image.append(pack_img)
                package_desc.append(pack_desc)
                package_price.append(pack_price)
                package_hotel.append(pack_hotel)
                package_restaursnt.append(pack_res)
                package_transportation.append(pack_trans)
                package_spot.append(pack_spot)
                recomand.append(count)
                startdate.append(s_date)
                enddate.append(e_date)
                
                pack_id.append(id)
            print(package_name)

            pack_list = zip(startdate,enddate,package_district,package_name,package_image,package_desc,package_price,package_hotel,package_restaursnt,package_transportation,package_spot, pack_id,recomand)

        return render(request,'admin_packagelist.html',{'packdata':pack_list})


#--------------------------- UPDATE PACKAGE------------------------------


def updatepack(request):
  adminid = request.session.get('adminid')
  if adminid is None:
        return redirect('adminlog')
  else:

         packname = request.POST['packname']
         packdesc = request.POST['desc']
         startdate = request.POST['startdate']
         enddate = request.POST['enddate']
         packprice = request.POST['packprice']
         hotel = request.POST['hotel']
         res = request.POST['res']
         trans = request.POST['trans']
         spot = request.POST['spot']
         packid = request.POST['packid']

         updatedata = {
          'packname':packname,
          'packdesc':packdesc,
          'packprice':packprice,
          'startdate':startdate,
          'enddate':enddate,
          'hotel':hotel,
          'res':res,
          'trans':trans,
          'spot':spot
         }
         database.child('Package').child(packid).update(updatedata)

         return redirect('packagelist')


#--------------------------- DELETE PACKAGE ------------------------------

def deletepack(request):
  adminid = request.session.get('adminid')
  if adminid is None:
        return redirect('adminlog')
  else:
         packid = request.POST['packid']

         database.child('Package').child(packid).remove()

         return redirect('packagelist')



#--------------------------- MANAGE TOUR LIST ------------------------------

def tourlist(request):

  adminid = request.session.get('adminid')
  if adminid is None:
        return redirect('adminlog')
  else:

        postID = database.child('Tour').child('Place').shallow().get().val()
        if postID is not None:
            postData=[]
            for i in postID:

                postData.append(i)

            

            tour_name = []
            tour_image = []
            hotel=[]
            trans=[]
            tourid=[]


            for i in postData:

                hotelcheck=database.child('Tour').child('Place').child(i).child('Hotels').shallow().get().val()
                if hotelcheck is None:
                    hotelcount="0"
                else:
                 hotelcount=len(database.child('Tour').child('Place').child(i).child('Hotels').shallow().get().val())

                translcheckt=database.child('Tour').child('Place').child(i).child('Transportation').shallow().get().val()
                if translcheckt is None:
                    transcount="0"
                else:
                 transcount=len(database.child('Tour').child('Place').child(i).child('Transportation').shallow().get().val())

                pack_img = database.child('Tour').child('Place').child(i).child('place_img').get().val()
                pack_name = database.child('Tour').child('Place').child(i).child('place_name').get().val()

                id = i
                tour_name.append(pack_name)
                tour_image.append(pack_img)
                hotel.append(hotelcount)
                trans.append(transcount)
                
                tourid.append(id)
            print(tourid)

            tour_list = zip(tour_name,tour_image,hotel,trans,tourid)

        return render(request,'admin_tourlist.html',{'tourdata':tour_list})




#--------------------------- MANAGE PACKAGE BOOKING LIST ------------------------------

def packbooked(request):

  adminid = request.session.get('adminid')
  if adminid is None:
        return redirect('adminlog')
  else:

        postID = database.child('PackageOrders').shallow().get().val()
        if postID is not None:
            postData=[]
            for i in postID:

                postData.append(i)

            

            
            package_name = []
            package_price=[]
            username=[]
            userphone=[]
            booking_id=[]

            paystatus=[]
            transactionID=[]
            admin_transaction=[]


            for i in postData:

                pack_name = database.child('PackageOrders').child(i).child('Package_Name').get().val()
                pack_price = database.child('PackageOrders').child(i).child('Total_Amount').get().val()
                paystats = database.child('PackageOrders').child(i).child('Payment').get().val()
                transactionid = database.child('PackageOrders').child(i).child('TransactionID').get().val()
                uid = database.child('PackageOrders').child(i).child('uid').get().val()

                uname = database.child('users').child(uid).child('username').get().val()
                uphone = database.child('users').child(uid).child('phone').get().val()
                checktransaction = database.child('Transaction').child(i).child('TransactionID').get().val()
               

                id = i
               
                package_name.append(pack_name)
                package_price.append(pack_price)
                username.append(uname)
                userphone.append(uphone)
                paystatus.append(paystats)
                transactionID.append(transactionid)
                admin_transaction.append(checktransaction)

                
                booking_id.append(id)

            bookedpackdata = zip(package_name,package_price,username,userphone,booking_id,paystatus,transactionID,admin_transaction)

        return render(request,'admin_bookedpack.html',{'bookedpackdata':bookedpackdata})




#--------------------------- MANAGE PACKAGE BOOKING LIST ------------------------------

def tourbooked(request):

  adminid = request.session.get('adminid')
  if adminid is None:
        return redirect('adminlog')
  else:

        postID = database.child('Orders').shallow().get().val()
        if postID is not None:
            postData=[]
            for i in postID:

                postData.append(i)

            

            
            place_name = []
            total_price=[]
            paystatus=[]
            transactionID=[]
            username=[]
            userphone=[]
            booking_id=[]
            admin_transaction=[]

            for i in postData:

                p_name = database.child('Orders').child(i).child('Place_Name').get().val()
                t_price = database.child('Orders').child(i).child('Total_Amount').get().val()
                paystats = database.child('Orders').child(i).child('Payment').get().val()
                transactionid = database.child('Orders').child(i).child('TransactionID').get().val()
                uid = database.child('Orders').child(i).child('uid').get().val()

                uname = database.child('users').child(uid).child('username').get().val()
                uphone = database.child('users').child(uid).child('phone').get().val()
                checktransaction = database.child('Transaction').child(i).child('TransactionID').get().val()
               

                id = i

                place_name.append(p_name)
                total_price.append(t_price)
                paystatus.append(paystats)
                transactionID.append(transactionid)
                admin_transaction.append(checktransaction)
                username.append(uname)
                userphone.append(uphone)

                
                booking_id.append(id)

            bookedtourdata = zip(place_name,total_price,paystatus,transactionID,admin_transaction,username,userphone,booking_id)

        return render(request,'admin_bookedtour.html',{'bookedtourdata':bookedtourdata})


def comfirmtourbooking(request):

  adminid = request.session.get('adminid')
  if adminid is None:
        return redirect('adminlog')
  else:
         bookingid = request.POST['bookingid']
         data={
             'Payment':"Paid"
         }

         database.child('Orders').child(bookingid).update(data)

         return redirect('tourbooked')  



def recheckreq(request):

  adminid = request.session.get('adminid')
  if adminid is None:
        return redirect('adminlog')
  else:
         bookingid = request.POST['bookingid']
         data={
             'Payment':"Resend"
         }

         database.child('Orders').child(bookingid).update(data)

         return redirect('tourbooked')  




def packcomfirmtourbooking(request):

  adminid = request.session.get('adminid')
  if adminid is None:
        return redirect('adminlog')
  else:
         bookingid = request.POST['bookingid']
         data={
             'Payment':"Paid"
         }

         database.child('PackageOrders').child(bookingid).update(data)

         return redirect('packbooked')  



def packrecheckreq(request):

  adminid = request.session.get('adminid')
  if adminid is None:
        return redirect('adminlog')
  else:
         bookingid = request.POST['bookingid']
         data={
             'Payment':"Resend"
         }

         database.child('PackageOrders').child(bookingid).update(data)

         return redirect('packbooked')  


#--------------------------- DELETE PACKAGE ------------------------------

def deletetour(request):
  adminid = request.session.get('adminid')
  if adminid is None:
        return redirect('adminlog')
  else:
         tourid = request.POST['tourid']

         database.child('Tour').child('Place').child(tourid).remove()

         return redirect('tourlist')  




#--------------------------- ADD TOUR ------------------------------

def addtour(request):
  adminid = request.session.get('adminid')
  if adminid is None:
        return redirect('adminlog')
  else:


    if request.method=='POST':
         placename = request.POST['place_name']
         placeimg = request.POST['place_img']
               
        
       
         
         details = {
                 'place_name':placename,
                 'place_img':placeimg
                 
          
                 }





         check = database.child('Tour').child('Place').push(details)

         if check is not None:

                return redirect("addtour")
         else:
                messages.info(request,'invalid credentials')
                return redirect('/addtour')
    else:
        return render(request,'add_tour.html')

#--------------------------- ADD HOTEL FOR TOUR PLACE ------------------------------


def addhotel(request):
  adminid = request.session.get('adminid')
  if adminid is None:
        return redirect('adminlog')
  else:


    if request.method=='POST':
         hotelname = request.POST['hotel_name']
         price = request.POST['price']
         placeid = request.POST['placeid']
         hotelimg = request.POST['hotel_img']
         desc = request.POST['hotel_desc']
               
        
       
         
         details = {
                 'hotel_name':hotelname,
                 'room_price':price,
                 'hotel_img': hotelimg,
                 'hotel_descr':desc
                 
          
                 }





         check = database.child('Tour').child('Place').child(placeid).child('Hotels').push(details)

         if check is not None:

                return redirect("addhotel")
         else:
                messages.info(request,'invalid credentials')
                return redirect('/addhotel')
    else:

        postID = database.child('Tour').child('Place').get().val()
        if postID is not None:
            postData=[]
            for i in postID:

                postData.append(i)

            postData.sort(reverse=True)

            places=[]
            places1=[]
            places2=[]
            places3=[]
            placeID=[]
            
  


            for i in postData:

  
                pack_dis = database.child('Tour').child('Place').child(i).child('place_name').get().val()
                id=i

                places.append(pack_dis)
                places1.append('')
                places2.append('')
                places3.append('')
                placeID.append(id)
                




     
            print(places)
     
            dist = zip(places,places1,places2,places3,placeID)
            
  
        
            return render(request,'add_hotel.html',{'dist':dist})
        else:
            places=[]
            places1=[]
            places2=[]
            places3=[]

            places.append(pack_dis)
            places1.append('')
            places2.append('')
            places3.append('')
            dist = zip(places,places1,places2,places3)
            return render(request,'add_hotel.html',{'dist':dist})



#--------------------------- ADD TRANSPORTATION FOR TOUR PLACE ------------------------------



def addtransportation(request):
  adminid = request.session.get('adminid')
  if adminid is None:
        return redirect('adminlog')
  else:


    if request.method=='POST':
         name = request.POST['name']
         tname = request.POST['trans']
         seat = request.POST['seat']
         ttype = request.POST['type']
         placeid = request.POST['placeid']
         transimg = request.POST['trans_img']
         tprice = request.POST['tprice']
         timeone = request.POST['timeone']
         timetwo = request.POST['timetwo']
         timethree = request.POST['timethree']
               
        
       
         
         details = {
                 'trans':tname,
                 'trans_name':name,
                 'seats':seat,
                 'type':ttype,
                 'trans_img': transimg,
                 'ticket_price':tprice,
                 'time_one':timeone,
                 'time_two':timetwo,
                 'time_three':timethree
                 }





         check = database.child('Tour').child('Place').child(placeid).child('Transportation').push(details)

         if check is not None:

                return redirect("addtransportation")
         else:
                messages.info(request,'invalid credentials')
                return redirect('/addtransportation')
    else:

        postID = database.child('Tour').child('Place').get().val()
        if postID is not None:
            postData=[]
            for i in postID:

                postData.append(i)

            postData.sort(reverse=True)

            places=[]
            places1=[]
            places2=[]
            places3=[]
            placeID=[]
            
  


            for i in postData:

  
                pack_dis = database.child('Tour').child('Place').child(i).child('place_name').get().val()
                id=i

                places.append(pack_dis)
                places1.append('')
                places2.append('')
                places3.append('')
                placeID.append(id)
                




     
            print(places)
     
            dist = zip(places,places1,places2,places3,placeID)
            
  
        
            return render(request,'add_trans.html',{'dist':dist})
        else:
            places=[]
            places1=[]
            places2=[]
            places3=[]

            places.append(pack_dis)
            places1.append('')
            places2.append('')
            places3.append('')
            dist = zip(places,places1,places2,places3)
            return render(request,'add_trans.html',{'dist':dist})

#--------------------------- LOGOUR FOR ADMIN ------------------------------           
        

def adminlogout(request):
    del request.session['adminid']
    auth.logout(request)
  
    return redirect('adminlog')


