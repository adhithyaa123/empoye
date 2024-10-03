from django import forms

class EmployeeForm(forms.Form):

    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    designation=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    department=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    contact=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    address=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))


    def clean(self):

                cleaned_data=super().clean()

                salary=cleaned_data.get("salary")

                if int(salary)>100000 or int(salary)<50000:

                    error_message="salary should be in the range of 50000 and 100000"

                    self.add_error("salary",error_message)
