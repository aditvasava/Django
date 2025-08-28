from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

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
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    # db_index is used behind the scenes to optimize the db when doing read operations
    # we know that slug will be used a lot for rendering book_detail page, so we can set this parameter which will store the slugs in more
    # efficient manner, however don't set many columns as db_index as that will increase the time it takes to insert data, as for every new row
    # added, the db has to make internal adjusments for creating indexes (sorting)
    slug = models.SlugField(default="", null=False, db_index=True) # Harry Potter 1 => harry-potter-1

    # there is also another setting "blank=True" which can be used in replacement of "null=True"

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    # before we save the data to the db, this function gets executed and it creates the slug based on the title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # This method is used to view the data when running command from the shell. 
    def __str__(self):
        return f"{self.title} ({self.rating})"