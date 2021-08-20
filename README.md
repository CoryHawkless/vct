# newStack API
An open source solution to the complexities of manaing virtual infrastrucuture
Very opinionated VM\ Networking and storage orchestration system. By being strongly opinionated we can elimate significant amounts of complexity, this is not a 'one-size-fits-all' solution. It does what it does and nothing else, but this keep the code base clean, simple and stable

### Terminal commands
Note: make sure you have `pip` and `virtualenv` installed.

    Initial installation: make install

    To run test: make tests - *Broken

    To run application: make run

    To run all commands at once : make all

Make sure to run the initial migration commands to update the database.
    
    > python manage.py db init

    > python manage.py db migrate --message 'initial database migration'

    > python manage.py db upgrade


### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/


### Using Postman ####

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"

    Postman examples in postman folder

### Reference article ###
https://medium.freecodecamp.org/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563