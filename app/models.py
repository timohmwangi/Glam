from sqlalchemy import (
    Column, Integer, DateTime, Float, Boolean, Text, 
    ForeignKey, String
)
from flask_login import UserMixin
from sqlalchemy.orm import relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash

# local imports
from .mixins import Model
from .extensions import login_manager


class Users(Model, UserMixin):
    """
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)
    profile_url = Column(String, unique=True)
    password = Column(String, nullable=False)
    authenticated = Column(Boolean(True))

    @login_manager.user_loader
    def load_user(user_id:int):
        """
        """
        return Users.query.get(user_id)

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def is_active(self):
        """True, as all users are active."""
        return True
        
    def set_password(self, password):
        """Set password."""
        self.password = generate_password_hash(password)

    def check_password(self, value:str):
        """Check password."""
        return check_password_hash(self.password, value)

    __mapper_args__ = {
        "polymorphic_identity": "users",
        "polymorphic_on": type
    }


class Client(Users):
    """
    """
    __tablename__ = 'client'
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    client_user = relationship("Users", backref=backref('client', lazy='dynamic'), foreign_keys=[id])

    __mapper_args__ = {
        "polymorphic_identity": "client",
    }


class Spa(Users):
    """
    """
    __tablename__ = 'spa'
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    name = Column(String, nullable=False)
    spa_user = relationship("Users", backref=backref('spa', lazy='dynamic'), foreign_keys=[id])

    __mapper_args__ = {
        "polymorphic_identity": "spa",
    }


class Employee(Users):
    """
    """
    __tablename__ = 'employee'
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    employee_user = relationship("Users", backref=backref('employee', lazy='dynamic'), foreign_keys=[id])

    __mapper_args__ = {
        "polymorphic_identity": "employee",
    }


class Service(Model):
    """
    """
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(Float(2), nullable=False)


class Bookings(Model):
    """
    """
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    booking_time = Column(DateTime(timezone=True), nullable=False)
    
    client = relationship("Client", backref=backref('bookings', lazy='dynamic'))


class ServiceBookings(Model):
    """
    """
    __tablename__ = 'service_bookings'
    booking_id = Column(Integer, ForeignKey('bookings.id'), primary_key=True)
    service_id = Column(Integer, ForeignKey('service.id'), primary_key=True)
    served_by_id = Column(Integer, ForeignKey('employee.id'), nullable=True)
    complete = Column(Boolean, default=False)
    booking = relationship("Bookings", backref=backref('service_bookings', lazy='dynamic'))
    service = relationship("Service", backref=backref('bookings', lazy='dynamic'))
    served_by = relationship("Employee", backref=backref('services_offered', lazy='dynamic'))


class BookingPayments(Model):
    """
    """
    __tablename__ = 'booking_payments'
    id = Column(Integer, primary_key=True)
    amount = Column(Float(2))
    booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=False)
    booking = relationship("Bookings", backref=backref('payment', lazy='dynamic'))


class Testimonial(Model):
    """
    """
    __tablename__ = 'testimonial'
    client_id = Column(Integer, ForeignKey('client.id'), primary_key=True)
    testimonial = Column(Text, nullable=False)
    client = relationship('Client', backref=backref('testimonial', lazy='dynamic'))
