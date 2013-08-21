angular.module('someitemService', ['ngResource']).
    factory('SomeItem', function($resource){
  		return $resource('/api/v1/someitem/:someitemId', {}, {
    		query:   {method:'GET',     params:{someitemId : ''},          isArray : true},
    		get:     {method:'GET',     params:{someitemId : ''},          isArray : false},
    		save:    {method:'POST',    params:{someitemId : ''},          isArray : false},
    		update:  {method:'PUT',     params:{someitemId : '@_id.$oid'}, isArray : false},
  		});
	});


angular.module('mapService', ['ngResource']).
    factory('Map', function($resource){
  		return $resource('/api/v1/map/:mapId', {}, {
    		query:   {method:'GET',     params:{mapId : ''},          isArray : true},
    		get:     {method:'GET',     params:{mapId : ''},          isArray : false},
    		save:    {method:'POST',    params:{mapId : ''},          isArray : false},
    		update:  {method:'PUT',     params:{mapId : '@_id.$oid'}, isArray : false},
  		});
	});


