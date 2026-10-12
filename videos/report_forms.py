from django import forms


class ReportForm(forms.Form):
    reason = forms.ChoiceField(choices=[
        ("spam", "Spam"),
        ("copyright", "Copyright"),
        ("misleading", "Misleading content"),
        ("abusive", "Abusive language"),
        ("other", "Other"),
    ])
    note = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}), required=False)
