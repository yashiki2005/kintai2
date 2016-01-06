def index():
    if auth.user: redirect(URL('home'))
    return locals()

def user():
    return dict(form=auth())

def kintai():
	return db.kintai
	
def intime():
	import datetime
	now = datetime.datetime.now()
	t = now.strftime("%Y-%m-%d")
	n = now.strftime("%H:%M:%S")
	id = db.kintai.insert(userid=auth.user.email,dateoftoday=t,intime=n,outtime=n,nippo="特に無し")
	redirect(URL('home'))
   
def outtime():
	import datetime
	now = datetime.datetime.now()
	t = now.strftime("%Y-%m-%d")
	n = now.strftime("%H:%M:%S")
	s1 = (db.kintai.userid==auth.user.email) & (db.kintai.dateoftoday==t)
	rows = db(s1).select(db.kintai.ALL)
	#db.kintai[t].update(outtime=n)
	redirect(URL('home'))

def download():
    return response.download(request,db)

def call():
    session.forget()
    return service()

# our home page, will show our posts and posts by friends
@auth.requires_login()
def home():
    return locals()


