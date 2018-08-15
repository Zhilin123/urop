# urop
Summer 2018 Research Internship supervised by Dr Andrew Caines and Russell Moore, NLP Computer Lab Cambridge.

for an example see zw322.pythonanywhere.com (username: a@c.com, pw: asd) Ideally, use on a phone

Basically a webapp that allows students to do math questions

Tasks done by Week 5
- Webapp uses a flask web server
- Questions can be set up with text and images
- responses saved in a sqlite database
- Student centered design
    - embedded hints (videos etc)
        - when students are not sure about the answer, can view it to be clearer
    - users can click on difficult words to find out their definitions
    - users can translate into different languages such as indian languages
        - for now, chinese is used for demo because its the only other language I can read
- convert some images into html table elements etc (ie question 1, 2 and more )
- improve logging (log use of hints and translation)

Tasks to do:

- include more questions into the database
    - free resources available online?
    - classify questions based on topics
    - automate suggesting hints based on question type
    - some questions from collaborators?
- change logging to per question basis, including session id
- allow student to pick up from previously attempted question
- front end user profile
- create a page where users can just upload questions
- Pack more pedagogically significant features into the webapp
    - maybe having questions sorted into categories for easy practice
    - make it into a gamified environment
    - step by step solutions to improve extent of scaffolding
    - make it into a companion website for their textbook / popularly used learning resources so that they can consult the website when they encounter difficulties with learning on their textbook.
- Convert the website into a phone app that can be used offline (a bit of this)
- Awaiting feedback from collaborator as well as supervisors

Notes

- when uploading to pythonanywhere, copy the users.db and qns.db to the root folder, for some reason, it doesn't work in the child folder
