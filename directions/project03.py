from .createmapquestapi import *
from .mapquestclass import *

def main():

    try:
        routes = create_tuples(gather_locations())
        encoded_routes = url_encode(routes)
        data = parse_the_response(http_response(encoded_routes))
        list_of_stats = gather_stats()
        print()


        for stat in list_of_stats:

            if stat.upper() == 'LATLONG':
                Lat_Long().look_up(data)
                print()
            elif stat.upper() == 'STEPS':
                steps = Directions().look_up(data)
                if not steps:
                    print()
                    break
                else:
                    for turn in steps:
                        print(turn)
                print()
            elif stat.upper() == 'TOTALTIME':
                Time().look_up(data)
                print()
            elif stat.upper() == 'TOTALDISTANCE':
                Distance().look_up(data)
                print()
            elif stat.upper() == 'ELEVATION':
                e = elevation_full_url(Lat_Long().list_lat_and_lng(data))
                Elevation().look_up(e)
                print()

        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')

    except:
        print()
        print('MAPQUEST ERROR')


if __name__ == '__main__':
    main()

# 460 s burlington ave la ca 90057
# 1215 seward la ca 90038
