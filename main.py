"""
Demo SocketIO application

For simple test cases. To start the program, install the requirements said
in the 'requirements.txt' file and start a 'uvicorn' server as stated
below:

# Create and activate a virtual environment
$ python3 -m venv .venv
$ source .venv/bin/activate

# Install requirements
(.venv) $ python3 -m pip install -r requirements.txt

# Start a uvicorn server on http://localhost:3000 with '--reload' support
# which watches the directory contents for change and reloads on change
# (very handy during fast developement).
(.venv) $ python3 -m uvicorn main:app --reload \
                  --host localhost --port 3000

Original author:
    Pedram Ashofteh Ardakani <pedramardakani@pm.me>
Contributing author(s):

Copyright(c) 2022

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
version 3 or later as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; see the file COPYING.LIB.  If not, write
to the Free Software Foundation, Inc., 51 Franklin Street, Fifth
Floor, Boston, MA 02110-1301, USA.
"""

from project import create_app

app = create_app()
