
# Testing

## Code Validators

* [W3C HTML Validator](https://validator.w3.org/) was used to check all HTML content, warnings were found for "type=text/javascript" code as being unnecessary, after these were removed no more errors were found.

* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to test the CSS content, this passed with no errors.

* [JSHint](https://jshint.com/) was used to check the javaScript content, this returned no errors, but a number of 'Undefined variable' messages, which I think were because of using Jquery.

* [PEP8](http://pep8online.com/) was used to check for PEP8 compliance in the python file and flake8 was used in the IDE terminal, pep8 found multiple issues with "missing whitespace around operator", after googling this I found that these errors can be 'false positive' so I left them as the were. with flake8 there were a couple of instances of 'line too long' warnings in code I had written, but I didnt want to change the code on these in case it broke functionality. As a side note, both utilities produced different issues which also left me unsure if and how they should be addressed.

* [Chrome DevTools](https://developer.chrome.com/docs/devtools/) was an absolutely invaluable resource in the projects development. it helped with multiple alignment issues. I also used the 'Lighthouse' utility, with most pages scoring over 80%, although the various product pages had impared performance scores, this I think has something to do with caching from AWS.

## Responsiveness

* Chrome dev. tools was also used at every stage of designing the website to ensure that the core structure and style of the website remained the same across all devices.

## User Stories Testing

* As a visitor to this website, I would like the navagation to be instantly understandable.
  - The Layout of the sites navagation follows modern design standards and all navagation buttons are placed where the user would expect them to be.

* As a visitor I would like an inventory of stock to browse through.
  - This is addresed by the various 'Products' pages, which give a gallery like browsing experience.

* As a visitor I would like the ability to search for products by name.
  - This can by done using the search bar on desktop view and by tapping the search icon on mobile view.

* As a visitor I would like the ability to register for an account for secure purchasing.
  - This can be done by clicking the 'my account' tab and then the 'register' option.

* As a visitor I would like an email sign up option, to be kept up to date with site news.
  - This can be done on the footer of every page of the site as there is an email sign up box with form validation.

* As a visitor I would like the option to follow the site on social media platforms.
  - This can be done by clicking on the various social media icons also in the footer of every page.

* As a visitor I would like the ability to comment on the blog posts I have read.
  - Users have this option available without the need to login at the bottom of each blog post page.

* As a menber of the website, I would like to 'Login' to my profile and view past purchases.
  - Registered users have this facility to them on their 'Profile' page once they have logged in.

* As a member of the website, I would the ability to manage and update my shipping and payment details.
  - Registered users can also update their shipping details on their 'Profile' page once they have logged in.

* As a member of the website, I would like to be able to read reviews and review products myself.
  - This can be done on each individual product page, allowing the user to give a star rating and leave a written comment if wished. The user must be logged in tho have this option.

* As an Admin of the website, I would like all of the above capabilities, but also the ability to add categories of products and the products themselves to the website, including price ratings and images, and the ability to delete reviews and blog comments which may be inappropriate or not in keeping with the sites ethos.
  - A user with 'Admin' privilages, has full CRUD control of the site through the 'django Administration' control panel, which can be accessed by adding /admin to the websites url. 

## Aditional Testing

* A gmail acccount was setup to recieve the emails from the sign up form in the footer, this did recieve the users email address with a sign up request message as intended.
* Navagation bar elements tested and functional across all device sizes, each link directing to the appropriate page
and from each page back.
* Website title heading in the navagetion bar acts as alternate home button link as intended.
* Hamburger navagation menu, expands correctly, without affecting other elements, in all screen sizes.
* Email sign up box will only accept a valid email address and returns a confirmation when the submit button is pressed, as intended.
* Social media icons in the footer all direct to their respective websites in a new tab as intended.

## Issues

* Editing CSS was a bit time consuming, as I could not see the changes unless I pushed them to github and then to heroku, perhaps this is because the static files were now on AWS, there is probably an easy fix for this, but I could not spend any more time trying to figure it out!

## Devices 

In addition to emulated devices in chrome dev tools the Website was inspected on the following physical devices:
* Surface pro 4 12" screen
* Surface pro 4 connected to 27" monitor.
* Samsung Galaxy S9 Plus
* Apple Macbook Air 2017

## Browsers used
* Google Chrome on Windows 10
* Microsoft Edge on Windows 10