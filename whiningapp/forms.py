from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, validators, SelectField


# Form for Wine Tasting
class WineForm(Form):
    # Name of wine tasted.
    wine_name = StringField("Name *", [validators.DataRequired("Please enter the name of the wine.")])
    # Country of wine tasted.
    wine_country = StringField("Country *", [validators.DataRequired("Please enter the wine's country of origin.")])
    # State of wine tasted.
    wine_state = StringField("State *", [validators.DataRequired("Please enter the wine's state of origin.")])
    # Vineyard of wine tasted.
    wine_vineyard = StringField("Vineyard *", [validators.DataRequired("Please enter the wine's vineyard  of origin.")])
    # Type of wine tasted.  Example Pinot
    wine_type = StringField("Type (Example: Pinot) *", [validators.DataRequired("Please enter the wine type.")])
    # Vintage of wine tasted.
    wine_vintage = StringField("Vintage *", [validators.DataRequired("Please enter the vintage of the wine.")])
    # First choice is what is displayed.  Second is what app uses - ie display Arizona, but form uses AZ
    # Example could also be inventory.  Display could be apples, that item number in my inventory could be 3
    # Color Choices
    wine_color_choices = [("", ""), ("Red", "Red"), ("White", "White")]
    # List of wine color, used for dropdown menu
    wine_color = SelectField("Choose Wine Color ", choices=wine_color_choices)
    # Sweetness Choices
    wine_sweetness_choices = [("",""), ("Sweet", "Sweet"), ("Semi-dry", "Semi-dry"), ("Dry", "Dry")]
    # List of wine sweetness, used for dropdown menu
    wine_sweetness = SelectField("Choose Wine Sweetness", choices=wine_sweetness_choices)
    # Wine flavor profile
    wine_flavor = StringField("Flavor *", [validators.DataRequired("Please enter the wine's state of origin.")])
    # Comments section.  Expandable text field to enter any comments.  Not required.
    wine_comments = TextAreaField("Any comments or additional notes?")
    # wine rating choices
    wine_rating_choices = [("", ""), ("Hated It!", "Hated It!"), ("Didn't like it", "Didn't like it"),
                           ("Ehh", "Ehh"), ("Okay", "Okay"), ("Good", "Good"), ("Really Good", "Really Good"),
                           ("I'll take a case", "I'll take a case")]
    # Rank how the wine tasted, used for dropdown menu
    wine_rating = SelectField("Rate the Wine", choices=wine_rating_choices)
    # Submit form.
    submit = SubmitField("Submit My Review")


# Form for Scotch Tasting
class ScotchForm(Form):
    # Name of scotch tasted.
    scotch_name = StringField("Label *", [validators.DataRequired("Please enter the name of the scotch.")])
    # Years scotch was aged.
    scotch_age = StringField("Age *", [validators.DataRequired("Please enter the age of the scotch.")])
    # Region Choices.
    scotch_region_choices = [("", ""), ("Islay", "Islay"), ("Highland", "Highland"), ("Lowland", "Lowland"),
                             ("Speyside", "Speyside"), ("Island", "Island")]
    # Region of Scotch Tasted
    scotch_region = SelectField("Region", choices=scotch_region_choices)
    # Scotch Type Choices
    scotch_type_choices = [("", ""), ("Single Malt", "Single Malt"), ("Blended", "Blended")]
    # List of scotch type, used for dropdown menu - Single Malt or Blended
    scotch_type = SelectField("Choose Scotch Type", choices=scotch_type_choices)
    # Smoothness choices
    scotch_smoothness_choices = [("", ""), ("Very Strong", "Very Strong"), ("Strong", "Strong"),
                                 ("Not too bad", "Not too bad"), ("Smooth", "Smooth"), ("Very Smooth", "Very Smooth")]
    # List of scotch strength, used for dropdown menu - Is it harsh when it goes down
    scotch_smoothness = SelectField("Select Smoothness", choices=scotch_smoothness_choices)
    # Flavor of scotch tasted.  Smokey, flowery, citrus, toffee, caramel
    scotch_flavor = StringField("Flavor *", [validators.DataRequired("Please enter the wine's state of origin.")])
    # Comments section.  Expandable text field to enter any comments.  Not required.
    scotch_comments = TextAreaField("Any comments or additional notes?")
    # Rating Choices
    scotch_rating_choices = [("", ""), ("Hated It!", "Hated It!"), ("Didn't like it", "Didn't like it"),
                             ("Ehh", "Ehh"), ("Okay", "Okay"), ("Good", "Good"), ("Really Good", "Really Good"),
                             ("I'll take a case", "I'll take a case")]
    # Scotch Rating
    scotch_rating = SelectField("Rate the scotch", choices=scotch_rating_choices)
    # Submit form.
    submit = SubmitField("Submit My Review")
