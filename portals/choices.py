from portals.constants import * 
from django.db import models 

class UserChoices(models.TextChoices):
    ADMIN            = ADMIN,ADMIN
    SELLER           = SELLER,SELLER
    BUYER            = BUYER,BUYER


class PriceChoices(models.TextChoices):
    BEGINNER         = BEGINNER,BEGINNER
    INTERMEDIATE     = INTERMEDIATE,INTERMEDIATE
    PRO              = PRO,PRO

class BookingChoices(models.TextChoices):
    PENDING          = PENDING,PENDING
    APPROVED         = APPROVED,APPROVED
    ASSIGNED         = ASSIGNED,ASSIGNED
    ONGOING          = ONGOING,ONGOING
    REFUNDED         = REFUNDED,REFUNDED
    COMPLETED        = COMPLETED,COMPLETED
    CANCELLED        = CANCELLED,CANCELLED
    REJECTED         = REJECTED,REJECTED
    FAILED           = FAILED,FAILED
    RESCHEDULED      = RESCHEDULED,RESCHEDULED













