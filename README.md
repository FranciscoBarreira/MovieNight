## Movie Night

------

Movie Night is an e-commerce platform centered around movies, tv shows and documentaries.It includes the ability to sign up for newsletters, make suggestions via an in-site form and uses stripe payment. This platform was fully developed in Django.


The link to the deployed website can be found [here.](https://movienight2022.herokuapp.com/)

The link to the Github repository can be found [here.](https://github.com/FranciscoBarreira/MovieNight/)


![mockup site generator image](/media/mockup.png "mockup preview")

## Table of Contents 

[User Experience](#user-experience)

   - [User Requirements](#user-requirements)
   - [User Stories](#user-stories)

[Design](#design)   

   - [Images](#images)
   - [Colour Scheme](#colour-scheme)
   - [Fonts](#fonts)

[Technologies Used](#technologies-used) 

[Features](#features)   

   - [Top Page](#top-page)
   - [Carousel](#carousel) 
   - [Blog Posts](#blog-posts)
   - [Footer](#footer)
   - [Post Detail](#post-detail)  
   - [Authentication](#authentication)
   - [Future Features](#future-features)    


[Models](#models)   

   - [Post Model](#post-model)
   - [Comment model](#comment-model)
   - [Diagram](#diagram)


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


### User Requirements 
<a name="user-requirements"></a>

- The website should be easy to navigate
- The posts should include the category to understand the topic in discussion
- Commenting and upvoting/downvoting should be featured
- The website's visuals should be maintained across all pages
- Login/signup process should be quick and intuitive
- The website should adapt to different screen sizes on different devices


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

- Summernote for adding fields to the posts

- Google fonts to add custom fonts to the website

- Font Awesome for icons

- Bootstrap for quick HTML mobile first design

- Cloudinary for online image storage

- dbdiagram for the models diagram

- W3C CSS Validator to validate CSS

- W3C Markup Validator to validate HTML

- Codebeautify to make HTML and CSS easier to read


## features  
<a name="features"></a>
------

### Top Page
<a name="top-page"></a>
  
At the top of the page lies there is a navbar with a short welcome message and the Home/Signup/Login options. If the user is already logged in, the options change to Home/Sign out. Below, there is an background image with the Metagaming name and logo. 

![logo/navbar image](/static/media/images/nav.png "logo and navbar")



### Carousel
<a name="carousel"></a>

Below the Metagaming image, there is a carousel that contains 3 posts. The first is fixed, displaying a message to sign up. The remaining two are the last posts created in the blog. On the right, there is a search bar so users can search for the content they desire. There are 3 additional side widgets, Upcoming Events, Recommended Games and Recommended Streamers below the search bar.   

![carousel image](/static/media/images/carousel.png "carousel")

### Blog Posts
<a name="blog-posts"></a>

The blog posts are displayed below the carousel. Each page contains up to 6 posts, that include image, author, category, date, title and excerpt. The users can open the posts either by clicking on the image or on the read more button.

![blog image](/static/media/images/posts.png "blog")


### Footer
<a name="footer"></a>

This is where users can find all the social media links. The background color is the same as the navbar to maintain visual consistency. There are aria labels in all of the links for screen readers. 

![footer image](/static/media/images/footer.png "footer")



### Post Detail
<a name="post-detail"></a>

Whenever a uder clicks on a post, they will open the post detail page. Inside it, there is all the relevant information such as author, image, category and date, followed by the text content. At the bottom of the page, there is are upvote/downvote buttons and a comment section so users can show the way they feel about that content. Those are features that can only be accessed by registered users. 

![post detail ](/static/media/images/postdetail.png "post-detail")
![post detail2 ](/static/media/images/postdetail2.png "post-detail2")


### Authentication
<a name="authentication"></a>

This blog contains 3 authentication related pages: login, sign up and sign out. The login page includes a link to the sign up page and vice versa. That way, users can complete their desired action in an intuitive manner. 

![login image](/static/media/images/login.png "login")
![sign up image](/static/media/images/sign-up.png "sign up")
![sign out image](/static/media/images/sign-out.png "sign out")


### Future Features
<a name="future-features"></a>

- List of upvoted posts
- Search by categories
- Save posts 


## Models
<a name="models"></a>

------

### Post Model
<a name="post-model"></a>

![Post Model image](/static/media/images/post-model.png "post-model")
![Post Model image2](/static/media/images/post-model2.png "post-model2")

### Comment Model
<a name="comment-model"></a>

![Comment Model image](/static/media/images/comment-model.png "Comment-model")

### Diagram
<a name="diagram"></a>

![Diagram image](/static/media/images/dbdiagram.png "Diagram")


## Testing
<a name="testing"></a>

------

### General Testing
<a name="general-testing"></a>

- Nav Bar: When a user is logged in, Home and Sign Out appears on the nav bar as opposed to Home, Sign In and Sign Up.

![non-authenticated image](/static/media/images/nav.png "non-authenticated")
![authenticated image](/static/media/images/nav2.png "authenticated")

- Comment Section and Upvotes/Downvotes: When a user is authenticated, they can comment and upvote/downvote the post. For those who are not, the comments and upvotes/downvotes still appear, but in an non-interactive way(see image below).  

![non-authenticated comment/upvote/downvote image](/static/media/images/comment-signout.png "non-authenticated comment/upvote/downvote")

- In this scenario, the user is logged in and has both upvoted and downvoted the post(for testing purposes), which is why both buttons have a red background.

![authenticated comment/upvote/downvote image](/static/media/images/comment.png "authenticated comment/upvote/downvote")

- Edit/Delete Comment: If authenticated, the user can delete or edit a comment they made. Pressing delete will permanently erase the comment, while pressing edit will take the user to the screen shown below. 

![edit/delete image](/static/media/images/edit.png "edit/delete")

- Sign in message: After logging in, a successful sign in message appears for two seconds.

![sucessful sign in image](/static/media/images/sign-in-message.png "successful sign in")

- Sign out message: After signint out, a successful sign out message appears for two seconds.

![sucessful sign out image](/static/media/images/sign-out-message.png "successful sign out")

- Search bar: When a search is performed, a list of posts that match said search appear.

![search image](/static/media/images/search.png "search")



### Validator Testing
<a name="validator-testing"></a>

HTML

[Home Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2F)

[All Products Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fproducts%2F)

[Product Detail Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fproducts%2F73%2F)

[Bag Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fbag%2F)

[Checkout Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fproducts%2F)

[Order Confirmation Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fcheckout%2Fcheckout_success%2FB211F86EB677449A966981E1DA2036E3)

[Profile Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fprofile%2F)

[Product Management](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fproducts%2Fadd%2F)

[Logout Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fprofile%2F)

[Signup Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Faccounts%2Fsignup%2F)

[Login Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Faccounts%2Flogin%2F)

[About Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fabout%2F)

[Contacts](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fcontacts%2F)

[Newsletter](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fnewsletter%2F)

[Suggestion](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmovienight2022.herokuapp.com%2Fsuggestion%2F)

CSS 

Both CSS files had no errors on it when I ran them [through](https://jigsaw.w3.org/css-validator/)



Javascript 

All Javascript was put [through](https://jshint.com/) and no errors were found.




Python

Every python file was passed [through](http://pep8online.com/) and came back with no errors.








CSS- No errors were shown when put through the [CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ffranciscobarreira.github.io%2Fjavascript-project%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=pt-BR)


### Responsiveness Testing
<a name="responsiveness-testing"></a>

This blog was designed with the help of bootstrap, which is a mobile first design tool. The website is responsible to all sorts of different devices. 


## Bugs and Issues
<a name="bugs-and-issues"></a>

------

- No username in comments: The username was not showing in the posted comments. This was because I wrongly set comment_form.instance.username = request.user.username. The problem was fixed when i changed it to comment_form.instance.name = request.user.username.

- Categories bug: I could not get the full name to display in the post category, as it was not getting the human readable value. To fix this, I used the get_FOO_display.

- Carousel bug: The carousel featured in the home page was presenting 4 posts when it should be limited to 3. This was fixed by using slice:2. 




## Site Deployment
<a name="site-deployment"></a>

------

The Metagaming repository was created on GitHub by following these steps:

- Select the Code Institute template

- Click create new repository after naming it 

- Click on the green Gitpod button to create the workspace


This site was deployed to Heroku. To do so, I followed the steps in the [Django Blog cheatsheet.](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)




## Credits
<a name="credits"></a>

------

### Media
<a name="media"></a>

All the images used in the blog were taken from other websites, including:

- Google images for all the images in the posts, the Metagaming page header and placeholder image.
- Twitch.tv for the images in the recommended streamer widget.

I do understand that it is better to use sites such as unsplash for images, but given the highly specific nature of the images required I decided to use google images.

All the icons were taken from "Font Awesome".

### Content
 <a name="content"></a>

For this project, the following sources of information were used:

- Stackoverflow for various code related doubts

- Django documentation for ideas on how to make ideas come true

- All the post content was taken from IGN.com, Gamespot.com and Destructoid.com

- The I think, therefore I do project for helping with login and pagination.


### Acknowledgements
 <a name="acknowledgements"></a>

 I want to thank the following people for helping me with this project:

 - My mentor, Akshat Garg, for helping me go in the right direction

 - The tutors at CodeInstitute for helping me sort small issues with the blog.