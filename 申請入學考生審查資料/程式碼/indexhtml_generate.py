import webbrowser
import json
import sys
import pandas as pd
from pathlib import Path
import json
import math
import json2table
import json
from json2html import *
import os
import webbrowser

 
 
GEN_HTML ="index.html"
   
f = open(GEN_HTML,'w', encoding='utf-8-sig')
with open( 'index.txt', 'r' ,encoding='utf-8') as g:
    str1 = g.read() 
    
message = """
<html><head>
<link href="首頁.css" rel="stylesheet" type="text/css">
<script src="new.js"></script>       </head>
    <table>
<thead>
    <tr>
        <th colspan="20">科系列表</th>
    </tr>
</thead>
<tbody>

%s
        </tbody>
</table>

</body>
</html>
"""%(str1)
    
f.write(message) 
    
f.close()  




