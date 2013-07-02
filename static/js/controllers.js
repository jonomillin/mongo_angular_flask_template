
var infatics = angular.module('infatics-app', ['someitemService', ],
    function($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
});

/*
 * SomeItemCtrl 
 *
 */
function SomeItemCtrl($scope, SomeItem) {
    
    $scope.someitems  = SomeItem.query( function(d) {
        console.log('Received someitem');
        console.log(d);
        
    });

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

