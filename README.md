# django-rest-api-example
A simple example of a Django REST API <br>
<br>
METHOD: GET<br>
<br>
Query params:<br>
  &nbsp; lists:<br>
     &nbsp;&nbsp;&nbsp;-> channels,<br> 
     &nbsp;&nbsp;&nbsp;->countries, <br>
     &nbsp;&nbsp;&nbsp;->os, <br>
     &nbsp;&nbsp;&nbsp;->fields(any fields of the Performance model to be listed in the response plus the cpi i.e spends/installs)),<br>
     &nbsp;&nbsp;&nbsp;->group_by(fields to group query by (only fields listed in fields list),<br>
     &nbsp;&nbsp;&nbsp;->order_by (fields do order by(preced by '-' for descending order)))<br>
  &nbsp;uniques:<br>
     &nbsp;&nbsp;&nbsp;->date_from (for the data field in the '%Y-%m-%d' format),<br>
     &nbsp;&nbsp;&nbsp;->date_to (for the data field in the '%Y-%m-%d' format)<br>
    
