# -*- coding: utf-8 -*-

import json
import sys
import os

def get_info_environment(filename, env):
        path_name_file= (os.path.join(os.path.abspath(os.path.realpath(filename))))
        try:
            file = open(path_name_file,'a+')
            json_string = file.read()
            if json_string.strip():
                data = json.loads(json_string)
            return data['QA']
        except Exception as error:
            print "Could not open file:", filename, error
            sys.exit()
