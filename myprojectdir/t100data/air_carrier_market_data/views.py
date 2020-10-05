# Create your views here.
import pdb
from django.views.generic import ListView
from django.db.models import Max, Sum, Count, Avg, Min
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.views.generic.detail import SingleObjectMixin


from . models import MarketData



class MarketDataList(ListView):
    model = MarketData

# What are the top 5 airports in terms of: Total passengers by origin
class Top5AirportsPaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total passengers by destination
class Top5AirportsPaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_pax=Sum('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_destination.html"



# What are the top 5 airports in terms of: Total Freight by origin
class Top5AirportsFreByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_fre=Sum('freight')) \
                        .order_by('-total_fre')[0:5]
    template_name="freightorder_list_origin.html"
	
	
	
	
# What are the top 5 airports in terms of: Total Freight by destination
class Top5AirportsFreByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_fre=Sum('freight')) \
                                 .order_by('-total_fre')[0:5]
    template_name="freight_list_destination.html"


# What are the top 5 airports in terms of: Total Mail by origin
class Top5AirportsMailByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:5]
    template_name="mailorder_list_origin.html"
	
	
	
	
# What are the top 5 airports in terms of: Total Mail by destination
class Top5AirportsMailByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_mail=Sum('mail')) \
                                 .order_by('-total_mail')[0:5]
    template_name="mail_list_destination.html"


# What are the top 5 airports in terms of: Total Distance by origin
class Top5AirportsDistByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_dist=Sum('distance')) \
                        .order_by('-total_dist')[0:5]
    template_name="distorder_list_origin.html"
	
	
	
	
# What are the top 5 airports in terms of: Total Distance by destination
class Top5AirportsDistByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_dist=Sum('distance')) \
                                 .order_by('-total_dist')[0:5]
    template_name="dist_list_destination.html"

# Which airport reported the longest distance by month?
class TopDistanceByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_distance_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_distance=Max('distance')) \
                .order_by('-total_distance')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list


# Which airport reported the most passengers by month?
class TopPassengerByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_passenger_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_passengers=Max('passengers')) \
                .order_by('-total_passengers')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list


# Which airline reported the most freight carried?
class AirlineMostFreight(ListView):
    context_object_name = "carrier_list"
    queryset = MarketData.objects.values('carrier_id','carrier_name') \
                                 .annotate(total_fre=Sum('freight')) \
                                 .order_by('-total_fre')[0:1]    
    template_name="airline_reported_freight.html"
	

# Which airline reported the most passengers carried?
class AirlineMostPassenger(ListView):
    context_object_name = "carrier_list"
    queryset = MarketData.objects.values('carrier_id','carrier_name') \
                                 .annotate(total_passengers=Sum('passengers')) \
                                 .order_by('-total_passengers')[0:1]  
    template_name="airline_reported_passengers.html"


# Which airline reported the most mail carried?
class AirlineMostMail(ListView):
    context_object_name = "carrier_list"
    queryset = MarketData.objects.values('carrier_id','carrier_name') \
                                 .annotate(total_mail=Sum('mail')) \
                                 .order_by('-total_mail')[0:1] 
    template_name="airline_reported_mails.html"

		
		
		
# Which airline reported the longest flight distance?
class AirlineMostDistance(ListView):
    context_object_name = "carrier_list"
    queryset = MarketData.objects.values('carrier_id','carrier_name') \
                                 .annotate(total_distance=Max('distance')) \
                                 .order_by('-total_distance')[0:1] 
    template_name="airline_reported_distance.html"



# Rank order passengers carried, by month, for these airlines:


class passenger_by_month_for_airlines(ListView):
    context_object_name = "carrier_list"
    template_name="passenger_by_month_for_airlines.html"


    def get_queryset(self):
        carrier_id = self.kwargs['carrier_id']
        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_id',
                        'carrier_name',
                        'month') \
                .filter(month__exact=month,carrier_id__exact=carrier_id) \
                .annotate(count_passengers=Count('passengers')) \
                .order_by('-count_passengers')
            
            # off by one error for assignment

            month_list.append(queryset)
            
        # return list
        return month_list


# Which airline reported the longest flight distance?
class AirlineMostDistance(ListView):
    context_object_name = "carrier_list"
    queryset = MarketData.objects.values('carrier_id','carrier_name') \
                                 .annotate(total_distance=Max('distance')) \
                                 .order_by('-total_distance')[0:1] 
    template_name="airline_reported_distance.html"



# Find the average number of passengers for flights into:


class AverageNumberPassengersByAirport(ListView):
    context_object_name = "airport_list"
    template_name="average_number_of_paasenger_by_airport.html" 
    def get_queryset(self):
        dest_iata_code = self.kwargs['dest_iata_code']   
        queryset = MarketData.objects.values('dest_iata_code') \
                                .annotate(avg_passengers=Avg('passengers')) \
                                .filter(dest_iata_code=dest_iata_code)  
        # return list
        return queryset   
        


# Find the average volume of freight for flights departing:


class AverageVolumeofFreightByAirport(ListView):
    context_object_name = "airport_list"
    template_name="average_volume_of_freight_by_airport.html" 
    def get_queryset(self):
        orig_iata_code = self.kwargs['orig_iata_code']   
        queryset = MarketData.objects.values('orig_iata_code') \
                                .annotate(avg_freight=Avg('freight')) \
                                .filter(orig_iata_code=orig_iata_code)  
        # return list
        return queryset   



#What city pairs represent the most freight carried for the longest distance?
class CityPairMostFreightandMaxDistance(ListView):
    context_object_name = "city_list"
    queryset = MarketData.objects.values('orig_city_name','dest_city_name') \
                                 .annotate(max_distance=Max('distance'), sum_freight=Sum('freight')) \
                                 .order_by('-sum_freight','-max_distance' )[0:1] 
    template_name="city_pair_with_max_freightanddist.html"



#What city pairs represent the most mail carried for the shortest distance?
class CityPairMostMailandShortDistance(ListView):
    context_object_name = "city_list"
    queryset = MarketData.objects.values('orig_city_name','dest_city_name') \
                                 .annotate(max_distance=Min('distance'), sum_mail=Sum('mail')) \
                                 .order_by('-sum_mail','-max_distance' )[0:1] 
    template_name="city_pair_with_most_mail_and_short_distance.html"