from flask_script import Manager
from myResume2 import app, db, Professor, Course

manager = Manager(app)


# reset the database and create some initial data
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    p1 = Professor(name='Hartono', department='MIS')
    p2 = Professor(name='Harry', department='MIS')
    p3 = Professor(name='Robin', department='ENTI')
    course1 = Course(course_number='MISY225', title='Introduction to Programming Business Applications', description="Use of higher level contemporary computing languages to structure Prototyping applications of systems. PREREQ: MISY160", professor=p1)
    course2 = Course(course_number='MISY350', title='Business Application Development II', description="This course Covers concepts related to client side development. PREREQ: MISY225", professor=p2)
    course3 = Course(course_number='ENTR458', title='App Development for New Technology', description="Presents frameworks for developing commercially feasible applications of new technology.", professor=p3)
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
