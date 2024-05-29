![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!


Welcome to Academic Exam's Mark Sheet Grade producer App
# 

## Table of Contents
 + [Purpose](#purpose)
 + [UX Wireframe](#wireframe)
 + [Responsiveness](#responsiveness)
 + [Testing](#testing)
   - [DevTools](#devtools)
 + [Bugs](#bugs)
   -  [Fixing](#fixing)
 + [Validation](#validation)
   - [HTML](#html)
   - [CSS](#css)
 + [Acknowledgements](#acknowledgements)
   - [Credits](#credits)
   - [Technologies Used](#technologies-used)
   - [Languages Used](#languages-used)
   - [Websites](#websites)
   - [Content](#content)
   -  [Softwares](#softwares)
 + [Deployment](#deployment)
 + [Conclusion](#conclusion)
 
## Purpose
Wellcome to [Little Chess Club](https://abdurrahimb.github.io/chess-club/) Website!

This wesite is intended to the Chess loving people who wants to learn how to play chess. If they want to learn playing chess or even they want their children to learn and grow interest. This website offers information about benifits of playing chess. They will find information about the positive impact of playing chess by the recreational players or even pupils of ADHD and Dementia. The website offers three different courses on a different page called "Courses" and interested people who wants to sign up can contact us in a different page called Contact Us. This is a fully responsive website. People can access the site from their mobile phones all the way upto any size over 1200px.

## Wireframe
I have used balsamiq to produce wireframes. Here i share the screenshots of related work both by mobile and desktop.
Here are the screenshots how I drew my project for mobile device on banlamiq wireframe.

  + Mobile 

On mobile device all three pages looks exactly how it is designed for.

|Index|Courses|Contact Us|
|---|---|--|
  |![index-mob!](assets/images/wireframe/index-mob.png)|![courses!](assets/images/wireframe/courses.png)|![contact-us!](assets/images/wireframe/contact-us.png)|

  + Desktop

  Here are the screenshots how I drew my project for larger device on banlamiq wireframe.

  Index Page or home page should look like this.

 ![index.desk!](assets/images/wireframe/index.desk.png) 

 Courses Page should look like this.

  ![courses-desk1!](assets/images/wireframe/courses-desk1.png) 

  Contact Us Page should look like this.

  ![contact-us-desk1!](assets/images/wireframe/contact-us-desk1.png)

## Responsiveness

 Here are the screenshots how it look like on different devices when the project finished.

![responsive!](/assets/images/screenshots/responsive.png)

## Navigation (Mobile)

  When clicked on menu bar it opens up the menubar and looks like this on the mobile devices.

![mob-nav!](/assets/images/wireframe/mob-nav.png)

 +  Just Nav Bar

When not clicked on menu bar it looks like this on mobile devices.

![mob-nav-1!](/assets/images/wireframe/mob-nav-1.png)

  + Desktop

On the desktop or larger devices menu bar shows like this as extended header.

 ![desk-nav!](/assets/images/wireframe/desk-nav.png)

## Courses Page

 + Mobile

The course page looks like the folloing on the mobile devices. All three lesson packages should show in a column one after another making it easy for the user to read and decide which course is suitable to them.

![courses-mob!](/assets/images/screenshots/courses-mob.png)

 + Desktop

The course page looks like the folloing on the Desktop or larger devices.
![courses-desk!](/assets/images/screenshots/courses-desk.png)

## Contact Us Page

 + Mobile

The Contact Us page looks like the folloing on the mobile devices.
![contact-us-mob!](/assets/images/screenshots/contact-us-mob.png)

 + Desktop

The Contact Us page looks like the folloing on the Desktop or larger devices.

![contact-us-desk!](/assets/images/screenshots/contact-us-desk.png)

## Footer Section

The footer section looks like the following across the different size devices.

 ![footer!](/assets/images/screenshots/footer.png)

## Testing

I have tested the site manually which looked fine on all devices. I checked the form filled out and send on from both sizes. It successfully submitted to the server. Fields needs to have inputs, email field needs a valid email address, set minlength in the fileds. 

|  | Test | Result |
|---|:---|---|
| 1 | All links on navigation works fine | Pass |
| 2 | footer icons bring them to the linked sites | Pass |
| 3 | Contact for submits only if all the fields meet requirements | Pass |
| 4 | external links opens in a new tab | Pass |
| 5 | name field needs to add a value | Pass |
| 6 | email field needs a valied email | Pass |
| 7 | submit button register to the designated destination | Pass |
| 8 | 5 visitors were added to check the site's functionality | Pass |
| 9 | responsiveness trigers when meets required screen size | Pass |
| 10 | navigation burger icon disappears when full menu appears | Pass |
| 11| header bar always stick to the top on mobile devices | Pass |
| 12| images show the alt text | Pass |

## DevTools

With the chrome devtool, I checked, Which looked all good. It has good performance on lighthouse scoring system.
All the three pages screenshots are here
  + This is score of the Home Page, it is satisfactory to me as a developper.

![index-lh!](/assets/images/screenshots/index-lh.png)

  + This is the score of the courses page, it is satisfactory to me as a developper.

![courses-lh!](/assets/images/screenshots/courses-lh.png)

  + This is the score of the Contact Us Page, it is satisfactory to me as a developper.

  ![contact-lh!](/assets/images/screenshots/contact-lh.png)

## Bugs

  ### Result

  I found a bug when the site finished. Results and solutions are as follow:

1. On the mobile device header covered the heading of the courses page.
2. There was no heading for section footer.

  ### Fixing

  1. I added margin to the header and resolved the issue.
  2. I added a hidden heading style upon adding the heading.

## Validation

I have used HTML and Css validators for all three pages and stylesheet. There was no errors or warning.

+ Python Validation

[Lynter](https://pep8ci.herokuapp.com/)



## Credits

I gained a lot of knowledge from doing the Full Stack Software Development programme with [Code Institute](https://learn.codeinstitute.net/)


## Technologies Used

 + GitHub
 + GitPod
 + LMS

## Languages Used

  + HTML5
  + CSS

### Websites

The websites that has been providing knowledge and materials to build this website are following:

1. Responsive Screensostes [Website](https://ui.dev/amiresponsive)
2. Website Ideas from [Love Running Project](https://abdurrahimb.github.io/Love-Running/)
3. Icons from [Fontawesome](https://fontawesome.com/)
4. Fonts from [Google Fonts](https://fonts.google.com/)
5. Code learning from [W3schools](https://www.w3schools.com/)
6. Favicon[Website](https://favicon.io/)
7. Mark Down Table of Contents Tutorial [Youtube](https://www.youtube.com/watch?v=EKqhENATIKg)
8. Adding images to .md tutorial [Youtube](https://www.youtube.com/watch?v=Ljj1wGFJqPY)

## Content

1. This website contains some information inspired from the [Website](https://www.brainscape.com/academy/does-chess-make-you-smarter/)
2. Some information inspired me from the [Website](https://www.ymcapkc.org/blog/6-reasons-learn-chess-how-playing-can-boost-your-brainpower)

## Acknowledgements

My lovely classmates on Code Institute, Tutors and My Mentor Mr. Alan Bushell. 

## Softwares

I have used different softwares to prepare this site. Here are the used softwares
  + Wireframe Tutorial [Balsamiq](https://www.youtube.com/watch?v=E5Z1QOly72E)
  + Adobe Photoshop
  + Windows Image Resizer
  + [Online image converter to .webp](https://convertio.co/jpg-webp/)

## Deployment

Here is the step by step process to deploy a depository to GitHub.
 1. First we need to go to related repository [My Repo](https://github.com/AbdurRahimB/chess-club)
 2. From the top menu bar click on Settings
 3. From the side bar click on Pages
 4. In the Build and deployment section under the source, select "Deploy from a branch"
 5. Under the Branch, select main
 6. Finally save.

## Conclusion

This is a three page mobile first fully responsive Chess Club website. The website is attractive to the specifit type of people who would love playing or joining a chess club. There are plenty of information why you should join in playing chess and enough attraction to join this specific club. Courses are designed for every level of player regardless their age. This README file covers all the process of building journey of this beautiful site. 