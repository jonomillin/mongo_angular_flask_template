
var infatics = angular.module('infatics-app', ['someitemService', 'mapService',],
    function($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
});

/*
 * SomeItemCtrl 
 *
 */
function SomeItemCtrl($scope, SomeItem) {
    


    $scope.someitems = [
        {
            name    : 'Tester',
            value_1 : 'Static',
            value_2 : 'Item',
            value_3 : 'set',
        },

    ]


    // $scope.someitems  = SomeItem.query( function(d) {
    //     console.log('Received someitem');
    //     console.log(d);
        
    // });

    $scope.new_someitem = {
        name    : 'Not set yet',
        value_1 : 'Not set yet',
        value_2 : 'Not set yet',
        value_3 : 'Not set yet',
    };

    $scope.selected_someitem = undefined;

    $scope.save = function(someitem)
    {
        SomeItem.save(someitem, function(d) {
            $scope.someitems.push(d);
            $scope.new_someitem = {
                name    : 'Not set yet',
                value_1 : 'Not set yet',
                value_2 : 'Not set yet',
                value_3 : 'Not set yet',
            };

        });     
    }

    $scope.deselect = function() {
        $scope.selected_someitem = undefined;
    }

    $scope.select = function(someitem)
    {
        $scope.selected_someitem = someitem;
    }

    $scope.update = function(someitem)
    {
        SomeItem.update(someitem);
    }

    $scope.updateSelected = function()
    {
        $scope.update($scope.selected_someitem);
    }
}


/*
 * MapCtrl 
 *
 */
function MapCtrl($scope, Map) {
    
    $scope.maps = [
        {
            name        : 'First Tester',
            email       : 'jono@dronedeploy.com',
            waypoints   : [
                {
                    wp_no : 0,
                    lat : 45.102,
                    lng : 20.213,
                    alt : 100,
                    action : "FLY"
                },

                {
                    wp_no : 1,
                    lat : 45.112,
                    lng : 20.223,
                    alt : 120,
                    action : "FLY"
                },

                {
                    wp_no : 2,
                    lat : 45.13,
                    lng : 20.23,
                    alt : 150,
                    action : "FLY"
                },
            ],
            creation_date : "20/08/2013, 2pm",
            
        }
    ]
    // $scope.maps  = Map.query( function(d) {
    //     console.log('Received map');
    //     console.log(d);
    // });

    $scope.new_map = {
        name        : 'Not set yet',
        email       : 'Not set yet',
        waypoints   : [],
    };

    $scope.new_waypoint = {
        wp_no : 0,
        lat : 0,
        lng : 0,
        alt : 100,
        action : "NONE"
    };

    $scope.selected_map = undefined;

    $scope.add_waypoint = function(wp)
    {
        $scope.new_map.waypoints.push(wp);

        // Reset initial waypoint
        $scope.new_waypoint = {
            wp_no : wp.wp_no+1,
            lat : 0,
            lng : 0,
            alt : 100,
            action : "NONE"
        };
        // $scope.$digest();
    }

    $scope.save = function(map)
    {
        // Map.save(map, function(d) {
            $scope.maps.push(map);
            $scope.new_map = {
                name        : 'Not set yet',
                email       : 'Not set yet',
                waypoints   : [],
            };
            $scope.new_waypoint.wp_no = 0;

        // });     
    }

    $scope.deselect = function() {
        $scope.selected_map = undefined;
    }

    $scope.select = function(map)
    {
        $scope.selected_map = map;
    }

    $scope.update = function(map)
    {
        Map.update(map);
    }

    $scope.updateSelected = function()
    {
        $scope.update($scope.selected_map);
    }
}

