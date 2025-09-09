# Fableseed Storytelling Forum

Insert Image

View the live project here

This collaborative storytelling forum has been created as a project during my [Code Institute](https://codeinstitute.net/) Level 5 Web App Development course.

## **Table of Contents**
* [Welcome to Fableseed](#welcome-to-fableseed)
    * [Fableseed Poem](#create-your-garden---fableseed-poem)
* [Inspiration](#inspiration)
* [Fableseed Goals](#fableseed-goals)
* [User Experience (UX)](#user-experience-\(ux\))
    * [Types of Users](#types-of-users)
        * [Primary User Types](#primary-user-types)
        * [Secondary / Future Users](#secondary-/-future-users)
    * [User Stories](#user-stories)
        * [Guests](#guests)
        * [Writers](#writers)
        * [Admin](#admin)
* [Design](#design)
    * [Colour Palette](#colour-palette)
    * [Colour Accessibility](#colour-accessibility)
    * [DaisyUI Custom Theme Creator](#daisyui-custom-theme-creator)
    * [Imagery](#imagery)
    * [Typography](#typography)
    * [Wireframes](#wireframes)
    * [End product design changes](#end-product-design-changes)
* [Features](#features)
    * [Users](#users)
    * [Stories](#stories)
    * [Incentivisation System](#incentivisation-system)
    * [Responsiveness](#responsiveness)
    * [Header](#header)
    * [Footer](#footer)
    * [Animations](#animations)
    * [Nursery Page](#nursery-page)
    * [User Garden](#user-garden)
* [Security Features](#deployment-security)
    * [Authentication & User Management](#deployment-security)
    * [Access Control](#deployment-security)
    * [Permissions & Roles](#deployment-security)
    * [Environment Variables](#deployment-security)
    * [Deployment Security](#deployment-security)
* [Future Features](#future-features)
* [Data and Models]
    * [Database Schema](#database-schema)
    * [Entity Relationship Diagram](#entity-relationship-diagram)
    * [Model Relationship Declaration](#model-relationship-declaration)
    * [Model Fields](#model-fields)
    * [Cardinalities](#cardinalities)
* [Testing](#testing)
    * [User Story Testing](#user-story-testing)
    * [Automated Testing](#automated-testing)
    * [The W3C Markup Validation Service](#the-w3c-markup-validation-service)
    * [The W3C CSS Validation Service](#the-w3c-css-validation-service)
    * [The JSHint Validation Service](#the-jshint-validation-service)
    * [The WAVE Webb Accessibility Evaluation Tool](#the-wave-webb-accessibility-evaluation-tool)
    * [Chrome Lighthouse](#chrome-lighthouse)
    * [Manual Testing](#manual-testing)
    * [Unit Tests](#unit-tests)
* [Technology used](#technology-used)
* [Coding help](#coding-help)
* [Interesting Bugs](#interesting-bugs)
* [Credits](#credits)
* [Media](#media)

## **Welcome to Fableseed**
A collaborative storytelling platform where stories grow like plants and words breathe life into a blooming world. Users plant seeds of stories (i.e. story starters), and other users add branches (chapters/replies) to grow the story. Each story “grows” like a plant, with branching paths and twists with each piece of user-generated creativity. Think mini-Wattpad meets Choose-Your-Own-Adventure — with full CRUD built in.

In Fableseed, stories are as essential as oxygen.

Plant the seeds of imagination and watch your garden blossom with vibrant flowers, each one nurtured by the tales you and others tell. These blossoms aren’t just beautiful — they cradle your stories in their petals, keeping them alive in the garden at the end of the world.

#### Fableseed Poem
The world is a desolate wasteland.  
Nothing grows here.  
Nothing thrives.

You wander through the ruin and wreckage, alone.  
Until you see a single green shoot in the decay.  
Struggling against the darkness.

You give it water.  
There is no response.  
There is no sun or warmth.

So you begin to speak.  
You tell it tall tales, fantasy fables, silly stories.  
Legends, parables, and yarns spun from nothing but hope.

The more stories you share, the taller it grows.  
The stronger it becomes.  
Until one day, it blooms.

A single, impossible flower — born of imagination.  
From it, you gather seeds.

And with them, you grow the last garden at the end of the world. {#and-with-them,-you-grow-the-last-garden-at-the-end-of-the-world.}

## **Inspiration**
I’m a person who likes to read and write, and who tries to come up with creative ways to get others to enjoy reading and writing, too. My passion for stories and storytelling began with books when I was a kid, but then extended into online, collaborative storytelling forums when I was a teenager. This lasted until I was almost 30, when life got super busy.

10 years later my life finally settled down a bit, but when I poked about on the net I discovered that those collaborative storytelling platforms didn’t exist anymore. All I could find were fan fiction sites - there’s nothing wrong with fan fiction sites, I just wanted to find a place where I could make my own characters and evolve them within a shared story world.

So when it came time to start my 3rd project as part of Code Institute’s Level 5 in Webb App Development, I had an inkling of what I wanted to create but not the confidence to plough ahead. I figured I probably needed to do something a bit more sensible this time around, something that addresses a customer need, or solves a business problem, that shows how diverse I can be across different sectors and industries.

I settled on an induction booking system for the library I work in \- we were using Microsoft bookings and I thought maybe I could create something more customisable to our needs. But I sat at my computer and, instead of planning out the models for a booking system, I sat dreaming about my storytelling platform. How I could use it with my students in the Gameracy programme to get them reading, and writing stories based on small prompts. How they could use those stories and characters in their own games they were creating using [TWINE](https://twinery.org/).

To stop the madness, I plugged the project criteria into ChatGPT and asked it to make suggestions on projects based on those criteria and the short timeframe, as well as taking into account the style and inspiration behind [Lila’s Lost Words](https://nexiauk.github.io/Lila/). 

My prompt: “The task is to create something like a restaurant booking system, or a reddit style news site, as the project has to showcase CRUD capabilities but I don't want to create something that boring\!”

ChatGPT immediately suggested I create a collaborative storytelling forum and that was that: Fableseed was born.

## **Fableseed Goals**
**Fableseed** is more than a web development project — it's a creative platform designed to inspire, connect, and empower users through collaborative storytelling. While it meets the technical and educational criteria of a CRUD-based web application using Django, Python, JavaScript, HTML/CSS, and SQL, its value extends far beyond the brief.

1. **Inspire Collaborative Creativity**  
    Provide a calm, imaginative space where users co-create branching stories, encouraging meaningful creative expression in a fast-paced digital world.

2. **Revive Communal Storytelling**  
    Digitally reimagine storytelling as a shared, evolving tradition — letting users plant story "seeds" and grow them together through narrative contributions.

3. **Support Mental Wellness Through Writing**  
    Offer a therapeutic outlet by encouraging reflective, low-pressure writing, helping users connect with themselves and others.

4. **Encourage Deep, Meaningful Engagement**  
    Replace vanity metrics with creative actions — every prompt, branch, and flower reflects real participation and narrative growth.

5. **Empower Aspiring Writers**  
    Lower the barrier to entry for young or beginner writers by allowing modular participation — start a story or contribute to one in progress.

6. **Design for Growth and Scalability**  
    Build a strong MVP with room to evolve — future features may include comments, visual story maps, AI prompts, and seasonal events.

7. **Deliver a Whimsical, Emotional User Experience**  
    Stand out with a unique, metaphor-rich interface that feels magical, hopeful, and emotionally resonant — more than just a functional app.

**In summary**, *Fableseed* is a technically sound, narratively rich, and emotionally engaging platform that fulfils academic requirements **while also addressing real-world needs**: creativity, collaboration, and connection in a time when those things are more vital than ever.

## **User Experience (UX)**
### *Types of Users*
#### Primary User Types
* Young or Beginner Writers - Gentle, non-judgmental space for emerging voices and playful exploration.  
* Experienced Writers - Low-pressure creative outlet for storytelling practice and experimentation.  
* Writers of All Abilities - Inclusive collaboration and community-driven creativity.  
* Casual & Social Users - People who enjoy prompts, shared writing, or cosy creativity without pressure.  
* Reflective Users - Those using writing as self-care, or drawn to the calming metaphor of growing stories.

#### Secondary / Future Users
* Educational Users - Teachers and students using Fableseed in learning environments.  
* Gamified & Puzzle-Oriented Users - Players and interactive fiction fans interested in story-unlocking mechanics.

### *User Stories* {#user-stories}
I used a [Github Kanban Board](https://github.com/users/Nexiauk/projects/8) to track my user stories and development tasks and help keep me on track.

#### Guests {#guests}
Prospective users who want to browse the forum, read some content and see if they want to join up. Guests shouldn’t be able to create content and have limited access to posted content.

As a guest:

* I want to be able to browse the forum (read-only) and view some story content to see if it’s something I want to participate in  
* I should be able to view some information on how the story forum works and what it’s about  
* I should be able to easily register for an account if I want to

#### **Writers**
Logged-in users who can create fableseeds, grow branches, and achieve rewards for doing so.

As a writer:

* I want to easily post a new Fableseed story prompt with minimal effort or complication  
* I want the ability to browse through posted Fableseeds, to decide where I want to grow some new branches  
* I want to see at a glance what type of flower I’ll gain, if I branch from a specific Fableseed prompt  
* I want the ability to grow a branch directly from a story prompt  
* I want to see the flowers I’ve earned in my user profile  
* I want to see my Fablebud balance in my user profile  
* I want to edit my own Fableseeds and Fablebranches to correct errors and spelling or grammar  
* I want to be delete my own Fableseeds and Fablebranches

#### **Admin**
* Can also participate as writers
* Also have the ability to approve/reject Fableseeds

As Admin

* I want to interact with the Fableseeds and Fablebranches in the same way as as a writer  
* I also want the additional ability to easily approve or reject Fableseeds  
* I want the ability to add new flowers in the admin interface

## **Design**
* **Flowers and literature**
[A Guide to Studying Flower Symbolism in Literature — Petal & Poem \- HK's Top Luxury Florist](https://www.petalandpoem.com/floral-thoughts/a-guide-to-studying-flower-symbolism-in-literature#:~:text=Flowers%20often%20align%20with%20overarching,the%20fleeting%20nature%20of%20life.)

Flowers and storytelling are inextricably intertwined, from the healing powers of The Secret Garden, to the whimsy of Hobbits smoking pipeweed, to the rose slowly decaying in Beauty and the Beast. Flowers and plantlife feature heavily in fiction not only as background details, but to convey emotion, as symbolism, as well as forming plot devices and connections in overarching themes.

This is why the theme of a garden and growing flowers from stories makes sense as a concept and will allow for emotive imagery and a complementary colour scheme.

* **Flowers and symbolism**
[List of plants with symbolism - Wikipedia](https://en.wikipedia.org/wiki/List_of_plants_with_symbolism)

[Floriography: The Secret Language of Flowers in the Victorian Era — Planterra Conservatory](https://planterraevents.com/blog/floriography-secret-language-flowers-victorian-era)

Various folklores, cultures and mythologies assign symbolism to plants and flowers. In Victorian times flowers were used to pass messages to friends, lovers and enemies, with extensive floral codes collated into dictionaries. Religious imagery and spiritual traditions are associated with different plants and flowers, for example the Lotus is a symbol of spiritual enlightenment and transcendence in Indian and Chinese texts.  

It was difficult to find a definitive list of flowers and their symbolism that wasn’t related to the traditionally Victorian pastime of using flowers to convey messages. Wikipedia had the most extensive list which I searched for the theme of rebirth, keeping in mind the idea that I am trying to resurrect collaborative storytelling, as well as the forum’s integral storyline of new life growing from the ashes of the old world.

Four flowers emerged from the list:

* Lotus - *an aquatic plant, doesn’t fit the imagined terrain*  
* Rainflower - *lovely, but very tiny*  
* Spider lily - *not very nice looking*  
* **Tulip - *beautiful, elegant, one of my favourite flowers***

![][image1]

Purple tulips represent royalty and rebirth, black tulips represent power and strength. I wanted to include black because I liked the idea of the power and strength of words, as well as it being representative of the apocalyptic devastation the flowers and stories are fighting back against.

* **Black Hero tulip**, with colours ranging from a dark maroon through mahogany to midnight black.  
  ![][image2]  
* **Black Parrot tulip** is a blackish purple tulip that is exotic and full of drama \- it looks a little less like a tulip but in a good way. It is one of the darkest tulips available.  
  ![][image3]  
* **Queen of Night tulips are** known for their rich purple-black colour.  
  ![][image4]

#### Colour Palette

Using [Adobe Colour](https://color.adobe.com/) I plugged an image of each tulip into the [Extract Theme](https://color.adobe.com/create/image) tool and generated a palette of colours.

**Black Hero**
![][image5]

**Black Parrot 1**
![][image6]
**Queen of Night**
![][image7]

**Black Parrot 2**
![][image8]

I decided to go with the **Black Parrot 1** for its balanced mix of greens and purples, with a lighter colour suitable for text. I also took Woodsmoke (almost black) from **Black Parrot 2.**

[Colorkit](https://colorkit.co/color/6830c1/) was used to find the closest matching Tailwind colours.

![][image9]
**Claret:** #730E3D  
**RGB:** 115, 14, 61  
**Closest Tailwind Colour:** pink-900  
**oklch(0.3683 0.1374 359.46)**

![][image10]
**Eggplant:** #400E37  
**RGB:** 64, 14, 55  
**Closest Tailwind Colour:** brown-900  
oklch(0.15 0.25 336.06)

![][image11]
**Black Smoke:** #0D0D0D  
**RGB:** 13, 13, 13  
**Closest Tailwind Colour:** Black  
oklch(0.1591 0 0)

![][image12]
**Deep Green:** #045911  
**RGB:** 4, 89, 17  
**Closest Tailwind Colour:**   
green-900  
oklch(0.4037 0.1274 144.22)

![][image13]
**Leafy Green:** #55A605  
**RGB:** 85,166, 5   
**Closest Tailwind Colour:** light-green-800  
oklch(0.6477 0.1888 135.3)

![][image14]
**White Smoke:** #F2F2F2  
**RGB:** 242, 242, 242  
**Closest Tailwind Colour:** grey-100  
oklch(0.9612 0 0)

#### Colour Accessibility
According to [Adobe colour’s accessibility](https://color.adobe.com/create/color-accessibility) tool, the Black Parrot theme was colour blind safe. 

[Adobe’s colour contract checker](https://color.adobe.com/create/color-contrast-analyzer) showed the following colour pairings to be accessible:

* **#730E3D** and #F2F2F2  
* **#0D0D0D** and #F2F2F2  
* **#045911** and #F2F2F2  
* **#400E37** and #F2F2F2  
* **#55A605** and **0D0D0D**  
* **#55A605** AND **#400E37**  
* **#55A605** and **#730E3D** - only for font 18pt and above and actionable icons and graphics

The colour scheme gave me a wide variety of pairings to work with, allowing versatility within Fableseed.

#### DaisyUI Custom Theme Creator
I decided to add the [Daisy UI](https://daisyui.com/) Tailwind plugin to my build as it provides useful component class names to help with writing less code and building faster. The [DaisyUI theme generator](https://daisyui.com/theme-generator/?lang=en) generates CSS from preset themes to add to your main Tailwind import css file, but you can also use it to generate your own custom colour scheme and it will even show whether your foreground and background colours are WCAG AAA compatible. Below are screenshots of my theme in the generator:

![][image15]

![][image16]

#### Imagery
I searched the internet with a clear image in mind of a flower growing from a post-apocalyptic city. My first inspiration came from this photo from an article about flowers that grow after wildfires. - [see credits section](#credits)

![][image17]

My second inspiration came from this image of a small shoot growing out of a cracked city street. - [see credits section](#credits)

[![][image18]](https://www.freepik.com/free-ai-image/plant-growing-from-soil_268350286.htm)

I found this image of a tulip that I wanted to use as the basis for my hero image - [see credits section](#credits)

![][image19]

I used [Adobe Firefly](https://www.adobe.com/products/firefly.html) to generate a scene of a tulip growing out of a devastated cityscape, using this particular tulip as a composition reference.

**Prompt:** “A black-purple tulip growing out of the ashes of a fallen, post apocalyptic city. The sky is darkened and the earth is devastated. The background is slightly out of focus and the tulip is highlighted in a slightly vibrant glow. The tulip has lots of luscious green leaves”

I used one of the generated images to create a portrait and a landscape hero image.

* Portrait Hero Image
![][image20]

* Landscape Hero Image
![][image21]

* Edited version for responsive styling
![][image22]

I used [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html) to grab the tulip by itself to plug back into Firefly so I could create a logo out of it using the following prompt and settings:

**Prompt:** “Purple-black tulip growing from the pages of a book”

**Settings:** Square, Flat Design, Vector Look, Bold Lines, Line Drawing, Bioluminescent, Vibrant Colours, Backlighting.

* Generated Image:

![][image23]

I used Photoshop again to crop and re-colour the design to match Fableseed’s colour palette, using masking techniques and the re-colour tool.

* Logo image:

![][image24]

The images for the different flower types were created in Canva using flowers of a similar art style. Where a matching flower image didn’t exist, I created one and ended up with 12 images I was very happy with.

![][image25]![][image26]![][image27]![][image28]![][image29]![][image30]![][image31]![][image32]![][image33]![][image34]![][image35]![][image36]

#### Typography {#typography}
I used two sites to search for fonts and compare them against each other:

[https://fontjoy.com/](https://fontjoy.com/)

[https://fonts.google.com/](https://fonts.google.com/)

The set I came up with is listed below:

* **Great Vibes** for the logo/site main header  
* **Merriweather Sans** for sub-headings  
* **Inclusive Sans** for body text

Great Vibes is high contrast vs Merriweather Sans and Inclusive Sans \- this was a purposeful choice as high contrast typography pairing can be used to improve readability, establish visual hierarchy, and create interest.

*  **Great Vibes**
I wanted a flowing, plantlike script for Fableseed’s main title/logo font, however it also needed to be legible and readable. Lots of flowing and calligraphy fonts have partial letters (the top of an ‘S’ missing) or badly formed letters (‘e’ sometimes looks like ‘a’) or even added flicks and flourishes that make a capital ‘F’ look like a weirdly-shaped capital ‘E’.

I fell in love with the font called Fondamento, but couldn’t get over how the capital ‘F’ looked:
![][image37]

The Great Vibes font is nicely formed and easy to read at a larger font size. It only has one style, which isn’t a problem as I only want to use it exactly as it is and for only two words \- ‘Fableseed’ and ‘Garden’.
![][image38]

* **Merriweather Sans**
A sans-serif font known for its readability on screens, particularly at smaller sizes, and its traditional feel. With italics applied, double storey letters become single storey letters, ideal for people with specific learning difficulties. It’s traditional in style, despite the modern shapes it has adopted.

* **Inclusive Sans**
Inclusive Sans is a text font designed for accessibility and readability. It fits very cohesively with Merriweather as they are both San-serif, so it also contrasts well with the title/logo font, Great Vibes.

I’d also looked at Raleway as a choice for the sub-headings, as it also changes double storey letters into single storey with italics applied. So, I had a chat with ChatGPT about the suitability and feel of the scheme with each sub-heading font applied.

ChatGPT gave me some useful insights, which can be found at this link: [ChatGPT Font discussion](https://chatgpt.com/share/686a52b0-61a4-8005-9e36-e24e77b2c71d). It also produced code to use in [CodePen](https://codepen.io/Nexiauk/pen/JodgNvy), allowing me to look at both options together. This is ultimately what helped me to decide on Merriweather vs Raleway. It simply looked nicer.

![][image39]

#### Wireframes
I was inspired by collaborative storytelling platforms that I used to frequent on Proboards and FreeForums. [Here is a link to Event Horizon,](https://eventhorizon.freeforums.net/) a site I created myself more than 10 years ago. I wanted to keep the same sort of boxy, table-style vibe that freeforums and proboards have as a sort of homage, as well as it being a neat way to display many Fableseeds and their content.

I started by creating my wireframes on a Canva whiteboard just so I could be as messy as I liked and move things about. I then transferred these into a [Canva website mockup](https://www.canva.com/design/DAGyZh0LIn0/oZaWEPu1ycptgKwQmzO8Mw/view?utm_content=DAGyZh0LIn0&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h3a80639be5) for mobile and desktop.


![][image40]

#### End product design changes
I think my end product is very representative of my original wireframe design. I had a very clear image of the vibrant colour scheme I wanted to use and the style of site I wanted to create. The Fableseed list is purposefully a table rather than something more modern, like cards, as a nostalgic throwback, although I hope my table is better looking and prettier than the original Proboards ones.

The only significant change to the end product was the background image that I overlaid my background colour with. It just felt like it was missing a pretty *something* and that something turned out to be flowers - which is part of Fableseed's core mechanics. I found a frame I liked in Canva, made it transparent, 'glued' several iterations of the frame together and rotated it to sit nicely on desktop. I've purposefully chosen to hide it on mobile to leave the design uncluttered on smaller screens. It's also layered over a different coloured-background on index.html, but that darker background was part of the original design as a striking entry into the site.

I also decided that I wanted to explore GSAP animations. It's something I wanted to do in my last project and didn't get a chance, so I introduced SplitText and Scrolltrigger for a slowly unfolding storybook feel. The only issue I have with this is that GSAP automatically applies aria hidden to the elements and aria hidden shouldn't be paired with paragraphs, so this gives errors for accessibility. I tried changing to divs instead but the layout was silly and still produced the errors, probably because lighthouse has decided that the aria-hidden is unnecessary or prohibitive to screen-readers, even though the aria-hidden is removed as the elements appear.

## **Features**
### *Users*
* Register/login/logout
* User profile: “My Garden” showing stories planted or contributed to  
  * Display Name, Profile picture, Bio  
  * Edit profile, which allows an image change by the user.

### *Stories*
* Users create a **Story Seed** (title + intro)
* Story seeds approved by admin
* Others can contribute **Branches** (replies on seed threads)
* Admin approval system for seeds

### *Incentivisation System*
* Each branch posted on a a Fableseed with a previously uncollected flower, grants that flower to the user's garden
* Flower quantity increases by +1 with each branch posted
* +1 Fablebud granted to the user's profile
* Fablebud spend to post branches - not currently implemented.

### *Responsiveness*
Fableseed has been built mobile-first and is responsive on screen sizes from 320px through to 2560px. Tailwind breakpoints have been applied to classes across many different elements to ensure that they look good, are legible, and resize nicely. 
* I did a lot of experimentation with trying to get the background overlay image looking nice.
* The navigation menu collapses on mobile and tablet and opens via a burger icon.
* The nursery table hides all of the columns aside from Flower and title on mobile, which is all you really need to get going on Fableseed, especially as the autho and created info is on the fableseed view.
* Fableseeds and Fablebranches have a stacked internal layout on mobile, inclusive of the Tend and Prune buttons.
* My Garden also stacks the profile area on mobile and implements flex on the Earned flowers section.
* The timeline on the About page alternates steps from left to right on tablets and up, but on mobile it all sits on the same side to make full use of the smaller space.
* Crispy Forms has been used and allowed to handle form responsiveness across devices. I have used the Crispy form helper layout in forms.py to apply additional styling

### *Header*

### *Footer*

### *Animations*

### *Nursery Page*

### *User Garden*

### *About Page*

##  **Security Features**
### *Authentication & User Management*
* Django Allauth is used to handle user registration, login, logout, and account management.  
* Provides built-in security features such as password hashing, email verification, and session handling.  
* Ensures only authenticated users can create and manage their own Fableseeds, FableBranches, and Profiles.  
* Guests have read-only access and cannot create, edit, or delete records.

### *Access Control*
* Actions such as creating, editing, and deleting Fableseeds and FableBranches, and editing Profiles, are protected with @login_required on Django views.  
* Buttons and UI elements for these actions are only rendered for authenticated users (if user.is_authenticated).  
* Guests cannot perform restricted actions even if they try to access the URLs directly.  
* This ensures proper access control and prevents unauthorized modifications.


### *Permissions & Roles*
Users:
*  Can create, edit, and delete their own Fableseeds and FableBranches, and edit their own Profiles (cannot delete them).

Admins:
* Can create, edit, and delete any Fableseed or FableBranch.  
* Can create, edit, and delete Flowers and manage user Flowers.  
* Can approve Seeds and delete users.

Guests: 
* Can view content but cannot create, edit, or delete.  
* Seeds with existing Branches cannot be deleted by regular users, protecting relational integrity.

### *Environment Variables*
* Sensitive data is stored securely in an env.py file, which is hidden via .gitignore.  
* Keys and settings stored in env.py include:  
* SECRET_KEY (Django project key)  
* DATABASE_URL (PostgreSQL database connection)  
* CLOUDINARY_URL (media storage)  
* .venv (virtual environment) is also excluded from GitHub, ensuring no dependencies or system files are exposed.

### *Deployment Security*
* DEBUG mode is disabled in production.  
* No passwords, API keys, or sensitive information are ever committed to the repository.  
* All environment-specific settings are managed securely via env.py.

## **Future Features**
* Filter by: most grown stories, newest seeds, flowers
* Search by: specific flowers
* Visual story tree (JS or D3.js)
* Word count goals per chapter (live JS tracker)
* “Garden Stats” page: most popular authors/stories
* ‘Like’ system grants additional flowers of that type
* Seasonal events
* WYSIWYG text editor for colours, fonts and effects


Each flower icon in profile gardens could:
* **Bloom open on hover** with a tooltip (“Luna Lily: Symbol of quiet magic”)
* **Link to a filtered view** of authored branches for that flower type
* Visually change as you collect more (e.g. 1–3 is a bud, 4–7 is a full bloom, 8 \+ is a golden sparkle version)
* A sample **JavaScript animation** to make flowers bloom on like

## **Fableseed Application – Models and Data Relationships**
### *Entity Relationship Diagram*
This Entity Relationship Diagram for Fableseed was created using [Mermaid](https://mermaid.js.org/)’s built-in ERD diagramming tool. [ChatGPT](https://openai.com/index/chatgpt/) was used to help me understand the syntax and symbols used, as well as to double check my logic.

![][image41]

### *Overview*
This module contains the Django models for the **Fableseed** application, a storytelling platform where users create story seeds, branch stories, and earn flower rewards.  

**Models included:**
- **Fableseed**: Story seeds created by users.  
- **Flower**: Flowers associated with seeds and rewards.  
- **FableBranch**: Branching replies to seeds.  
- **UserProfile**: Extended user information for display purposes.  
- **UserFlower**: Tracks flowers earned by users from seeds and branches.  

The project uses Django’s built-in `User` model extended via a `UserProfile`.

### *Model Relationships (ERD Notation)*

**USER ||--|| USER_PROFILE : "has profile"**  
Each user has exactly one profile.  
The profile stores extended info like display name, picture, and bio, while the base USER holds login credentials nad name.

---

**USER ||--|{ FABLESEED : "writes"**  
 One user can write many Fableseeds.  
 Think of a Fableseed as a story idea or starter. A user might create several of them.

---

**USER ||--|{ FABLE_BRANCH : "writes"**  
 One user can write many Fable Branches.  
Each branch is a continuation of a story. A user can write different branches for different stories.

---

**FABLESEED ||--|{ FABLE_BRANCH : "has branches"**  
One Fableseed can grow into many branches.  
Each seed can sprout multiple paths (storylines), like chapters or what-if versions of a story.

---

**FABLESEED ||--|| FLOWERS : "assigned flower"**  
 Every Fableseed must be assigned exactly one flower type.  
 This flower is the "reward type" for the story seed. Different seeds may share the same flower type.

---

**USER ||--|{ USER_FLOWER : "earns"**  
 Each user can earn many flowers.  
 Flowers represent rewards or achievements tied to that user.

---

**FLOWERS ||--|{ USER_FLOWER : "is earned as"**  
 Each flower type can be earned by many users.  
 For example, a tulip might be earned by multiple users, tracked through a USER\_FLOWER record.

---

**FABLE_BRANCH ||--|{ USER_FLOWER : "earns flower"**  
A branch can reward one flower type, but multiple users can earn it, with quantity tracked per user.

 ---
**Explanation:**
- Each **user** has exactly **one profile** (`USER_PROFILE`).  
- A **user** can write many **Fableseeds** and **FableBranches**.  
- Each **Fableseed** can grow into multiple **FableBranches**.  
- Each **Fableseed** is assigned exactly **one flower type**, shared across seeds.  
- Users can earn multiple flowers (`USER_FLOWER`) as rewards.  
- Each **flower** type can be earned by many users.  
- A **FableBranch** can earn exactly **one flower type**, with the quantity stored in `USER_FLOWER`.  
### *Model Fields*

**USER**
| Field | Type | Notes |
|-------|------|------|
| id | int PK | Primary key |
| username | CharField | Unique login name |
| email | EmailField | Validated email |
| password | CharField | Password hash |
---
**USER_PROFILE**
| Field | Type | Notes |
|-------|------|------|
| id | int PK | Primary key |
| user_id | int FK | One-to-one link to `USER` |
| display_name | CharField | Name displayed in the app |
| profile_picture | CloudinaryField | User avatar |
| bio | TextField | Short biography |
| fablebuds_count | PositiveIntegerField | User’s reward points |
---
**FABLESEED**
| Field | Type | Notes |
|-------|------|------|
| seed | AutoField PK | Primary key |
| flower_type | FK | References `FLOWERS` (PROTECT) |
| title | CharField | Story seed title |
| body | CharField | Story prompt |
| approval_status | BooleanField | Pending or Approved |
| created_on | DateTimeField | Auto timestamp |
| edited_on | DateTimeField | Auto timestamp |
| author | FK | References `USER` (SET_NULL on deletion) |
| fablebuds_earnt | PositiveIntegerField | Reward points earned by seed |
---
**FABLE_BRANCH**
| Field | Type | Notes |
|-------|------|------|
| branch | AutoField PK | Primary key |
| seed | FK | References `FABLESEED` (PROTECT) |
| body | TextField | Story content |
| created_on | DateTimeField | Auto timestamp |
| edited_on | DateTimeField | Auto timestamp |
| author | FK | References `USER` (SET_NULL on deletion) |
| fablebuds_cost | PositiveIntegerField | **Deprecated** — now determined by flower type |
---
**FLOWERS**
| Field | Type | Notes |
|-------|------|------|
| flower | AutoField PK | Primary key |
| flower_name | CharField | Name of the flower |
| flower_image | CloudinaryField | Image of the flower |
| fablebuds_cost | PositiveIntegerField | Cost of the flower in fablebuds |
---
**USER_FLOWER**
| Field | Type | Notes |
|-------|------|------|
| id | AutoField PK | Primary key |
| user_id | FK | References `USER` |
| flower_id | FK | References `FLOWERS` |
| quantity | PositiveIntegerField | Number of this flower earned by the user |
| earned_from_seed_id | FK | References `FABLESEED` |
| earned_from_branch_id | FK | References `FABLE_BRANCH` |
| earned_on | DateTimeField | Timestamp of earning |
---

### *Cardinalities Table*

| Relationship | Type | Meaning |
|--------------|------|---------|
| USER → USER_PROFILE | 1..1 to 1..1 | Each user has exactly one profile. |
| USER → FABLESEED | 1..1 to 0..* | A user can write many seeds. Each seed has one author. |
| USER → FABLE_BRANCH | 1..1 to 0..* | A user can write many branches. Each branch has one author. |
| FABLESEED → FABLE_BRANCH | 1..1 to 0..* | A seed can have many branches. Each branch belongs to one seed. |
| FABLESEED → FLOWERS | 1..1 to 0..* | Each seed must have one flower type. A flower type can belong to many seeds. |
| USER → USER_FLOWER | 1..1 to 0..* | A user can earn many flowers. Each earned flower belongs to one user. |
| FLOWERS → USER_FLOWER | 1..1 to 0..* | A flower type can be earned by many users. |
| FABLE_BRANCH → USER_FLOWER | 1..1 to 0..1 | A branch can earn one flower type. Quantity is tracked per user. |

---

### *Design Notes*

- **User model**: Used Django’s built-in `User` model extended via `UserProfile` for extra fields.  
- **Author deletion**: Seeds and branches remain if a user deletes their account. The author is displayed as **“Deleted User”**.  
- **Flower cost**: The `fablebuds_cost` field in `FABLE_BRANCH` was removed; cost is now determined by the associated flower to ensure consistency and scalability.  
- **FableBranch rewards**: Each branch earns **one flower type**, but multiple users can earn it. Quantity is stored in `USER_FLOWER`.  

I ended up using Django’s built-in user model and extending it with a user profile model with extra fields. This was purely by accident as at the time I didn’t know you couldn’t extend the user model if you’d already migrated, which I had.

Halfway through development, I realised that storing `fablebuds_cost` on `FABLE_BRANCH` was redundant. The cost should be determined by the flower type, so that rarer flowers are more valuable and the system remains consistent and scalable.


## **Testing**

### *User Story Testing*

### *Automated Testing*

#### The W3C Markup Validation Service
I used the text input method to validate the HTML of each page. I copied the fully rendered HTML from the browser’s page source, ensuring that all Django template variables were resolved before checking.

**cultivate.html**<br>
*No errors or warnings to show.*<br>
Initial erors were as follows:
* Hamburger icon svg urls included https, when it should be http. Hamburger icon lives in base.html so corrected it there.
* The crispy form was wrapped in form tags, which doubled it up. Removed the form tags.
---

**fableseed-view.html**<br>
*No errors or warnings to show.*<br>
Initial errors were as follows: 
* Bad value for height and width set on img elements. Removed px.
* Time element wasn't in correct format (ISO8601), so added date:"c" for proper output
* Sections do not have headings - added headings.
---

**nursery.html** <br>
*No errors or warnings to show.*
Initial errors were as follows:<br>
* Bad value for height and width on img elements. Removed px.
* Trailing space on aria-curren page - removed the space.
---

**404.html**<br>
*No errors or warnings to show.*

---

**500.html**<br>
*No errors or warnings to show.*

---

**mygarden.html**<br>
*No errors or warnings to show.*<br>
Initial errors were as follows:
* Bad value for height and width on img elements. Removed px.
* Unclosed Div - this was the div containing the edit profile button.
---

**edit-profile.html**<br>
*No errors or warnings to show.*<br>
Initial errors were as follows:
* The crispy form was wrapped in form tags, which doubled it up. Removed the form tags.
---

**index.html**<br>
*No errors or warnings to show.*
No initial errors.

---

**about.html**<br>
*No errors or warnings to show.*
No initial errors.

___




#### The W3C CSS Validation Service
The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) reports errors for @layer and @property. These are not actual mistakes -  they are rules that are part of modern CSS features: Cascade Layers (@layer) for organizing groups of CSS rules, and CSS Houdini (@property) for creating animatable, typed custom properties. Current W3C validation tools do not yet recognize these newer specifications, but all modern browsers support them.<br>

There were no other warnings or errors - all clear.

#### The JSHint Validation Service
I used [JSHint Validation Service](https://jshint.com/) to check my JavaScript files.

**script.js**<br>
*Passed with no errors.*<br>
Initial errors related only to missins semi-colons, which has been rectified.

---

**gsap.js**<br>
*Passed with no errors.*<br>
Initial errors related to missing semicolons and undefined variables for gsap, SplitText and ScrollTrigger, so added /* global gsap, SplitText, ScrollTrigger */ at the top of the file to prevent the error, as the global variables are loaded via CDN.

---

#### CI Python Linter
I used the [Code Institute Python Linter](https://pep8ci.herokuapp.com/), along with the [VS Code autopep8 formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8#:~:text=The%20autopep8%20extension%20for%20Visual,how%20to%20customize%20this%20extension.&text=Customize%20autopep8%3A%20You%20can%20customize,args%20setting.) to ensure that my python files met [PEP8](https://peps.python.org/pep-0008/) standards.
All initial checks came back with errors, such as trailing spaces and lines that were too long. The list below is for the final check of each file.

* Nursery - models.py - *All clear, no errors found*
* Nursery - views.py - *All clear, no errors found*
* Nursery - urls.py - *All clear, no errors found*
* Nursery - tests.py - *All cleaar, no errors found*
* Nursery - forms.py - *All clear, no errors found*
* Nursery - apps.py - *All clear, no errors found*
* Nursery - admin.py - *All clear, no errors found*


#### The WAVE Webb Accessibility Evaluation Tool

**index.html**
0 errors

**about.html**
0 errors

**nursery.html**
1 error relating to an empty table header. Rectified this by adding a font awesome icon.
0 errors.

**view-fableseed.html**
0 errors

**cultivate.html**
0 errors

**login.html**
0 errors

**signup.html**
0 errors

**mygarden.html**
0 errors

**edit-profile.html**
0 errors

**404.html**
0 errors

**500.html**
This page is a duplicate of 400.html

#### Chrome Lighthouse

**Index.html**
*Mobile Results*
Performance was at 80, so added STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage" to settings.py, as it serves compressed static files with caching
and, 'django.middleware.gzip.GZipMiddleware' to middleware in settings.py as it compresses responses like HTML, JSON and sometimes CSS/JS.
Best practice is on the low side due to cookies set by Cloudinary.
*Desktop Results*
Initial tests indicated that etwork despondency tree could be improved - created an extra css block on base.html and used that for font awesome on only the pages that use font awesome icons. I also added preconnect links for google fonts in the head of base.html, to let the fonts start downloading straightaway instead of waiting for the stylesheets to load. These measures improved desktop and mobile performance.
*Final results for both:*

Accessibility at 95 is due to the use of aria labelling by GSAP animation library. I have split paragraph text and aria shouldn't be applied to paragraphs.

**about.html**
*Mobile results*
*Desktop results*

**Nursery.html**
*Mobile results*
Performance low due to file format and size of plant images. Resized, changed format, replaced on cloudinary and performance improved.
*Desktop results*

**view-fableseed.html**
*Mobile results*
Best practice score adversely impacted by the cloudinary cookies, which are abundant on this page due to the use of the placeholder imager that is stored on cloudinary and used for all profiles that haven't selected their own profile image.
*Desktop results*

**cultivate.html**
*Mobile results*
*Desktop results*

**login.html**
*Mobile results*
*Desktop results*

**signup.html**
*Mobile results*
*Desktop results*

**mygarden.html**
*Mobile results*
*Desktop results*

**edit-profile.html**
*Mobile results*
*Desktop results*

**404.html**
*Mobile results*
*Desktop results*

**500.html**
*Mobile results*
*Desktop results*

Best Practice score was relatively low on all pages across mobile and desktop, worse on desktop than on mobile. This came directly from the fact that Cloudinary assets come from res.cloudinary.com, a 3rd party domain, and Chrome is phasing out third party cookies. My images load fine and give good perofmrance, but I can't fix Cloudinary's cookie headers because its on their CDN configuration. I tried adding CLOUDINARY_STORAGE = {'SECURE': True,} to settings.py, but it didn't help in the slightest and adversely affected the performance of the pages, so I took it back out again. I double-checked my images by opening them up in a new tab to look at their urls, and they are being delivered securely by https and appear as 'Allowed" in the trust and safety section of Best Practice. I think for a future project I would look into an alternative image-hosting site which doesn't cause these best practice issues.


### *Manual Testing*

### *Unit Tests*

## 

## **Technology used**
* [Adobe Color](https://color.adobe.com/)  
* [Adobe Firefly](https://www.adobe.com/uk/products/firefly.html)  
* [Adobe Photoshop](https://www.adobe.com/products/photoshop.html)  
* [Canva](https://www.canva.com/en_gb/)  
* [Cloudinary](https://cloudinary.com/)  
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/)  
* [Daisy UI](https://daisyui.com/)  
* [DJ-database-url](https://pypi.org/project/dj-database-url/)  
* [Django](https://www.djangoproject.com/)  
* [Django allauth](https://docs.allauth.org/)  
* [Google Docs](https://docs.google.com/)  
* [Google Drive](https://drive.google.com/drive/quota)  
* [GSAP](https://gsap.com/)  
* [Gunicorn](https://gunicorn.org/)  
* [Javascript](https://www.w3schools.com/js/)  
* [Mermaid](https://mermaid.js.org/)  
* [Paint.NET](http://Paint.NET)  
* [Psycopg2](https://pypi.org/project/psycopg2/)  
* [Tailwind CSS](https://tailwindcss.com/)  
* [Whitenoise](https://whitenoise.readthedocs.io/en/stable/django.html)

## **Coding help**

* Verbose names for models in the admin site - [Django Model Admin Display](https://unfoldai.com/django-model-admin-display-name/#:~:text=Model%20instance%20display%20names,-The%20simplest%20way&text=When%20Django%20renders%20this%20model,see%20the%20actual%20country%20name.)  
* Help understanding returning Django model data to my website [Django model data display](https://medium.com/@justp1x3l/return-django-model-data-to-our-website-98d1e12b854d)  
* Help putting together unit tests [GeeksforGeeks Python unit test tutorial](http://geeksforgeeks.org/python/unit-testing-python-unittest/)  
* Help displaying images in admin model for flowers [dev.to](https://dev.to/vijaysoni007/how-to-show-images-of-the-model-in-django-admin-5hk4)  
* Help with Tailwind tables - [Materialtailwind.com](https://www.material-tailwind.com/docs/html/table)  
* Help with Tailwind media query classes - [StackOverflow](https://stackoverflow.com/questions/67446381/how-in-tailwindcss-table-hide-column-on-small-devices)  
* Help understanding how to make a page for individual fableseed posts after clicking on a link \- [mostlypython.com](https://www.mostlypython.com/django-from-first-principles-part-10/)  
* Help understanding how to extend the user model and connect it up when a new user is created [medium.com](https://medium.com/@karimdhrif4444/mastering-user-management-comprehensive-guide-to-extending-djangos-user-model-51c2ccd793d4)  
* Help creating a stacked inline user profile added to the base user model - [learndjango.com](https://learndjango.com/tutorials/django-userprofile-model)  
* Help with redirecting a user to another view on submission of a form - [geeksforgeeks](https://www.geeksforgeeks.org/python/django-redirects/)  
* Help with querying and getting parameters in a url - [djangocentral](https://djangocentral.com/capturing-query-parameters-of-requestget-in-django/)  
* Help on how to build a crispy forms helper layout to style form fields with tailwind classes - [BugBytes](https://www.youtube.com/watch?v=g-5tuE2d6JI)  
* Django login/logout tutorial - [learndjango.com](https://learndjango.com/tutorials/django-login-and-logout-tutorial)  
* Extending django allauth forms - [geeksforgeeks](https://www.geeksforgeeks.org/python/python-extending-and-customizing-django-allauth/)  
* Styling dt and dd tags in a description list, used on the mygarden page - [geeksforgeeks](https://www.geeksforgeeks.org/css/how-to-write-dt-and-dd-element-on-the-same-line-using-css/)  
* Help understanding how create functionality to edit profiles - [dev.to](https://dev.to/earthcomfy/django-update-user-profile-33ho)  
* Help understanding GSAP SplitText - [GSAP](https://gsap.com/docs/v3/Plugins/SplitText/)  
* Help styling the file input type - [Stack Overflow](https://stackoverflow.com/questions/572768/styling-an-input-type-file-button)  
* Website for generating a CSS glow effect, also generates Tailwind CSS classes - [notchtools.com](https://notchtools.com/css-glow-generator)  
* OKLCH colour picker for some of the Daisy UI theme colours - [oklch.com](https://oklch.com/#0.9612,0,0,100)
* Couldn't get profile area borders on fablebranch replies to alternate colours. ChatGPT helped me by suggesting n if statement: {% if forloop.counter|divisibleby:2 %} border-base-300 {% else %} border-primary-content {% endif %}. Worked really well.


## **Interesting Bugs**

* Discovered that the crispy forms helper layout couldn’t or wouldn’t target the select dropdown box of database flowers. Ended up styling that myself in a custom.css file after trawling through crispy layout templates for far longer than necessary.  
* Gitignore in .venv wasn’t hiding [env.py](http://env.py) - I had this setup from a codealong project from code institute. Added files to project level gitignore and ran git rm -r cached to stop git from tracking and then changed my env variables and secret key.  
* Profile image not updating when user edits via the form - needed enctype=multipart/form-data hard-coding on the template rather than through the form in [forms.py](http://forms.py)  
* Couldn’t figure out how to style the file input field on the edit profile for. Ended up with a a mix of styling via the Crispy forms helper layout and styling input[type="file"] directly in custom.css to make the file picker look like a properly styled button.  
* Chrome Lighthouse performance score on index.html was poor on mobile and okay on desktop - it came back with lots of suggestions and errors I didn't understand. After using ChatGPT to help me understand what was going on, I made the following changes:
    * Added GZip middleware to settings.py for response compression
    * Added whitenoise compressed static storage config to serve compressed static files with caching. 
    * Removed font awesome link from base.html and replaced with an extra_css block, then served font awesome link only on pages that actually use it - about.html and nursery.html. 
    * Added preconnect links to google fonts in the head of base.html to allow the fonts to immediately load. 

All these measures massively improved google lighthouse performance on mobile and desktop

## **Credits**

### *Media*

* [Bas Meeuws \- Tulip \#17](https://www.the-low-countries.com/article/the-seventeenth-century-tulip-field-of-bas-meeuws/)  
* [Smokedsystem.com \- wildfire flowers](https://smokedsystem.com/which-flowers-often-appear-after-a-wildfire/)  
* [freepik.com \- plant growing from soil](https://www.freepik.com/free-ai-image/plant-growing-from-soil_268350286.htm)