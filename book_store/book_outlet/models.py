from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

# One author can have only one address
class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    
    # To change the display name in the /admins/
    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

# every custom class that we define has to import or extend another class which is - models.Model
# a field named "id" that will auto-increment is automatically created.

# If the schema settings is modified or new columns are added, then again do the makemigrations step
# also when doing that, it will prompt in terminal about what to do with existing data in the db that does not have
# any value for the new fields that will be added. so edit the new model and give them some defaults.

# If new method is added to the model, then there is no need to do makemigration
class Book(models.Model):
    title = models.CharField(max_length=50)
    # rating can either be between 1 to 5
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # author = models.CharField(null=True, max_length=100)
    # We set the another model as the data type
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books") # Cascade means if an author is deleted from the db, then delete all the records in the book table which had that author
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, editable=False) # Harry Potter 1 => harry-potter-1
    # db_index is used behind the scenes to optimize the db when doing read operations
    # we know that slug will be used a lot for rendering book_detail page, so we can set this parameter which will store the slugs in more
    # efficient manner, however don't set many columns as db_index as that will increase the time it takes to insert data, as for every new row
    # added, the db has to make internal adjusments for creating indexes (sorting)

    # blank=True & editable=False was added after the admin was set up, as we don't enter values for slug from the UI, this field is set up
    # automatically from the title.

    # there is also another setting "blank=True" which can be used in replacement of "null=True"

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    # before we save the data to the db, this function gets executed and it creates the slug based on the title
    """
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    """

    # This method is used to view the data when running command from the shell. 
    def __str__(self):
        return f"{self.title} ({self.rating})"