from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Mainpage,Staffuser,Productservice,Managecustomer,Managevendor,Managebankaccount,Managebanktransfer,Invoice1,Managerevenue,Managecreditnotes,Bill,Managepayment,Managedebitnotes,Registration,Adminregistration,Managesuperuser,Plan,Coupon
import easygui


#main-page
def mainpage(request):
    return render(request,'mainpage.html')

def mainpage1(request):
    if request.method=='POST':
        mainpage1=Mainpage(contactname=request.POST['contactname'],contactemail=request.POST['contactemail'],contactsubject=request.POST['contactsubject'],contactmessage=request.POST['contactmessage'])
        mainpage1.save()
        easygui.msgbox("Send Message")
        return redirect('/mainpage')
    else:
        return render(request,'mainpage.html')

#loginpage
def loginpage(request):
    return render(request,'loginpage.html')

def loginvalidate(request):
    if request.method=='POST':
        if Registration.objects.filter(registeremail=request.POST['loginemail'],registerpass=request.POST['loginpassword']).exists():
            register=Registration.objects.get(registeremail=request.POST['loginemail'],registerpass=request.POST['loginpassword'])
            return render(request,'index1.html',{'register':register})
        else:
            return render(request,'loginpage.html')

#registration
def registration(request):
    if request.method=='POST':
        register=Registration(registername=request.POST['registername'],registeremail=request.POST['registeremail'],registerpass=request.POST['registerpass'])
        register.save()
        easygui.msgbox("successfull Registration")
        return redirect('/loginpage')
    else:
        return render(request,'registration.html')

#admin login
def adminlogin(request):
    return render(request,'adminlogin.html')

def loginadmin(request):
    if request.method=='POST':
        if Adminregistration.objects.filter(adminregisteremail=request.POST['adminloginemail'],adminregisterpass=request.POST['adminloginpassword']).exists():
            adminregister=Adminregistration.objects.get(adminregisteremail=request.POST['adminloginemail'],adminregisterpass=request.POST['adminloginpassword'])
            return render(request,'index.html',{'adminregister':adminregister})
        else:
            return render(request,'adminlogin.html')

def adminregistration(request):
    if request.method=='POST':
        adminregister=Adminregistration(adminregistername=request.POST['adminregistername'],adminregisteremail=request.POST['adminregisteremail'],adminregisterpass=request.POST['adminregisterpass'])
        adminregister.save()
        easygui.msgbox("successfull Registration")
        return redirect('/adminlogin')
    else:
        return render(request,'adminregistration.html')
        
#admin-index   
def index(request):
    return render(request,'index.html')

#admin-user
def manageuser(request):
    stfuser1=Staffuser.objects.all()
    return render(request,'manageuser.html',{'stfuser1':stfuser1})

def staffuser(request):
    if request.method=='POST':
        stfuser=Staffuser(staffname=request.POST['staffname'],staffemail=request.POST['staffemail'],staffpassword=request.POST['staffpassword'],staffuserrole=request.POST['staffuserrole'],custumefield=request.POST['custumefield'])
        stfuser.save()
        easygui.msgbox("successfull created")
        return redirect('/manageuser')
    else:
        return render(request,'staffuser.html')

def edituser(request,id):
    stfuser2=Staffuser.objects.get(id=id)
    return render(request,'updateuser.html',{'stfuser2':stfuser2})

def updateuser(request,id):
    if request.method=='POST':
        stfuser2=Staffuser.objects.get(id=id)
        stfuser2=Staffuser(staffname=request.POST['staffname'],staffemail=request.POST['staffemail'],staffpassword=request.POST['staffpassword'],staffuserrole=request.POST['staffuserrole'],custumefield=request.POST['custumefield'])
        stfuser2.save()
        easygui.msgbox("successfull Updated")
        return redirect('/manageuser')
    else:
        return render(request,'staffuser.html')

def deleteuser(request,id):
    stfuser3=Staffuser.objects.get(id=id)
    stfuser3.delete()
    easygui.msgbox("successfull Deleted")
    return redirect('/manageuser')

def staffuser1(request):
    return render(request,'staffuser.html')

 #productservice
def manageproductservice(request):
    productservice1=Productservice.objects.all()
    return render(request,'manageproduct&service.html',{'productservice1':productservice1})

def productserviceCreate(request):
    if request.method=='POST':
        productservice=Productservice(productservicename=request.POST['productservicename'],sku=request.POST['sku'],productservicedescription=request.POST['productservicedescription'],saleprice=request.POST['saleprice'],purchaseprice=request.POST['purchaseprice'],producttax=request.POST['producttax'],productcatagories=request.POST['productcatagories'],productunit=request.POST['productunit'],producttype=request.POST['producttype'],productcustomefield3=request.POST['productcustomefield3'])
        productservice.save()
        easygui.msgbox("successfull created")
        return redirect('/manageproduct&service')
    else:
        return render(request,'product&serviceCreate.html')

def editproductservice(request,id):
    productservice2=Productservice.objects.get(id=id)
    return render(request,'updateproductservice.html',{'productservice2':productservice2})

def updateproductservice(request,id):
    if request.method=='POST':
        productservice2=Productservice.objects.get(id=id)
        productservice2=Productservice(productservicename=request.POST['productservicename'],sku=request.POST['sku'],productservicedescription=request.POST['productservicedescription'],saleprice=request.POST['saleprice'],purchaseprice=request.POST['purchaseprice'],producttax=request.POST['producttax'],productcatagories=request.POST['productcatagories'],productunit=request.POST['productunit'],producttype=request.POST['producttype'],productcustomefield3=request.POST['productcustomefield3'])
        productservice2.save()
        easygui.msgbox("successfull Updated")
        return redirect('/manageproduct&service')
    else:
        return render(request,'updateproductservice.html')

def deleteproductservice(request,id):
    productservice3=Productservice.objects.get(id=id)
    productservice3.delete()
    easygui.msgbox("successfull Deleted")
    return redirect('/manageproduct&service')
#customer
def managecustomer(request):
    managecust1=Managecustomer.objects.all()
    return render(request,'managecustomer.html',{'managecust1':managecust1})

def editcustomer(request,id):
    managecust2=Managecustomer.objects.get(id=id)
    return render(request,'updatecustomer.html',{'managecust2':managecust2})

def createcustomer(request):
    if request.method=='POST':
        managecust=Managecustomer(cusname=request.POST['cusname'],cusnumber=request.POST['cusnumber'],cusemail=request.POST['cusemail'],cuspassword=request.POST['cuspassword'],cusfield1=request.POST['cusfield1'],cusbillname=request.POST['cusbillname'],cusbillcountry=request.POST['cusbillcountry'],cusbillstate=request.POST['cusbillstate'],cusbillcity=request.POST['cusbillcity'],cusbillphone=request.POST['cusbillphone'],cusbilzipcode=request.POST['cusbilzipcode'],cusbilladdress=request.POST['cusbilladdress'],shipadrsname=request.POST['shipadrsname'],shipadrscountry=request.POST['shipadrscountry'],shipadrsstate=request.POST['shipadrsstate'],shipadrscity=request.POST['shipadrscity'],shipadrsphone=request.POST['shipadrsphone'],shipadrszipcode=request.POST['shipadrszipcode'],shipadrsaddress=request.POST['shipadrsaddress'])
        managecust.save()
        easygui.msgbox("successfull Created")
        return redirect('/managecustomer')
    else:
        return render(request,'createcustomer.html')

def updatecustomer(request,id):
    if request.method=='POST':
        managecust2=Managecustomer.objects.get(id=id)
        managecust2=Managecustomer(cusname=request.POST['cusname'],cusnumber=request.POST['cusnumber'],cusemail=request.POST['cusemail'],cuspassword=request.POST['cuspassword'],cusfield1=request.POST['cusfield1'],cusbillname=request.POST['cusbillname'],cusbillcountry=request.POST['cusbillcountry'],cusbillstate=request.POST['cusbillstate'],cusbillcity=request.POST['cusbillcity'],cusbillphone=request.POST['cusbillphone'],cusbilzipcode=request.POST['cusbilzipcode'],cusbilladdress=request.POST['cusbilladdress'],shipadrsname=request.POST['shipadrsname'],shipadrscountry=request.POST['shipadrscountry'],shipadrsstate=request.POST['shipadrsstate'],shipadrscity=request.POST['shipadrscity'],shipadrsphone=request.POST['shipadrsphone'],shipadrszipcode=request.POST['shipadrszipcode'],shipadrsaddress=request.POST['shipadrsaddress'])
        managecust2.save()
        easygui.msgbox("successfull Updated")
        return redirect('/managecustomer')
    else:
        return render(request,'updatecustomer.html',{'managecust2':managecust2})

def deletecustomer(request,id):
    managecust3=Managecustomer.objects.get(id=id)
    managecust3.delete()
    easygui.msgbox("successfull Deleted")
    return redirect('/managecustomer')

#vendor
def managevendor(request):
    managevendor1=Managevendor.objects.all()
    return render(request,'managevendor.html',{'managevendor1':managevendor1})

def editvendor(request,id):
    managevend2=Managevendor.objects.get(id=id)
    return render(request,'updatevendor.html',{'managevend2':managevend2})


def updatevendor(request,id):
    if request.method=='POST':
        managevend2=Managevendor.objects.get(id=id)
        managevend2=Managevendor(vendorname=request.POST['vendorname'],vendornumber=request.POST['vendornumber'],vendoremail=request.POST['vendoremail'],vendorpassword=request.POST['vendorpassword'],vendorfield1=request.POST['vendorfield1'],vendorbillname=request.POST['vendorbillname'],vendorbillcountry=request.POST['vendorbillcountry'],vendorbillstate=request.POST['vendorbillstate'],vendorbillcity=request.POST['vendorbillcity'],vendorbillphone=request.POST['vendorbillphone'],vendorbillzipcode=request.POST['vendorbillzipcode'],vendorbilladdress=request.POST['vendorbilladdress'],vendorshipadrsname=request.POST['vendorshipadrsname'],vendorshipadrscountry=request.POST['vendorshipadrscountry'],vendorshipadrsstate=request.POST['vendorshipadrsstate'],vendorshipadrscity=request.POST['vendorshipadrscity'],vendorshipadrsphone=request.POST['vendorshipadrsphone'],vendorshipadrszipcode=request.POST['vendorshipadrszipcode'],vendorshipadrsaddress=request.POST['vendorshipadrsaddress'])
        managevend2.save()
        easygui.msgbox("successfull Updated")
        return redirect('/managevendor')
    else:
        return render(request,'updatevendor.html',{'managevend2':managevend2})

def createvendor(request):
    if request.method=='POST':
        managevendor=Managevendor(vendorname=request.POST['vendorname'],vendornumber=request.POST['vendornumber'],vendoremail=request.POST['vendoremail'],vendorpassword=request.POST['vendorpassword'],vendorfield1=request.POST['vendorfield1'],vendorbillname=request.POST['vendorbillname'],vendorbillcountry=request.POST['vendorbillcountry'],vendorbillstate=request.POST['vendorbillstate'],vendorbillcity=request.POST['vendorbillcity'],vendorbillphone=request.POST['vendorbillphone'],vendorbillzipcode=request.POST['vendorbillzipcode'],vendorbilladdress=request.POST['vendorbilladdress'],vendorshipadrsname=request.POST['vendorshipadrsname'],vendorshipadrscountry=request.POST['vendorshipadrscountry'],vendorshipadrsstate=request.POST['vendorshipadrsstate'],vendorshipadrscity=request.POST['vendorshipadrscity'],vendorshipadrsphone=request.POST['vendorshipadrsphone'],vendorshipadrszipcode=request.POST['vendorshipadrszipcode'],vendorshipadrsaddress=request.POST['vendorshipadrsaddress'])
        managevendor.save()
        easygui.msgbox("successfull Created")
        return redirect('/managevendor')
    else:
        return render(request,'createvendor.html')

def deletevendor(request,id):
    managevendor3=Managevendor.objects.get(id=id)
    managevendor3.delete()
    easygui.msgbox("successfull Deleted")
    return redirect('/managevendor')

#bankaccount
def managebankaccount(request):
    managebankaccount1=Managebankaccount.objects.all()
    return render(request,'managebankaccount.html',{'managebankaccount1':managebankaccount1})

def editbankaccount(request,id):
    managebankaccount2=Managebankaccount.objects.get(id=id)
    return render(request,'updatebankaccount.html',{'managebankaccount2':managebankaccount2})

def createbankaccount(request):
    if request.method=='POST':
        managebankaccount=Managebankaccount(bankusername=request.POST['bankusername'],bankname=request.POST['bankname'],accountnumber=request.POST['accountnumber'],openingbalance=request.POST['openingbalance'],bankcontact=request.POST['bankcontact'],bankaddress=request.POST['bankaddress'])
        managebankaccount.save()
        easygui.msgbox("successfull Created")
        return redirect('/managebankaccount')
    else:
        return render(request,'createbankaccount.html')

def updatebankaccount(request,id):
    if request.method=='POST':
        managebankaccount2=Managebankaccount.objects.get(id=id)
        managebankaccount2=Managebankaccount(bankusername=request.POST['bankusername'],bankname=request.POST['bankname'],accountnumber=request.POST['accountnumber'],openingbalance=request.POST['openingbalance'],bankcontact=request.POST['bankcontact'],bankaddress=request.POST['bankaddress'])
        managebankaccount2.save()
        easygui.msgbox("successfull Updated")
        return redirect('/managebankaccount')
    else:
        return render(request,'updatebankaccount.html',{'managebankaccount2':managebankaccount2})

def deletebankaccount(request,id):
    managebankaccount3=Managebankaccount.objects.get(id=id)
    managebankaccount3.delete()
    easygui.msgbox("successfull Deleted")
    return redirect('/managebankaccount')

#banktransfer
def managebanktransfer(request):
    managebanktransfer1=Managebanktransfer.objects.all()
    return render(request,'managebanktransfer.html',{'managebanktransfer1':managebanktransfer1})
    
def createbanktransfer(request):
    if request.method=='POST':
        managebanktransfer=Managebanktransfer(fromaccount=request.POST['fromaccount'],toaccount=request.POST['toaccount'],transferamount=request.POST['transferamount'],transferdate=request.POST['transferdate'],transferrefrence=request.POST['transferrefrence'])
        managebanktransfer.save()
        easygui.msgbox("successfull Created")
        return redirect('/managebanktransfer')
    else:
        return render(request,'createbanktransfer.html')

def editbanktransfer(request,id):
    managebanktransfer2=Managebanktransfer.objects.get(id=id)
    return render(request,'updatebanktransfer.html',{'managebanktransfer2':managebanktransfer2})

def updatebanktransfer(request,id):
    if request.method=='POST':
        managebanktransfer2=Managebanktransfer.objects.get(id=id)
        managebanktransfer2=Managebanktransfer(fromaccount=request.POST['fromaccount'],toaccount=request.POST['toaccount'],transferamount=request.POST['transferamount'],transferdate=request.POST['transferdate'],transferrefrence=request.POST['transferrefrence'])
        managebanktransfer2.save()
        easygui.msgbox("successfull Updated")
        return redirect('/managebanktransfer')
    else:
        return render(request,'updatebanktransfer.html',{'managebanktransfer2':managebanktransfer2})

def deletebanktransfer(request,id):
    managebanktransfer3=Managebanktransfer.objects.get(id=id)
    managebanktransfer3.delete()
    easygui.msgbox("successfull Deleted")
    return redirect('/managebanktransfer')

#invoice
def manageinvoice(request):
    manageinvoice1=Invoice1.objects.all()
    return render(request,'manageinvoice.html',{'manageinvoice1':manageinvoice1})

def createinvoice(request):
    if request.method=='POST':
        manageinvoice=Invoice1(invoicecust=request.POST['invoicecust'],invoiceissudate=request.POST['invoiceissudate'],invoiceduedate=request.POST['invoiceduedate'],invoicenum=request.POST['invoicenum'],catagory=request.POST['catagory'],invoicerefnum=request.POST['invoicerefnum'],discount=request.POST['discount'],psitem=request.POST['psitem'],psquantity=request.POST['psquantity'],psprice=request.POST['psprice'],pstax=request.POST['pstax'],psdis=request.POST['psdis'],psdescription=request.POST['psdescription'])
        manageinvoice.save()
        easygui.msgbox("successfull Created")
        return redirect('/manageinvoice')
    else:
        return render(request,'createinvoice.html')

def editinvoice(request,id):
    manageinvoicer2=Invoice1.objects.get(id=id)
    return render(request,'updateinvoice.html',{'manageinvoicer2':manageinvoicer2})

def updateinvoice(request,id):
    if request.method=='POST':
        manageinvoicer2=Invoice1.objects.get(id=id)
        manageinvoicer2=Invoice1(invoicecust=request.POST['invoicecust'],invoiceissudate=request.POST['invoiceissudate'],invoiceduedate=request.POST['invoiceduedate'],invoicenum=request.POST['invoicenum'],catagory=request.POST['catagory'],invoicerefnum=request.POST['invoicerefnum'],discount=request.POST['discount'],psitem=request.POST['psitem'],psquantity=request.POST['psquantity'],psprice=request.POST['psprice'],pstax=request.POST['pstax'],psdis=request.POST['psdis'],psdescription=request.POST['psdescription'])
        manageinvoicer2.save()
        easygui.msgbox("successfull Updated")
        return redirect('/manageinvoice')
    else:
        return render(request,'updateinvoice.html',{'manageinvoicer2':manageinvoicer2})

def deleteinvoice(request,id):
    manageinvoicer3=Invoice1.objects.get(id=id)
    manageinvoicer3.delete()
    easygui.msgbox("successfull Deleted")
    return redirect('/manageinvoice')
    
#revenue
def managerevenue(request):
    managerevenue1=Managerevenue.objects.all()
    return render(request,'managerevenue.html',{'managerevenue1':managerevenue1})

def createrevenue(request):
    if request.method=='POST':
        managerevenue=Managerevenue(revenuedate=request.POST['revenuedate'],revenueamount=request.POST['revenueamount'],revenueaccount=request.POST['revenueaccount'],revenuecustomer=request.POST['revenuecustomer'],revenuebankaddress=request.POST['revenuebankaddress'],revenuecatagory=request.POST['revenuecatagory'],revenuerefrence=request.POST['revenuerefrence'])
        managerevenue.save()
        easygui.msgbox("successfull Created")
        return redirect('/managerevenue')
    else:
        return render(request,'createrevenue.html')

def editrevenue(request,id):
    managerevenue2=Managerevenue.objects.get(id=id)
    return render(request,'updaterevenue.html',{'managerevenue2':managerevenue2})

def updaterevenue(request,id):
    if request.method=='POST':
        managerevenue2=Managerevenue.objects.get(id=id)
        managerevenue2=Managerevenue(revenuedate=request.POST['revenuedate'],revenueamount=request.POST['revenueamount'],revenueaccount=request.POST['revenueaccount'],revenuecustomer=request.POST['revenuecustomer'],revenuebankaddress=request.POST['revenuebankaddress'],revenuecatagory=request.POST['revenuecatagory'],revenuerefrence=request.POST['revenuerefrence'])
        managerevenue2.save()
        easygui.msgbox("successfull Updated")
        return redirect('/managerevenue')
    else:
        return render(request,'updaterevenue.html',{'managerevenue2':managerevenue2})

def deleterevenue(request,id):
    managerevenue3=Managerevenue.objects.get(id=id)
    managerevenue3.delete()
    easygui.msgbox("successfull Deleted")
    return redirect('/managerevenue')

#creditnotes
def managecreditnotes(request):
    managecreditnotes1=Managecreditnotes.objects.all()
    return render(request,'managecreditnotes.html',{'managecreditnotes1':managecreditnotes1})

def createcreditnotes(request):
    if request.method=='POST':
        managecreditnotes=Managecreditnotes(creditcustomer=request.POST['creditcustomer'],creditamount=request.POST['creditamount'],creditdate=request.POST['creditdate'],creditdescription=request.POST['creditdescription'])
        managecreditnotes.save()
        easygui.msgbox("successfull Created")
        return redirect('/managecreditnotes')
    else:
        return render(request,'createcreditnotes.html')

def editcreditnotes(request,id):
    managecreditnotes2=Managecreditnotes.objects.get(id=id)
    return render(request,'updatecreditnotes.html',{'managecreditnotes2':managecreditnotes2})

def updatecreditnotes(request,id):
    if request.method=='POST':
        managecreditnotes2=Managecreditnotes.objects.get(id=id)
        managecreditnotes2=Managecreditnotes(creditcustomer=request.POST['creditcustomer'],creditamount=request.POST['creditamount'],creditdate=request.POST['creditdate'],creditdescription=request.POST['creditdescription'])
        managecreditnotes2.save()
        easygui.msgbox("successfull Updated")
        return redirect('/managecreditnotes')
    else:
        return render(request,'updatecreditnotes.html',{'managecreditnotes2':managecreditnotes2})

def deletecreditnotes(request,id):
    managecreditnotes3=Managecreditnotes.objects.get(id=id)
    managecreditnotes3.delete()
    easygui.msgbox("successfull Deleted")
    return redirect('/managecreditnotes')

#bill
def managebill(request):
    managebill1=Bill.objects.all()
    return render(request,'managebill.html',{'managebill1':managebill1})

def createbill(request):
    if request.method=='POST':
        managebill=Bill(billvendor=request.POST['billvendor'],billdate=request.POST['billdate'],billduedate=request.POST['billduedate'],billnum=request.POST['billnum'],billcatagory=request.POST['billcatagory'],billordernum=request.POST['billordernum'],billdiscount=request.POST['billdiscount'],billitem=request.POST['billitem'],billquantity=request.POST['billquantity'],billprice=request.POST['billprice'],billtax=request.POST['billtax'],billdis=request.POST['billdis'],billdescription=request.POST['billdescription'])
        managebill.save()
        easygui.msgbox("successfull Created")
        return redirect('/managebill')
    else:
        return render(request,'createbill.html')

def editbill(request,id):
    managebill2=Bill.objects.get(id=id)
    return render(request,'updatebill.html',{'managebill2':managebill2})

def updatebill(request,id):
    if request.method=='POST':
        managebill2=Bill.objects.get(id=id)
        managebill2=Bill(billvendor=request.POST['billvendor'],billdate=request.POST['billdate'],billduedate=request.POST['billduedate'],billnum=request.POST['billnum'],billcatagory=request.POST['billcatagory'],billordernum=request.POST['billordernum'],billdiscount=request.POST['billdiscount'],billitem=request.POST['billitem'],billquantity=request.POST['billquantity'],billprice=request.POST['billprice'],billtax=request.POST['billtax'],billdis=request.POST['billdis'],billdescription=request.POST['billdescription'])
        managebill2.save()
        easygui.msgbox("successfull Updated")
        return redirect('/managebill')
    else:
        return render(request,'updatebill.html',{'managebill2':managebill2})

def deletebill(request,id):
    managebill3=Bill.objects.get(id=id)
    managebill3.delete()
    easygui.msgbox("successfull Deleted")
    return redirect('/managebill')

#payment
def managepayment(request):
    managepayment1=Managepayment.objects.all()
    return render(request,'managepayment.html',{'managepayment1':managepayment1})

def editpayment(request,id):
    managepayment2=Managepayment.objects.get(id=id)
    return render(request,'updatepayment.html',{'managepayment2':managepayment2})

def createpayment(request):
    if request.method=='POST':
        managepayment=Managepayment(paymentdate=request.POST['paymentdate'],paymentamount=request.POST['paymentamount'],paymentaccount=request.POST['paymentaccount'],paymentvendor=request.POST['paymentvendor'],paymentbankaddress=request.POST['paymentbankaddress'],paymentcatagory=request.POST['paymentcatagory'],paymentref=request.POST['paymentref'])
        managepayment.save()
        easygui.msgbox("successfull Created")
        return redirect('/managepayment')
    else:
        return render(request,'createpayment.html')

def updatepayment(request,id):
    if request.method=='POST':
        managepayment2=Managepayment.objects.get(id=id)
        managepayment2=Managepayment(paymentdate=request.POST['paymentdate'],paymentamount=request.POST['paymentamount'],paymentaccount=request.POST['paymentaccount'],paymentvendor=request.POST['paymentvendor'],paymentbankaddress=request.POST['paymentbankaddress'],paymentcatagory=request.POST['paymentcatagory'],paymentref=request.POST['paymentref'])
        managepayment2.save()
        easygui.msgbox("successfull Updated")
        return redirect('/managepayment')
    else:
        return render(request,'updatepayment.html',{'managepayment2':managepayment2})

def deletepayment(request,id):
    managepayment3=Managepayment.objects.get(id=id)
    managepayment3.delete()
    easygui.msgbox("successfull Deleted")
    return redirect('/managepayment')

#debitnotes
def managedebitnotes(request):
    managedebitnotes1=Managedebitnotes.objects.all()
    return render(request,'managedebitnotes.html',{'managedebitnotes1':managedebitnotes1})

def createdebitnotes(request):
    if request.method=='POST':
        managedebitnotes=Managedebitnotes(debitbill=request.POST['debitbill'],debitamount=request.POST['debitamount'],debitdate=request.POST['debitdate'],debitdescription=request.POST['debitdescription'])
        managedebitnotes.save()
        easygui.msgbox("successfull Created")
        return redirect('/managedebitnotes')
    else:
        return render(request,'createdebitnotes.html')

def editdebitnotes(request,id):
    managedebitnotes2=Managedebitnotes.objects.get(id=id)
    return render(request,'updatedebitnotes.html',{'managedebitnotes2':managedebitnotes2})

def updatedebitnotes(request,id):
    if request.method=='POST':
        managedebitnotes2=Managedebitnotes.objects.get(id=id)
        managedebitnotes2=Managedebitnotes(debitbill=request.POST['debitbill'],debitamount=request.POST['debitamount'],debitdate=request.POST['debitdate'],debitdescription=request.POST['debitdescription'])
        managedebitnotes2.save()
        easygui.msgbox("successfull Updated")
        return redirect('/managedebitnotes')
    else:
        return render(request,'updatedebitnotes.html',{'managedebitnotes2':managedebitnotes2})

def deletedebitnotes(request,id):
    managedebitnotes3=Managedebitnotes.objects.get(id=id)
    managedebitnotes3.delete()
    easygui.msgbox("successfull Deleted")
    return redirect('/managedebitnotes')

#super-admin
def index1(request):
    return render(request,'index1.html')

#superuser
def manageusersuperadmin(request):
    superuser1=Managesuperuser.objects.all()
    return render(request,'manageusersuperadmin.html',{'superuser1':superuser1})

def createuser(request):
    if request.method=='POST':
        superuser=Managesuperuser(superusername=request.POST['superusername'],superuseremail=request.POST['superuseremail'],superuserpassword=request.POST['superuserpassword'],superuserrole=request.POST['superuserrole'],supercustumefield=request.POST['supercustumefield'])
        superuser.save()
        easygui.msgbox("successfull Created")
        return redirect('/manageusersuperadmin')
    else:
        return render(request,'createuser.html')

def editsuperuser(request,id):
    superuser2=Managesuperuser.objects.get(id=id)
    return render(request,'updatesuperuser.html',{'superuser2':superuser2})

def updatesuperuser(request,id):
    if request.method=='POST':
        superuser2=Managesuperuser.objects.get(id=id)
        superuser2=Managesuperuser(superusername=request.POST['superusername'],superuseremail=request.POST['superuseremail'],superuserpassword=request.POST['superuserpassword'],superuserrole=request.POST['superuserrole'],supercustumefield=request.POST['supercustumefield'])
        superuser2.save()
        easygui.msgbox("successfull Updated")
        return redirect('/manageusersuperadmin')
    else:
        return render(request,'createuser.html')

def deletesuperuser(request,id):
    superuser3=Managesuperuser.objects.get(id=id)
    superuser3.delete()
    easygui.msgbox("successfull Deleted")
    return redirect('/manageusersuperadmin')

#plan
def manageplan(request):
    plan1=Plan.objects.all()
    return render(request,'manageplan.html',{'plan1':plan1})

def createnewplan(request):
    if request.method=='POST':
        plan=Plan(planname=request.POST['planname'],planprice=request.POST['planprice'],planduration=request.POST['planduration'],maxiuser=request.POST['maxiuser'],maxicustomer=request.POST['maxicustomer'],maxivendor=request.POST['maxivendor'],plandescription=request.POST['plandescription'])
        plan.save()
        easygui.msgbox("successfull Created")
        return redirect('/manageplan')
    else:
        return render(request,'createnewplan.html')

def editplan(request,id):
    plan2=Plan.objects.get(id=id)
    return render(request,'updateplan.html',{'plan2':plan2})

def updateplan(request,id):
    if request.method=='POST':
        plan2=Plan.objects.get(id=id)
        plan2=Plan(planname=request.POST['planname'],planprice=request.POST['planprice'],planduration=request.POST['planduration'],maxiuser=request.POST['maxiuser'],maxicustomer=request.POST['maxicustomer'],maxivendor=request.POST['maxivendor'],plandescription=request.POST['plandescription'])
        plan2.save()
        easygui.msgbox("successfull Updated")
        return redirect('/manageplan')
    else:
        return render(request,'createplan.html')

def deleteplan(request,id):
    plan3=Plan.objects.get(id=id)
    plan3.delete()
    easygui.msgbox("successfull Deleted")
    return redirect('/manageplan')

#coupon
def managecoupon(request):
    coupon1=Coupon.objects.all()
    return render(request,'managecoupon.html',{'coupon1':coupon1})

def editcoupon(request,id):
    coupon2=Coupon.objects.get(id=id)
    return render(request,'updatecoupon.html',{'coupon2':coupon2})

def createnewcoupon(request):
    if request.method=='POST':
        coupon=Coupon(couponname=request.POST['couponname'],coupondiscount=request.POST['coupondiscount'],couponlimits=request.POST['couponlimits'],code=request.POST['code'],coupondescription=request.POST['coupondescription'])
        coupon.save()
        easygui.msgbox("successfull Created")
        return redirect('/managecoupon')
    else:
        return render(request,'createnewcoupon.html')

def updatecoupon(request,id):
    if request.method=='POST':
        coupon2=Coupon.objects.get(id=id)
        coupon2=Coupon(couponname=request.POST['couponname'],coupondiscount=request.POST['coupondiscount'],couponlimits=request.POST['couponlimits'],code=request.POST['code'],coupondescription=request.POST['coupondescription'])
        coupon2.save()
        easygui.msgbox("successfull Updated")
        return redirect('/managecoupon')
    else:
        return render(request,'updatecoupon.html')

def deletecoupon(request,id):
    coupon3=Coupon.objects.get(id=id)
    coupon3.delete()
    easygui.msgbox("successfull Deleted")
    return redirect('/managecoupon')