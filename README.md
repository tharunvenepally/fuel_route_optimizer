## Fuel Route Optimizer API

Task: https://docs.google.com/document/d/1o9i5DR7BwdGmwRgDsVlTg_gJ4L_rcXQWq4TAcmnEFC0/edit?tab=t.0 <br>

Steps I took: <br>
1. First, I began by inspecting the requirement file provided by Spotter and the Excel file to get the key points and what was required of me.<br>
   Key takeaway were: <br>
      i) Assignment task
   
   ![image](https://github.com/user-attachments/assets/e4569d31-5056-47a0-8e69-58b34083ab90)
   
      ii) Requirements

   ![image](https://github.com/user-attachments/assets/6378df55-da54-4db9-bbd6-8f7724b989c6)

2. To meet the task requirement, I identified a free maps route API from MAPQUEST. <br>
    Which has several API request quotas of 15,000 requests, which was enough for this project.<br>
    
3. Then, I created an API key to test the API endpoints, which they provided to help me design my route_fuel_optimizer API. <br>
    So, I ensure that my requests will be as efficient as possible, with minimal requests to their endpoints. <br>
    - I identified two endpoints which stood out:
      
      a) Direction API; GET Route: I tested like this: GET https://www.mapquestapi.com/directions/v2/route?          
         key=KEY&from=Clarendon_Blvd,Arlington,VA&to=2400+S+Glebe+Rd,+Arlington,+VA

     # Returned JSON:<br>

      ```json
      {
        "route": {
          "hasTollRoad": false,
          "computedWaypoints": [],
          "fuelUsed": 0.23,
          "hasUnpaved": false,
          "hasHighway": false,
          "realTime": 653,
          "boundingBox": {
            "ul": {
              "lng": -77.089424,
              "lat": 38.893276
            },
            "lr": {
              "lng": -77.077087,
              "lat": 38.848926
            }
          },
          "distance": 3.693,
          "time": 501,
          "locationSequence": [
            0,
            1
          ],
          "hasSeasonalClosure": false,
          "sessionId": "55e60cd9-00b6-001a-02b7-20ac-00163e7dd551",
          "locations": [
            {
              "latLng": {
                "lng": -77.077959,
                "lat": 38.893165
              },
              "adminArea4": "Arlington",
              "adminArea5Type": "City",
              "adminArea4Type": "County",
              "adminArea5": "Arlington",
              "street": "[1700 - 1720] Clarendon Blvd",
              "adminArea1": "US",
              "adminArea3": "VA",
              "type": "s",
              "displayLatLng": {
                "lng": -77.077957,
                "lat": 38.893165
              },
              "linkId": 13257655,
              "postalCode": "22209-2713",
              "sideOfStreet": "L",
              "dragPoint": false,
              "adminArea1Type": "Country",
              "geocodeQuality": "STREET",
              "geocodeQualityCode": "B1AAA",
              "adminArea3Type": "State"
            },
            {
              "latLng": {
                "lng": -77.081229,
                "lat": 38.848932
              },
              "adminArea4": "Arlington",
              "adminArea5Type": "City",
              "adminArea4Type": "County",
              "adminArea5": "Arlington",
              "street": "2400 S Glebe Rd",
              "adminArea1": "US",
              "adminArea3": "VA",
              "type": "s",
              "displayLatLng": {
                "lng": -77.08123,
                "lat": 38.84893
              },
              "linkId": 14874674,
              "postalCode": "22206-2500",
              "sideOfStreet": "R",
              "dragPoint": false,
              "adminArea1Type": "Country",
              "geocodeQuality": "POINT",
              "geocodeQualityCode": "P1AAA",
              "adminArea3Type": "State"
            }
          ],
          "hasCountryCross": false,
          "legs": [
            {
              "hasTollRoad": false,
              "index": 0,
              "roadGradeStrategy": [
                []
              ],
              "hasHighway": false,
              "hasUnpaved": false,
              "distance": 3.693,
              "time": 501,
              "origIndex": 3,
              "hasSeasonalClosure": false,
              "origNarrative": "Go south on Arlington Blvd/US-50 W.",
              "hasCountryCross": false,
              "formattedTime": "00:08:21",
              "destNarrative": "Proceed to 2400 S GLEBE RD.",
              "destIndex": 5,
              "maneuvers": [
                {
                  "signs": [],
                  "index": 0,
                  "maneuverNotes": [],
                  "direction": 8,
                  "narrative": "Start out going east on Clarendon Blvd toward N Queen St.",
                  "iconUrl": "https://content.mapquest.com/mqsite/turnsigns/icon-dirs-start_sm.gif",
                  "distance": 0.031,
                  "time": 6,
                  "linkIds": [],
                  "streets": [
                    "Clarendon Blvd"
                  ],
                  "attributes": 0,
                  "transportMode": "AUTO",
                  "formattedTime": "00:00:06",
                  "directionName": "East",
                  "mapUrl": "https://www.mapquestapi.com/staticmap/v5/getmap?key=KEY&type=map&size=225,160&pois=purple-1,38.893164999999996,-77.077957,0,0|purple- 
                     2,38.893276,-77.077407,0,0|&center=38.8932205,-77.077682&zoom=15&rand=-1645843521&session=55e60cd9-00b6-001a-02b7-20ac-00163e7dd551",
                  "startPoint": {
                    "lng": -77.077957,
                    "lat": 38.893165
                  },
                  "turnType": 2
                },
                {
                  "signs": [],
                  "index": 1,
                  "maneuverNotes": [],
                  "direction": 4,
                  "narrative": "Turn right onto N Queen St.",
                  "iconUrl": "https://content.mapquest.com/mqsite/turnsigns/rs_right_sm.gif",
                  "distance": 0.168,
                  "time": 32,
                  "linkIds": [],
                  "streets": [
                    "N Queen St"
                  ],
                  "attributes": 0,
                  "transportMode": "AUTO",
                  "formattedTime": "00:00:32",
                  "directionName": "South",
                  "mapUrl": "https://www.mapquestapi.com/staticmap/v5/getmap?key=KEY&type=map&size=225,160&pois=purple-2,38.893276,-77.077407,0,0|purple- 
                  3,38.890857,-77.07708699999999,0,0|&center=38.8920665,-77.077247&zoom=12&rand=-1645843521&session=55e60cd9-00b6-001a-02b7-20ac-00163e7dd551",
                  "startPoint": {
                    "lng": -77.077407,
                    "lat": 38.893276
                  },
                  "turnType": 2
                },
                {
                  "signs": [],
                  "index": 2,
                  "maneuverNotes": [],
                  "direction": 7,
                  "narrative": "Turn right onto 14th St N.",
                  "iconUrl": "https://content.mapquest.com/mqsite/turnsigns/rs_right_sm.gif",
                  "distance": 0.003,
                  "time": 5,
                  "linkIds": [],
                  "streets": [
                    "14th St N"
                  ],
                  "attributes": 0,
                  "transportMode": "AUTO",
                  "formattedTime": "00:00:05",
                  "directionName": "West",
                  "mapUrl": "https://www.mapquestapi.com/staticmap/v5/getmap?key=KEY&type=map&size=225,160&pois=purple-3,38.890857,-77.07708699999999,0,0|purple- 
                 4,38.890842,-77.077148,0,0|&center=38.8908495,-77.07711749999999&zoom=15&rand=-1646228270&session=55e60cd9-00b6-001a-02b7-20ac-00163e7dd551",
                  "startPoint": {
                    "lng": -77.077087,
                    "lat": 38.890857
                  },
                  "turnType": 2
                },
                {
                  "signs": [
                    {
                      "text": "50",
                      "extraText": "",
                      "direction": 7,
                      "type": 2,
                      "url": "http://icons.mqcdn.com/icons/rs2.png?n=50&d=WEST"
                    }
                  ],
                  "index": 3,
                  "maneuverNotes": [],
                  "direction": 4,
                  "narrative": "Merge onto Arlington Blvd/US-50 W via the ramp on the left.",
                  "iconUrl": "https://content.mapquest.com/mqsite/turnsigns/rs_merge_left_sm.gif",
                  "distance": 1.606,
                  "time": 151,
                  "linkIds": [],
                  "streets": [
                    "Arlington Blvd",
                    "US-50 W"
                  ],
                  "attributes": 0,
                  "transportMode": "AUTO",
                  "formattedTime": "00:02:31",
                  "directionName": "South",
                  "mapUrl": "https://www.mapquestapi.com/staticmap/v5/getmap?key=KEY&type=map&size=225,160&pois=purple-4,38.890842,-77.077148,0,0|purple- 
                  5,38.87355,-77.089424,0,0|&center=38.882196,-77.08328599999999&zoom=9&rand=-1646228270&session=55e60cd9-00b6-001a-02b7-20ac-00163e7dd551",
                  "startPoint": {
                    "lng": -77.077148,
                    "lat": 38.890842
                  },
                  "turnType": 11
                },
                {
                  "signs": [],
                  "index": 4,
                  "maneuverNotes": [],
                  "direction": 4,
                  "narrative": "Turn left onto N Fillmore St.",
                  "iconUrl": "https://content.mapquest.com/mqsite/turnsigns/rs_left_sm.gif",
                  "distance": 0.408,
                  "time": 74,
                  "linkIds": [],
                  "streets": [
                    "N Fillmore St"
                  ],
                  "attributes": 0,
                  "transportMode": "AUTO",
                  "formattedTime": "00:01:14",
                  "directionName": "South",
                  "mapUrl": "https://www.mapquestapi.com/staticmap/v5/getmap?key=KEY&type=map&size=225,160&pois=purple-5,38.87355,-77.089424,0,0|purple- 
                  6,38.867782,-77.08811899999999,0,0|&center=38.870666,-77.0887715&zoom=10&rand=-1646228270&session=55e60cd9-00b6-001a-02b7-20ac-00163e7dd551",
                  "startPoint": {
                    "lng": -77.089424,
                    "lat": 38.87355
                  },
                  "turnType": 6
                },
                {
                  "signs": [],
                  "index": 5,
                  "maneuverNotes": [],
                  "direction": 4,
                  "narrative": "Stay straight to go onto S Walter Reed Dr.",
                  "iconUrl": "https://content.mapquest.com/mqsite/turnsigns/rs_straight_sm.gif",
                  "distance": 0.884,
                  "time": 149,
                  "linkIds": [],
                  "streets": [
                    "S Walter Reed Dr"
                  ],
                  "attributes": 0,
                  "transportMode": "AUTO",
                  "formattedTime": "00:02:29",
                  "directionName": "South",
                  "mapUrl": "https://www.mapquestapi.com/staticmap/v5/getmap?key=KEY&type=map&size=225,160&pois=purple-6,38.867782,-77.08811899999999,0,0|purple- 
                 7,38.855185999999996,-77.088584,0,0|&center=38.861484,-77.08835149999999&zoom=9&rand=-1646228270&session=55e60cd9-00b6-001a-02b7-20ac- 
                 00163e7dd551",
                  "startPoint": {
                    "lng": -77.088119,
                    "lat": 38.867782
                  },
                  "turnType": 0
                },
                {
                  "signs": [
                    {
                      "text": "120",
                      "extraText": "",
                      "direction": 0,
                      "type": 545,
                      "url": "http://icons.mqcdn.com/icons/rs545.png?n=120"
                    }
                  ],
                  "index": 6,
                  "maneuverNotes": [],
                  "direction": 5,
                  "narrative": "Turn slight left onto S Glebe Rd/VA-120.",
                  "iconUrl": "https://content.mapquest.com/mqsite/turnsigns/rs_slight_left_sm.gif",
                  "distance": 0.593,
                  "time": 84,
                  "linkIds": [],
                  "streets": [
                    "S Glebe Rd",
                    "VA-120"
                  ],
                  "attributes": 0,
                  "transportMode": "AUTO",
                  "formattedTime": "00:01:24",
                  "directionName": "Southeast",
                  "mapUrl": "https://www.mapquestapi.com/staticmap/v5/getmap?key=KEY&type=map&size=225,160&pois=purple-7,38.855185999999996,-77.088584,0,0|purple- 
                 8,38.848926,-77.08122999999999,0,0|&center=38.852056,-77.08490699999999&zoom=10&rand=-1646228270&session=55e60cd9-00b6-001a-02b7-20ac- 
                 00163e7dd551",
                  "startPoint": {
                    "lng": -77.088584,
                    "lat": 38.855186
                  },
                  "turnType": 7
                },
                {
                  "signs": [],
                  "index": 7,
                  "maneuverNotes": [],
                  "direction": 0,
                  "narrative": "2400 S GLEBE RD is on the right.",
                  "iconUrl": "https://content.mapquest.com/mqsite/turnsigns/icon-dirs-end_sm.gif",
                  "distance": 0,
                  "time": 0,
                  "linkIds": [],
                  "streets": [],
                  "attributes": 0,
                  "transportMode": "AUTO",
                  "formattedTime": "00:00:00",
                  "directionName": "",
                  "startPoint": {
                    "lng": -77.08123,
                    "lat": 38.848926
                  },
                  "turnType": -1
                }
              ],
              "hasFerry": false
            }
          ],
          "formattedTime": "00:08:21",
          "routeError": {
            "message": "",
            "errorCode": -400
          },
          "options": {
            "mustAvoidLinkIds": [],
            "drivingStyle": 2,
            "countryBoundaryDisplay": true,
            "generalize": -1,
            "narrativeType": "text",
            "locale": "en_US",
            "avoidTimedConditions": false,
            "destinationManeuverDisplay": true,
            "enhancedNarrative": false,
            "filterZoneFactor": -1,
            "timeType": 0,
            "maxWalkingDistance": -1,
            "routeType": "FASTEST",
            "transferPenalty": -1,
            "stateBoundaryDisplay": true,
            "walkingSpeed": -1,
            "maxLinkId": 0,
            "arteryWeights": [],
            "tryAvoidLinkIds": [],
            "unit": "M",
            "routeNumber": 0,
            "shapeFormat": "raw",
            "maneuverPenalty": -1,
            "useTraffic": false,
            "returnLinkDirections": false,
            "avoidTripIds": [],
            "manmaps": "true",
            "highwayEfficiency": 22,
            "sideOfStreetDisplay": true,
            "cyclingRoadFactor": 1,
            "urbanAvoidFactor": -1
          },
          "hasFerry": false
        },
        "info": {
          "copyright": {
            "text": "© 2023 MapQuest, Inc.",
            "imageUrl": "https://api.mqcdn.com/res/mqlogo.gif",
            "imageAltText": "© 2023 MapQuest, Inc."
          },
          "statuscode": 0,
          "messages": []
        }
      }
      
b) Second API which was of interest: Geocoding API <br>

  https://www.mapquestapi.com/geocoding/v1/address?key=KEY&location=Washington,DC

  # Response

  ```json

        {
          "info": {
              "statuscode": 0,
              "copyright": {
              "text": "© 2023 MapQuest, Inc.",
              "imageUrl": "https://api.mqcdn.com/res/mqlogo.gif",
              "imageAltText": "© 2023 MapQuest, Inc."
              },
              "messages": []
          },
          "options": {
              "maxResults": -1,
              "thumbMaps": true,
              "ignoreLatLngInput": false
          },
          "results": [
           {
              "providedLocation": {
                  "location": "Washington,DC"
              },
              "locations": [
                  {
                  "street": "",
                  "adminArea6": "",
                  "adminArea6Type": "Neighborhood",
                  "adminArea5": "Washington",
                  "adminArea5Type": "City",
                  "adminArea4": "District of Columbia",
                  "adminArea4Type": "County",
                  "adminArea3": "DC",
                  "adminArea3Type": "State",
                  "adminArea1": "US",
                  "adminArea1Type": "Country",
                  "postalCode": "",
                  "geocodeQualityCode": "A5XAX",
                  "geocodeQuality": "CITY",
                  "dragPoint": false,
                  "sideOfStreet": "N",
                  "linkId": "282772166",
                  "unknownInput": "",
                  "type": "s",
                  "latLng": {
                      "lat": 38.892062,
                      "lng": -77.019912
                  },
                  "displayLatLng": {
                      "lat": 38.892062,
                      "lng": -77.019912
                  },
                  "mapUrl": "https://www.mapquestapi.com/staticmap/v5/getmap?key=KEY&type=map&size=225,160&pois=purple-        
                   1,38.892062,-77.019912,0,0,|&center=38.892062,-77.019912&zoom=12&rand=306744981"
                  }
              ]
            }
          ]
        }
```
4. After that I inspected the Excel sheet with the rows to get how I will integrate them with the free API:<br>
   - Realized for me to calculate the most optimal routes and fueling points on the route I needed to work with latitudes and longitudes <br>
   - The problem was that the Excel sheet had no lat and lng rows: fuel-prices-for-be-assessment.csv <br>
   
     ![image](https://github.com/user-attachments/assets/45c8e2dc-1d0d-4f5a-b904-34f270839996)

  - I decided to build a small API worker in Nodejs to query the MAPQUEST API geocoding API with the address row on the Excel sheet<br>
    and fill in the missing latitudes and latitudes this would increase the Django server API speed and performance when querying the geocoding API each time  
    the user wanted to get fuel-efficient stations in terms of cost. Also, this assisted me in ensuring that my Django API would only do one API call to      
    accomplish this task. 

    ![image](https://github.com/user-attachments/assets/c71267a7-ca52-4d03-bac7-10e17d519752)

    and here is the code:

    ```javascript
      const express = require('express');
          const axios = require('axios');
          const fs = require('fs');
          const csv = require('csv-parser');
          const { createObjectCsvWriter } = require('csv-writer');
          const app = express();
          require('dotenv').config();
          
          const MAPQUEST_API_KEY = process.env.MAPQUEST_API_KEY;
          
          app.use(express.json());
          
          async function loadCSVData() {
              return new Promise((resolve, reject) => {
                  const results = [];
                  fs.createReadStream('fuel-prices-for-be-assessment.csv')
                      .pipe(csv())
                      .on('data', (row) => results.push(row))
                      .on('end', () => resolve(results))
                      .on('error', (error) => reject(error));
              });
          }
          
          async function getLatLng(address) {
              try {
                  const url = `https://www.mapquestapi.com/geocoding/v1/address?key=${MAPQUEST_API_KEY}&location=${encodeURIComponent(address)}`;
                  const response = await axios.get(url);
                  const locations = response.data.results[0].locations[0];
                  return {
                      lat: locations.latLng.lat,
                      lng: locations.latLng.lng
                  };
              } catch (error) {
                  console.error(`Error fetching data for address: ${address}`);
                  return null;
              }
          }
          
          function saveUpdatedCSV(rows) {
              const csvWriter = createObjectCsvWriter({
                  path: 'fuel-prices-for-be-assessment.csv', 
                  header: Object.keys(rows[0]).map(key => ({ id: key, title: key }))
              });
          
              return csvWriter.writeRecords(rows);
          }
          
          async function processCSVData() {
              const rows = await loadCSVData();
              let batchCount = 0;
          
              for (let i = 0; i < rows.length; i++) {
                  const row = rows[i];
          
                  if (row.Latitude && row.Longitude) {
                      console.log(`Skipping row ${i + 1} - Already has lat/lng`);
                      continue;
                  }
          
                  const address = `${row.Address}, ${row.City}, ${row.State}`;
                  const latLng = await getLatLng(address);
          
                  if (latLng) {
                      row.Latitude = latLng.lat;
                      row.Longitude = latLng.lng;
          
                      console.log(`Row ${i + 1} updated: ${address} -> Latitude: ${latLng.lat}, Longitude: ${latLng.lng}`);
          
                      await saveUpdatedCSV(rows);
                  } else {
                      console.log(`Failed to fetch lat/lng for row ${i + 1} - ${address}`);
                  }
          
                  if ((i + 1) % 500 === 0) {
                      console.log(`Processed ${i + 1} rows`);
                      batchCount++;
                  }
              }
          
              console.log(`Finished processing all rows. Total batches: ${batchCount}`);
          }
          
          app.get('/process-data', async (req, res) => {
              await processCSVData();
              res.send('Data processing started. Check console for updates.');
          });
          
          const PORT = process.env.PORT || 3000;
          app.listen(PORT, () => {
              console.log(`Server is running on port ${PORT}`);
          });
      ```
    The results:<br>

      ![image](https://github.com/user-attachments/assets/3e770cdc-7732-42d9-8797-7cdce991b067)

      ![image](https://github.com/user-attachments/assets/a9d132a0-dca4-42cd-85ef-c47fe1271f96)
      
    
5. The next step, I proceeded by setting up the Django project using Django:3.2.23: I created the fuel_route_optimizer project <br> and implemented the routing_api app. <br>
    -   This involved also setting the data folder with the filled latitudes and longitudes. 

6. Then, I installed the Django Rest Framework (DRF) for API endpoints and implemented my first API endpoint to test if it was successful: <br>

     ![image](https://github.com/user-attachments/assets/ac939b4f-7918-4529-925e-366b0fd5d394)

7. Then I proceeded to integrate the MapQuest API for Route Calculation:

     ![image](https://github.com/user-attachments/assets/8eacc874-14a1-4808-ae8d-9336c591fbcc)

     ![image](https://github.com/user-attachments/assets/f255bb6c-a695-418b-8911-62f370306ab9)

   
9. After that I implemented a module to check if the dataset was being loaded correctly:<br>

    - Tested by displaying the first five data rows:<br>

    ![image](https://github.com/user-attachments/assets/a2860117-c8dd-490c-b327-4390f37f6fc1)

11. Then I implemented the main API endpoint to integrate the two modules: Route and Fuel Data;

    ![image](https://github.com/user-attachments/assets/bc0f14ad-c602-4bdf-b1bf-f3d95401db24)

12. After implementing the final test, I had to optimize the API requests so I intergreatd<br> 
     cache to help me store the requests to avoid repeating the same request that I had br>    
    already made: Here are the results: <br>

    ![image](https://github.com/user-attachments/assets/f3ac1f91-9dfd-4f39-9acc-eb2a04b70494)

    My final project structure:

    ![image](https://github.com/user-attachments/assets/4e86c618-50f2-4e4a-8272-5b9a94416c54)

    An example of final API call results: <br>

    ```json


          {
    "route": {
        "sessionId": "AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car",
        "realTime": 13682,
        "distance": 228.3564,
        "time": 12936,
        "formattedTime": "03:35:36",
        "hasHighway": true,
        "hasTollRoad": true,
        "hasBridge": true,
        "hasSeasonalClosure": false,
        "hasTunnel": true,
        "hasFerry": false,
        "hasUnpaved": false,
        "hasTimedRestriction": false,
        "hasCountryCross": false,
        "legs": [
            {
                "index": 0,
                "hasTollRoad": true,
                "hasHighway": true,
                "hasBridge": true,
                "hasUnpaved": false,
                "hasTunnel": true,
                "hasSeasonalClosure": false,
                "hasFerry": false,
                "hasCountryCross": false,
                "hasTimedRestriction": false,
                "distance": 228.3564,
                "time": 13682,
                "formattedTime": "03:48:02",
                "origIndex": 0,
                "origNarrative": "",
                "destIndex": 0,
                "destNarrative": "",
                "maneuvers": [
                    {
                        "index": 0,
                        "distance": 0.0516,
                        "narrative": "Head toward Church St on Chambers St. Go for 272 ft.",
                        "time": 24,
                        "direction": 2,
                        "directionName": "Northwest",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:00:24",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 40.714532,
                            "lng": -74.007119
                        },
                        "turnType": 0,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "Chambers St"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=40.714532,-74.007119|marker-1||40.7149,-74.00797|marker-2||&center=40.714715999999996,-74.0075445&defaultMarker=none&zoom=16&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 1,
                        "distance": 0.2715,
                        "narrative": "Turn right onto Church St. Go for 0.3 mi.",
                        "time": 66,
                        "direction": 3,
                        "directionName": "Northeast",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:01:06",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 40.7149,
                            "lng": -74.00797
                        },
                        "turnType": 2,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "Church St"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=40.7149,-74.00797|marker-2||40.71829999999999,-74.00539|marker-3||&center=40.7166,-74.00668&defaultMarker=none&zoom=14&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 2,
                        "distance": 0.2541,
                        "narrative": "Keep left onto 6th Ave. Go for 0.3 mi.",
                        "time": 70,
                        "direction": 1,
                        "directionName": "North",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:01:10",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 40.71829999999999,
                            "lng": -74.00539
                        },
                        "turnType": 17,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "6th Ave",
                            "Avenue of the Americas"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=40.71829999999999,-74.00539|marker-3||40.72194,-74.00535000000002|marker-4||&center=40.720119999999994,-74.00537000000001&defaultMarker=none&zoom=14&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 3,
                        "distance": 0.1603,
                        "narrative": "Turn slightly left onto Canal St toward Holland Tunnel. Go for 0.2 mi.",
                        "time": 68,
                        "direction": 2,
                        "directionName": "Northwest",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:01:08",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 40.72194,
                            "lng": -74.00535000000002
                        },
                        "turnType": 7,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "Canal St"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=40.72194,-74.00535000000002|marker-4||40.72349999999999,-74.00759000000002|marker-5||&center=40.722719999999995,-74.00647000000002&defaultMarker=none&zoom=15&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 4,
                        "distance": 0.9091,
                        "narrative": "Turn right onto Holland Tunnel toward I-78/Holland Tunnel/New Jersey. Go for 0.9 mi.",
                        "time": 95,
                        "direction": 7,
                        "directionName": "West",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:01:35",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 40.72349999999999,
                            "lng": -74.00759000000002
                        },
                        "turnType": 2,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "Holland Tunnel",
                            "Hudson St"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=40.72349999999999,-74.00759000000002|marker-5||40.72762999999997,-74.02121000000002|marker-6||&center=40.725564999999975,-74.01440000000002&defaultMarker=none&zoom=13&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 5,
                        "distance": 1.0184,
                        "narrative": "Continue on Holland Tunnel. Go for 1.0 mi.",
                        "time": 120,
                        "direction": 7,
                        "directionName": "West",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:02:00",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 40.72762999999997,
                            "lng": -74.02121000000002
                        },
                        "turnType": 0,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "Holland Tunnel"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=40.72762999999997,-74.02121000000002|marker-6||40.731539999999995,-74.03944000000001|marker-7||&center=40.729584999999986,-74.03032500000002&defaultMarker=none&zoom=13&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 6,
                        "distance": 0.3076,
                        "narrative": "Continue on 14th St. Go for 0.3 mi.",
                        "time": 81,
                        "direction": 7,
                        "directionName": "West",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:01:21",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 40.731539999999995,
                            "lng": -74.03944000000001
                        },
                        "turnType": 0,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "14th St"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=40.731539999999995,-74.03944000000001|marker-7||40.732030000000016,-74.04519000000002|marker-8||&center=40.731785,-74.04231500000002&defaultMarker=none&zoom=14&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 7,
                        "distance": 8.0101,
                        "narrative": "Keep right onto I-78 W (New Jersey Tpke Ext) toward New Jersey Turnpike/I-78/I-95. Go for 8.0 mi.",
                        "time": 525,
                        "direction": 7,
                        "directionName": "West",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:08:45",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 40.732030000000016,
                            "lng": -74.04519000000002
                        },
                        "turnType": 16,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "I-78",
                            "New Jersey Tpke Ext",
                            "Newark Bay Brg",
                            "Vincent R Casciano Memorial Brg"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=40.732030000000016,-74.04519000000002|marker-8||40.70687999999999,-74.15248000000014|marker-9||&center=40.719455,-74.09883500000008&defaultMarker=none&zoom=10&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 8,
                        "distance": 53.5442,
                        "narrative": "Take the exit toward New Jersey Turnpike South/Trenton onto I-95 S (New Jersey Tpke Cars Only Ln). Go for 53.5 mi.",
                        "time": 2718,
                        "direction": 6,
                        "directionName": "Southwest",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:45:18",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 40.70687999999999,
                            "lng": -74.15248000000014
                        },
                        "turnType": 14,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "I-95",
                            "New Jersey Tpke Cars Only Ln",
                            "Sgt John Basilone Memorial Brg"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=40.70687999999999,-74.15248000000014|marker-9||40.10308999999997,-74.72391000000027|marker-10||&center=40.40498499999998,-74.4381950000002&defaultMarker=none&zoom=7&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 9,
                        "distance": 2.1549,
                        "narrative": "Continue on New Jersey Tpke Cars Only Ln toward New Jersey Turnpike-South/Camden/Wilmington. Go for 2.2 mi.",
                        "time": 104,
                        "direction": 6,
                        "directionName": "Southwest",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:01:44",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 40.10308999999997,
                            "lng": -74.72391000000027
                        },
                        "turnType": 0,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "New Jersey Tpke Cars Only Ln"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=40.10308999999997,-74.72391000000027|marker-10||40.079019999999964,-74.74972000000024|marker-11||&center=40.09105499999997,-74.73681500000026&defaultMarker=none&zoom=11&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 10,
                        "distance": 48.6894,
                        "narrative": "Continue on New Jersey Tpke. Go for 48.7 mi.",
                        "time": 2472,
                        "direction": 6,
                        "directionName": "Southwest",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:41:12",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 40.079019999999964,
                            "lng": -74.74972000000024
                        },
                        "turnType": 0,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "New Jersey Tpke"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=40.079019999999964,-74.74972000000024|marker-11||39.679690000000015,-75.47894000000016|marker-12||&center=39.87935499999999,-75.1143300000002&defaultMarker=none&zoom=7&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 11,
                        "distance": 0.507,
                        "narrative": "Continue on US-40 W (New Jersey Tpke). Go for 0.5 mi.",
                        "time": 29,
                        "direction": 7,
                        "directionName": "West",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:00:29",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 39.679690000000015,
                            "lng": -75.47894000000016
                        },
                        "turnType": 0,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "US-40",
                            "New Jersey Tpke"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=39.679690000000015,-75.47894000000016|marker-12||39.67925000000002,-75.48837000000017|marker-13||&center=39.679470000000016,-75.48365500000017&defaultMarker=none&zoom=13&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 12,
                        "distance": 1.1924,
                        "narrative": "Continue on I-295 S. Go for 1.2 mi.",
                        "time": 76,
                        "direction": 7,
                        "directionName": "West",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:01:16",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 39.67925000000002,
                            "lng": -75.48837000000017
                        },
                        "turnType": 0,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "I-295",
                            "US-40",
                            "Delaware Memorial Brg"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=39.67925000000002,-75.48837000000017|marker-13||39.68595000000001,-75.5089600000002|marker-14||&center=39.682600000000015,-75.49866500000019&defaultMarker=none&zoom=12&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 13,
                        "distance": 4.3328,
                        "narrative": "Continue on I-295 S (Delaware Memorial Brg). Go for 4.3 mi.",
                        "time": 288,
                        "direction": 7,
                        "directionName": "West",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:04:48",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 39.68595000000001,
                            "lng": -75.5089600000002
                        },
                        "turnType": 0,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "I-295",
                            "US-40",
                            "Delaware Memorial Brg"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=39.68595000000001,-75.5089600000002|marker-14||39.700349999999986,-75.58552000000027|marker-15||&center=39.69315,-75.54724000000024&defaultMarker=none&zoom=10&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 14,
                        "distance": 12.2702,
                        "narrative": "Take the left exit toward Baltimore onto I-95 S (Delaware Tpke). Go for 12.3 mi.",
                        "time": 682,
                        "direction": 7,
                        "directionName": "West",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:11:22",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 39.700349999999986,
                            "lng": -75.58552000000027
                        },
                        "turnType": 15,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "I-95",
                            "Delaware Tpke",
                            "John F Kennedy Memorial Hwy"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=39.700349999999986,-75.58552000000027|marker-15||39.63900000000006,-75.78766000000043|marker-16||&center=39.669675000000026,-75.68659000000035&defaultMarker=none&zoom=9&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 15,
                        "distance": 41.2746,
                        "narrative": "Continue on I-95 S (John F Kennedy Memorial Hwy). Go for 41.3 mi.",
                        "time": 2193,
                        "direction": 7,
                        "directionName": "West",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:36:33",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 39.63900000000006,
                            "lng": -75.78766000000043
                        },
                        "turnType": 0,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "I-95",
                            "John F Kennedy Memorial Hwy",
                            "Millard E Tydings Memorial Brg"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=39.63900000000006,-75.78766000000043|marker-16||39.389550000000014,-76.43814000000046|marker-17||&center=39.51427500000004,-76.11290000000045&defaultMarker=none&zoom=7&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 16,
                        "distance": 6.5374,
                        "narrative": "Keep left onto I-95 S (I-95 Express Toll Lanes). Go for 6.5 mi.",
                        "time": 329,
                        "direction": 6,
                        "directionName": "Southwest",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:05:29",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 39.389550000000014,
                            "lng": -76.43814000000046
                        },
                        "turnType": 17,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "I-95",
                            "I-95 Express Toll Lanes"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=39.389550000000014,-76.43814000000046|marker-17||39.32647000000004,-76.52613000000046|marker-18||&center=39.35801000000003,-76.48213500000045&defaultMarker=none&zoom=10&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 17,
                        "distance": 10.8299,
                        "narrative": "Take left exit 62 onto I-895 S (Harbor Tunnel Thwy). Go for 10.8 mi.",
                        "time": 700,
                        "direction": 6,
                        "directionName": "Southwest",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:11:40",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 39.32647000000004,
                            "lng": -76.52613000000046
                        },
                        "turnType": 15,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "I-895",
                            "Harbor Tunnel Thwy"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=39.32647000000004,-76.52613000000046|marker-18||39.23210000000007,-76.64886000000054|marker-19||&center=39.27928500000006,-76.5874950000005&defaultMarker=none&zoom=9&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 18,
                        "distance": 28.4538,
                        "narrative": "Take exit 4 toward Balt/Wash Parkway onto MD-295 S (Baltimore Washington Pkwy). Go for 28.5 mi.",
                        "time": 1980,
                        "direction": 6,
                        "directionName": "Southwest",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:33:00",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 39.23210000000007,
                            "lng": -76.64886000000054
                        },
                        "turnType": 14,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "MD-295",
                            "Baltimore Washington Pkwy",
                            "Star-Spangled Banner Bywy",
                            "Gladys Noon Spellman Pkwy"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=39.23210000000007,-76.64886000000054|marker-19||38.91224999999999,-76.93419000000085|marker-20||&center=39.07217500000003,-76.79152500000069&defaultMarker=none&zoom=8&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 19,
                        "distance": 3.9358,
                        "narrative": "Continue on DC-295 S (Kenilworth Ave NE). Go for 3.9 mi.",
                        "time": 571,
                        "direction": 6,
                        "directionName": "Southwest",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:09:31",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 38.91224999999999,
                            "lng": -76.93419000000085
                        },
                        "turnType": 0,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "DC-295",
                            "Kenilworth Ave NE",
                            "Anacostia Fwy"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=38.91224999999999,-76.93419000000085|marker-20||38.87196000000002,-76.98232000000074|marker-21||&center=38.89210500000001,-76.9582550000008&defaultMarker=none&zoom=11&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 20,
                        "distance": 2.255,
                        "narrative": "Take exit 1B-C toward I-695/Downtown/I-395 onto I-695 W (Southeast Fwy). Go for 2.3 mi.",
                        "time": 199,
                        "direction": 7,
                        "directionName": "West",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:03:19",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 38.87196000000002,
                            "lng": -76.98232000000074
                        },
                        "turnType": 14,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "I-695",
                            "Southeast Fwy",
                            "11th St Bridge",
                            "Officer Kevin Welsh Memorial Brg"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=38.87196000000002,-76.98232000000074|marker-21||38.882510000000046,-77.01556000000076|marker-22||&center=38.877235000000034,-76.99894000000074&defaultMarker=none&zoom=12&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 21,
                        "distance": 0.3716,
                        "narrative": "Continue on I-395 S (Southwest Fwy). Go for 0.4 mi.",
                        "time": 39,
                        "direction": 7,
                        "directionName": "West",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:00:39",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 38.882510000000046,
                            "lng": -77.01556000000076
                        },
                        "turnType": 0,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "I-395",
                            "Southwest Fwy"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=38.882510000000046,-77.01556000000076|marker-22||38.882580000000054,-77.02246000000075|marker-23||&center=38.88254500000005,-77.01901000000075&defaultMarker=none&zoom=14&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 22,
                        "distance": 0.4374,
                        "narrative": "Take exit 4 toward Maine Avenue/12th St/Downtown. Go for 0.4 mi.",
                        "time": 71,
                        "direction": 2,
                        "directionName": "Northwest",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:01:11",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 38.882580000000054,
                            "lng": -77.02246000000075
                        },
                        "turnType": 14,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=38.882580000000054,-77.02246000000075|marker-23||38.88498000000006,-77.02812000000074|marker-24||&center=38.88378000000006,-77.02529000000075&defaultMarker=none&zoom=14&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 23,
                        "distance": 0.179,
                        "narrative": "Turn right onto 12th St SW. Go for 0.2 mi.",
                        "time": 74,
                        "direction": 1,
                        "directionName": "North",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:01:14",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 38.88498000000006,
                            "lng": -77.02812000000074
                        },
                        "turnType": 2,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "12th St SW"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=38.88498000000006,-77.02812000000074|marker-24||38.88757000000007,-77.02795000000071|marker-25||&center=38.88627500000007,-77.02803500000073&defaultMarker=none&zoom=15&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 24,
                        "distance": 0.2144,
                        "narrative": "Turn left onto Independence Ave SW. Go for 0.2 mi.",
                        "time": 53,
                        "direction": 7,
                        "directionName": "West",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:00:53",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 38.88757000000007,
                            "lng": -77.02795000000071
                        },
                        "turnType": 6,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "Independence Ave SW"
                        ],
                        "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=38.88757000000007,-77.02795000000071|marker-25||38.88757000000007,-77.03195000000072|marker-26||&center=38.88757000000007,-77.02995000000072&defaultMarker=none&zoom=15&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z-pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 25,
                        "distance": 0.1939,
                        "narrative": "Turn right onto 14th St SW (US-1). Go for 0.2 mi.",
                        "time": 55,
                        "direction": 1,
                        "directionName": "North",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:00:55",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 38.88757000000007,
                            "lng": -77.03195000000072
                        },
                        "turnType": 2,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": [
                            "US-1",
                            "14th St SW",
                            "14th St NW"
                        ],
                          "mapUrl": "https://www.mapquestapi.com/staticmap/v5/map?  
                           key=hYyk5Ku8xkzbYV1MvC0HZ0EfOxuuYyET&size=225,160&locations=38.88757000000007,-77.03195000000072|marker- 
                           26||38.890370000000075,-77.03196000000072|marker- 
                           27||&center=38.88897000000007,-77.03195500000072&defaultMarker=none&zoom=15&session=AIoA_v___wcAAQDIAAAAeNpjOMHAwMTAwMCekVqUapWc2z- 
             pTBLIZficblnPwWOVFe89_9bnGBjtA6R3AGkGLABmwlRxZrAJO18s6mbgKT9k4Tnr2PJodJoBBzCrVdOeyAhkMC991cTQwMChAJdig9IcDAwOQMTIwMQEETjAMiGcWYMBAKOeLSnD3A8k:car"
                    },
                    {
                        "index": 26,
                        "distance": 0,
                        "narrative": "Arrive at 14th St NW (US-1).",
                        "time": 0,
                        "direction": 0,
                        "directionName": "None",
                        "signs": [],
                        "maneuverNotes": [],
                        "formattedTime": "00:00:00",
                        "transportMode": "car",
                        "startPoint": {
                            "lat": 38.890370000000075,
                            "lng": -77.03196000000072
                        },
                        "turnType": 0,
                        "attributes": 0,
                        "iconUrl": "",
                        "streets": []
                    }
                ]
            }
        ],
        "options": {
            "unit": "M",
            "routeType": "FASTEST",
            "narrativeType": "text",
            "enhancedNarrative": false,
            "walkingSpeed": -1,
            "highwayEfficiency": 22,
            "avoids": false,
            "generalize": -1,
            "shapeFormat": "raw",
            "locale": "en_US",
            "useTraffic": false,
            "timeType": 0,
            "dateType": 0,
            "doReverseGeocode": true,
            "manMaps": true,
            "tollCost": false,
            "sideOfStreetDisplay": true
        },
        "boundingBox": {
            "ul": {
                "lat": 40.73204000000002,
                "lng": -77.03196000000072
            },
            "lr": {
                "lat": 38.87038000000002,
                "lng": -74.00516
            }
        },
        "name": "I-95 and New Jersey Tpke",
        "maxRoutes": "",
        "locations": [
            {
                "street": "",
                "adminArea6": "",
                "adminArea6Type": "Neighborhood",
                "adminArea5": "New York",
                "adminArea5Type": "City",
                "adminArea4": "New York",
                "adminArea4Type": "County",
                "adminArea3": "NY",
                "adminArea3Type": "State",
                "adminArea1": "US",
                "adminArea1Type": "Country",
                "postalCode": "",
                "geocodeQualityCode": "A5XAX",
                "geocodeQuality": "CITY",
                "dragPoint": false,
                "sideOfStreet": "N",
                "linkId": "0",
                "unknownInput": "",
                "type": "s",
                "latLng": {
                    "lat": 40.71453,
                    "lng": -74.00712
                },
                "displayLatLng": {
                    "lat": 40.71453,
                    "lng": -74.00712
                },
                "mapUrl": ""
            },
            {
                "street": "",
                "adminArea6": "",
                "adminArea6Type": "Neighborhood",
                "adminArea5": "Washington",
                "adminArea5Type": "City",
                "adminArea4": "District of Columbia",
                "adminArea4Type": "County",
                "adminArea3": "DC",
                "adminArea3Type": "State",
                "adminArea1": "US",
                "adminArea1Type": "Country",
                "postalCode": "",
                "geocodeQualityCode": "A5XAX",
                "geocodeQuality": "CITY",
                "dragPoint": false,
                "sideOfStreet": "N",
                "linkId": "0",
                "unknownInput": "",
                "type": "s",
                "latLng": {
                    "lat": 38.89037,
                    "lng": -77.03196
                },
                "displayLatLng": {
                    "lat": 38.89037,
                    "lng": -77.03196
                },
                "mapUrl": ""
            }
        ],
        "locationSequence": [
            0,
            1
        ]
    },
    "fuel_stops": [
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        },
        {
            "truckstop_name": "SHEETZ #512",
            "address": "I-40, EXIT 203 & SR-66",
            "city": "Kernersville",
            "state": "NC",
            "fuel_price": 2.844,
            "distance_from_route": 456.33247388332364
        }
    ],
    "total_fuel_cost": 64.94456015999998
}

Installation and Running:
1. Creating and the .env and adding the MAPQUEST API key <br>
2. pip install -r requirements.txt <br>
- To install libraries <br>
3. Run server API <br>
- python manage.py runserver


    

  
