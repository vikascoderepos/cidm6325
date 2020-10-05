# urls.py
from django.urls import path
from air_carrier_market_data import views
from . views import MarketDataList, \
                    Top5AirportsPaxByOrigin, \
                    Top5AirportsPaxByDestination, \
                    Top5AirportsFreByOrigin, \
                    Top5AirportsFreByDestination, \
                    Top5AirportsMailByOrigin, \
                    Top5AirportsMailByDestination, \
                    Top5AirportsDistByOrigin, \
                    Top5AirportsDistByDestination, \
                    TopDistanceByMonth, \
                    TopPassengerByMonth, \
                    AirlineMostFreight, \
                    AirlineMostPassenger, \
                    AirlineMostMail, \
                    AirlineMostDistance, \
                    passenger_by_month_for_airlines, \
                    AverageNumberPassengersByAirport, \
                    AverageVolumeofFreightByAirport, \
                    CityPairMostFreightandMaxDistance, \
                    CityPairMostMailandShortDistance     


urlpatterns = [
    path('list/', MarketDataList.as_view(), name="list"),
    path('top5paxorigin/', 
        Top5AirportsPaxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Origin Airport"}
        ),
        name="top5paxorigin"),
    path('top5paxdestination/',  
        Top5AirportsPaxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Destination Airport"}
        ), 
        name="top5paxdestination"),
    path('top5freorigin/', 
        Top5AirportsFreByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Origin Airport"}
        ),
        name="top5freorigin"),
    path('top5fredestination/',  
        Top5AirportsFreByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Destination Airport"}
        ), 
        name="top5fredestination"),
    path('top5mailorigin/', 
        Top5AirportsMailByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Origin Airport"}
        ),
        name="top5mailorigin"),
    path('top5maildestination/',  
        Top5AirportsMailByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Destination Airport"}
        ), 
        name="top5maildestination"),
    path('top5distorigin/', 
        Top5AirportsDistByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Origin Airport"}
        ),
        name="top5distorigin"),
    path('top5distdestination/',  
        Top5AirportsDistByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Destination Airport"}
        ), 
        name="top5distdestination"),
    path('topdistance_month/',  
        TopDistanceByMonth.as_view(
            extra_context={'title': "Top Distance by Month"}
        ), 
        name="topdistance_month"),
    path('toppassengers_month/',  
        TopPassengerByMonth.as_view(
            extra_context={'title': "Top Passangers by Month"}
        ), 
        name="toppassengers_month"),
    path('airline_by_most_freight/',  
        AirlineMostFreight.as_view(
            extra_context={'title': "Airline Carrying maximum Freight"}
        ), 
        name="airline_by_most_freight"),
    path('airline_by_most_passengers/',  
        AirlineMostPassenger.as_view(
            extra_context={'title': "Airline Carrying maximum Passengers"}
        ), 
        name="airline_by_most_passengers"),
    path('airline_by_most_mail/',  
        AirlineMostMail.as_view(
            extra_context={'title': "Airline Carrying maximum Mails"}
        ), 
        name="airline_by_most_mail"),
    path('airline_by_most_distance/',  
        AirlineMostDistance.as_view(
            extra_context={'title': "Which airline reported the longest flight distance?"}
        ), 
        name="airline_by_most_distance"),
    path('passenger_by_month_for_airlines/<str:carrier_id>/',  
        passenger_by_month_for_airlines.as_view(
            extra_context={'title': "Rank order passengers carried, by month, for these airlines:"}
        ), 
        name="passenger_by_month_for_airlines"),
    path('average_number_passengers_dest_airport/<str:dest_iata_code>/',  
        AverageNumberPassengersByAirport.as_view(
            extra_context={'title': "Average number of passengers for flights:"}
        ), 
        name="average_number_passengers_dest_airport"),
    path('average_volume_freight_orig_airport/<str:orig_iata_code>/',  
        AverageVolumeofFreightByAirport.as_view(
            extra_context={'title': "Find the average volume of freight for flights departing:"}
        ), 
        name="average_volume_freight_orig_airport"),
    path('city_pair_most_freight/',  
        CityPairMostFreightandMaxDistance.as_view(
            extra_context={'title': "What city pairs represent the most freight carried for the longest distance?"}
        ), 
        name="city_pair_most_freight"),
    path('city_pair_most_mail/',  
        CityPairMostMailandShortDistance.as_view(
            extra_context={'title': "What city pairs represent the most mail carried for the shortest distance?"}
        ), 
        name="city_pair_most_mail"),
]