from django.db import models

class Mainpage(models.Model):
    contactname=models.CharField(max_length=100)
    contactemail=models.EmailField()
    contactsubject=models.CharField(max_length=100)
    contactmessage=models.CharField(max_length=100)

    def __str__(self):
        return self.contactname

class Registration(models.Model):
    registername=models.CharField(max_length=100)
    registeremail=models.EmailField()
    registerpass=models.CharField(max_length=8)

    def __str__(self):
        return self.registername

class Adminregistration(models.Model):
    adminregistername=models.CharField(max_length=100)
    adminregisteremail=models.EmailField()
    adminregisterpass=models.CharField(max_length=8)

    def __str__(self):
        return self.adminregistername

class Staffuser(models.Model):
    staffname=models.CharField(max_length=100)
    staffemail=models.EmailField()
    staffpassword=models.CharField(max_length=8)
    staffuserrole=models.CharField(max_length=50)
    custumefield=models.CharField(max_length=50)

    def __str__(self):
        return self.staffname

class Productservice(models.Model):
    productservicename=models.CharField(max_length=100)
    sku=models.CharField(max_length=100)
    productservicedescription=models.CharField(max_length=100)
    saleprice=models.CharField(max_length=50)
    purchaseprice=models.CharField(max_length=50)
    producttax=models.CharField(max_length=50)
    productcatagories=models.CharField(max_length=100)
    productunit=models.CharField(max_length=50)
    producttype=models.CharField(max_length=50)
    productcustomefield3=models.CharField(max_length=100)

    def __str__(self):
        return self.productservicename


class Managecustomer(models.Model):
    cusname=models.CharField(max_length=100)
    cusnumber=models.CharField(max_length=10)
    cusemail=models.EmailField()
    cuspassword=models.CharField(max_length=8)
    cusfield1=models.CharField(max_length=50)
    cusbillname=models.CharField(max_length=50)
    cusbillcountry=models.CharField(max_length=50)
    cusbillstate=models.CharField(max_length=50)
    cusbillcity=models.CharField(max_length=50)
    cusbillphone=models.CharField(max_length=10)
    cusbilzipcode=models.CharField(max_length=10)
    cusbilladdress=models.CharField(max_length=100)
    shipadrsname=models.CharField(max_length=100)
    shipadrscountry=models.CharField(max_length=50)
    shipadrsstate=models.CharField(max_length=50)
    shipadrscity=models.CharField(max_length=50)
    shipadrsphone=models.CharField(max_length=10)
    shipadrszipcode=models.CharField(max_length=10)
    shipadrsaddress=models.CharField(max_length=100)
    

    def __str__(self):
        return self.cusname

class Managevendor(models.Model):
    vendorname=models.CharField(max_length=100)
    vendornumber=models.CharField(max_length=10)
    vendoremail=models.EmailField()
    vendorpassword=models.CharField(max_length=8)
    vendorfield1=models.CharField(max_length=50)
    vendorbillname=models.CharField(max_length=50)
    vendorbillcountry=models.CharField(max_length=50)
    vendorbillstate=models.CharField(max_length=50)
    vendorbillcity=models.CharField(max_length=50)
    vendorbillphone=models.CharField(max_length=10)
    vendorbillzipcode=models.CharField(max_length=10)
    vendorbilladdress=models.CharField(max_length=100)
    vendorshipadrsname=models.CharField(max_length=100)
    vendorshipadrscountry=models.CharField(max_length=50)
    vendorshipadrsstate=models.CharField(max_length=50)
    vendorshipadrscity=models.CharField(max_length=50)
    vendorshipadrsphone=models.CharField(max_length=10)
    vendorshipadrszipcode=models.CharField(max_length=10)
    vendorshipadrsaddress=models.CharField(max_length=100)
    

    def __str__(self):
        return self.vendorname

class Managebankaccount(models.Model):
    bankusername=models.CharField(max_length=100)
    bankname=models.CharField(max_length=100)
    accountnumber=models.CharField(max_length=20)
    openingbalance=models.CharField(max_length=10000)
    bankcontact=models.CharField(max_length=10)
    bankaddress=models.CharField(max_length=100)

    def __str__(self):
        return self.bankusername

class Managebanktransfer(models.Model):
    fromaccount=models.CharField(max_length=100)
    toaccount=models.CharField(max_length=100)
    transferamount=models.CharField(max_length=20)
    transferdate=models.CharField(max_length=100)
    transferrefrence=models.CharField(max_length=10)
    

    def __str__(self):
        return self.fromaccount

class Invoice1(models.Model):
    invoicecust=models.CharField(max_length=100)
    invoiceissudate=models.CharField(max_length=100)
    invoiceduedate=models.CharField(max_length=100)
    invoicenum=models.CharField(max_length=100)
    catagory=models.CharField(max_length=100)
    invoicerefnum=models.CharField(max_length=100)
    discount=models.CharField(max_length=50)
    psitem=models.CharField(max_length=100)
    psquantity=models.CharField(max_length=100)
    psprice=models.CharField(max_length=100)
    pstax=models.CharField(max_length=100)
    psdis=models.CharField(max_length=100)
    psdescription=models.CharField(max_length=50)

    def __str__(self):
        return self.invoicecust

class Managerevenue(models.Model):
    revenuedate=models.CharField(max_length=100)
    revenueamount=models.CharField(max_length=100)
    revenueaccount=models.CharField(max_length=100)
    revenuecustomer=models.CharField(max_length=100)
    revenuebankaddress=models.CharField(max_length=100)
    revenuecatagory=models.CharField(max_length=100)
    revenuerefrence=models.CharField(max_length=100)

    def __str__(self):
        return self.revenuecustomer

class Managecreditnotes(models.Model):
    creditcustomer=models.CharField(max_length=100)
    creditamount=models.CharField(max_length=100)
    creditdate=models.CharField(max_length=100)
    creditdescription=models.CharField(max_length=100)

    def __str__(self):
        return self.creditcustomer

class Bill(models.Model):
    billvendor=models.CharField(max_length=100)
    billdate=models.CharField(max_length=100)
    billduedate=models.CharField(max_length=100)
    billnum=models.CharField(max_length=100)
    billcatagory=models.CharField(max_length=100)
    billordernum=models.CharField(max_length=100)
    billdiscount=models.CharField(max_length=50)
    billitem=models.CharField(max_length=100)
    billquantity=models.CharField(max_length=100)
    billprice=models.CharField(max_length=100)
    billtax=models.CharField(max_length=100)
    billdis=models.CharField(max_length=100)
    billdescription=models.CharField(max_length=50)

    def __str__(self):
        return self.billvendor

class Managepayment(models.Model):
    paymentdate=models.CharField(max_length=100)
    paymentamount=models.CharField(max_length=100)
    paymentaccount=models.CharField(max_length=100)
    paymentvendor=models.CharField(max_length=100)
    paymentbankaddress=models.CharField(max_length=100)
    paymentcatagory=models.CharField(max_length=100)
    paymentref=models.CharField(max_length=100)

    def __str__(self):
        return self.paymentvendor

class Managedebitnotes(models.Model):
    debitbill=models.CharField(max_length=100)
    debitamount=models.CharField(max_length=100)
    debitdate=models.CharField(max_length=100)
    debitdescription=models.CharField(max_length=100)

    def __str__(self):
        return self.debitbill

#Superadmin-user

class Managesuperuser(models.Model):
    superusername=models.CharField(max_length=100)
    superuseremail=models.EmailField()
    superuserpassword=models.CharField(max_length=8)
    superuserrole=models.CharField(max_length=50)
    supercustumefield=models.CharField(max_length=50)

    def __str__(self):
        return self.superusername

#superadmin-plan

class Plan(models.Model):
    planname=models.CharField(max_length=100)
    planprice=models.CharField(max_length=1000)
    planduration=models.CharField(max_length=500)
    maxiuser=models.CharField(max_length=1000)
    maxicustomer=models.CharField(max_length=1000)
    maxivendor=models.CharField(max_length=1000)
    plandescription=models.CharField(max_length=100)

    def __str__(self):
        return self.planname

#superadmin-coupon

class Coupon(models.Model):
    couponname=models.CharField(max_length=100)
    coupondiscount=models.CharField(max_length=1000)
    couponlimits=models.CharField(max_length=500)
    code=models.CharField(max_length=100)
    coupondescription=models.CharField(max_length=1000)

    def __str__(self):
        return self.couponname