
Pre-beginner Wagtail
==================
A not-even-built-yet version of Wagtail. Used for a workshop where people turn it into something like [Beginner Wagtail](https://github.com/heymonkeyriot/beginner-wagtail/)

# Installation locally
It should be sufficient to simply run `vagrant up` to load the project.
```
vagrant up
vagrant ssh
python manage.py runserver 0.0.0.0:8000
```

### Loading mock data
You can't load any data until you've built your models, so as far as you know there's no mock data!

### Troubleshooting local installation problems
On the `vagrant up` command the vagrant/provision.sh file will run

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

Occassionally (because the computer has gone to sleep etc) that process may not run smoothly. In that instance wait for `vagrant up` to complete, then `vagrant ssh` into the VM and run the above commands.

# Installation remotely
This project isn't designed to be deployed to a remote server, but rather for local playing and testing. An upcoming release will allow it to be deployed remotely.

# Apps included
If apps with empty models count as apps

- People
- Skills
- Location

# Purpose
This project is to help support a workshop giving a super simple introduction to what Wagtail is, and how easy it is to build websites using it.

## Documentation
There is inline commenting through the project, but more details docs are planned for an upcoming release.

