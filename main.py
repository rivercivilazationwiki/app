# -*- coding: utf-8 -*-
from flask import *
from wtforms import *
from flask_mongoengine import MongoEngine
#from mongoengine import *
#from flask_mongoengine import MongoEngine as me
app = Flask(__name__)
app.url_map.strict_slashes = False
#connect(host="mongodb+srv://root:scram@clusterx.wgjuz.mongodb.net/Md?retryWrites=true&w=majority")
app.config['SECRET_KEY'] = 'codax203040'
app.config['MONGODB_SETTINGS'] = {
    'db': 'Md',
    'host': 'mongodb+srv://root:scram@clusterx.wgjuz.mongodb.net/Md?retryWrites=true&w=majority',
    'username':'root',
    'password':'scram'
}
#db = flask_mongoengine.MongoEngine(app)
class patient(Document):
	name=StringField(max_length=9999999999999)
	immuniazationRecord=StringField(max_length=9999999999999)
	bloodWorks=StringField(max_length=9999999999999)
	age=StringField(max_length=9999999999999)
	sex=StringField(max_length=9999999999999)
	race=StringField(max_length=9999999999999)
	medicins=StringField(max_length=9999999999999)
	symptoms=StringField(max_length=9999999999999)
	healthConditions=StringField(max_length=9999999999999)
	allergies=StringField(max_length=9999999999999)
	doctor=StringField(max_length=9999999999999)
	locationOfCare=StringField(max_length=9999999999999)
	physicalCondition=StringField(max_length=9999999999999)
	ContactInfo=StringField(max_length=9999999999999)
	BillingInfo=StringField(max_length=9999999999999)
	Date=StringField(max_length=9999999999999)
	diagnosis=StringField(max_length=9999999999999)
	purposeOfVisit=StringField(max_length=9999999999999)
	other=StringField(max_length=9999999999999)
@app.route("/")
def home_page():
    return render_template("index.html")
@app.route("/insert", methods=['GET', 'POST'])
def insert():
  if request.method == 'POST':
        name=request.form.get("n")
        immuniazationRecord=request.form.get("ir")
        bloodWorks=request.form.get("bw")
        age=request.form.get("age")
        sex=request.form.get("sex")
        race=request.form.get("race")
        medicins=request.form.get("med")
        symptoms=request.form.get("sympt")
        hcond=request.form.get("hcond")
        allergies=request.form.get("allerg")
        doctoc=request.form.get("doc")
        locationOfCare=request.form.get("loc")
        physicalCondition=request.form.get("phys")
        ContactInfo=request.form.get("pnum")
        BillingInfo=request.form.get("bill")
        Date=request.form.get("d2")
        diagnosis=request.form.get("di")
        purposeOfVisit=request.form.get("p")
        other=request.form.get("other")
        p=patient(name=name,immuniazationRecord=immuniazationRecord,bloodWorks=bloodWorks,age=age,sex=sex,race=race,medicins=medicins,symptoms=symptoms,healthConditions=hcond,allergies=allergies,doctor=doctoc,locationOfCare=locationOfCare,physicalCondition=physicalCondition,ContactInfo=ContactInfo,BillingInfo=BillingInfo,Date=Date,diagnosis=diagnosis,purposeOfVisit=purposeOfVisit,other=other)
        p.save()
        return render_template("index.html")
  else:
      return render_template("M.html")
@app.route("/search")
def search():
    return render_template("S.html")
@app.route("/results/",methods=['POST','GET'])
def result():
    if request.method=='POST':
        nme=request.form.get("n")
        p = patient.objects(name=nme).get()	    
        name=p.name
        immuniazationRecord=p.immuniazationRecord
        bloodWorks=p.bloodWorks
        age=p.age
        sex=p.sex
        race=p.race        
        medicins=p.medicins
        symptoms=p.symptoms
        healthConditions=p.healthConditions
        allergies=p.allergies
        doctor=p.doctor
        BillingInfo=p.BillingInfo
        locationOfCare=p.locationOfCare
        physicalCondition=p.physicalCondition
        ContactInfo=p.ContactInfoBillingInfo=p.BillingInfo
        Date=p.Date   
        diagnosis=p.diagnosis        
        purposeOfVisit=p.purposeOfVisit
        other=p.other
        return render_template("R.html",name=name,immuniazationRecord=immuniazationRecord,bloodWorks=bloodWorks,age=age,sex=sex,race=race,medicins=medicins,symptoms=symptoms,ealthConditions=healthConditions,allergies=allergies,doctor=doctor,locationOfCare=locationOfCare,physicalCondition=physicalCondition,ContactInfo=ContactInfo,BillingInfo=BillingInfo,Date=Date,diagnosis=diagnosis,purposeOfVisit=purposeOfVisit,other=other)
@app.route("/update",methods=['GET','POST'])
def update():
    if request.method=='POST':
        n=request.form.get("n")
        f=request.form.get("f")
        c=request.form.get("c")
        name="name"
        ir="immuniazationRecord"
        bw="bloodWorks"
        age="age"
        sex="sex"
        race="race"        
        med="medicins"
        sympt="symtoms"
        hcond="healthConditions"
        allerg="allergies"
        doc="doctor"
        bill="BillingInfo"
        loc="locationOfCare"
        physn="physicalCondition"
        pnum="ContactInfo"
        Date="Date"   
        di="diagnosis"        
        p="puroseOfVisit"
        other="other"
        if f==name:
            patient.objects(name=n).updateone(name=c)
        elif f==ir:
            patient.objects(name=n).updateone(immuniazationRecord=c)
        elif f==bw:
            patient.objects(name=n).updateone(bloodWorks=c)
        elif f==age:
            patient.objects(name=n).update(age=c)
        elif f==sex:
            patient.objects(name=n).update(sex=c)
        elif f==race:
            patient.objects(name=n).update(race=c)
        elif f==med:
            patient.objects(name=n).update(medicins=c)
        elif f==sympt:
            patient.objects(name=n).update(symptoms=c)
        elif f==hcond:
            patient.objects(name=n).update(healthConditions=c)
        elif f==allerg:
            patient.objects(name=n).update(allergies=c)
        elif f==doc:
            patient.objects(name=n).update(doctor=c)
        elif f==loc:
            patient.objects(name=n).update(locationOfCare=c)
        elif f==phys:
            patient.objects(name=n).update(physicalCondition=c)
        elif f==bill:
            patient.objects(name=n).update(BillingInfo=c)
        elif f==date:
            patient.objects(name=n).update(date=c)
        elif f==di:
            patient.objects(name=n).update(diagnosis=c)
        elif f==p:
            patient.objects(name=n).update(purposeOfVisit=c)
        elif f==other:
            patient.objects(name=n).update(other=c)
        return render_template("index.html")          
    return render_template("U.html")
@app.route("/delete/",methods=['GET','POST'])
def delete():
    if request.method=='POST':
        n=request.form.get('n')
        p=patient.objects(name=n)
        p.delete()
        return render_template("index.html")
    return render_template("Res.html")


if __name__=='__main__':
    app.run(host= '0.0.0.0', port=5000)

