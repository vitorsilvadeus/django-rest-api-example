# django-rest-api-example
A simple example of a Django REST API

METHOD: GET

Query params:
  lists:
     -> channels, 
     ->countries, 
     ->os, 
     ->fields(any fields of the Performance model to be listed in the response plus the cpi i.e spends/installs)),
     ->group_by(fields to group query by (only fields listed in fields list),
     ->order_by (fields do order by(preced by '-' for descending order)))
  uniques:
     ->date_from (for the data field in the '%Y-%m-%d' format),
     ->date_to (for the data field in the '%Y-%m-%d' format)
    
