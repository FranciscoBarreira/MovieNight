## Movie Night

------

Movie Night is an e-commerce platform centered around movies, tv shows and documentaries.It includes the ability to sign up for newsletters, make suggestions via an in-site form and uses stripe payment. This platform was fully developed in Django.


The link to the deployed website can be found [here.](https://movienight2022.herokuapp.com/)

The link to the Github repository can be found [here.](https://github.com/FranciscoBarreira/MovieNight/)


![mockup site generator image](/media/mockup.png "mockup preview")

## Table of Contents 

[User Experience](#user-experience)

   
   - [User Stories](#user-stories)

[Design](#design)   

   - [Images](#images)
   - [Colour Scheme](#colour-scheme)
   - [Fonts](#fonts)

[Business Model](#business-model) 

[Keywords](#keywords) 

[Technologies Used](#technologies-used) 

[Wireframes](#wireframes) 

[Data Model](#data-model) 

[Features](#features)   

   - [Home Page](#home-page)
   - [Products Page](#products-page) 
   - [Product Detail](#product-detail)
   - [Bag](#bag)
   - [Checkout](#checkout)  
   - [Order Confirmation](#order-confirmation)
   - [Product Management](#product-management)
   - [Profile](#profile)
   - [About Us](#about-us)
   - [Contacts](#contacts)
   - [Newsletter](#newsletter)
   - [Suggestion](#suggestion)
   - [Facebook page](#facebookpage)
   - [Future Features](#future-features)    


[Testing](#testing)   

   - [General Testing](#general-testing)
   - [Validator Testing](#validator-testing)
   - [Responsiveness Testing](#responsiveness-testing)

[Bugs and Issues](#bugs-and-issues) 

[Site Deployment](#site-deployment) 

[Credits](#credits)   

   - [Media](#media)
   - [Content](#content)
   - [Acknowledgements](#acknowledgements)  
  


## User Experience 
<a name="user-experience"></a>

------


### User Stories
 <a name="user-stories"></a>

In order to better organize the workflow using agile tools, a series of epics were created, each containing multiple user stories. The repositoty including the labels(epic+must have/nice to have) can be found [here.](https://github.com/FranciscoBarreira/MovieNight/projects/1)

Epic - Acoount

- Login : As a user I can login so that I can access my profile.
- Sign Up : As a user I can sign up for a new account so that I can save my information
- Edit Profile: As a user I can change the information on my profile so that it always stays updated.
- Confirmation Email: As a user I can get a confirmation email when I sign up for a new account so I can verify it.
- Set up a new password: As a user I can set up a new password so I can access my account if i forget it.
- Create, edit, delete products in admin: As an admin, I can create, edit and delete products so I can manage the site.

Epic - Communication

- Newsletter signup:As a user I can opt in to receive a newsletter from Movie Night so I can view all the latest offers.
- Request a movie: As a user I can request a movie so that it may become available in the store.
- Social Media Links: As a user, I can see all the links to the social media pages so I can follow Movie Night on those platforms.
- Contacts: As a user I can see the contacts both on the contact page and on the footer so I can easily contact Movie Night.
- About Us Section: As a user, I can click on the about us section to learn about movie night, contact them and sign up for the newsletter.
- Suggestions: As a user, I can suggest movies, tv shows and documentaries to Movie Night so I can try to get the products that are unavailable at the moment.

Epic - Shopping

- See Products in Cart : As a user I can see the products so that I know what is currently in the Shopping cart.
- See Shopping Cart Total Value : As a user I can see the total value of the shopping cart so that I know exactly how much I would be spending.
- Secure Payment: As a user I want to be able to proceed to secure checkout so that I feel safe about my personal data.
- Delete Products From Cart: As a user I can delete products from my shopping cart so that the current cart only includes the products I want.
- Order Information: As a buyer, I can access my order information so that I can check if all the details are correct.
- Order Information History: As a user I can access my order information history, so that I have proof of my previous purchases
- Save Profile Details: As an authenticated user, I can save my personal details, so I can have them pre-filled when I make a new order.
- Bag Quantity: As a user I can change the quantities in the bag so that I can adjust it.
- Order Confirmation Details: As a user, I can receive a confirmation email containing order information so I can use it as a proof of transaction.

Epic - Site Navigation

- Product Detail : As a user I can see the product detail page so that I can see all available information for that product.
- Ratings : As an authenthicated user, I can see a product's rating so that I can make an informed choice.
- Product List: As a user I can view a list of products so that I can browse through them,
- Filter Products: As a user, I can filter products by price, rating and category so that discovery is made easier.
- Site Navigation: As a user I can easily navigate the website so that I can always find the products or pages I want.
- Search Bar: As a user I can search for a specific term so that I can find exactly what i am looking for: As an admin, I can create, edit and delete products so I can manage the site.

The Following user stories were set as 'to be added later' as they did not make the final project:

- Rate Products: As a user I can rate products so that i can leave a review.
- Favourite Products: As an authenticated user, I can add a product to my list so that i can have easy access to my favourite products.
- Movie Editions: As a user, I can select an edition (dvd, bluray or 4k) so I can decide which to buy

## Design
 <a name="design"></a>

 ------

### Images 
<a name="images"></a>


All the images used in the blog were taken from other websites, including:

- Unsplash.com
- IMDB (movie covers)

### Colour Scheme 
<a name="colour-scheme"></a>

The colour scheme chosen for the site can be seen below:

![colour palette image image](/media/palette.png "colour palette")



- Additionally , Black is used for text as it improves readibility over the dark grey.


### Fonts 
<a name="fonts"></a>

Cinzel is used for the logo as it stands out from regular fonts and gives a nice touch to the website. The rest of the text is in Roboto, a font that improves readability.


## Business Model
<a name="business-model"></a>

------


Movie Night is an exclusively online B2C shop that focus on the selling of entertainment in the form of movies, tv shows and documentaries. 

Obviously understanding the difficulty that physical media is in right now, we have a section in the About Us explaining why physical ownership is so important to the preservation of art. Additionally, movie buffs are quite the collectors so there is still a demand for physical media in this area. 

Communication is always vital for an healthy business, which is why we encourage our users to get in touch with us and to even make suggestions of products they would like to see added to the store.

Another key part of the business is getting users to sign up for Movie Night's newsletter. That way, they can be engaged regularly with brand new offers, discounts and latest information about upcoming arrivals.

To make the lives of our users easier, Movie Night's website is super intuitive, easy to navigate, and its shop can be accessed from everywhere so potential customers are never far away from the products they want. It's also our obligation to provide them with accurate details such as shipping costs, and to remind them those can be free if they just spend a little bit more. 

To improve our presence on the internet, a Facebook page for Movie Night exists and is updated with all relevant information(photos provided in the features section).



## Keywords
<a name="keywords"></a>

------


To improve Movie Night's online discoverability, a number of keywords were added in the metatags, including:

- movies
- tv 
- tv-series
- tv-shows
- documentaries
- dvd
- blu-ray
- 4k
- comedy
- action
- drama
- sci-fi
- thriller
- horror
- sport
- animation
- musical
- romance
- war
- western
- adventure
- shop
- online
- worldwide
- shipping

Long tail keywords would eventually be added for each movie (according to financial possibilities), i.e: buy Shawshank redemption online.



## Technologies Used
<a name="technologies-used"></a>

------


- HTML

- CSS

- Python

- Django

- GitHub for software hosting

- GitPod for development hosting

- Heroku for project deployment

- Balsamiq for wireframes

- Google fonts to add custom fonts to the website

- Font Awesome for icons

- Bootstrap for quick HTML mobile first design

- AWS storage

- drawsql for the models diagram

- W3C CSS Validator to validate CSS

- W3C Markup Validator to validate HTML

- jshint for javascript validation

- pep8 for python validation

- crispyforms for forms

- Stripe for payments

- PostgreSQL as a heroku database

- Coolors for the colour palette


## Wireframes
<a name="wireframes"></a>

------


- Home page 

![balsamiq home](/media/balsamiqhome.png "balsamiqhome")

![balsamiq home2](/media/balsamiqhomesmall.png "balsamiqhome2")


- Products Page

![balsamiq products](/media/balsamiqproducts.png "balsamiqproducts")

![balsamiq products2](/media/balsamiqproductssmall.png "balsamiqproducts2")


- Product Detail Page

![balsamiq detail](/media/balsamiqdetail.png "balsamiqdetail")

![balsamiq detail2](/media/balsamiqsmalldetail.png "balsamiqdetail2")


- Bag

![balsamiq bag](/media/balsamiqbag.png "balsamiqbag")

![balsamiq bag2](/media/balsamiqbagsmall.png "balsamiqbag2")


- Checkout

![balsamiq checkout](/media/balsamiqcheckout.png "checkout")

![balsamiq checkout2](/media/balsamiqcheckoutsmall.png "balsamiqcheckout2")


- About

![balsamiq about](/media/balsamiqabout.png "balsamiqabout")

![balsamiq about2](/media/balsamiqaboutsmall.pngg "balsamiqabout2")


- Contacts

![balsamiq contacts](/media/balsamiqcontacts.png "balsamiqcontacts")

![balsamiq contacts2](/media/balsamiqcontactssmall.png "balsamiqcontacts2")


- Suggestion

![balsamiq suggestion](/media/balsamiqsuggestion.png "balsamiqsuggestion")

![balsamiq suggestion2](/media/balsamiqsuggestionsmall.png "balsamiqsuggestion2")


- Newsletter

![balsamiq newsletter](/media/balsamiqnewsletter.png "balsamiqnewsletter")

![balsamiq newsletter2](/media/balsamiqnewslettersmall.png "balsamiqnewsletter2")


## Data Model 
<a name="data-model"></a>

------


- The data model for the website can be found below:

![data model](/media/modeldiagram.png "datamodel")



## features  
<a name="features"></a>
------

### Home Page
<a name="home-page"></a>
  
Home page contains a fully working nav, including search bar, profile and shopping bag. Profile can also include product management if the user is an admin. The main attraction is the cinema-related image, which includes a shop now button. Below that, there are two sections containing the highest rated and latest arrivals. The footer consists on 3 parts: the logo, contacts and a call for a newsletter signup. 

![home page](/media/homepage1.png "homepage")
![home page2](/media/homepage2.png "homepage2")
![home page3](/media/homepage3.png "homepage3")
![home page4](/media/homepage4.png "homepage4")


### Products Page
<a name="products-page"></a>

In this page, a list of all the products is displayed, detailing the most important information such as price, rating, title. The user also has the option to sort products by price, rating and title, from either ascending or descending order. Admin users have the ability to edit and delete the product from here.   

![products page](/media/productspage.png "productspage")

### Product Detail
<a name="product-detail"></a>

The product detail consists of an image of the product to the left and all the relevant information about it on the right. This includes everything that is displayed on the product card plus sinopsys, director, subcategory, quantity to add to bag and edition (only dvd will be available, as the others will be implemented later). Admin users have the ability to edit and delete the product from here. 

![products page](/media/productdetailpage.png "productspage")
![products page2](/media/productdetailpage2.png "productspage2")

If a user adds a procut to their bag, a confirmation screen will pop-up.

![add to bag](/media/addtobag.png "addtobag")


### Bag
<a name="bag"></a>

This is where users can find all the the products they have added to the bag. From here, they can review what they are purchasing, update quantities or delete what they no longer want to purchase, and finally go to checkout. There is also an option to go back to shopping.

![bag page](/media/bagpage1.png "bagpage")
![bag page2](/media/bagpage2.png "bagpage2")



### Checkout
<a name="checkout"></a>

In the Checkout page, the user is presented with a summary of their order. If everything checks, users will need to fill in personal details, delivery and card payment. Details will be pre-filled if the user checked the save info option on a previous order. From there, they can either completer the order or go back to bag and adjust their order. 

![checkout page](/media/checkoutpage1.png "checkoutpage")
![checkout page2](/media/checkoutpage2.png "checkoutpage2")
![checkout page3](/media/checkoutpage3.png "checkoutpage3")

### Order Confirmation
<a name="order-confirmation"></a>

Once an order is completed, the order confirmation page will be displayed, containing all the information regarding the order. A confirmation email will also be sent to the user.

![order confirmation](/media/checkoutpage1.png "orderconfirmation")
![order confirmation2](/media/checkoutpage2.png "orderconfirmation2")


### Product Management
<a name="product-management"></a>

This area is only available to the admins. They can use this page to add a product without going to the admin. 

![productmanagement](/media/productmanagementpage.png "productmanagement")
![productmanagement2](/media/productmanagementpage2.png "productmanagement2")
![productmanagement3](/media/productmanagementpage3.png "productmanagement3")

### Profile
<a name="profile"></a>

This is where the users can see and edit their private details and check their order history. 

![profilepage](/media/profilepage.png "profilepage")


### About Us 
<a name="about-us"></a>

This page includes information about Movie Night. The first part includes a lot of the SEO keywords present in the meta description for better search engine results, while the 2nd part purely explains the importance of physical media (as part of the business strategy to get people to buy from Movie Night) 

![aboutuspage](/media/aboutus.png "aboutuspage")


### Contacts 
<a name="contacts"></a>

In this page, users can find all the contacts to movie-night, as well as the link to the make a suggestion page, in case they want to contact Movie Night in the website. 

![contactspage](/media/contactspage.png "contactspage")


### Newsletter
<a name="newsletter"></a>

In this page, users can subscribe to Movie Night's newsletter so they can stay informed about all the offers, latest arrivals, etc...

![newsletter page](/media/newsletterpage.png "newsletterpage")


### Suggestion
<a name="suggestion"></a>

In this page, users can contact Movie Night and ask for any movie, TV show or Documentary they can't find on the website. They can also use the form for other queries.

![suggestion page](/media/suggestionpage.png "suggestionpage")


### Facebook Page
<a name="facebookpage"></a>

As part of this project, a Facebook business page was created for Movie Night. It includes description, contacts, cover and profile picture, a shop button, business hours, amongst other relevant information. Two posts were made, the first one just promoting the store was pinned, while the other is a more casual post as you would expect from a store. 

![facebook page](/media/facebook1.png "facebookpage")

![facebook page2](/media/facebook2.png "facebookpage2")

![facebook page3](/media/facebook3.png "facebookpage3")

![facebook page4](/media/facebook4.png "facebookpage4")

![facebook page5](/media/facebook5.png "facebookpage5")


### Future Features
<a name="future-features"></a>

- Rate Products
- Favourite Products
- Movie Editions: The option to select an edition (dvd, bluray or 4k).



## Testing
<a name="testing"></a>

------

### General Testing
<a name="general-testing"></a>

- Search bar working correctly and presents all the results that match either text contained on the title and in the sinopsys

- authentication working well, with users being able to login, singup and logout with no issues

- product detail presents all the relevant information, with the add to bag link functioning well

- updating or removing items from bag is available to users and instantly reflects on the bag

- admin users can edit and delete products from the product detail/all products page as well as from the product management page with no issues

- all the links in the nav and footer are working correctly (the facebook link may be removed by facebook as they tend to delete 'fake' business pages)

- Users can subscribe to the newsletter 

- Users can leave a suggestion and they will receive a confirmation message. 

- All the popup messages are working correctly, including authentication success, edit/delete/add product success or fail, order confirmation and add to bag success. 


### Validator Testing
<a name="validator-testing"></a>

HTML

- [Home Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2F)

- [All Products Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fproducts%2F)

- [Product Detail Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fproducts%2F73%2F)

- [Bag Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fbag%2F)

- [Checkout Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fproducts%2F)

- [Order Confirmation Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fcheckout%2Fcheckout_success%2FB211F86EB677449A966981E1DA2036E3)

- [Profile Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fprofile%2F)

- [Product Management](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fproducts%2Fadd%2F)

- [Logout Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fprofile%2F)

- [Signup Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Faccounts%2Fsignup%2F)

- [Login Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Faccounts%2Flogin%2F)

- [About Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fabout%2F)

- [Contacts](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fcontacts%2F)

- [Newsletter](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fnewsletter%2F)

- [Suggestion](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fsuggestion%2F)


CSS 


- Both CSS files had no errors on it when I ran them through the [validator](https://jigsaw.w3.org/css-validator/) 



Javascript 

- All Javascript was put through the [validator](https://jshint.com/) and no errors were found.




Python


- Every python file was passed through the [validator](http://pep8online.com/) and came back with no errors.




### Responsiveness Testing
<a name="responsiveness-testing"></a>

This blog was designed with the help of bootstrap, which is a mobile first design tool. The website is responsible to all sorts of different devices. 


## Bugs and Issues
<a name="bugs-and-issues"></a>

------

- The mobile header was overflowing: The problem was that I had a row within another row and that was causing erratic behaviour in which users would have had to scroll to see all the icons.

- Margins: Some of the content wasn't showing in most of the pages, so I had to include margins in all of them so they displayed properly.

- Duplicate id in bag.html : I had divided the bag.html in small files to use as includes, but the form was generating a duplicate id, so i switched back to use that bit of code in the main template again and it fixed it. 




## Site Deployment
<a name="site-deployment"></a>

------

The Movie Night repository was created on Heroku by following these steps:

- Login to Heroku 

- Create a new app and choose the region (name must be unique)

- Add Postgres database in resources tab

- Install dj_database_url and psycopg2 in gitpod

- Run the command pip3 freeze > requirements.txt to make sure Heroku knows to install them

- Comment out the local database and add dj_database to imports. Go to heroku, get the database url and copy it to settings.py

- dry run migrations

- run all migrations

- Import all the categories, subcategories and edition using the command 'python3 manage.py load data name'

- Create a new Superuser

- Create a Procfile so Heroku knows to create a web dyno

- On Heroku, go to settings, reveal config vars and add DISABLE_COLLECTSTATIC=1

- In settings.py add the name of the heroku app and add localhost 

- Go to Heroku, deploy tab, select github and connect to your repository, and add automatic deployment

- Deploy tha app

- Copy the secretkey to the env.py file

- Set debug to false



The AWS S3 deployment followed these steps:



- Login to was.amazon.com

- Search for S3 on the search bar 

- Create a Bucket by naming it appropriately and choosing a region, uncheck the box that says Block Public Access and enable ACl under Bucket ownership.

- Open the bucket and paste in the CORS Configuration: 
[ { "AllowedHeaders": [ "Authorization" ], "AllowedMethods": [ "GET" ], "AllowedOrigins": [ "*" ], "ExposeHeaders": [] } ]

- turn on staitc website hosting on the properties tab

- In the Bucket's policy tab, click on policy generator and create a new policy. Copy it in the policy editor and before saving add /* at the end of the resource key to allow access to all Bucket resources.

- Go to Access Control List tab, click on the edit option and enable List for Everyone (public access)

- Search for IAM on the search bar

- Click on create new group on the sidbar and call it appropriately

- Click on policies on the side menu and then Create Policies

- In the JSON tab select 'import managed policy' which will let us import the 'S3 Full Access Policy' that AWS has pre-built for full access to S3. But because we want to allow full access to our bucket we need to get the bucket ARN from the bucket policy page in S3 and paste it under Resource as a list.First, we will paste the ARN as it is, and then, paste again with /* at the end to add another rule for all files and folders in the bucket

- After reviewing it, give the policy a name and description and click on Create Policy

- Go to the group you created, click attach policy, you can then search for the policy you created and add it

- Click Users to create a user in the group

- Create a user, select programatic access and then click next

- Select the group created and click Create User

- A CSV file containing all the keys you will need to connect to django will appear for download. Save the file in a folder familiar to you, as you won't be able to download it again if you leave

- On Django, go to settings.py and create an if statement in the static files section to check if there is an environment variable called USE_AWS. The if statement should include the AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME, access key and secret access key

- On Heroku, go to settings, reveal config vars and add the AWS keys

- Set USE_AWS to TRUE and delete DISABLE_COLLECTSTATIC

- Go to settings.py and set up your bucket 

- Create a new file called custom_storages.py at the same level as manage.py

- Import settings from django and s3boto3 storage class from django storages and create a new class called static_storages that inherits from django s3boto3

- On that class, add location = settings.STATICFILES_LOCATION, which is where the static files will be stored. 

- Repeat the process for the media class, and add location = settings.MEDIAFILES_LOCATION instead.

- Go to settings.py and set a variable that points to the new storage classes we just created and that the location it should save static files is a folder called 'static'. Do the same for media files

- Override the previously set static and media storage locations and set the URL's with our new locations. 

- Deploy to Heroku

- Go to the Bucket created in S3, and check for a static files folder, as it should be there. All of the static files should be in it every time the site is deployed. Next to the static folder, create a media folder, and then upload all the images you have on the media file to there. 



## Credits
<a name="credits"></a>

------

### Media
<a name="media"></a>

All the images used in the site were taken from other websites, including:

- Unsplash.com
- IMDB for the movie covers

All the icons were taken from "Font Awesome".

### Content
 <a name="content"></a>

For this project, the following sources of information were used:

- Stackoverflow for various code related doubts

- Django documentation for ideas on how to make ideas come true

- The Boutique ado project for helping with stripe, orders etc...


### Acknowledgements
 <a name="acknowledgements"></a>

 I want to thank the following people for helping me with this project:

 - My mentor, Akshat Garg, for helping me go in the right direction

 - The tutors at CodeInstitute for helping me sort small issues with the blog.