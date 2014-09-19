setup python3 virtual env - install deps

setup npm, install deps

run gulp dev


## MacOS getting started instructions

### dependencies

1.  fork https://github.com/aheld/zenview.git to your repo
1.  git clone https://github.com/<you>/zenview.git
1.  brew install python3  # if needed
1.  cd zenview/
1.  python3 -m venv ./zenvenv
1.  source ./zenvenv/bin/activate
1.  # remove ionotify from requirements
1.  pip install -r requirement.txt
1.  cp config_example.py config.py
1.  # edit to add in your own credentials
1.  nosetests zd_lib.py --nocapture
2.  npm install

### running

1.  python:  in a shell run ``python server.py`` and let it stew
2.  gulp:  in another shell run ``./node_modules/.bin/gulp dev``

### testing

1.  load default web page ``http://127.0.0.1:5000/``
2.  edit something e.g. ``app/index.html``
3.  save in editor
4.  observe live reload in page
5.  load api ''http://localhost:5000/api/zendesk/ticket/11803''
