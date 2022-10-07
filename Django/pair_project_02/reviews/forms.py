from django.forms import ModelForm, NumberInput
from .models import Reviews


class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = "__all__"
        widgets = {
            "grade": NumberInput(
                attrs={
                    "maxlength": "1",
                    "max": "5",
                    "min": "1",
                }
            ),
        }
