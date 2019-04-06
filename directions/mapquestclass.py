class Directions:
    def look_up(self, data):
        directions = []
        try:
            legs = data['route']['legs']
            print('DIRECTIONS')
            for d in legs:
                for diction in d['maneuvers']:
                    #print(diction['narrative'])
                    directions.append(diction['narrative'])
            return directions

        except KeyError:
            print('NO ROUTE FOUND')
            return directions


class Distance:
    def look_up(self, data):
        try:
            print('TOTAL DISTANCE: ' + str(round(data['route']['distance'])) + ' mile(s)')
        except KeyError:
            print('NO DISTANCE FOUND')



class Time:
    def look_up(self, data):
        # try:
        #     original_time = data['route']['formattedTime'][:2] + data['route']['formattedTime'][3:5]
        #     answer_1 = int(original_time) * .60
        #     answer_2 = int(original_time) - answer_1
        #     final_answer = answer_1 + answer_2
        #     print('TOTAL TIME: ' + str(round(final_answer)) + ' minute(s)')
        # except KeyError:
        #     print('NO TIME FOUND')
        try:
            print('TOTAL TIME: ' + str(round(data['route']['time'] / 60)) + ' minutes')

        except KeyError:
            print('NO TIME FOUND')






class Lat_Long:
    def look_up(self, data):
        try:

            list_of_lat_and_long = []
            data = data['route']['locations']
            print('LATLONGS')
            for d in data:
                new = d['latLng']
                if new['lat'] > 0 and new['lng'] > 0:
                    print(str(round(new['lat'], 2)) + 'N' + ' ' + str(round(new['lng'], 2))[1:] + 'E')
                    #print('{:.2f}N {:.2f}W'.format(new['lat'], float(str(new['lng']).replace("-", ""))))
                elif new['lat'] > 0 and new['lng'] < 0:
                    print(str(round(new['lat'], 2)) + 'N' + ' ' + str(round(new['lng'], 2))[1:] + 'W')
                elif new['lat'] < 0 and new['lng'] > 0:
                    print(str(round(new['lat'], 2)) + 'S' + ' ' + str(round(new['lng'], 2))[1:] + 'E')
                elif new['lat'] < 0 and new['lng'] < 0:
                    print(str(round(new['lat'], 2)) + 'S' + ' ' + str(round(new['lng'], 2))[1:] + 'W')
                list_of_lat_and_long.append(new['lat'])
                list_of_lat_and_long.append(new['lng'])
            return list_of_lat_and_long

        except KeyError:
            print('NO LATLONG FOUND')

    def list_lat_and_lng(self, data):
        try:
            list_of_lat_and_long = []
            data = data['route']['locations']
            for d in data:
                new = d['latLng']
                list_of_lat_and_long.append(new['lat'])
                list_of_lat_and_long.append(new['lng'])
            return list_of_lat_and_long

        except KeyError:
            print('')




class Elevation:
    def look_up(self, data):
        try:
            elevate = data['elevationProfile']
            print('ELEVATIONS')
            for diction in elevate:
                print(round(diction['height']))

        except:
            print('NO ELEVATION FOUND')






