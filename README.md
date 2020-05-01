# RecipeBox V1

Create a new application that serves recipes from different authors.

## Intended layout

- An index page that lists all titles of the loaded recipes. 
- Each title is a link that takes you to a single page with the content of that recipe.
- Each detailed view for a recipe has the author name, along with all the information for the recipe arranged in a reasonable format.
- Clicking on the author's name should take you to an Author Detail page, where you can see a list of all the recipes that Author has contributed to.
- Make editing all of the models accessible through the admin panel only.

There are three types of pages: a simple list view (`main.html`), a recipe detail view (`recipes.html`), and an author detail view (`authors.html`). And the admin panel will handle the creation views.

### Author model

- Name
- Bio

### Recipe model

- Title
- Author
- Description
- Time Required
- Instructions
