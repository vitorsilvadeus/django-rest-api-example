# django-rest-api-example
A simple example of a Django REST API <br>
<br>
METHOD: GET<br>
<br>
Query params:<br>
  lists:<br>
     -> channels,<br> 
     ->countries, <br>
     ->os, <br>
     ->fields(any fields of the Performance model to be listed in the response plus the cpi i.e spends/installs)),<br>
     ->group_by(fields to group query by (only fields listed in fields list),<br>
     ->order_by (fields do order by(preced by '-' for descending order)))<br>
  uniques:<br>
     ->date_from (for the data field in the '%Y-%m-%d' format),<br>
     ->date_to (for the data field in the '%Y-%m-%d' format)<br>
    
