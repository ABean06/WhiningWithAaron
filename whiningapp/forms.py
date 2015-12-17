from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, validators, SelectField


# Form for Wine Tasting
class WineForm(Form):
    # List of wine color, used for dropdown menu - red or white
    wine_color = [(""), ("Red"), ("White")]
    # List of wine sweetness, used for dropdown menu - sweet, semi-dry, or dry
    wine_sweetness = [(""), ("Sweet"), ("Semi-dry"), ("Dry")]
    # Rank how the wine tasted, used for dropdown menu
    # May give error if don't have ie ("Ehh","Ehh") which is ("submitted", "displayed")
    wine_taste = [(""), ("Hated It!"), ("Didn't like it"), ("Ehh"), ("Okay"), ("Good"),
                  ("Really Good"), ("I'll take a case")]
    # Type of wine tasted.  Example Pinot
    wine_type = StringField("Type (Example: Pinot) *", [validators.DataRequired("Please enter the wine type.")])
    # Name of wine tasted.
    wine_name = StringField("Name *", [validators.DataRequired("Please enter the name of the wine.")])
    # Vintage of wine tasted.
    wine_vintage = StringField("Vintage *", [validators.DataRequired("Please enter the vintage of the wine.")])
    # Country of wine tasted.
    wine_country = StringField("Country *", [validators.DataRequired("Please enter the wine's country of origin.")])
    # State of wine tasted.
    wine_state = StringField("State *", [validators.DataRequired("Please enter the wine's state of origin.")])
    # Vineyard of wine tasted.
    wine_vineyard = StringField("Vineyard *", [validators.DataRequired("Please enter the wine's vineyard  of origin.")])
    # Comments section.  Expandable text field to enter any comments.  Not required.
    wine_comments = TextAreaField("Any comments or additional notes?")
    # Submit form.
    submit = SubmitField("Submit My Review")


# Form for Scotch Tasting
class ScotchForm(Form):
    # List of wine type, used for dropdown menu - Single Malt or Blended
    scotch_type = [(""), ("Single Malt"), ("Blended")]
    # List of scotch strengty, used for dropdown menu - Is it harsh when it goes down
    scotch_strength = [(""), ("Very Strong"), ("Strong"), ("Not too bad"), ("Smooth"), ("Very Smooth")]
    # Rank how the scotch tasted, used for dropdown menu
    # May give error if don't have ie ("Ehh","Ehh") which is ("submitted", "displayed")
    scotch_taste = [(""), ("Hated It!"), ("Didn't like it"), ("Ehh"), ("Okay"), ("Good"),
                    ("Really Good"), ("I'll take a case")]
    # Name of scotch tasted.
    scotch_name = StringField("Name *", [validators.DataRequired("Please enter the name of the scotch.")])
    # Years scotch was aged.
    scotch_age = StringField("Vintage *", [validators.DataRequired("Please enter the age of the scotch.")])
    # Country of scotch tasted.
    scotch_country = StringField("Country *", [validators.DataRequired("Please enter the scotch's country of origin.")])
    # Flavor of scotch tasted.  Smokey, flowery, citrus etc.
    scotch_flavor = StringField("State *", [validators.DataRequired("Please enter the wine's state of origin.")])
    # Comments section.  Expandable text field to enter any comments.  Not required.
    scotch_comments = TextAreaField("Any comments or additional notes?")
    # Submit form.
    submit = SubmitField("Submit My Review")
