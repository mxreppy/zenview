setup python3 virtual env - install deps

setup npm, install deps

run gulp dev

won't work - install angular

npm install angular --save

try again

## MacOS getting started instructions

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
