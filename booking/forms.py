from django import forms


class SearchRoom(forms.Form):
    dates = forms.DateField(label='Check in - Check out', widget=forms.DateInput(attrs={'class': 'form-control mr-sm-2',
                                                                                        'name': 'dates'}))
    NUM_PEOPLE = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('family', 'Family'),
    )
    capacity = forms.ChoiceField(choices=NUM_PEOPLE, widget=forms.Select(attrs={'class': 'form-control mr-sm-2'}),
                                 label='Person')
    # Check_out = forms.DateField(widget=forms.DateInput(attrs={'class' : 'form-control mr-sm-2', 'name':'dates'}))
