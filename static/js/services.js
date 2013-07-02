angular.module('someitemService', ['ngResource']).
    factory('SomeItem', function($resource){
  		return $resource('/api/v1/someitem/:someitemId', {}, {
    		query:   {method:'GET',     params:{someitemId : ''},          isArray : true},
    		get:     {method:'GET',     params:{someitemId : ''},          isArray : false},
    		save:    {method:'POST',    params:{someitemId : ''},          isArray : false},
    		update:  {method:'PUT',     params:{someitemId : '@_id.$oid'}, isArray : false},
  		});
	});


