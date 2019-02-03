from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *
from .constants import *
from django.forms import BaseModelFormSet


class AddStudentForm(forms.Form):
    stud_username = forms.CharField(max_length=50)
    stud_password = forms.CharField(max_length=100)
    dob = forms.DateField(required=False)
    stud_fname = forms.CharField(max_length=50, label="Firstname")
    stud_sname = forms.CharField(max_length=50, label="Surname")
    stud_oname = forms.CharField(max_length=50, required=False, label="Othername")
    stud_religion = forms.CharField(widget=forms.Select(choices=RELIGION),max_length=14, 
        label="Religion", required=False)
    stud_address = forms.CharField(max_length=200,label="Address", required=False)
    stud_class = forms.CharField(max_length=20, label="Class")
    stud_gender = forms.CharField(widget=forms.Select(choices=GENDER), label="Gender" , required=False)
    stud_state = forms.CharField(max_length=100, label="State", required=False)
    stud_email = forms.EmailField(required=False, label="Student Email Address")
    stud_lga = forms.CharField(max_length=150, label="Local Govt.", required=False)
    stud_blood_group = forms.CharField(max_length=2, label="Blood Group", required=False)
    stud_roll_number = forms.CharField(max_length=50, label="Roll number")
    stud_phone_number = forms.CharField(max_length=15, label="Phone number", required=False)
    stud_year_of_admission = forms.CharField(max_length=4, label="Year of admission", required=False)
    parent_username = forms.CharField(max_length=50, label="Parent username", required=False)
    parent_password = forms.CharField(max_length=100, label="Parent password", required=False)
    parent_fname = forms.CharField(max_length=50, label="Parent firstname", required=False)
    parent_sname = forms.CharField(max_length=50, label="Parent surname", required=False)
    parent_oname = forms.CharField(max_length=50, label="Parent othername", required=False)
    parent_phone_number = forms.CharField(max_length=15, label="Parent Phone number", required=False)
    parent_state = forms.CharField(max_length=50, label="Parent state of origin", required=False)
    parent_address = forms.CharField(max_length=200, label="Parent Address", required=False)
    parent_email = forms.EmailField(required=False, label="Parent email address")
    parent_lga = forms.CharField(max_length=30, required=False, label="Parent Local Govt.")

    stud_picture = forms.ImageField(required=False, label="Student picture")
    parent_picture = forms.ImageField(required=False, label="Parent picture")

    existing_parent = forms.CharField(max_length=100, required=False, label="Existing parent")