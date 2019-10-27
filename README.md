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
     
Use case url examples:<br>
    &nbsp;1. Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order:<br> ?date_to=2017-06-01&fields=channel&fields=country&fields=impressions&fields=clicks&group_by=channel&group_by=country&order_by=-clicks <br><br>
    &nbsp;2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order:<br> ?date_from=2017-05-01&date_to=2017-05-31&fields=date&fields=installs&group_by=date&order_by=date<br><br>
    &nbsp;3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order:<br> ?date_from=2017-06-01&date_to=2017-06-01&fields=os&fields=revenue&group_by=os&order_by=-revenue<br><br>
    &nbsp;4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order:<br> ?fields=channel&fields=cpi&fields=spend&group_by=channel&order_by=-cpi<br>

    
