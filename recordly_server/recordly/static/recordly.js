RecordlyApp = angular.module('RecordlyApp', ['ngResource'])
    .config(['$interpolateProvider', function($interpolateProvider) { // angular usually uses {{}} but since djangos templating lang uses that too, we rename angular's
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    }])
    // this directive drives the tabbing behavior so that clicking on different tabs shows different content
    .directive('recordlyNavigator', ['$resource',
        function(                     $resource) {
        return {
            restrict: 'A',
            scope: {
            },
            link: function(scope, elem, attrs) {
                elem.find('#main-nav-explore a').click(function() {
                    $('#main-nav-search').removeClass('active')
                    $('#main-nav-explore').addClass('active')
                    $('#recordly-search').hide();
                    $('#recordly-explore').show();
                });
                elem.find('#main-nav-search a').click(function() {
                    $('#main-nav-search').addClass('active')
                    $('#main-nav-explore').removeClass('active')
                    $('#recordly-search').show();
                    $('#recordly-explore').hide();
                });
            }
        }
    }])
    .directive('recordlyExplore', ['$resource',
        function(           $resource) {
        return {
            restrict: 'A',
            scope: {
                artistlist: '=',
                albumlist: '=',
                songlist: '='
            },
            link: function(scope, elem, attrs) {
                var retrieveExplorerResults = function(filterFavorites) {
                    var filter = filterFavorites ? 'favorites' : '';

                    $resource('http://localhost:8000/artist/:filter', null, {'query': {method: 'GET', isArray: true}}).query(
                        { filter: filter },
                        function(data) {
                            scope.artistlist = data;
                        }
                    );
                    $resource('http://localhost:8000/album/:filter', null, {'query': {method: 'GET', isArray: true}}).query(
                        { filter: filter },
                        function(data) {
                            scope.albumlist = data;
                        }
                    );
                    $resource('http://localhost:8000/song/:filter', null, {'query': {method: 'GET', isArray: true}}).query(
                        { filter: filter },
                        function(data) {
                            scope.songlist = data;
                        }
                    );
                }
                retrieveExplorerResults(false);
                $('.checkbox .favorites').first().change(function() {
                    retrieveExplorerResults(this.checked);
                });
            }
        }
    }])
    .directive('recordlySearch', ['$resource', '$timeout',
        function(           $resource, $timeout) {
        return {
            restrict: 'A',
            scope: {
                results: '=',
            },
            link: function(scope, elem, attrs) {
                var throttling = false;
                var performThrottledSearch = function() {
                    if (throttling) {
                        return;
                    }
                    throttling = true;

                    $timeout(function() { // pause 
                        retrieveSearchResults($('#searchbox').val());
                        throttling = false;
                    }, 500);
                }
                var retrieveSearchResults = function(searchterm) {
                    $resource('http://localhost:8000/search/:searchterm', { searchterm: searchterm }).query(
                        function(data) {
                            scope.results = data;
                        }
                    );
                }
                $('#searchbox').keyup(function() {
                    performThrottledSearch();
                });
            }
        }
    }])
;

