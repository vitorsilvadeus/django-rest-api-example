from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, FloatField, F
from performance.models import Performance
from datetime import datetime


# TEST URL:
# ?date_from=2017-05-17&date_to=2017-05-17&fields=date&fields=cpi&fields=os&fields=channel&fields=clicks&group_by=os&group_by=channel&order_by=-os&order_by=channel
# SQL:
# SELECT date,os,channel,SUM(spend / installs) AS cpi,SUM(clicks) AS clicks
# FROM performance_performance
# WHERE date >= '2017-05-17' AND date <= '2017-05-17'
# GROUP BY date,os,channel
# ORDER BY channel ,os DESC


'''API endpoint, which is capable of filtering, grouping and sorting. Dataset represents performance metrics (impressions, clicks,
 installs, spend, revenue) for a given date, advertising channel, country and operating system'''

class PerformanceAPIView(APIView):

    def get(self, request):

        query_data = dict(request.query_params)
        p = Performance.objects.all()

        date_from = query_data.get('date_from',None)
        if date_from is not None :
            date_from = datetime.strptime(date_from[0], '%Y-%m-%d')
            p = p.filter(
                date__date__gte=date_from
            )

        date_to = query_data.get('date_to',None)
        if date_to is not None :
            date_to = datetime.strptime(date_to[0], '%Y-%m-%d')
            p = p.filter(
                date__date__lte=date_to
            )

        channels = query_data.get('channels',None)
        if channels is not None :
            p = p.filter(channel__in=channels)

        countries = query_data.get('countries',None)
        if countries is not None :
            p = p.filter(country__in=countries)

        os = query_data.get('os',None)
        if countries is not None :
            p = p.filter(os__in=os)

        # ->Two annotate calls in order to achieve cpi calc due
        # to the fact that annonate on same field in same
        # annotation call raises error
        p = p.values(*query_data.get('group_by',[])).annotate(
            cpi=Sum(F('spend') / F('installs'), output_field=FloatField())).annotate(
            impressions=Sum('impressions'),
            clicks=Sum('clicks'),
            installs=Sum('installs'),
            spend=Sum('spend'),
            revenue=Sum('revenue'),
        ).order_by(
            *query_data.get('order_by', [])
        )

        return Response(p.values(*query_data.get('fields',[])))
