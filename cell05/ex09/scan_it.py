#!/usr/bin/env python3

import sys
import re

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    content = sys.argv[2]
    pattern = f'({keyword})'

    result = re.findall(pattern, content)
    result_count = len(result)

    if result_count >= 1 :
        print(result_count)
    else:
        print('none')
else:
    print('none')
