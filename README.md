# Molten Java

![Heading Responsive image](testing/homepage.jpg)

[View the Live website here](https://jay359-molten-java.herokuapp.com/)


### Molten Java is the ficticious business website of Molten Java.

Molten java is a fictitious coffee shop and coffee roasters business in cork city.
This website serves as en e-commerce platform for the business, as well as being a social point of contact with existing and potential customers.

## UX

### This website is for:

* Visitors to the website are ideally coming to purchase coffee and coffee accessories from the business, but the interesting blog posts and opportunity to sign up for update emails may also make it a more informational social resource also.

### User Stories

* As a visitor to this website, I would like the navagation to be instantly understandable.
* As a visitor I would like an inventory of stock to browse through.
* As a visitor I would like the ability to search for products by name.
* As a visitor I would like the ability to register for an account for secure purchasing.
* As a visitor I would like an email sign up option, to be kept up to date with site news.
* As a visitor I would like the option to follow the site on social media platforms.
* As a visitor I would like the ability to comment on the blog posts I have read.

* As a menber of the website, I would like to 'Login' to my profile and view past purchases.
* As a member of the website, I would the ability to manage and update my shipping and payment details.
* As a member of the website, I would like to be able to read reviews and review products myself.

* As an Admin of the website, I would like all of the above capabilities, but also the ability to add categories of products and the products themselves to the website, including price ratings and images, and the ability to delete reviews and blog comments which may be inappropriate or not in keeping with the sites ethos.

## Design

![color Scheme](wireframes/Color-Scheme.jpg)

* Colors - The entire site is rendered in contemporary tones of black, charcoal, gold and white, This was a considered design choice to reflect the tones of other contemporary coffee brands, which suit the product quite well.

* Font - The font I have used for the site is [Roboto](http://fonts.google.com/specimen/Roboto), this font covers all text elements, I selected this font because of its versatility, in that it is modern, but also clear and bold in its various weights.

* Icons - The Icons used in this project are taken from [Font Awesome](https://fontawesome.com/), which hosts a diverse set of options.

### Wireframes

* [Homepage](wireframes/homepage.pdf)
* [Products page](wireframes/products.pdf)
* [Single product page](wireframes/single-product.pdf)
* [Blog Homepage](wireframes/blog-home.pdf)
* [Blog article view](wireframes/blog-article.pdf)

## Features

* The navagation and footer with sign up extend across all pages.

### Home page 

* The Home page features a full screen 'hero image' which makes it very clear what the focus of the site will be.
* Overlaying the image is a welcome slogan plus a button, which lets the visitor go straight to the coffee page.
* A centered card features an image of a new coffee product with a link to go to that products page.

### Shop Coffee - Pages 
* This tab has several coffee product categories, once selected the user is brought to a gallery type page where products can be viewed and clicked on to view more information about them.

### Accoutrements - Pages 
* This tab also has several product categories for brewing products and molten java merchandise. As before once selected the user is brought to gallery pages where the products can be viewed in detail.

### All Products 
* This tab is a way of viewing all the products together, organised by different criteria, price, name etc.

### Product Reviews
* On accessing an individual product details, a user has the opportunity to leave a star rating and a review of that product. The user needs to be registered and logged in to access this facility.

### Blog - Page
* This tab brings you directly to the blog page, where blog posts can be seen in chronological order.
* On accessing the individual blog posts a user is also give the opportunity to comment on that post. the user does not need to be logged in to do this.

### My Account 
* This clickable link will bring the user , to the login, logout and register options, if the user has admin privileges there will also be a product managment link.

### Page Footer
* This area consists of an email sign up form and social media links.
* On entering an email address and submitting it, an email is sent to a gmail address I have setup (moltenjava21@gmail.com), requesting to join the mailing list.
* Several clickable icons for social media sites will take you to those sites.

### Admin CRUD functionality

* An Admin user has full control of all content on the site, such as:
* adding and editing/deleting new products and categories of products.
* adding and editing/deleting blog posts.
* adding and editing/deleting blog post comments.
* adding and editing/deleting product reviews.
* The ability to delete users profiles completly.

## Features left to add
* In the coffee products page a dropdown option is there for three different size of bags, and although the size is stored in the checkout, the price for each size is the same, which would obviously not be ideal in a real world situation, so in the future a product/size/price model could be made to fix this. I unfortunately didn't have the time to figure it out.
* I was also going to add the option for the customer to choose the type of grind for their selected coffee beans, this I also didn't have time to implement, and removed the option from the finished website, but the option still exists in the 'django admin' page.

## Technologies Used

### Languages uses

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://www.python.org/)
* [Jquery](https://jquery.com/)

### Frameworks, libraries etc.

* [Gitpod](https://gitpod.io/) - Developer environment was used to write the code.
* [Github](https://github.com/) - Used to host the project.
* [Heroku](https://heroku.com/) - Used to deploy the finished project.
* [Bootstrap](https://getbootstrap.com/) - Used for responsive grid system, utilizing components for navagation, cards and forms etc.
* [Django](https://www.djangoproject.com/) - Used as the backbone of the project with front and backend utilities.
* [Stripe](https://stripe.com/) - Used for handling the payments on the site.
* [Amazon Web Servies](http://aws.amazon.com/) - Cloud platform for hosting static and media files.
* [emailJs](https://www.emailjs.com/) - Used to foward email from email sign up in footer.
* [Google Fonts](https://fonts.google.com/) - Used for the websites various fonts.
* [Font Awsome](https://fontawesome.com/) - The Font Awesome library was used for the icons the website.
* [favicon.io](favicon.io) - Was used to create the favicon for the browser tab.
* [TinyJPG](https://tinyjpg.com/) - Used to compress the websites images.
* [Balsamiq](https://balsamiq.com/) - Used to create wireframes.

### Database
* All products, categories, blog posts were added to the site using the Django admin 

## Testing
* Details can be found in a separate [Testing](testing.md) page.

## Deployment

### Local Deployment
The website was built using [Gitod](https://gitpod.io), its code was then pushed to [Github](https://github.com) for version control and from there was pushed to [Heroku](https://heroku.com) to host the live site.

To clone the project: 

1. From the application's repository, click the "code" button and download the a zip file containing the repository.
    Alternatively, you can clone the repository using the following line in your terminal:

    ``` 
    git clone https://github.com/jaydavis359/Molten-Java.git
    ``` 

1. Access the folder in your terminal and install the application's [required dependencys](https://github.com/jaydavis359/Molten-Java/blob/39f67b6dba1d8021d06194af3f54550c16da858d/requirements.txt) using the following command:

    ```
    pip3 install -r requirements.txt
    ```

1. In your IDE, create a file containing your environmental variables called env.py at the root level of the application. 
    It will need to contain the following lines and variables:
    ```
    import os

    os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
    os.environ["DEVELOPMENT"] = "True"

    os.environ["DEFAULT_FROM_EMAIL"] = 'DEFAULT_FROM_EMAIL'

    os.environ["STRIPE_PUBLIC_KEY"] = "STRIPE_PUBLIC_KEY"
    os.environ["STRIPE_SECRET_KEY"] = "STRIPE_SECRET_KEY"
    os.environ["STRIPE_WH_SECRET"] = "STRIPE_WH_SECRET"
    os.environ["STRIPE_CURRENCY"] = "EUR"

    ```
    
    The stripe variables can be located at [Stripe](https://stripe.com/)

    Ensure that env.py is added to your .gitignore file when pushing to an open public repository.

1. Migrate the database models with the following command
    ```
    python3 manage.py migrate
    ```
1. Create a superuser and set up the credentials with the following command
    ```
    python3 manage.py createsuperuser
    ```
1. Run the app with the following command
    ```
    python manage.py runserver
    ```
    The address to access the website is displayed in the terminal  
    Add /admin to the end to access the admin panel with your superuser credentials

## Heroku Deployment

1. Setuo or Login to your Heroku account and create a new app. Choose your region. 
1. Once the app is created click on the resources button and under Add-ons, look for the Heroku Postgres to attach a postgres database to your project.
    Select the Hobby Dev - Free plan and click Submit

1. Scroll back up and click "settings". Scroll down and click "Reveal config vars". Set up the same variables as in your env.py ():
    !You shouldn't set the DEBUG variable in under config vars, only in your env.py to prevent DEBUG being active on live website. 

    ```
    AWS_ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"
    AWS_SECRET_ACCESS_KEY = "AWS_SECRET_ACCESS_KEY"
    AWS_S3_REGION_NAME = "AWS_S3_REGION_NAME"
    AWS_STORAGE_BUCKET_NAME = "AWS_STORAGE_BUCKET_NAME"
    USE_AWS = True
    
    DATABASE_URL = "This variable is automatically set when adding the Postgres Add on"

    SECRET_KEY = "SECRET_KEY"

    STRIPE_PUBLIC_KEY = "STRIPE_PUBLIC_KEY"
    STRIPE_SECRET_KEY = "STRIPE_SECRET_KEY"
    STRIPE_WH_SECRET = "STRIPE_WH_SECRET"
    STRIPE_CURRENCY = EUR

    DEFAULT_FROM_EMAIL = "DEFAULT_FROM_EMAIL"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_PASS = "EMAIL_HOST_PASS"
    EMAIL_HOST_USER = "EMAIL_HOST_USER"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    ```
1. From this screen, copy the value of DATABASE_URL
1. After this go to your settings.py the 'molten java' main directory and comment out the default database configuration and add:
    ```
    DATABASES = {
        'default': dj_database_url.parse('Put your DATABASE_URL here'))
    }
    ```
1. Migrate again with the following command
    ```
    python3 manage.py migrate
    ```


1. Create a superuser for the postgres database so you can have access to the django admin by setting up the credentials with the following command
    ```
    python3 manage.py createsuperuser
    ```

1. Load the data into your newly created database by using the following command: 

    ```
    python3 manage.py loaddata <name of file containing the data *>
    ``` 

1. After migrations are complete, change database configurations to:
```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
```
This will allow your site to use Postgres in deployment and sqlite3 in development.


1. Get uour requirements.txt file and your Procfile. To do this:
    Requirements:
    ```
    pip3 freeze --local > requirements.txt
    ```
    Procfile:
    ```
    echo web: python app.py > Procfile
    ```
1. The Procfile should contain the following line:
    ```
    web: gunicorn <project_name>.wsgi:application

    ```

1. Add your files and commit them to GITHUB by running the following commands:
    ```
    git add . 
    git commit -m "Your commit message"
    git push
    ```

1. Add your Heroku app URL to ALLOWED_HOSTS in your settings.py file
1. Disable collect static so that Heroku doesn't try to collect static files when you deploy by typing the following command in the terminal
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1
    ```
1. Go back to HEROKU and click "Deploy" in the navigation. 
1. Scroll down to Deployment method and Select Github. 
1. Look for your repository and click connect. 
1. Under automatic deploys, click 'Enable automatic deploys'

1. Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.
1. In order to commit your changes to the branch, use git push to push your changes. 

### AWS Static File Storage

1. Store your static files and media files on [Amazon Web Services](https://aws.amazon.com/)

1. Set up email service to send confirmation email and user verification email to the users. You can do this by following the next steps (Gmail only)

* Go to your email account and go to your account settings
* Under Security, scroll down to sign in to Google and make sure 2 step verification is turned on
* Under the same heading you will see the 'App passwords' option.
* Click on the option, select mail for the app and under device type select other and fill in 'Django'
* You will now get a password which you should copy and set it as a config variable in Heroku:

```
    EMAIL_HOST_PASS = 'Password you just copied'
    EMAIL_HOST_USER = 'Your gmail account
```
* Go to your settings.py in the molten java directory and add the following:

```
    if "DEVELOPMENT" in os.environ:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_USE_TLS = True
        EMAIL_PORT = 587
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
```


## Credits

* [W3Schools](https://www.w3schools.com/) and [Stack Overflow](https://stackoverflow.com/) for all kinds of help during the project.
* Youtube channel[Code with stein](https://www.youtube.com/c/CodeWithStein/) For help with the logic for product reviews and blog comments

### Images

* Images were taken from [unsplash](https://unsplash.com/).
  - Home page cover image which extends across the website by 🇸🇮 Janko Ferlič on unsplash.
  - Image in about section of homepage by rawkkim on unsplash
* Product images were taken from their various companies websites.

## This website is for educational purposes only.
=======
