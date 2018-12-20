from app import db

class TestModel (db.Model):
    status = db.Column(db.Boolean,default=False)
    content = db.Column(db.String(140), index=True)
    title = db.Column(db.String(140), index=True)
    date = db.Column(db.Date)
    Id = db.Column(db.Integer, primary_key=True)    
    def __repr__(self):
        return  self.content + ' ' + self.stauts + ' ' + self.date

 