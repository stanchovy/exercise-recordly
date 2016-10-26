RecordlyApp = angular.module('RecordlyApp', ['ngResource'])
    .directive('artists', ['$resource',
        function(           $resource) {
        return {
            restrict: 'A',
            scope: {
                results: '='
            },
            link: function(scope, elem, attrs) {
                return $resource('http://localhost:8000/artist/').get();
            }
        }
    }]);

