# RecipeBox

Create a new application that serves recipes from different authors.

## Intended layout

- An index page that lists all titles of the loaded recipes.
- Each title is a link that takes you to a single page with the content of that recipe.
- Each detailed view for a recipe has the author name, along with all the information for the recipe arranged in a reasonable format.
- Clicking on the author's name should take you to an Author Detail page, where you can see a list of all the recipes that Author has contributed to.
- Make editing all of the models accessible through the admin panel only.
- Homepage has links for adding recipes and adding authors.
- A log in and a log out button that handle the authentication of the current user
- Non-staff users can only submit recipes selecting themselves and not others as an author.

There are seven pages in total:

### 3 simple views:

- A simple view for the home page
- A recipe detail view
- An author detail view

### 3 form views:

- To add recipes
- To add authors / Create accounts
- A log in page so that people can sign in

### 1 error view:

- Displays an error when non-staff users try to acces the author creation page

The admin panel will handle the creation views.

### Author model

- Name
- User (**OnetoOneField**)
- Username
- Bio

_The password field wil be handled by **forms**_

### Recipe model

- Title
- Author
- Description
- Time Required
- Instructions
