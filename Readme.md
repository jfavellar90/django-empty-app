# Getting started

# Installation of dependencies
```
pip install -r requirements/dev.txt
```

# Management and usage
## Development:
```
sudo su twototango
source ../venvs/tango.app/bin/activate

python manage.py runserver 0.0.0.0:8000 --settings=app.settings.dev
```

## Running Matches
```
python manage.py create_empty_matches --settings=app.settings.dev [options]
```
Options:

* p (--pack): Select id of the pack for which matches will be generated
* r (--ruleset): Select id of the ruleset that will be used for all the generated matches
* (--verbose)
* (--silent)

```
python manage.py run_matches --settings=app.settings.dev [options]
```
Options:

* m (--match): Select a specific match id to be run
* l (--list): Select a list of match ids to be run. e,g: 1,2,5-8
* p (--pack): Will run all the matches where the profiles come out
               of a cross product of the loaded people on a pack
* r (--ruleset): Will rull matches that have this as its defined ruleset.
                  Can be used together with --pack for better results
* e (--persons): Select a list of person ids to run all the matches among them. See --nostrict
* (--verbose)
* (--silent)
* (--nostrict): modifier to get the matches only using one ID, either left or right
* d (--dev): Select fake profiles and create a match with them
* R (--ruleset-pattern): Select the ruleset to be loaded. Only for development


## Running matches remotely

```
sudo su twototango -s /bin/bash
cd /t2t/app/twototango/tango.app/
source ../venvs/tango.app/bin/activate
python manage.py create_empty_matches --settings=app.settings.prod -p X -r X
python manage.py run_matches --settings=app.settings.prod -p X -r X
```

# Test

```
coverage run --branch --source='app.djangoapps.matching.rules' manage.py test app.djangoapps.matching.tests --settings=app.settings.test
coverage html
```

# Notes




