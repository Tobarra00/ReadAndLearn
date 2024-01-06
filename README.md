<header>
    <h1>Read&Learn 📚</h1>
</header>

<div>
    <p>Welcome to Read&Learn, a Django-based backend project that aims to simulate a web page filled with a vast collection of books, allowing users to explore detailed information about each book. 
      The primary focus of Read&Learn lies in its backend functionality, ensuring a seamless experience for book enthusiasts.</p>
    
</div>

<section>
  <h2>Features</h2>

  All features will be followed by a demonstration video showing as much as possible. In some cases (such as the filters video), some parts of the we don't appear in the video but are actually there.<br><br>
<ul>
<li>Book Information: Access comprehensive details about each book in the collection, including title, author, genre, and more.</li><br><br>



https://github.com/Tobarra00/ReadAndLearn/assets/94169504/1fe647a8-285f-4845-a7d9-6d7f42549d63


<br><br>
<li>Search Books by Filters: Explore books easily by utilizing search filters such as title, genre, and number of pages. This feature enhances the user experience, allowing for a more targeted and personalized discovery of books.</li><br><br>



https://github.com/Tobarra00/ReadAndLearn/assets/94169504/21aafad1-38a8-4206-a985-9d7e8f019d07



<br><br>
<li>User Registration: To unlock personalized features, users can register on Read&Learn. This opens up the ability to save and manage their favorite books.</li><br><br>


https://github.com/Tobarra00/ReadAndLearn/assets/94169504/62729a8d-4462-4f9d-b78d-e44f95992158


<br><br>
<li>Create and Manage Lists: Users can create personalized lists to categorize and organize their favorite books. Each book can be added to these lists for easy reference.</li><br><br>


https://github.com/Tobarra00/ReadAndLearn/assets/94169504/d9c59b4c-9e88-4ed6-820d-c393d15048cc


<br><br>
<li>Duplicate Check: When adding a book to a list, Read&Learn checks if the book is already present in any of the user's existing lists, preventing duplication.</li><br><br>


https://github.com/Tobarra00/ReadAndLearn/assets/94169504/707291f3-fddf-41b8-908d-45715002ac7f


<br><br>
<li>Sharing Lists: Enhance the reading experience by sharing your personal lists with other users. It's a great way to discover new books and share your literary preferences.</li><br><br>


https://github.com/Tobarra00/ReadAndLearn/assets/94169504/e13889db-e2bc-4179-90a3-07d426ceb483


<br><br>
<li>List Editing and Deletion: Users have the flexibility to edit or delete their lists, ensuring full control over their curated content. However, shared lists remain intact to maintain a shared experience.</li><br><br>

<br><br>
<li>Class-based and function-based views: The project uses both class-based and function-based views, providing a versatile approach to handling different aspects of the application.</li><br><br>

<br><br>
<li>Custom Commands for Data Loading: To populate the database, custom commands have been implemented to load books from JSON formatted files. This ensures efficient and consistent data management, avoiding duplicate data.</li><br><br>

<br><br>
  </ul>
</section>


<section>
    <h2>Technologies 🧑‍💻</h2>
    <p>These are the technologies used in this project:</p>
    <ul>
        <li>Python</li>
        <li>Django</li>
        <li>Postgresql</li>
        <li>HTML</li>
        <li>CSS</li>
        <li>Javascript</li>
        <li>Bootstrap</li>
    </ul>

</section>

<section>
    <h2>How to make it work 🔧</h2>
    <p>In this section I will show step by step how to make this code work:</p>
    <ol>
        <li>Use <code>git clone</code> to clone the repository. After that, create a virtual environment with:<br><br>
        <ul>
            <li><code>pip install virtualenv</code><br><br></li>
            <li><code>virtualenv venv</code><br><br></li>
        </ul>
        After that, activate the virtual environment and use this command to install the requirements to make the project work properly:<br><br>
        <ul>
            <li><code>pip install -r requirements.txt</code><br><br></li>
        </ul>
        </li>
        <li>The next step is to manage the database. Create a local postgresql database and fill the <code>NAME</code>, <code>USER</code> and <code>PASSWORD</code> fields in the <code>settings.py</code> file. To continue, apply the migrations:<br><br>
            <ul>
                <li><code>python manage.py makemigrations</code><br><br></li>
                <li><code>python manage.py migrate</code><br><br></li>
            </ul>
          Now you should have everything set up, except for the actual books. I have created a custom command to load books into the database. Use the <code>books.json</code> file to do so. If you want to add more books to the database, you should use the same format.
          Once you have all the books you want, load them into the database with the command:<br><br>
          <ul>
                <li><code>python manage.py load_books</code><br><br></li>
            
![image](https://github.com/Tobarra00/ReadAndLearn/assets/94169504/fdbfc2ec-4db5-4b41-be32-e0a948fa65ce)
          </ul>
        </li>
        <li>Finally, if everything went right, you should be able to run the server and visualize the website and utilize its functionalities by using the command:<br><br>
            <ul>
                <li><code>python manage.py runserver</code><br><br></li>
            </ul>
        </li>
        <li>And that's all, you should be able to navigate and try the website with all of its functionallity 😉.<br><br></li>
    </ol>
</section>


<section>
    <h2>
        Contact me:
    </h2>
    <p>In case you have any doubt or you are interested about my work, you can contact me here: </p>
    <ul>
        <li><a href="https://www.linkedin.com/in/pedro-tobarra-leal/">Linkedin</li>
        <li>My email: <a href="mailto:pedro.tobarra.leal@gmail.com">Pedro.tobarra.leal@gmail.com</a></li>
    </ul>
</section>
