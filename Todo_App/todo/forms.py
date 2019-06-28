from django import forms

class TodoForm(forms.Form):
    todo_text = forms.CharField(max_length=30,
    widget = forms.TextInput(
    attrs={'class':'form-control', 'placeholder':'Enter todo e.g. Delete junk files', 'aria-label':'Todo', 'aria-describedby': 'add-btn' }))


    
